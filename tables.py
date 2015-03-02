# -*- coding: utf-8 -*-
from util.peewee import *
from util.log import *
from models import *


class TableBase(object):
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
            if hasattr(self.model, k):
                setattr(self.model, k, v)

    def fill_default_fileds(self, defaults, **kwargs):
        '''
            填充如comment的field属性值

        :param defaults: field名的list
        :param **kwargs: fields(field=value)
        '''
        """填充如comment的field属性值"""
        for k, v in defaults.items():
            if k not in kwargs.keys() and hasattr(self.model, k):
                setattr(self.model, k, v)

    def delete_attr(self, attr_list=['comment']):
        '''
            删除特定的attribute
        如果MSSQL返回错误
        1. You cannot add or change a record because a related record is required in table 'Subject'
        2. xxx cannot be a zero-length string
        这是因为peewee里这些field如果不赋值，会有默认的值，例如0或''，sql语句里会有，此时要删除这些field

        :param attr_list: 要删除的属性列表
        :return:
        '''
        #TODO Bug:如果连续使用一张table，第二次就没有comment这个field了
        for attr in attr_list:
            if hasattr(self.model, attr) and getattr(self.model, attr) == None:
                #print self.model._meta.fields[attr]
                if attr in self.model._meta.fields.keys():
                    self.model._meta.fields.pop(attr)

    def get_foreignkey_items(self, **kwargs):
        """查找外键，存入字典里"""
        field_types = self.model.get_field_type()
        foreignkey_items = {}
        for k, v in kwargs.items():
            if hasattr(self.model, k):
                #如果类型不同，则提取外键（一般是用描述性字符串代替外键的id）
                if type(v) != field_types[k]:
                    foreignkey_items[k] = v
        return foreignkey_items

    def get_max_id(self):
        id_list = []
        r = self.model.select()
        for i in r:
            id_list.append(i.id)
        log("max id in %s table is %d" % (self.model.__class__.__name__, max(id_list)))
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
            log(("没有Field: %s" %(attr_name)).decode("utf-8"))
            raise NameError
        if attr_name in self.foreignkey_items.keys():
            r = foreign_model.get(**{foreign_search_attr_name : getattr(self.model, attr_name)})
            value = getattr(r, foreign_attr_name)
            debug(("转换外键%s = %s" %(attr_name, str(value))).decode("utf-8"))
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
                #log(("记录已存在，跳过......").decode("utf-8"))

    def update(self, id=0, **kwargs):
        _id = id
        if _id:
            self.model.update(**kwargs).where(id=_id).execute()
            log(("更新记录%d" %(_id)).decode("utf-8"))

    #@classmethod
    def add(self):
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.save()
        return self.model.id


