# -*- coding: utf-8 -*-
from datetime import datetime
import os
import re
from .pypyodbc import connect as odbc_connect
import time
from ..util.log import log, debug

#DATABASE_NAME = os.environ.get('PEEWEE_DATABASE', 'peewee.db')
#DATABASE_NAME = "test.mdb"
DATABASE_ENGINE = "Driver={Microsoft Access Driver (*.mdb)};DBQ="


class Database(object):

    def __init__(self, database):
        self.database = database
        self._conn = None

    # connect database only when it's accessed, instead of connect during define
    @property
    def conn(self):
        if self._conn == None:
            self._conn = self.get_connection()
        return self._conn

    def get_connection(self):
        if os.path.isfile(self.database):
            debug("连接数据库: " + self.database)
            return odbc_connect(DATABASE_ENGINE + self.database)
        else:
            # TODO 先不生成数据库
            #log("create database: " + self.database)
            # pypyodbc.win_create_mdb(self.database)
            # return pypyodbc.connect(DATABASE_ENGINE + self.database)
            pass
        # return sqlite3.connect(self.database)

    def execute(self, sql, commit=False):
        cursor = self.conn.cursor()
        debug(sql)
        res = cursor.execute(sql)
        if commit:
            self.conn.commit()
        return res

    def last_insert_id(self):
        result = self.execute("SELECT @@IDENTITY;")
        return result.fetchone()[0]

    def create_table(self, model_class):
        #framing = "IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = N'%s' AND type = 'U')"
        #self.execute(framing % (model_class._meta.db_table))

        framing = "CREATE TABLE %s (%s);"
        columns = []

        for field in model_class._meta.fields.values():
            columns.append(field.to_sql())

        self.execute(framing % (model_class._meta.db_table, ', '.join(columns)))
        self.conn.commit()

    def drop_table(self, model_class):
        cursor = self.conn.cursor()
        cursor.execute('DROP TABLE %s;' % model_class._meta.db_table)
        self.conn.commit()


#database = Database(DATABASE_NAME)


class QueryResultWrapper(object):
    _result_cache = []

    def __init__(self, model, cursor):
        self.model = model
        self.cursor = cursor

    def model_from_rowset(self, model_class, row_dict):
        instance = model_class()
        for attr, value in row_dict.items():
            if attr in instance._meta.fields:
                field = instance._meta.fields[attr]
                setattr(instance, attr, field.python_value(value))
            else:
                setattr(instance, attr, value)
        return instance

    def _row_to_dict(self, row, result_cursor):
        return dict((result_cursor.description[i][0], value)
                    for i, value in enumerate(row))

    def __iter__(self):
        return self

    # pyton3 use __next__ instead of next
    def __next__(self):
        row = self.cursor.fetchone()
        if row:
            row_dict = self._row_to_dict(row, self.cursor)
            # 强行将id改为小写的键
            for key in row_dict.keys():
                if key in ['id', 'ID', 'Id', 'iD']:
                    value = row_dict[key]
                    row_dict.pop(key)
                    row_dict['id'] = value
            return self.model_from_rowset(self.model, row_dict)
        else:
            raise StopIteration

    def next(self):
        row = self.cursor.fetchone()
        if row:
            row_dict = self._row_to_dict(row, self.cursor)
            # 强行将id改为小写的键
            for key in row_dict.keys():
                if key in ['id', 'ID', 'Id', 'iD']:
                    value = row_dict[key]
                    row_dict.pop(key)
                    row_dict['id'] = value
            return self.model_from_rowset(self.model, row_dict)
        else:
            raise StopIteration


def asc(f):
    return (f, 'ASC')


def desc(f):
    return (f, 'DESC')


