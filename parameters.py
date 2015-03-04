# -*- coding: utf-8 -*-
from models import *
from tables import *

Yes = True
No = False
yes = True
no = False

"""
格式：
   （表名，
    {
            filed名1：参数，
            filed名2：参数，
    }
    ),
"""

#############################################################Display部分##########################################################
h2s_level_quantity_parameters = [
    #1. 加新的单位类型
    (QuantityType, 
     {
         'Name':'Q_PARTS_PER_MILLION',
     }
     ),
    #2. 加ppm的字符串定义
    (StringDefines, 
     {
         "DefineName" : "SID_PPM",
         "TypeId"     : "Quantity Unit",
     }
     ),
    #3. 加ppm相应的字符串
    (Strings, 
     {
         'String'     : 'ppm',
         'LanguageId' : 'DEV_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    (Strings, 
     {
         'String'     : 'ppm',
         'LanguageId' : 'UK_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    #4. SubjectRelation里的MpcUnits要加上Q_PARTS_PER_MILLION
    (SubjectRelation, 
     {
         'Name'           : 'Q_PARTS_PER_MILLION',
         'ObserverTypeId' : 'MpcUnits',
     }
     ),
]

h2s_level_label_parameters = [
    #1. 添加h2s label
    (DisplayComponent,
     {
         'Name'            : '1.1 SystemStatus l1 h2s level',
         'ComponentType'   : 'Label',
         'ParentComponent' : 0,
         'Visible'         : True,
         'ReadOnly'        : True,
         'x1'              : 0,
         'x2'              : 0,
         'y1'              : 0,
         'y2'              : 0,
         'DisplayId'       : 0,
         'HelpString'      : 0,
         'Transparent'     : False,
     }
     ),
    #2. 添加数值label
    (DisplayComponent,
     {
         'Name'            : '1.1 SystemStatus l1 h2s level nq',
         'ComponentType'   : 'NumberQuantity',
         'ParentComponent' : 0,
         'Visible'         : True,
         'ReadOnly'        : True,
         'x1'              : 0,
         'x2'              : 0,
         'y1'              : 0,
         'y2'              : 0,
         'DisplayId'       : 0,
         'HelpString'      : 0,
         'Transparent'     : False,
     }
     ),
    #3. 加字符串定义
    (StringDefines,
     {
         'DefineName' : 'SID_H2S_LEVEL',
         'TypeId'     : 'Value type',
     }
     ),
    #4. label加相应的字符串
    (Strings,
     {
         'String'     : 'H2S level',
         'LanguageId' : 'DEV_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    (Strings,
     {
         'String'     : 'H2S level',
         'LanguageId' : 'UK_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    #5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id'       : '1.1 SystemStatus l1 h2s level',
         'StringId' : 'SID_H2S_LEVEL',
     }
     ),
    #6. 定义label的text排列方式
    (DisplayText,
     {
         'id'          : '1.1 SystemStatus l1 h2s level',
         'Align'       : 'VCENTER_LEFT',
         'FontId'      : 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin'  : 2,
         'RightMargin' : 0,
         'WordWrap'    : False,
     }
     ),
    #7. 定义数值的text排列方式
    (DisplayText,
     {
         'id'          : '1.1 SystemStatus l1 h2s level nq',
         'Align'       : 'VCENTER_LEFT',
         'FontId'      : 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin'  : 0,
         'RightMargin' : 0,
         'WordWrap'    : False,
     }
     ),
    #8. 数值与新加单位'ppm'对应
    (DisplayNumberQuantity,
     {
         'id'             : '1.1 SystemStatus l1 h2s level nq',
         'QuantityType'   : 'Q_PARTS_PER_MILLION',
         'NumberOfDigits' : 3,
         'NumberFontId'   : 'DEFAULT_FONT_13_LANGUAGE_INDEP',
         'QuantityFontId' : 'DEFAULT_FONT_13_LANGUAGE_INDEP',
     }
     ),
    #9. 数值与subject对应
    #TODO 先用已有的subject数据total_energy_j_for_display
    (DisplayObserverSingleSubject,
     {
         'id'            : '1.1 SystemStatus l1 h2s level nq',
         'SubjectId'     : 'total_energy_j_for_display',
         'SubjectAccess' : 'Read',
     }
     ),
    #10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId' : '1.1 SystemStatus List 1',
     }
     ),
    #11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId' : '1.1 SystemStatus l1 h2s level',
         'ColumnIndex' : 0,
     }
     ),
    #12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId' : '1.1 SystemStatus l1 h2s level nq',
         'ColumnIndex' : 2,
     }
     ),
]

