# -*- coding: utf-8 -*-
from util.peewee import *
from util.log import *
from models import *


class BaseTable(object):

    ''' 所有表的基类 '''

    def __init__(self, model, *args, **kwargs):
        '''
            初始化

        :param model: model类
        :param *args:
        :param **kwargs: fields(field=value)
        :return:
        '''
        self.model = model
        self.fill_fields(**kwargs)
        self.foreignkey_items = self.get_foreignkey_items(**kwargs)
        self.delete_attr()

    def fill_fields(self, **kwargs):
        '''
            填充各个field属性值，没有的则为None

        :param **kwargs: fields(field=value)
        '''
        for k, v in kwargs.items():
            if k in ['id', 'ID', 'iD', 'Id']:
                k = k.lower()
            if hasattr(self.model, k):
                setattr(self.model, k, v)

    def fill_default_fileds(self, defaults, **kwargs):
        '''
            填充如Comment的field属性值

        :param defaults: field名的list
        :param **kwargs: fields(field=value)
        '''
        """填充如Comment的field属性值"""
        for k, v in defaults.items():
            if k not in kwargs.keys() and hasattr(self.model, k):
                setattr(self.model, k, v)

    def delete_attr(self, attr_list=['Comment']):
        '''
            删除特定的attribute
        如果MSSQL返回错误
        1. You cannot add or change a record because a related record is required in table 'Subject'
        2. xxx cannot be a zero-length string
        这是因为peewee里这些field如果不赋值，会有默认的值，例如0或''，sql语句里会有，此时要删除这些field

        :param attr_list: 要删除的属性列表
        :return:
        '''
        # TODO Bug:如果连续使用一张table，第二次就没有Comment这个field了
        for attr in attr_list:
            if hasattr(self.model, attr) and getattr(self.model, attr) == None:
                # print self.model._meta.fields[attr]
                if attr in self.model._meta.fields.keys():
                    self.model._meta.fields.pop(attr)

    def get_foreignkey_items(self, **kwargs):
        """查找外键，存入字典里"""
        field_types = self.model.get_field_type()
        foreignkey_items = {}
        for k, v in kwargs.items():
            if hasattr(self.model, k):
                # 如果类型不同，则提取外键（一般是用描述性字符串代替外键的id）
                if not isinstance(v, field_types[k]):
                    foreignkey_items[k] = v
        return foreignkey_items

    def get_max_id(self):
        id_list = []
        r = self.model.select()
        for i in r:
            id_list.append(i.id)
        debug("Max id in %s table is %d" % (self.model.__class__.__name__, max(id_list)))
        self.model.id = max(id_list) + 1

    def convert_foreignkey(self, attr_name, foreign_model, foreign_search_attr_name, foreign_attr_name='id'):
        '''
            转换外键

        :param attr_name: 要转换的外键field名
        :param foreign_model: 关联表
        :param foreign_search_attr_name: 关联表搜索的field
        :param foreign_attr_name: 得到的关联表field
        '''
        if not hasattr(self.model, attr_name):
            log(("没有Field: %s" % (attr_name)).decode("utf-8"))
            raise NameError
        if attr_name in self.foreignkey_items.keys():
            r = foreign_model.get(**{foreign_search_attr_name: getattr(self.model, attr_name)})
            value = getattr(r, foreign_attr_name)
            debug(("转换外键%s = %s" % (attr_name, str(value))).decode("utf-8"))
            setattr(self.model, attr_name, value)

    def query(self, id=None):
        _id = id
        field_dict = self.model.get_field_dict()
        field_names = field_dict.keys()
        print '\t'.join(field_names)
        if _id:
            results = self.model.select().where(id=_id)
        else:
            results = self.model.select()
        if results:
            for result in results:
                olist = []
                for field in field_names:
                    olist.append(str(getattr(result, field)))
                output = '\t'.join(olist)
                print output
                # log(("记录已存在，跳过......").decode("utf-8"))

    def update(self, id=0, **kwargs):
        _id = id
        if _id:
            self.model.update(**kwargs).where(id=_id).execute()
            debug(("表%s成功更新记录，id=%d!" % ((self.model._meta.db_table), _id)).decode('utf-8'))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            #debug(("更新记录%d" %(_id)).decode("utf-8"))

    #@classmethod
    def add(self):
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return
        self.model.save()
        return self.model.id