class BaseQuery(object):
    operations = {
        'lt': '< %s',
        'lte': '<= %s',
        'gt': '> %s',
        'gte': '>= %s',
        'eq': '= %s',
        'in': ' IN (%s)',
        'icontains': "LIKE '%%%s%%'",
        'contains': "GLOB '*%s*'",
    }
    query_separator = '__'
    requires_commit = True

    def __init__(self, database, model):
        self.database = database
        self.model = model
        self.query_context = model
        self._where = {}
        self._joins = []

    def parse_query_args(self, **query):
        parsed = {}
        for lhs, rhs in query.items():
            if self.query_separator in lhs:
                lhs, op = lhs.rsplit(self.query_separator, 1)
            else:
                op = 'eq'

            field = self.query_context._meta.get_field_by_name(lhs)
            if op == 'in':
                lookup_value = ','.join([field.lookup_value(op, o) for o in rhs])
            else:
                lookup_value = field.lookup_value(op, rhs)
            parsed[field.name] = self.operations[op] % lookup_value

        return parsed

    def where(self, query='', **kwargs):
        self._where.setdefault(self.query_context, {})
        if query != '':
            if '__raw__' in self._where[self.query_context]:
                raise ValueError('A raw query has already been specified')
            self._where[self.query_context]['__raw__'] = query
        if kwargs:
            parsed = self.parse_query_args(**kwargs)
            self._where[self.query_context].update(**parsed)

        return self

    def join(self, model):
        if self.query_context._meta.rel_exists(model):
            self._joins.append(model)
            self.query_context = model
        else:
            raise AttributeError('No foreign key found between %s and %s' %
                                 (self.query_context.__name__, model.__name__))
        return self

    def use_aliases(self):
        return len(self._joins) > 0

    def combine_field(self, alias, field_name):
        if alias:
            return '%s.%s' % (alias, field_name)
        return field_name

    def compile_where(self):
        alias_count = 0
        alias_map = {}

        alias_required = self.use_aliases()

        joins = list(self._joins)
        if self._where or len(joins):
            joins.insert(0, self.model)

        where_with_alias = []
        computed_joins = []

        for i, model in enumerate(joins):
            if alias_required:
                alias_count += 1
                alias_map[model] = 't%d' % alias_count
            else:
                alias_map[model] = ''

            if model in self._where:
                for name, lookup in self._where[model].items():
                    if name == '__raw__':
                        where_with_alias.append(lookup)
                    else:
                        where_with_alias.append('%s %s' % (
                            self.combine_field(alias_map[model], name), lookup))

            if i > 0:
                from_model = joins[i - 1]
                field = from_model._meta.get_related_field_for_model(model)
                if field:
                    left_field = field.name
                    right_field = 'id'
                else:
                    field = from_model._meta.get_reverse_related_field_for_model(model)
                    left_field = 'id'
                    right_field = field.name

                computed_joins.append(
                    'INNER JOIN %s AS %s ON %s = %s' % (
                        model._meta.db_table,
                        alias_map[model],
                        self.combine_field(alias_map[from_model], left_field),
                        self.combine_field(alias_map[model], right_field),
                    )
                )

        return computed_joins, where_with_alias, alias_map

    def raw_execute(self):
        query = self.sql()
        # 将"改成'，否则MSSQL不认
        if '\"' in query:
            query = query.replace('\"', '\'')
        result = self.database.execute(query, self.requires_commit)
        return result


class SelectQuery(BaseQuery):

    """
    Model.select('*').where(field=val).join(RelModel).where(rel_field=val)
    """
    requires_commit = False

    def __init__(self, database, model, query=None):
        self.query = query or '*'
        self._group_by = []
        self._having = []
        self._order_by = []
        self._pagination = None  # return all by default
        super(SelectQuery, self).__init__(database, model)

    def paginate(self, page_num, paginate_by=20):
        self._pagination = (page_num, paginate_by)
        return self

    def count(self):
        tmp_pagination = self._pagination
        self._pagination = None

        tmp_query = self.query

        if self.use_aliases():
            self.query = 'COUNT(t1.id)'
        else:
            self.query = 'COUNT(id)'

        cursor = self.database.conn.cursor()
        res = cursor.execute(self.sql())

        self.query = tmp_query
        self._pagination = tmp_pagination

        return res.fetchone()[0]

    def group_by(self, clause):
        self._group_by.append(clause)
        return self

    def having(self, clause):
        self._having.append(clause)
        return self

    def order_by(self, field_or_string):
        if isinstance(field_or_string, tuple):
            field_or_string, ordering = field_or_string
        else:
            ordering = 'ASC'

        self._order_by.append((self.query_context, '%s %s' % (field_or_string, ordering)))

        return self

    def sql(self):
        joins, where, alias_map = self.compile_where()

        table = self.model._meta.db_table
        if alias_map.get(self.model, None):
            table = '%s AS %s' % (table, alias_map[self.model])
            if self.query == '*':
                self.query = '%s.*' % alias_map[self.model]
            else:
                pass  # handle list of params here

        select = 'SELECT %s FROM %s' % (self.query, table)
        joins = '\n'.join(joins)
        where = ' AND '.join(where)
        group_by = ', '.join(self._group_by)
        having = ' AND '.join(self._having)

        order_by = []
        for piece in self._order_by:
            model, clause = piece
            if model in alias_map:
                piece = '%s.%s' % (alias_map[model], clause)
            else:
                piece = clause
            order_by.append(piece)

        pieces = [select]

        if joins:
            pieces.append(joins)
        if where:
            pieces.append('WHERE %s' % where)
        if group_by:
            pieces.append('GROUP BY %s' % group_by)
        if having:
            pieces.append('HAVING %s' % having)
        if order_by:
            pieces.append('ORDER BY %s' % ', '.join(order_by))
        if self._pagination:
            page, paginate_by = self._pagination
            if page > 0:
                page -= 1
            pieces.append('LIMIT %d OFFSET %d' % (paginate_by, page * paginate_by))

        return ' '.join(pieces)

    def execute(self):
        return QueryResultWrapper(self.model, self.raw_execute())

    def __iter__(self):
        return self.execute()