h2s_control_label_parameters = [
    #1. 添加h2s control label
    (DisplayComponent,
     {
         'Name'            : '4.2 AdvancedFunc h2scontol',
         'ComponentType'   : 'Label',
         'ParentComponent' : 0,
         'Visible'         : True,
         'ReadOnly'        : True,
         'x1'              : 0,
         'x2'              : 0,
         'y1'              : 0,
         'y2'              : 0,
         #'DisplayId'       : 0,         #DisplayComponent里DisplayId为0，需要指向要显示的group
         'HelpString'      : 0,
         'Transparent'     : False,
     }
     ),
    #2. 加字符串定义
    (StringDefines,
     {
         'DefineName' : 'SID_H2S_CONTROL',
         'TypeId'     : 'Display name',
     }
     ),
    #3. label加相应的字符串
    (Strings,
     {
         'String'     : 'H2S Control',
         'LanguageId' : 'DEV_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    (Strings,
     {
         'String'     : 'H2S Control',
         'LanguageId' : 'UK_LANGUAGE',
         'Status'     : 'UnEdit',
     }
     ),
    #4. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id'       : '4.2 AdvancedFunc h2scontol',
         'StringId' : 'SID_H2S_CONTROL',
     }
     ),
    #5. 定义label的text排列方式
    (DisplayText,
     {
         'id'          : '4.2 AdvancedFunc h2scontol',
         'Align'       : 'VCENTER_LEFT',
         'FontId'      : 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin'  : 8,
         'RightMargin' : 0,
         'WordWrap'    : False,
     }
     ),
    #6. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId' : '4.2 AdvancedFunc List 1',
     }
     ),
    #7. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId' : '4.2 AdvancedFunc h2scontol',
         'ColumnIndex' : 0,
     }
     ),
]

h2s_control_group_parameters = [
    #1. 添加group，也就是另起一页
    (DisplayComponent,
     {
         'Name'            : '4.2.14 H2SContol Group',
         'ComponentType'   : 'Group',
         'ParentComponent' : 0,
         'Visible'         : True,
         'ReadOnly'        : False,
         'x1'              : 33,
         'x2'              : 239,
         'y1'              : 0,
         'y2'              : 305,
         'DisplayId'       : 0,
         'HelpString'      : 0,
         'Transparent'     : False,
     }
     ),
]

h2s_control_display_parameters = [
    #Display
    (Display,
     {
         'RootGroupId': '4.2.14 H2SContol Group',
         'DisplayNumber': '4.2.14',
         'Name': 'H2S Control',
         #'FocusComponentId':0,   #set from listview later
         'AbleToShow': True,
         'Show':False,
         'FirstWizardDisplay':False,
     }
     ),
]

h2s_control_listview_parameters = [
    (DisplayComponent,
     {
         'Name'            : '4.2.14 H2SContol List',
         'ComponentType'   : 'ListView',
         #'ParentComponent' : 0,                          #set later
         'Visible'         : True,
         'ReadOnly'        : False,
         'x1'              : 15,
         'x2'              : 239,
         'y1'              : 0,
         'y2'              : 271,
         'DisplayId'       : 0,
         'HelpString'      : 0,
         'Transparent'     : False,
     }
     ),
    (DisplayListView,
     {
         'id'          : '4.2.14 H2SContol List',
         'RowHeight'   : 15,
         'SelectedRow' : 0,
         'NextListId'  : 0,  # - None -
         'PrevListId'  : 0,  # - None -
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId'  : '4.2.14 H2SContol List',
         'ColumnIndex' : 0,
         'Columnwidth' : 160,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId'  : '4.2.14 H2SContol List',
         'ColumnIndex' : 1,
         'Columnwidth' : 64,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId'  : '4.2.14 H2SContol List',
         'ColumnIndex' : 2,
         'Columnwidth' : 0,
     }
     ),
]


#############################################################Factor部分##########################################################
h2s_observer_parameters = [
    #1. 加ObserverType
    (ObserverType,
     {
         'Name'        : 'DDACtrl',
         'ShortName'   : 'DDA',
         'IsSingleton' : False,
         'IsSubject'   : False,
     }
     ),
    #2. 加Observer
    (Observer,
     {
         'Name'            : 'dosing_pump_ctrl',
         #'TypeId'          : 96,      #set from ObserverType
         'TaskId'          : 'LowPrioPeriodicTask',
         #'TaskOrder'       : None,
         #'SubjectId'       : None,
         #'ConstructorArgs' : None,
     }
     ),
]

h2s_subject_parameters = [
    #1. 加Subject
    (Subject,
     {
         'Name'       : 'dda_control_enabled',
         'TypeId'     : 'BoolDataPoint',
         'GeniAppIf'  : False,
         'Save'       : 'Value',              #save是model的函数，要用大写的Save
         'FlashBlock' : 'Config',
         'Verified'   : False,
     }
     ),
     #2. 对应的DataPoint也要添加
    (BoolDataPoint,
     {
         'id'           : 'dda_control_enabled',
         'Value'        : 0,
     }
     ),
]

h2s_observer_subject_parameters = [
    #1. 先添加SubjectRelation
    (SubjectRelation, 
     {
         'Name'           : 'dda_control_enabled'.upper(),    #必须用大写字母
         'ObserverTypeId' : 'DDACtrl',
     }
     ),
    #2. 再添加ObserverSubjects，会用到SubjectRelation添加的Name
    (ObserverSubjects, 
     {
         'SubjectId'         : 'dda_control_enabled',
         'ObserverId'        : 'dosing_pump_ctrl',
         'ObserverTypeId'    : 'DDACtrl',
         'SubjectRelationId' : 'dda_control_enabled'.upper(),
         'SubjectAccess'     : 'Read',
     }
     ),
]
#用到的SubjectPtr名字SP_DDA_DDA_CONTROL_ENABLED
SP = 'SP_' + h2s_observer_parameters[0][1]['ShortName'] + '_' + h2s_subject_parameters[0][1]['Name'].upper()

#TODO test
test_parameters = [
    (IntDataPoint,
     {
         'id'           : 'test',
         'Type'         : 'U16',
         'Min'          : '0',
         'Max'          : '0xFFFF',
         'Value'        : '0',
         'QuantityType' : 'Q_NO_UNIT',
         'Verified'     : False,
     }
     ),
]
