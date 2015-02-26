# -*- coding: utf-8 -*-
from util.peewee import *
from util.log import *
from models import *

class TableBase(object):
    """table base"""
    def __init__(self, model, *args, **kwargs):
        """init with model"""
        self.model = model
        self.fill_fields(**kwargs)
        self.foreignkey_items = self.get_foreignkey_items(**kwargs)

    def fill_fields(self, **kwargs):
        """填充各个field属性值，没有的则为None"""
        for k, v in kwargs.items():
            if hasattr(self.model, k):
                setattr(self.model, k, v)

    def fill_default_fileds(self, defaults, **kwargs):
        """填充如comment的field属性值"""
        for k, v in defaults.items():
            if k not in kwargs.keys() and hasattr(self.model, k):
                setattr(self.model, k, v)

    def delete_attr(self, attr_list):
        """ 如果MSSQL返回错误
        1. You cannot add or change a record because a related record is required in table 'Subject'
        2. xxx cannot be a zero-length string
        这是因为peewee里这些field如果不赋值，会有默认的值，例如0或''，sql语句里会有，此时要删除这些field
        要从_meta.fields里删除field
        """
        #TODO Bug:如果连续使用一张table，第二次就没有comment这个field了
        for attr in attr_list:
            if hasattr(self.model, attr) and getattr(self.model, attr) == None:
                #print self.model._meta.fields[attr]
                if self.model._meta.fields.has_key(attr):
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
        log("max id in %s table is %d" %(self.model.__class__.__name__, max(id_list)))
        self.model.id = max(id_list) + 1
    
    def convert_foreignkey(self, attr_name, foreign_model, foreign_search_attr_name, foreign_attr_name='id'):
        """ 转换外键
            attr_name: 要转换的外键field名
            foreign_model: 关联表
            foreign_search_attr_name: 关联表搜索的field
            foreign_attr_name: 得到的关联表field
        """
        if not hasattr(self.model, attr_name):
            log(("没有Field: %s" %(attr_name)).decode("utf-8"))
            raise NameError
        if attr_name in self.foreignkey_items.keys():
            r = foreign_model.get(**{foreign_search_attr_name : getattr(self.model, attr_name)})
            log(("转换外键%s" %(attr_name)).decode("utf-8"))
            setattr(self.model, attr_name, getattr(r, foreign_attr_name))

    #@classmethod
    def add(self):
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.save()

#Factory Database Models       
class Observer_Table(TableBase):
    """操作表Observer"""
    def __init__(self, *args, **kwargs):
        self.model = Observer()
        super(Observer_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('taskid', Task, 'name', 'id')
        attr_list = ['comment', 'subjectid', 'constructorargs']
        self.delete_attr(attr_list)

class ObserverSubjects_Table(TableBase):
    """操作表ObserverSubjects"""
    def __init__(self, *args, **kwargs):
        self.model = ObserverSubjects()
        super(ObserverSubjects_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('subjectid', Subject, 'name', 'id')
        self.convert_foreignkey('observerid', Observer, 'name', 'id')
        self.convert_foreignkey('subjectrelationid', SubjectRelation, 'name', 'id')
        self.convert_foreignkey('subjectaccess', SubjectAccessType, 'name', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

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
        attr_list = ['comment']
        self.delete_attr(attr_list)

class SubjectRelation_Table(TableBase):
    """操作表SubjectRelation"""
    def __init__(self, *args, **kwargs):
        """ 
        SubjectRelation.name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
        """
        self.model = SubjectRelation()
        super(SubjectRelation_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('observertypeid', ObserverType, 'name', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

#Display Database Models       
class DisplayComponent_Table(TableBase):
    """操作表DisplayComponent"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayComponent()
        super(DisplayComponent_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('componenttype', DisplayComponentTypes, 'name', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

class DisplayLabel_Table(TableBase):
    """操作表DisplayLabel"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayLabel()
        super(DisplayLabel_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('stringid', StringDefines, 'definename', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

class DisplayListViewItem_Table(TableBase):
    """操作表DisplayListViewItem"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayListViewItem()
        super(DisplayListViewItem_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('listviewid', DisplayComponent, 'name', 'id')
        self.get_max_id()
        attr_list = ['comment']
        self.delete_attr(attr_list)

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
        attr_list = ['comment']
        self.delete_attr(attr_list)

class DisplayNumberQuantity_Table(TableBase):
    """操作表DisplayNumberQuantity"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayNumberQuantity()
        super(DisplayNumberQuantity_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('quantitytype', QuantityType, 'name', 'id')
        self.convert_foreignkey('numberfontid', DisplayFont, 'fontname', 'id')
        self.convert_foreignkey('quantityfontid', DisplayFont, 'fontname', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

class DisplayObserverSingleSubject_Table(TableBase):
    """操作表DisplayObserverSingleSubject"""
    def __init__(self, *args, **kwargs):
        self.model = DisplayObserverSingleSubject()
        super(DisplayObserverSingleSubject_Table, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent, 'name', 'id')
        self.convert_foreignkey('subjectid', Subject, 'name', 'id')
        self.convert_foreignkey('subjectaccess', SubjectAccessType, 'name', 'id')
        attr_list = ['comment']
        self.delete_attr(attr_list)

class QuantityType_Table(TableBase):
    """操作表QuantityType"""
    def __init__(self, *args, **kwargs):
        self.model = QuantityType()
        super(QuantityType_Table, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()
        attr_list = ['comment']
        self.delete_attr(attr_list)

    def get_max_id(self):
        r = self.model.select()
        id_list = []
        for i in r:
            id_list.append(i.id)
        id_list.sort()
        #最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
        self.model.id = id_list[-2] + 1
        log("new quantitytype id is: %d" %(self.model.id))

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.id = stored_id 
        self.model.save()

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
        attr_list = ['comment']
        self.delete_attr(attr_list)

    def add(self):
        """id在这张表里是唯一的，用id检查记录是否存在"""
        #r = self.model.get(id=self.model.id)
        r = self.model.select().where(id=self.model.id)
        if r:
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.save()
            
#Language Database 
class StringDefines_Table(TableBase):
    """操作表StringDefines"""
    def __init__(self, *args, **kwargs):
        self.model = StringDefines()
        super(StringDefines_Table, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()
        self.convert_foreignkey('typeid', StringTypes, 'type', 'id')
        attr_list = ['location', 'ukdescription', 'displaynumbers']
        self.delete_attr(attr_list)

    def add(self):
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            return
        self.model.id =stored_id 
        self.model.save()

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
                    log("string %s exist, id is %d" %(str, i.id))
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