class UpdateQuery(BaseQuery):

    """
    Model.update(field=val, field2=val2).where(some_field=some_val)
    """

    def __init__(self, database, model, **kwargs):
        self.update_query = kwargs
        super(UpdateQuery, self).__init__(database, model)

    def parse_update(self):
        sets = []
        for k, v in self.update_query.items():
            field = self.model._meta.get_field_by_name(k)
            # string是MSSQL保留字，会报语法错误，需要用[]包起来
            if k.lower() in ['string', 'value']:
                k = "[" + k + "]"
            sets.append('%s=%s' % (k, field.lookup_value(None, v)))

        return ', '.join(sets)

    def sql(self):
        joins, where, alias_map = self.compile_where()
        set_statement = self.parse_update()

        update = 'UPDATE %s SET %s' % (self.model._meta.db_table, set_statement)
        where = ' AND '.join(where)

        pieces = [update]

        if where:
            pieces.append('WHERE %s' % where)

        return ' '.join(pieces)

    def join(self, *args, **kwargs):
        raise AttributeError('Update queries do not support JOINs in sqlite')

    def execute(self):
        result = self.raw_execute()
        return result.rowcount


class DeleteQuery(BaseQuery):

    """
    Model.delete().where(some_field=some_val)
    """

    def sql(self):
        joins, where, alias_map = self.compile_where()

        delete = 'DELETE FROM %s' % (self.model._meta.db_table)
        where = ' AND '.join(where)

        pieces = [delete]

        if where:
            pieces.append('WHERE %s' % where)

        return ' '.join(pieces)

    def join(self, *args, **kwargs):
        raise AttributeError('Update queries do not support JOINs in sqlite')

    def execute(self):
        result = self.raw_execute()
        return result.rowcount


class InsertQuery(BaseQuery):

    """
    Model.insert(field=val, field2=val2)
    """

    def __init__(self, database, model, **kwargs):
        self.insert_query = kwargs
        super(InsertQuery, self).__init__(database, model)

    def parse_insert(self):
        cols = []
        vals = []
        for k, v in self.insert_query.items():
            field = self.model._meta.get_field_by_name(k)
            # string是MSSQL保留字，会报语法错误，需要用[]包起来
            if k.lower() in ['string', 'value']:
                k = "[" + k + "]"
            if v not in ['', "", None]:
                cols.append(k)
                vals.append(str(field.lookup_value(None, v)))

        return cols, vals

    def sql(self):
        cols, vals = self.parse_insert()

        insert = "INSERT INTO %s(%s) VALUES (%s)" % (
            self.model._meta.db_table, ','.join(cols), ','.join(vals))

        return insert

    def where(self, *args, **kwargs):
        raise AttributeError('Insert queries do not support WHERE clauses')

    def join(self, *args, **kwargs):
        raise AttributeError('Insert queries do not support JOINs')

    def execute(self):
        result = self.raw_execute()
        return self.database.last_insert_id()
        # print result.rowcount
        # return 0


class Field(object):
    db_field = ''
    field_template = "%(db_field)s"

    def get_attributes(self):
        return {}

    def __init__(self, *args, **kwargs):
        self.attributes = self.get_attributes()
        if 'db_field' not in kwargs:
            kwargs['db_field'] = self.db_field
        self.attributes.update(kwargs)

    def add_to_class(self, klass, name):
        self.name = name
        setattr(klass, name, None)

    def render_field_template(self):
        return self.field_template % self.attributes

    def to_sql(self):
        rendered = self.render_field_template()
        return '"%s" %s' % (self.name, rendered)

    def db_value(self, value):
        return value or "NULL"

    def python_value(self, value):
        return value

    def lookup_value(self, lookup_type, value):
        return self.db_value(value)

    def get_type(self):
        return None


