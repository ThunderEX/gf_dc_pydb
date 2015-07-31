# -*- coding: utf-8 -*-
from util.peewee import *
from util.log import *
from util.prettytable import PrettyTable
from models import *


class BaseTable(object):

    ''' 所有表的基类 '''

    def __init__(self, model, *args, **kwargs):
        '''
            初始化

        :param model: model类
        :param *args: 暂时没用
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
        for k, v in defaults.items():
            if k not in kwargs.keys() and hasattr(self.model, k):
                setattr(self.model, k, v)

    def delete_attr(self, attr_list=None):
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
        if attr_list is None:
            attr_list = ['Comment']
        for attr in attr_list:
            if hasattr(self.model, attr) and getattr(self.model, attr) == None:
                # print self.model._meta.fields[attr]
                if attr in self.model._meta.fields.keys():
                    self.model._meta.fields.pop(attr)

    def get_foreignkey_items(self, **kwargs):
        """查找外键，存入字典里"""
        field_types = self.model.get_field_type()
        foreignkey_items = []
        for k, v in kwargs.items():
            if hasattr(self.model, k):
                # 如果类型不同，则提取外键（一般是用描述性字符串代替外键的id）
                if not isinstance(v, field_types[k]):
                    foreignkey_items.append(k)
        return foreignkey_items

    def get_max_id(self):
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

    def query(self, suppress=False, **kwargs):
        _id = id
        field_dict = self.model.get_field_dict()
        field_names = field_dict.keys()
        #简单排序，让id在第一位
        if 'id' in field_names:
            id_index = field_names.index('id')
            if id_index is not 0:
                field_names[id_index] = field_names[0]
                field_names[0] = 'id'
        table = PrettyTable(field_names)
        if (kwargs):
            results = self.model.select().where(**kwargs)
        else:
            results = self.model.select()
        if results:
            for result in results:
                olist = [getattr(result, field) for field in field_names]
                table.add_row(olist)
        if not suppress:
            log(table)
        return results

    def update(self, id=0, **kwargs):
        _id = id
        if _id:
            self.model.update(**kwargs).where(id=_id).execute()
            debug(("表%s成功更新记录，id=%d!" % ((self.model._meta.db_table), _id)).decode('utf-8'))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            #debug(("更新记录%d" %(_id)).decode("utf-8"))

    def check_exist(self):
        if self.model.check_exist():
            return True
        return False

    def add(self):
        if self.check_exist():
            #log(("记录已存在，跳过......").decode("utf-8"))
            debug(("内容=%s" % (str(self.model.get_field_dict()))).decode('utf-8'))
            return 0
        else:
            self.model.save()
            return self.model.id


# Factory Database
class AlarmConfig(BaseTable):

    """操作表AlarmConfig"""

    def __init__(self, *args, **kwargs):
        self.model = AlarmConfig_Model()
        super(AlarmConfig, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('AlarmConfigId', Subject_Model, 'Name', 'id')
        #self.convert_foreignkey('AlarmType', SubjectTypes_Model, 'Name', 'id', force=True)
        self.convert_foreignkey('AlarmCriteria', AlarmCriteriaType_Model, 'name', 'value', force=True)
        self.convert_foreignkey('QuantityTypeId', QuantityType_Model, 'Name', 'id')


class AlarmCriteriaType(BaseTable):

    """操作表AlarmCriteriaType"""

    def __init__(self, *args, **kwargs):
        self.model = AlarmCriteriaType_Model()
        super(AlarmCriteriaType, self).__init__(self.model, *args, **kwargs)


class AlarmDataPoint(BaseTable):

    """操作表AlarmDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = AlarmDataPoint_Model()
        super(AlarmDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('AlarmConfigId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('AlarmConfig2Id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('ErroneousUnitTypeId', ErroneousUnitType_Model, 'Name', 'id')
        # TODO 貌似这里需要多转了一次，用StringDefines里的StringId从DisplayAlarmStrings得到AlarmId
        #self.convert_foreignkey('AlarmId', DisplayAlarmStrings_Model, 'StringId', 'AlarmId')
        r = StringDefines_Model.get(**{'DefineName': getattr(self.model, 'AlarmId')})
        value = getattr(r, 'id')     #得到StringDefines的id
        r = DisplayAlarmStrings_Model.get(**{'StringId': value})
        value = getattr(r, 'AlarmId')     #得到DisplayAlarmStrings的AlarmId
        setattr(self.model, 'AlarmId', value)


class AlarmPresentType(BaseTable):

    """操作表AlarmPresentType"""

    def __init__(self, *args, **kwargs):
        self.model = AlarmPresentType_Model()
        super(AlarmPresentType, self).__init__(self.model, *args, **kwargs)


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


class EnumTypes(BaseTable):

    """操作表EnumTypes"""

    def __init__(self, *args, **kwargs):
        self.model = EnumTypes_Model()
        super(EnumTypes, self).__init__(self.model, *args, **kwargs)


class ErroneousUnitType(BaseTable):

    """操作表ErroneousUnitType"""

    def __init__(self, *args, **kwargs):
        self.model = ErroneousUnitType_Model()
        super(ErroneousUnitType, self).__init__(self.model, *args, **kwargs)


class FlashBlockTypes(BaseTable):

    """操作表FlashBlockTypes"""

    def __init__(self, *args, **kwargs):
        self.model = FlashBlockTypes_Model()
        super(FlashBlockTypes, self).__init__(self.model, *args, **kwargs)


class FloatDataPoint(BaseTable):

    """操作表FloatDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = FloatDataPoint_Model()
        super(FloatDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')


class GeniAppIf(BaseTable):

    """操作表GeniAppIf"""

    def __init__(self, *args, **kwargs):
        self.model = GeniAppIf_Model()
        super(GeniAppIf, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('SubjectId', Subject_Model, 'Name', 'id')
        self.convert_foreignkey('GeniConvertId', GeniConvert_Model, 'Comment', 'id')


class GeniConvert(BaseTable):

    """操作表GeniConvert"""

    def __init__(self, *args, **kwargs):
        self.model = GeniConvert_Model()
        super(GeniConvert, self).__init__(self.model, *args, **kwargs)


class IntDataPointTypes(BaseTable):

    """操作表IntDataPointTypes"""

    def __init__(self, *args, **kwargs):
        self.model = IntDataPointTypes_Model()
        super(IntDataPointTypes, self).__init__(self.model, *args, **kwargs)


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


class Observer(BaseTable):

    """操作表Observer"""

    def __init__(self, *args, **kwargs):
        #TODO Bug！ 有的Observer用到ConstructorArgs，有的用不到，但由于delete_attr引起的bug，会导致前面用不到的Observer把ConstructorArgs删掉了，后面加不上去。这个在peewee的meta里，不懂怎么处理的。
        #现在只能让用到ConstructorArgs的Observer放在前面，用不到的放在后面
        self.model = Observer_Model()
        #super(Observer, self).__init__(self.model, *args, **kwargs)
        self.fill_fields(**kwargs)
        self.foreignkey_items = ['TaskId']
        if hasattr(self.model, 'ConstructorArgs') and getattr(self.model, 'ConstructorArgs') != None:
            #log(self.model._meta.get_field_by_name('ConstructorArgs'))
            saved_constructor_args = self.model._meta.get_field_by_name('ConstructorArgs')
        default_list = ['Comment', 'SubjectId', 'ConstructorArgs']
        if len(default_list) != 0:
            self.delete_attr(default_list)
        if hasattr(self.model, 'ConstructorArgs') and getattr(self.model, 'ConstructorArgs') != None:
            self.model._meta.fields['ConstructorArgs'] = saved_constructor_args
        self.convert_foreignkey('TaskId', Task_Model, 'Name', 'id')


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


class QuantityType(BaseTable):

    """操作表QuantityType"""

    def __init__(self, *args, **kwargs):
        self.model = QuantityType_Model()
        super(QuantityType, self).__init__(self.model, *args, **kwargs)
        self.get_max_id()

    def get_max_id(self):
        r = self.model.select()
        id_list = [i.id for i in r]
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


class ResetType(BaseTable):

    """操作表ResetType"""

    def __init__(self, *args, **kwargs):
        self.model = ResetType_Model()
        super(ResetType, self).__init__(self.model, *args, **kwargs)


class SaveTypes(BaseTable):

    """操作表SaveTypes"""

    def __init__(self, *args, **kwargs):
        self.model = SaveTypes_Model()
        super(SaveTypes, self).__init__(self.model, *args, **kwargs)


class StringDataPoint(BaseTable):

    """操作表StringDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = StringDataPoint_Model()
        super(StringDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')


class Subject(BaseTable):

    """ 操作表Subject """

    def __init__(self, *args, **kwargs):
        self.model = Subject_Model()
        super(Subject, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('TypeId', SubjectTypes_Model, 'Name', 'id')
        self.convert_foreignkey('Save', SaveTypes_Model, 'Name', 'id')
        self.convert_foreignkey('FlashBlock', FlashBlockTypes_Model, 'Name', 'id')


class SubjectAccessType(BaseTable):

    """操作表SubjectAccessType"""

    def __init__(self, *args, **kwargs):
        self.model = SubjectAccessType_Model()
        super(SubjectAccessType, self).__init__(self.model, *args, **kwargs)


class SubjectRelation(BaseTable):

    """操作表SubjectRelation"""

    def __init__(self, *args, **kwargs):
        """
        SubjectRelation.name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
        """
        self.model = SubjectRelation_Model()
        super(SubjectRelation, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ObserverTypeId', ObserverType_Model, 'Name', 'id')


class SubjectTypes(BaseTable):

    """操作表SubjectTypes"""

    def __init__(self, *args, **kwargs):
        self.model = SubjectTypes_Model()
        super(SubjectTypes, self).__init__(self.model, *args, **kwargs)


class Task(BaseTable):

    """操作表Task"""

    def __init__(self, *args, **kwargs):
        self.model = Task_Model()
        super(Task, self).__init__(self.model, *args, **kwargs)


class TaskType(BaseTable):

    """操作表TaskType"""

    def __init__(self, *args, **kwargs):
        self.model = TaskType_Model()
        super(TaskType, self).__init__(self.model, *args, **kwargs)


class UserIoConfig(BaseTable):

    """操作表UserIoConfig"""

    def __init__(self, *args, **kwargs):
        self.model = UserIoConfig_Model()
        super(UserIoConfig, self).__init__(self.model, *args, **kwargs)


class VectorDataPoint(BaseTable):

    """操作表VectorDataPoint"""

    def __init__(self, *args, **kwargs):
        self.model = VectorDataPoint_Model()
        super(VectorDataPoint, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', Subject_Model, 'Name', 'id')
        if self.model.Type not in ['Bool', 'Double', 'EventLog', 'Float', 'I32', 'U16', 'U32', 'U8']:
            log(('VectorDataPoint的Type必须为Bool, Double, EventLog, Float, I32, U16, U32, U8').decode("utf-8"))
            raise TypeError


class VectorDataPointTypes(BaseTable):

    """操作表VectorDataPointTypes"""

    def __init__(self, *args, **kwargs):
        self.model = VectorDataPointTypes_Model()
        super(VectorDataPointTypes, self).__init__(self.model, *args, **kwargs)


# Display Database
class Colours(BaseTable):

    """操作表Colours"""

    def __init__(self, *args, **kwargs):
        self.model = Colours_Model()
        super(Colours, self).__init__(self.model, *args, **kwargs)


class Display(BaseTable):

    """操作表Display"""

    def __init__(self, *args, **kwargs):
        self.model = Display_Model()
        super(Display, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('RootGroupId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('Name', Strings_Model, 'String', 'id')


class DisplayAlarmStrings(BaseTable):

    """操作表DisplayAlarmStrings"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayAlarmStrings_Model()
        super(DisplayAlarmStrings, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')
        #self.set_alarm_id()

    def set_alarm_id(self):
        r = self.model.select()
        id_list = [i.AlarmId for i in r]
        debug("Max AlarmId in %s table is %d" % (self.model.__class__.__name__, max(id_list)))
        self.model.AlarmId = max(id_list) + 1   #得到最大AlarmId并+1

class DisplayAvailable(BaseTable):

    """操作表DisplayAvailable"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayAvailable_Model()
        super(DisplayAvailable, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')

class DisplayComponent(BaseTable):

    """操作表DisplayComponent"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayComponent_Model()
        super(DisplayComponent, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ComponentType', DisplayComponentTypes_Model, 'Name', 'id')
        self.convert_foreignkey('HelpString', StringDefines_Model, 'DefineName', 'id')
        #self.convert_foreignkey('displayid', Display_Model, 'Name', 'id')


class DisplayComponentColour(BaseTable):

    """操作表DisplayComponentColour"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayComponentColour_Model()
        super(DisplayComponentColour, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayComponentTypes(BaseTable):

    """操作表DisplayComponentTypes"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayComponentTypes_Model()
        super(DisplayComponentTypes, self).__init__(self.model, *args, **kwargs)


class DisplayFont(BaseTable):

    """操作表DisplayFont"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayFont_Model()
        super(DisplayFont, self).__init__(self.model, *args, **kwargs)


class DisplayFrame(BaseTable):

    """操作表DisplayFrame"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayFrame_Model()
        super(DisplayFrame, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayImage(BaseTable):

    """操作表DisplayImage"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayImage_Model()
        super(DisplayImage, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('ComponentId', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('ImagesId', DisplayImages_Model, 'Name', 'id')


class DisplayImages(BaseTable):

    """操作表DisplayImages"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayImages_Model()
        super(DisplayImages, self).__init__(self.model, *args, **kwargs)


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
        idx_list = [i.Index for i in r]
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


class DisplayMenuTab(BaseTable):

    """操作表DisplayMenuTab"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayMenuTab_Model()
        super(DisplayMenuTab, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayModeCheckBox(BaseTable):

    """操作表DisplayModeCheckBox"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayModeCheckBox_Model()
        super(DisplayModeCheckBox, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayMultiNumber(BaseTable):

    """操作表DisplayMultiNumber"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayMultiNumber_Model()
        super(DisplayMultiNumber, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayNumber(BaseTable):

    """操作表DisplayNumber"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayNumber_Model()
        super(DisplayNumber, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')


class DisplayNumberQuantity(BaseTable):

    """操作表DisplayNumberQuantity"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayNumberQuantity_Model()
        super(DisplayNumberQuantity, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('QuantityType', QuantityType_Model, 'Name', 'id')
        self.convert_foreignkey('NumberFontId', DisplayFont_Model, 'FontName', 'id')
        self.convert_foreignkey('QuantityFontId', DisplayFont_Model, 'FontName', 'id')


class DisplayObserver(BaseTable):

    """操作表DisplayObserver"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayObserver_Model()
        super(DisplayObserver, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')
        self.convert_foreignkey('ObserverId', Observer_Model, 'Name', 'id')


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

class DisplayUnitStrings(BaseTable):

    """操作表DisplayUnitStrings"""

    def __init__(self, *args, **kwargs):
        self.model = DisplayUnitStrings_Model()
        super(DisplayUnitStrings, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('UnitType', ErroneousUnitType_Model, 'Name', 'id')
        self.convert_foreignkey('StringId', StringDefines_Model, 'DefineName', 'id')

class WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay(BaseTable):

    """操作表WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay"""

    def __init__(self, *args, **kwargs):
        self.model = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay_Model()
        super(WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay, self).__init__(self.model, *args, **kwargs)
        self.convert_foreignkey('id', DisplayComponent_Model, 'Name', 'id')

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
        if kwargs.has_key('String'):
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