# Factory Database
class BoolDataPoint(BaseTable):

    """操作表BoolDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = BoolDataPoint_Model()
        super(BoolDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


class EnumDataPoint(BaseTable):

    """操作表EnumDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = EnumDataPoint_Model()
        super(EnumDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


class FloatDataPoint(BaseTable):

    """操作表FloatDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = FloatDataPoint_Model()
        super(FloatDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')


class IntDataPoint(BaseTable):

    """操作表IntDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = IntDataPoint_Model()
        super(IntDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')
        if self.model.Type not in ['I16', 'I32', 'U16', 'U32', 'U8']:
            log(('IntDataPoint的Type必须为I16, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


class StringDataPoint(BaseTable):

    """操作表StringDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = StringDataPoint_Model()
        super(StringDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


class Observer(BaseTable):

    """操作表Observer"""

    def __init__(self, *args, **kwargs):
        self.model = Observer_Model()
        super(Observer, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('TaskId', Task_Model, 'Name', 'id')
        self.delete_attr(['Comment', 'SubjectId', 'ConstructorArgs'])


class ObserverSubjects(BaseTable):

    """操作表ObserverSubjects"""

    def __init__(self, *args, **kwargs):
        self.model = ObserverSubjects_Model()
        super(ObserverSubjects, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('ObserverId', Observer_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectRelationId', SubjectRelation_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectAccess', SubjectAccessType_Model, 'Name', 'id')


class ObserverType(BaseTable):

    """操作表ObserverType"""

    def __init__(self, *args, **kwargs):
        self.model = ObserverType_Model()
        super(ObserverType, self).__init__(self.model, *args, **kwargs)
        self.delete_attr(['Comment', 'NameSpace'])


class Subject(BaseTable):

    """操作表Subject
    save : '-', 'All', 'Value'
    """

    def __init__(self, *args, **kwargs):
        self.model = Subject_Model()
        super(Subject, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('TypeId', SubjectTypes_Model, 'Name', 'id')
        self.convert_foreignkey('Save', SaveTypes_Model, 'Name', 'id')
        self.convert_foreignkey('FlashBlock', FlashBlockTypes_Model, 'Name', 'id')


class SubjectRelation(BaseTable):

    """操作表SubjectRelation"""

    def __init__(self, *args, **kwargs):
        """
        SubjectRelation.name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
        """
        self.model = SubjectRelation_Model()
        super(SubjectRelation, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ObserverTypeId', ObserverType_Model, 'Name', 'id')


class VectorDataPoint(BaseTable):

    """操作表VectorDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = VectorDataPoint_Model()
        super(VectorDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        if self.model.Type not in ['Bool', 'Double', 'EventLog', 'Float', 'I32', 'U16', 'U32', 'U8']:
            log(('VectorDataPoint的Type必须为Bool, Double, EventLog, Float, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


# Display Database
class Display(BaseTable):

    """操作表Display"""

    def __init__(self, *args, **kwargs):
        self.model = Display_Model()
        super(Display, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('RootGroupId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('Name', Strings_Model, 'String', 'id')


class DisplayComponent(BaseTable):

    """操作表DisplayComponent"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayComponent_Model()
        super(DisplayComponent, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ComponentType', DisplayComponentTypes_Model, 'Name', 'id')
        #self.convert_foreignkey('displayid', Display_Model, 'Name', 'id')


class DisplayLabel(BaseTable):

    """操作表DisplayLabel"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayLabel_Model()
        super(DisplayLabel, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')


class DisplayListView(BaseTable):

    """操作表DisplayListView"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayListView_Model()
        super(DisplayListView, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('NextListId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('PrevListId', DisplayComponent_Model, 'Name', 'id')


class DisplayListViewColumns(BaseTable):

    """操作表DisplayListViewColumns"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewColumns_Model()
        super(DisplayListViewColumns, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ListViewId', DisplayComponent_Model, 'Name', 'id')


class DisplayListViewItem(BaseTable):

    """操作表DisplayListViewItem"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewItem_Model()
        super(DisplayListViewItem, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ListViewId', DisplayComponent_Model, 'Name', 'id')
        self.get_max_id()

    def get_max_id(self):
        # 找出同一个listview下的item有多少个，选出最大的index
        r = DisplayListViewItem_Model.select().where(ListViewId=self.model.ListViewId)
        idx_list = []
        for i in r:
            idx_list.append(i.Index)
        if len(idx_list):
            max_idx = max(idx_list)
            debug("max index in DisplayListViewItem table and id=%d is %d" % (self.model.ListViewId, max_idx))
            self.model.Index = max_idx + 1
        else:
            self.model.Index = 0

    def get_listviewid_index(self):
        return self.model.ListViewId, self.model.Index


class DisplayListViewItemComponents(BaseTable):

    """操作表DisplayListViewItemComponents"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewItemComponents_Model()
        super(DisplayListViewItemComponents, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ComponentId', DisplayComponent_Model, 'Name', 'id')


class DisplayNumberQuantity(BaseTable):

    """操作表DisplayNumberQuantity"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayNumberQuantity_Model()
        super(DisplayNumberQuantity, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')
        self.convert_foreignkey('NumberFontId', DisplayFont_Model, 'FontName', 'id')
        self.convert_foreignkey('QuantityFontId', DisplayFont_Model, 'FontName', 'id')


class DisplayObserverSingleSubject(BaseTable):

    """操作表DisplayObserverSingleSubject"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayObserverSingleSubject_Model()
        super(DisplayObserverSingleSubject, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectAccess', SubjectAccessType_Model, 'Name', 'id')


class DisplayOnOffCheckBox(BaseTable):

    """操作表DisplayOnOffCheckBox"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayOnOffCheckBox_Model()
        super(DisplayOnOffCheckBox, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class QuantityType(BaseTable):

    """操作表QuantityType"""

    def __init__(self, *args, **kwargs):
        self.model = QuantityType_Model()
        super(QuantityType, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()

    def get_max_id(self):
        r = self.model.select()
        id_list = []
        for i in r:
            id_list.append(i.id)
        id_list.sort()
        # 最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
        self.model.id = id_list[-2] + 1
        debug("new QuantityType id is: %d" % (self.model.id))

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return
        self.model.id = stored_id
        self.model.save()
        return self.model.id


class DisplayText(BaseTable):

    """操作表DisplayText"""

    def __init__(self, *args, **kwargs):
        aligns = {
            "TOP_LEFT"        : 0,
            "TOP_RIGHT"       : 1,
            "TOP_HCENTER"     : 2,
            "BOTTOM_LEFT"     : 4,
            "BOTTOM_RIGHT"    : 5,
            "BOTTOM_HCENTER"  : 6,
            "VCENTER_LEFT"    : 12,
            "VCENTER_RIGHT"   : 13,
            "VCENTER_HCENTER" : 14,
        }
        self.model = DisplayText_Model()
        super(DisplayText, self).__init__(self.model, *args, **kwargs)
        self.model.Align = aligns[kwargs['Align']]
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('FontId', DisplayFont_Model, 'FontName', 'id')

    def add(self):
        """id在这张表里是唯一的，用id检查记录是否存在"""
        #r = self.model.get(id=self.model.id)
        r = self.model.select().where(id=self.model.id)
        if r:
            for i in r:
                log(("id=%d的记录已存在，跳过......" % (i.id)).decode("utf-8"))
                debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
                return
        self.model.save()
        return self.model.id


# Language Database
class StringDefines(BaseTable):

    """操作表StringDefines"""

    def __init__(self, *args, **kwargs):
        self.model = StringDefines_Model()
        super(StringDefines, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()
        self.convert_foreignkey('TypeId', StringTypes_Model, 'Type', 'id')
        self.delete_attr(['Location', 'UKDescription', 'DisplayNumbers'])

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return
        self.model.id = stored_id
        self.model.save()
        return self.model.id


class Strings(BaseTable):

    """操作表Strings"""

    def __init__(self, *args, **kwargs):
        self.model = Strings_Model()
        super(Strings, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('LanguageId', Languages_Model, 'Language', 'id')
        self.get_strings_max_id(kwargs['String'])

    def get_strings_max_id(self, str):
        r = Strings_Model.select().where(String=str)
        if r:
            for i in r:
                if i.id:
                    self.model.id = i.id
                    debug("string %s exist, id is %d" % (str, i.id))
                    return
        self.get_max_id()


class StringTypes(BaseTable):

    """操作表StringTypes"""

    def __init__(self, *args, **kwargs):
        self.model = StringTypes_Model()
        super(StringTypes, self).__init__(self.model, *args, **kwargs)


class Languages(BaseTable):

    """操作表Languages"""

    def __init__(self, *args, **kwargs):
        self.model = Languages_Model()
        super(Languages, self).__init__(self.model, *args, **kwargs)