class BooleanField(Field):
    db_field = 'YESNO'

    def db_value(self, value):
        return value or False

    def get_type(self):
        return type(True)


class CharField(Field):
    db_field = 'VARCHAR'
    field_template = "%(db_field)s(%(max_length)d) NOT NULL"

    def get_attributes(self):
        return {'max_length': 255}

    def db_value(self, value):
        value = value or ''
        return value[:self.attributes['max_length']]

    def lookup_value(self, lookup_type, value):
        if lookup_type in ('contains', 'icontains'):
            return self.db_value(value)
        else:
            return '"%s"' % self.db_value(value)

    def get_type(self):
        return type('')


class TextField(Field):
    db_field = 'TEXT'

    def db_value(self, value):
        return value or ''

    def lookup_value(self, lookup_type, value):
        if lookup_type in ('contains', 'icontains'):
            return self.db_value(value)
        else:
            return '"%s"' % self.db_value(value)

    def get_type(self):
        return type('')


class DateTimeField(Field):
    db_field = 'DATETIME'
    field_template = "%(db_field)s"

    def python_value(self, value):
        if value is not None:
            return datetime(*time.strptime(value, '%Y-%m-%d %H:%M:%S')[:6])

    def db_value(self, value):
        if value is not None:
            return '"%s"' % value.strftime('%Y-%m-%d %H:%M:%S')
        return "NULL"

    def get_type(self):
        return type('')


class IntegerField(Field):
    db_field = 'INTEGER'
    field_template = "%(db_field)s NOT NULL"

    def db_value(self, value):
        return value or 0

    def python_value(self, value):
        return int(value or 0)

    def get_type(self):
        return type(0)


class FloatField(Field):
    db_field = 'REAL'
    field_template = "%(db_field)s NOT NULL"

    def db_value(self, value):
        return value or 0.0

    def python_value(self, value):
        return float(value or 0)

    def get_type(self):
        return type(0.0)


class PrimaryKeyField(IntegerField):
    field_template = "%(db_field)s NOT NULL PRIMARY KEY"


class ForeignRelatedObject(object):

    def __init__(self, to, name):
        self.field_name = name
        self.to = to
        self.cache_name = '_cache_%s' % name

    def __get__(self, instance, instance_type=None):
        if not getattr(instance, self.cache_name, None):
            id = getattr(instance, self.field_name, 0)
            qr = self.to.select().where(id=id).execute()
            setattr(instance, self.cache_name, qr.next())
        return getattr(instance, self.cache_name)

    def __set__(self, instance, obj):
        assert isinstance(obj, self.to), "Cannot assign %s, invalid type" % obj
        setattr(instance, self.field_name, obj.id)
        setattr(instance, self.cache_name, obj)


class ReverseForeignRelatedObject(object):

    def __init__(self, related_model, name):
        self.field_name = name
        self.related_model = related_model

    def __get__(self, instance, instance_type=None):
        query = {self.field_name: instance.id}
        qr = self.related_model.select().where(**query)
        return qr


class ForeignKeyField(IntegerField):
    field_template = '%(db_field)s NOT NULL REFERENCES "%(to_table)s" ("id")'

    def __init__(self, to, *args, **kwargs):
        self.to = to
        kwargs['to_table'] = to._meta.db_table
        super(ForeignKeyField, self).__init__(*args, **kwargs)

    def add_to_class(self, klass, name):
        self.descriptor = name
        self.name = name + '_id'
        self.related_name = klass._meta.db_table + '_set'
        setattr(klass, self.descriptor, ForeignRelatedObject(self.to, self.name))
        setattr(klass, self.name, None)

        reverse_rel = ReverseForeignRelatedObject(klass, self.name)
        setattr(self.to, self.related_name, reverse_rel)

    def lookup_value(self, lookup_type, value):
        if isinstance(value, Model):
            return value.id
        return value or "NULL"


