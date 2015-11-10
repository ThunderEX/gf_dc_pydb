# -*- coding: utf-8 -*-
from util.peewee import *
from util.log import *
from util.prettytable import PrettyTable
from models import *

def AutoInit(cls):
    old_init = cls.__init__
    def new_init(self, *args, **kwargs):
        self.model = globals()[self.__class__.__name__+"_Model"]()
        old_init(self, *args, **kwargs)
        self.init(self, *args, **kwargs)
    cls.__init__ = new_init
    return cls


class BaseTable(object):

    ''' 所有表的基类 '''

    def __init__(self, *args, **kwargs):
        '''
            初始化

        :param *args: 暂时没用
        :param **kwargs: fields(field=value)
        :return:
        '''
        self.fill_fields(**kwargs)
        self.foreignkey_items = self.get_foreignkey_items(**kwargs)

    def init(self, *args, **kwargs):
        pass

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

    def get_foreignkey_items(self, **kwargs):
        '''
            查找外键，存入字典里
        
        :param **kwargs: fields(field=value)
        :return: 外键名形成的list
        '''
        field_types = self.model.get_field_type()
        # 如果属性存在且类型不同，则提取外键（一般是用描述性字符串代替外键的id）
        foreignkey_items = [k for k, v in kwargs.items() if hasattr(self.model, k) and not isinstance(v, field_types[k])]
        return foreignkey_items

    def get_max_id(self):
        '''
            得到id的最大值并将id的值设为最大值+1
        :return:
        '''
        r = self.model.select()
        id_list = [i.id for i in r]
        debug("Max id in %s table is %d" % (self.model.__class__.__name__, max(id_list)))
        self.model.id = max(id_list) + 1

    def convert_foreignkey(self, attr_name, foreign_model, foreign_attr_from, foreign_attr_to = 'id', force = False):
        '''
            转换外键

        :param attr_name: 要转换的外键field名
        :param foreign_model: 关联表
        :param foreign_attr_from: 关联表搜索的field
        :param foreign_attr_to: 得到的关联表field
        :force 强制转换外键，不论该键是不是在foreignkey_items里
        '''
        if not hasattr(self.model, attr_name):
            log(("没有Field: %s" % (attr_name)).decode("utf-8"))
            raise NameError
        if attr_name in self.foreignkey_items and force is not True:
            r = foreign_model.get(**{foreign_attr_from: getattr(self.model, attr_name)})
            value = getattr(r, foreign_attr_to)
            debug(("转换外键%s = %s" % (attr_name, str(value))).decode("utf-8"))
            setattr(self.model, attr_name, value)
        elif force is True:
            r = foreign_model.get(**{foreign_attr_from: getattr(self.model, attr_name)})
            value = getattr(r, foreign_attr_to)
            debug(("转换外键%s = %s" % (attr_name, str(value))).decode("utf-8"))
            setattr(self.model, attr_name, value)
        else:
            debug("不存在键%s" % (attr_name))

    def query(self, suppress_log=False, **kwargs):
        '''
            查询数据库
        
        :param suppress_log: 不输出log
        :param **kwargs: 查询的条件
        :return: 
        '''
        field_dict = self.model.get_field_dict()
        field_names = field_dict.keys()
        #简单排序，让id在第一位
        if 'id' in field_names:
            id_index = field_names.index('id')
            if id_index is not 0:
                field_names[id_index], field_names[0] = field_names[0], 'id'
        table = PrettyTable(field_names)
        if (kwargs):
            results = self.model.select().where(**kwargs)
        else:
            results = self.model.select()
        if results:
            for result in results:
                olist = [getattr(result, field) for field in field_names]
                table.add_row(olist)
        if not suppress_log:
            log(table)
        return results

    def update(self, id=0, **kwargs):
        '''
            根据id更新数据库
        
        :param id: id
        :param **kwargs: 更新的内容
        :return: 
        '''
        _id = id
        if _id:
            self.model.update(**kwargs).where(id=_id).execute()
            debug(("表%s成功更新记录，id=%d!" % ((self.model._meta.db_table), _id)).decode('utf-8'))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            #debug(("更新记录%d" %(_id)).decode("utf-8"))

    def check_exist(self):
        '''
            检查记录是否存在
        :return: True - 如果存在， False - 不存在
        '''
        return True if self.model.check_exist() else False

    def add(self):
        '''
            添加数据
        :return: 插入数据后的id
        '''
        if self.check_exist():
            debug(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return 0
        else:
            self.model.save()
            return self.model.id


# Factory Database
@AutoInit
class AlarmConfig(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('AlarmConfigId', Subject_Model, 'Name', 'id')
        #self.convert_foreignkey('AlarmType', SubjectTypes_Model, 'Name', 'id', force=True)
        self.convert_foreignkey('AlarmCriteria', AlarmCriteriaType_Model, 'name', 'value', force=True)
        self.convert_foreignkey('QuantityTypeId', QuantityType_Model, 'Name', 'id')


@AutoInit
class AlarmCriteriaType(BaseTable):
    pass


@AutoInit
class AlarmDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('AlarmConfigId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('AlarmConfig2Id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('ErroneousUnitTypeId', ErroneousUnitType_Model, 'Name', 'id')
        r = StringDefines_Model.get(**{'DefineName': getattr(self.model, 'AlarmId')})
        value = getattr(r, 'id')     #得到StringDefines的id
        r = DisplayAlarmStrings_Model.get(**{'StringId': value})
        value = getattr(r, 'AlarmId')     #得到DisplayAlarmStrings的AlarmId
        setattr(self.model, 'AlarmId', value)


@AutoInit
class AlarmPresentType(BaseTable):
    pass


@AutoInit
class BoolDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


@AutoInit
class EnumDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


@AutoInit
class EnumTypes(BaseTable):
    pass


@AutoInit
class ErroneousUnitType(BaseTable):
    pass


@AutoInit
class FlashBlockTypes(BaseTable):
    pass


@AutoInit
class FloatDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')


@AutoInit
class GeniAppIf(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('GeniConvertId', GeniConvert_Model, 'Comment', 'id')


@AutoInit
class GeniConvert(BaseTable):
    pass


@AutoInit
class IntDataPointTypes(BaseTable):
    pass


@AutoInit
class IntDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')
        if self.model.Type not in ['I16', 'I32', 'U16', 'U32', 'U8']:
            log(('IntDataPoint的Type必须为I16, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError
        if self.model.Min and not isinstance(self.model.Min, str):
            log(('IntDataPoint的Min必须为string类型').decode("utf-8"))
            raise TypeError
        if self.model.Max and not isinstance(self.model.Max, str):
            log(('IntDataPoint的Max必须为string类型').decode("utf-8"))
            raise TypeError
        if self.model.Value and not isinstance(self.model.Value, str):
            log(('IntDataPoint的Value必须为string类型').decode("utf-8"))
            raise TypeError


@AutoInit
class Observer(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('TaskId', Task_Model, 'Name', 'id')


@AutoInit
class ObserverSubjects(BaseTable):
    def init(self, *args, **kwargs):
        if kwargs.has_key('SubjectAccess') and kwargs['SubjectAccess'] not in ['Not decided', 'Write', 'Read', 'Read/Write']:
            log(('DisplayObserverSingleSubject的SubjectAccess必须为Not decided, Write, Read, Read/Write').decode("utf-8"))
            raise NameError
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('ObserverId', Observer_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectRelationId', SubjectRelation_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectAccess', SubjectAccessType_Model, 'Name', 'id')


@AutoInit
class ObserverType(BaseTable):
    pass


@AutoInit
class QuantityType(BaseTable):
    def init(self, *args, **kwargs):
        self.get_max_id()

    def get_max_id(self):
        r = self.model.select()
        id_list = [i.id for i in r]
        id_list.sort()
        # 最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
        self.model.id = id_list[-2] + 1
        debug("new QuantityType id is: %d" % (self.model.id))

    def add(self):
        ''' 在检查是否存在记录时需要去掉id来检查 '''
        stored_id = self.model.id
        self.model.id = None
        if self.model.check_exist():
            log(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return
        self.model.id = stored_id
        self.model.save()
        return self.model.id


@AutoInit
class ResetType(BaseTable):
    pass


@AutoInit
class SaveTypes(BaseTable):
    pass


@AutoInit
class StringDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


@AutoInit
class Subject(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('TypeId', SubjectTypes_Model, 'Name', 'id')
        self.convert_foreignkey('Save', SaveTypes_Model, 'Name', 'id')
        self.convert_foreignkey('FlashBlock', FlashBlockTypes_Model, 'Name', 'id')


@AutoInit
class SubjectAccessType(BaseTable):
    pass


@AutoInit
class SubjectRelation(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ObserverTypeId', ObserverType_Model, 'Name', 'id')


@AutoInit
class SubjectTypes(BaseTable):
    pass


@AutoInit
class Task(BaseTable):
    pass


@AutoInit
class TaskType(BaseTable):
    pass


@AutoInit
class UserIoConfig(BaseTable):
    pass


@AutoInit
class VectorDataPoint(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        if self.model.Type not in ['Bool', 'Double', 'EventLog', 'Float', 'I32', 'U16', 'U32', 'U8']:
            log(('VectorDataPoint的Type必须为Bool, Double, EventLog, Float, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


@AutoInit
class VectorDataPointTypes(BaseTable):
    pass


# Display Database
@AutoInit
class Colours(BaseTable):
    pass


@AutoInit
class Display(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('RootGroupId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('Name', Strings_Model, 'String', 'id')


@AutoInit
class DisplayAlarmStrings(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')


@AutoInit
class DisplayAvailable(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayComponent(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ComponentType', DisplayComponentTypes_Model, 'Name', 'id')
        self.convert_foreignkey('HelpString', StringDefines_Model, 'DefineName', 'id')
        #self.convert_foreignkey('displayid', Display_Model, 'Name', 'id')


@AutoInit
class DisplayComponentColour(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayComponentTypes(BaseTable):
    pass


@AutoInit
class DisplayFont(BaseTable):
    pass


@AutoInit
class DisplayFrame(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayImage(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ComponentId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('ImagesId', DisplayImages_Model, 'Name', 'id')


@AutoInit
class DisplayImages(BaseTable):
    pass


@AutoInit
class DisplayLabel(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')


@AutoInit
class DisplayListView(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('NextListId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('PrevListId', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayListViewColumns(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ListViewId', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayListViewItem(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ListViewId', DisplayComponent_Model, 'Name', 'id')
        self.get_max_id()

    def get_max_id(self):
        # 找出同一个listview下的item有多少个，选出最大的index
        r = DisplayListViewItem_Model.select().where(ListViewId=self.model.ListViewId)
        idx_list = [i.Index for i in r]
        if len(idx_list):
            max_idx = max(idx_list)
            debug("max index in DisplayListViewItem table and id=%d is %d" % (self.model.ListViewId, max_idx))
            self.model.Index = max_idx + 1
        else:
            self.model.Index = 0


@AutoInit
class DisplayListViewItemComponents(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('ComponentId', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayMenuTab(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayModeCheckBox(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayMultiNumber(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayNumber(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayNumberQuantity(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')
        self.convert_foreignkey('NumberFontId', DisplayFont_Model, 'FontName', 'id')
        self.convert_foreignkey('QuantityFontId', DisplayFont_Model, 'FontName', 'id')


@AutoInit
class DisplayObserver(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('ObserverId', Observer_Model, 'Name', 'id')


@AutoInit
class DisplayObserverSingleSubject(BaseTable):
    def init(self, *args, **kwargs):
        if kwargs.has_key('SubjectAccess') and kwargs['SubjectAccess'] not in ['Not decided', 'Write', 'Read', 'Read/Write']:
            log(('DisplayObserverSingleSubject的SubjectAccess必须为Not decided, Write, Read, Read/Write').decode("utf-8"))
            raise NameError
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('SubjectAccess', SubjectAccessType_Model, 'Name', 'id')


@AutoInit
class DisplayOnOffCheckBox(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


@AutoInit
class DisplayText(BaseTable):
    def init(self, *args, **kwargs):
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
        self.model.Align = aligns[kwargs['Align']]
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('FontId', DisplayFont_Model, 'FontName', 'id')

    def add(self):
        """id在这张表里是唯一的，用id检查记录是否存在"""
        r = self.model.select().where(id=self.model.id)
        if r:
            for i in r:
                log(("id=%d的记录已存在，跳过......" % (i.id)).decode("utf-8"))
                debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
                return
        self.model.save()
        return self.model.id


@AutoInit
class DisplayUnitStrings(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('UnitType', ErroneousUnitType_Model, 'Name', 'id')
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')


@AutoInit
class WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


# Language Database
@AutoInit
class StringDefines(BaseTable):
    def init(self, *args, **kwargs):
        self.get_max_id()
        self.convert_foreignkey('TypeId', StringTypes_Model, 'Type', 'id')

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


@AutoInit
class Strings(BaseTable):
    def init(self, *args, **kwargs):
        self.convert_foreignkey('LanguageId', Languages_Model, 'Language', 'id')
        if 'String' in kwargs:
            self.get_strings_max_id(kwargs['String'])

    def get_strings_max_id(self, str):
        '''
            检查是否已有字符串，如果有，则用相同的id，没有取最大id+1
        
        :param str: 用来查询的字符串
        '''
        r = Strings_Model.select().where(String=str)
        if r:
            for i in r:
                if i.id:
                    self.model.id = i.id
                    debug("string %s exist, id is %d" % (str, i.id))
                    return
        self.get_max_id()

    def update(self, id=0, language_id=0, **kwargs):
        '''
            根据id更新数据库
        
        :param id: id
        :param **kwargs: 更新的内容
        :return: 
        '''
        _id = id
        if _id:
            self.model.update(**kwargs).where(id=_id, LanguageId=language_id).execute()
            debug(("表%s成功更新记录，id=%d!" % ((self.model._meta.db_table), _id)).decode('utf-8'))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            #debug(("更新记录%d" %(_id)).decode("utf-8"))
    


@AutoInit
class StringTypes(BaseTable):
    pass


@AutoInit
class Languages(BaseTable):
    pass