#Factory Database Models
class BoolDataPoint_Table(TableBase):
    """操作表BoolDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = BoolDataPoint()
        super(BoolDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')


class EnumDataPoint_Table(TableBase):
    """操作表EnumDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = EnumDataPoint()
        super(EnumDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')


class FloatDataPoint_Table(TableBase):
    """操作表FloatDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = FloatDataPoint()
        super(FloatDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')
        self.convert_foreignkey('quantitytype', QuantityType, 'name', 'id')


class IntDataPoint_Table(TableBase):
    """操作表IntDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = IntDataPoint()
        super(IntDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')
        self.convert_foreignkey('quantitytype', QuantityType, 'name', 'id')
        if self.model.type not in ['I16', 'I32', 'U16', 'U32', 'U8']:
            log(('IntDataPoint的Type必须为I16, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


class StringDataPoint_Table(TableBase):
    """操作表StringDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = StringDataPoint()
        super(StringDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')


class Observer_Table(TableBase):
    """操作表Observer"""
    def __init__(self, *args, **kwargs):
        self.model = Observer()
        super(Observer_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('taskid', Task, 'name', 'id')
        self.delete_attr(['comment', 'subjectid', 'constructorargs'])


class ObserverSubjects_Table(TableBase):
    """操作表ObserverSubjects"""
    def __init__(self, *args, **kwargs):
        self.model = ObserverSubjects()
        super(ObserverSubjects_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('subjectid', Subject, 'name', 'id')
        self.convert_foreignkey('observerid', Observer, 'name', 'id')
        self.convert_foreignkey('subjectrelationid', SubjectRelation, 'name', 'id')
        self.convert_foreignkey('subjectaccess', SubjectAccessType, 'name', 'id')


class Subject_Table(TableBase):
    """操作表Subject
    save : '-', 'All', 'Value'
    """
    def __init__(self, *args, **kwargs):
        self.model = Subject()
        super(Subject_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('typeid', SubjectTypes, 'name', 'id')
        self.convert_foreignkey('Save', SaveTypes, 'name', 'id')
        self.convert_foreignkey('flashblock', FlashBlockTypes, 'name', 'id')


class SubjectRelation_Table(TableBase):
    """操作表SubjectRelation"""
    def __init__(self, *args, **kwargs):
        """
        SubjectRelation.name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
        """
        self.model = SubjectRelation()
        super(SubjectRelation_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('observertypeid', ObserverType, 'name', 'id')


class VectorDataPoint_Table(TableBase):
    """操作表VectorDataPoint"""
    def __init__(self, *args, **kwargs):
        self.model = VectorDataPoint()
        super(VectorDataPoint_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject, 'name', 'id')
        if self.model.type not in ['Bool', 'Double', 'EventLog', 'Float', 'I32', 'U16', 'U32', 'U8']:
            log(('VectorDataPoint的Type必须为Bool, Double, EventLog, Float, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


#Display Database Models
class Display_Table(TableBase):
    """操作表Display"""
    def __init__(self, *args, **kwargs):
        self.model = Display()
        super(Display_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('rootgroupid', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('name', Strings, 'string', 'id')

class DisplayComponent_Table(TableBase):
    """操作表DisplayComponent"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayComponent()
        super(DisplayComponent_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('componenttype', DisplayComponentTypes, 'name', 'id')
        #self.convert_foreignkey('displayid', Display, 'name', 'id')


class DisplayLabel_Table(TableBase):
    """操作表DisplayLabel"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayLabel()
        super(DisplayLabel_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('stringid', StringDefines, 'definename', 'id')


class DisplayListView_Table(TableBase):
    """操作表DisplayLabel"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayListView()
        super(DisplayListView_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('nextlistid', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('prevlistid', DisplayComponent, 'name', 'id')


class DisplayListViewItem_Table(TableBase):
    """操作表DisplayListViewItem"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewItem()
        super(DisplayListViewItem_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('listviewid', DisplayComponent, 'name', 'id')
        self.get_max_id()

    def get_max_id(self):
        #找出同一个listview下的item有多少个，选出最大的index
        r = DisplayListViewItem.select().where(listviewid=self.model.listviewid)
        idx_list = []
        for i in r:
            idx_list.append(i.index)
        max_idx = max(idx_list)
        log("max index in DisplayListViewItem table and id=%d is %d" %(self.model.listviewid, max_idx))
        self.model.index = max_idx + 1

    def get_listviewid_index(self):
        return self.model.listviewid, self.model.index


class DisplayListViewItemComponents_Table(TableBase):
    """操作表DisplayListViewItemComponents"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewItemComponents()
        super(DisplayListViewItemComponents_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('componentid', DisplayComponent, 'name', 'id')


class DisplayNumberQuantity_Table(TableBase):
    """操作表DisplayNumberQuantity"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayNumberQuantity()
        super(DisplayNumberQuantity_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('quantitytype', QuantityType, 'name', 'id')
        self.convert_foreignkey('numberfontid', DisplayFont, 'fontname', 'id')
        self.convert_foreignkey('quantityfontid', DisplayFont, 'fontname', 'id')


class DisplayObserverSingleSubject_Table(TableBase):
    """操作表DisplayObserverSingleSubject"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayObserverSingleSubject()
        super(DisplayObserverSingleSubject_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('subjectid', Subject, 'name', 'id')
        self.convert_foreignkey('subjectaccess', SubjectAccessType, 'name', 'id')


class QuantityType_Table(TableBase):
    """操作表QuantityType"""
    def __init__(self, *args, **kwargs):
        self.model = QuantityType()
        super(QuantityType_Table, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()

    def get_max_id(self):
        r = self.model.select()
        id_list = []
        for i in r:
            id_list.append(i.id)
        id_list.sort()
        #最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
        self.model.id = id_list[-2] + 1
        log("new quantitytype id is: %d" % (self.model.id))

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.id = stored_id
        self.model.save()
        return self.model.id


class DisplayText_Table(TableBase):
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
        self.model = DisplayText()
        super(DisplayText_Table, self).__init__(self.model, *args, **kwargs)
        self.model.align = aligns[kwargs['align']]
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('fontid', DisplayFont, 'fontname', 'id')

    def add(self):
        """id在这张表里是唯一的，用id检查记录是否存在"""
        #r = self.model.get(id=self.model.id)
        r = self.model.select().where(id=self.model.id)
        if r:
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.save()
        return self.model.id


#Language Database
class StringDefines_Table(TableBase):
    """操作表StringDefines"""
    def __init__(self, *args, **kwargs):
        self.model = StringDefines()
        super(StringDefines_Table, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()
        self.convert_foreignkey('typeid', StringTypes, 'type', 'id')
        self.delete_attr(['location', 'ukdescription', 'displaynumbers'])

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.id = stored_id
        self.model.save()
        return self.model.id


class Strings_Table(TableBase):
    def __init__(self, *args, **kwargs):
        self.model = Strings()
        super(Strings_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('languageid', Languages, 'language', 'id')
        self.get_strings_max_id(kwargs['string'])

    def get_strings_max_id(self, str):
        r = Strings.select().where(string=str)
        if r:
            for i in r:
                if i.id:
                    self.model.id = i.id
                    log("string %s exist, id is %d" % (str, i.id))
                    return
        self.get_max_id()


class StringTypes_Table(TableBase):
    def __init__(self, *args, **kwargs):
        self.model = StringTypes()
        super(StringTypes_Table, self).__init__(self.model, *args, **kwargs)


class Languages_Table(TableBase):
    def __init__(self, *args, **kwargs):
        self.model = Languages()
        super(Languages_Table, self).__init__(self.model, *args, **kwargs)