class BaseModel(type):

    def __new__(cls, name, bases, attrs):
        cls = super(BaseModel, cls).__new__(cls, name, bases, attrs)

        class Meta(object):
            fields = {}

            def __init__(self, model_class):
                self.model_class = model_class
                #self.database = self.model_class.database

            def get_field_by_name(self, name):
                if name in self.fields:
                    return self.fields[name]
                print('Field name <%s> not found' % name)
                raise AttributeError

            def get_related_field_for_model(self, model):
                for field in self.fields.values():
                    if isinstance(field, ForeignKeyField) and field.to == model:
                        return field

            def get_reverse_related_field_for_model(self, model):
                for field in model._meta.fields.values():
                    if isinstance(field, ForeignKeyField) and field.to == self.model_class:
                        return field

            def rel_exists(self, model):
                return self.get_related_field_for_model(model) or \
                    self.get_reverse_related_field_for_model(model)

        _meta = Meta(cls)
        setattr(cls, '_meta', _meta)

        # 原来的代码把_前面的都去掉了
        #_meta.db_table = re.sub('[^a-z]+', '_', cls.__name__.lower())
        _meta.db_table = cls.__name__.lower()
        # 在后面加了_Model，去掉
        _meta.db_table = _meta.db_table.replace('_model', '')

        has_primary_key = False

        for name, attr in cls.__dict__.items():
            if isinstance(attr, Field):
                attr.add_to_class(cls, name)
                _meta.fields[attr.name] = attr
                if isinstance(attr, PrimaryKeyField):
                    has_primary_key = True

        if not has_primary_key:
            pk = PrimaryKeyField()
            pk.add_to_class(cls, 'id')
            _meta.fields['id'] = pk

        if hasattr(cls, '__unicode__'):
            setattr(cls, '__repr__', lambda self: '<%s: %s>' % (
                self.__class__.__name__, self.__unicode__()))

        return cls


# Python 2/3 compatibility helpers. These helpers are used internally and are
# not exported.
def with_metaclass(meta, base=object):
    return meta("NewBase", (base,), {})

class Model(with_metaclass(BaseModel)):
    #database = Database()

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        return other.__class__ == self.__class__ and self.id and other.id == self.id

    def get_field_dict(self):
        field_val = lambda f: (f.name, getattr(self, f.name))
        # print type(self._meta.fields)
        pairs = map(field_val, self._meta.fields.values())
        return dict(pairs)

    def get_field_type(self):
        """ 得到各个field的类型 """
        field_val = lambda f: (f.name, f.get_type())
        pairs = map(field_val, self._meta.fields.values())
        # for v in self._meta.fields.values():
        #print (v.get_type())
        return dict(pairs)

    @classmethod
    def raw_execute(cls, sql):
        cls.database.execute(sql, commit=True)

    @classmethod
    def create_table(cls):
        cls.database.create_table(cls)

    @classmethod
    def drop_table(cls):
        cls.database.drop_table(cls)

    @classmethod
    def select(cls, query=None):
        return SelectQuery(cls.database, cls, query)

    @classmethod
    def update(cls, **query):
        return UpdateQuery(cls.database, cls, **query)

    @classmethod
    def insert(cls, **query):
        return InsertQuery(cls.database, cls, **query)

    @classmethod
    def delete(cls, **query):
        return DeleteQuery(cls.database, cls, **query)

    @classmethod
    def get(cls, **query):
        return cls.select().where(**query).execute().next()

    def check_exist(self):
        field_dict = self.get_field_dict()
        for k in list(field_dict):
            if getattr(self, k) == None:
                field_dict.pop(k)
        rs = self.select().where(**field_dict)
        count = 0
        if rs:
            for r in rs:
                count = count + 1  # SelectQuery支持迭代，但没有len方法，count()又出错，只能用蠢办法算结果数量
        if count:
            log("找到%d条记录于表%s" % (count, self._meta.db_table))
        else:
            debug("表%s没有找到记录" % (self._meta.db_table))

        return count

    def validate(self):
        pass

    def save(self):
        field_dict = self.get_field_dict()
        # 当id为0或none时，删除id键值，否则id会insert到数据库里，引起错误
        if self.id is None or self.id == 0:
            field_dict.pop('id')  # 删除id键值
        insert = self.insert(**field_dict)
        try:
            self.id = insert.execute()
            debug("表%s成功添加记录，id=%d!" % (self._meta.db_table, self.id))
            debug("内容=%s" % (str(field_dict)))
        except Exception as e:
            log("！！！错误！！！表%s无法添加记录" % (self._meta.db_table))
            raise e
        return
