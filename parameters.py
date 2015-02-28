# -*- coding: utf-8 -*-
from models import *
from tables import *

"""
格式：
   （表名+ _Table，
    {
            filed名1：参数，
            filed名2：参数，
    }
    ),
"""

h2s_quantity_parameters = [
    #1. 加新的单位类型
    (QuantityType_Table, 
     {
         'name':'Q_PARTS_PER_MILLION',
     }
     ),
    #2. 加ppm的字符串定义
    (StringDefines_Table, 
     {
         "definename" : "SID_PPM",
         "typeid"     : "Quantity Unit",
     }
     ),
    #3. 加ppm相应的字符串
    (Strings_Table, 
     {
         'string'     : 'ppm',
         'languageid' : 'DEV_LANGUAGE',
         'status'     : 'UnEdit',
     }
     ),
    (Strings_Table, 
     {
         'string'     : 'ppm',
         'languageid' : 'UK_LANGUAGE',
         'status'     : 'UnEdit',
     }
     ),
    #4. SubjectRelation里的MpcUnits要加上Q_PARTS_PER_MILLION
    (SubjectRelation_Table, 
     {
         'name'           : 'Q_PARTS_PER_MILLION',
         'observertypeid' : 'MpcUnits',
     }
     ),
]

h2s_label_parameters = [
    #1. 添加h2s label
    (DisplayComponent_Table,
     {
         'name'            : '1.1 SystemStatus l1 h2s level',
         'componenttype'   : 'Label',
         'parentcomponent' : 0,
         'visible'         : True,
         'readonly'        : True,
         'x1'              : 0,
         'x2'              : 0,
         'y1'              : 0,
         'y2'              : 0,
         'displayid'       : 0,
         'helpstring'      : 0,
         'transparent'     : False,
     }
     ),
    #2. 添加数值label
    (DisplayComponent_Table,
     {
         'name'            : '1.1 SystemStatus l1 h2s level nq',
         'componenttype'   : 'NumberQuantity',
         'parentcomponent' : 0,
         'visible'         : True,
         'readonly'        : True,
         'x1'              : 0,
         'x2'              : 0,
         'y1'              : 0,
         'y2'              : 0,
         'displayid'       : 0,
         'helpstring'      : 0,
         'transparent'     : False,
     }
     ),
    #3. 加字符串定义
    (StringDefines_Table,
     {
         'definename' : 'SID_H2S_LEVEL',
         'typeid'     : 'Value type',
     }
     ),
    #4. label加相应的字符串
    (Strings_Table,
     {
         'string'     : 'H2S level',
         'languageid' : 'DEV_LANGUAGE',
         'status'     : 'UnEdit',
     }
     ),
    (Strings_Table,
     {
         'string'     : 'H2S level',
         'languageid' : 'UK_LANGUAGE',
         'status'     : 'UnEdit',
     }
     ),
    #5. 将字符串和label对应起来
    (DisplayLabel_Table,
     {
         'id'       : '1.1 SystemStatus l1 h2s level',
         'stringid' : 'SID_H2S_LEVEL',
     }
     ),
    #6. 定义label的text排列方式
    (DisplayText_Table,
     {
         'id'          : '1.1 SystemStatus l1 h2s level',
         'align'       : 'VCENTER_LEFT',
         'fontid'      : 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'leftmargin'  : 2,
         'rightmargin' : 0,
         'wordwrap'    : False,
     }
     ),
    #7. 定义数值的text排列方式
    (DisplayText_Table,
     {
         'id'          : '1.1 SystemStatus l1 h2s level nq',
         'align'       : 'VCENTER_LEFT',
         'fontid'      : 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'leftmargin'  : 0,
         'rightmargin' : 0,
         'wordwrap'    : False,
     }
     ),
    #8. 数值与新加单位'ppm'对应
    (DisplayNumberQuantity_Table,
     {
         'id'             : '1.1 SystemStatus l1 h2s level nq',
         'quantitytype'   : 'Q_PARTS_PER_MILLION',
         'numberofdigits' : 3,
         'numberfontid'   : 'DEFAULT_FONT_13_LANGUAGE_INDEP',
         'quantityfontid' : 'DEFAULT_FONT_13_LANGUAGE_INDEP',
     }
     ),
    #9. 数值与subject对应
    #TODO 先用已有的subject数据total_energy_j_for_display
    (DisplayObserverSingleSubject_Table,
     {
         'id'            : '1.1 SystemStatus l1 h2s level nq',
         'subjectid'     : 'total_energy_j_for_display',
         'subjectaccess' : 'Read',
     }
     ),
    #10. 在对应的listview下面新加一个item
    (DisplayListViewItem_Table,
     {
         'listviewid' : '1.1 SystemStatus List 1',
     }
     ),
    #11. 在新加的item下面添加label
    (DisplayListViewItemComponents_Table,
     {
         'componentid' : '1.1 SystemStatus l1 h2s level',
         'columnindex' : 0,
     }
     ),
    #12. 在新加的item下面添加数值
    (DisplayListViewItemComponents_Table,
     {
         'componentid' : '1.1 SystemStatus l1 h2s level nq',
         'columnindex' : 0,
     }
     ),
]

#TODO test
h2s_observer_parameters = [
    #1. 加Observer
    (Observer_Table,
     {
         'name'            : 'test1111',
         'typeid'          : 96,
         'taskid'          : 'LowPrioPeriodicTask',
         #'taskorder'       : None,
         #'subjectid'       : None,
         #'constructorargs' : None,
     }
     ),
]

h2s_subject_parameters = [
    #1. 加Subject
    (Subject_Table,
     {
         'name'       : 'test',
         'typeid'     : 'IntDataPoint',
         'geniappif'  : False,
         'Save'       : '-',              #save是model的函数，要用大写的Save
         'flashblock' : '-',
         'verified'   : False,
     }
     ),
    (IntDataPoint_Table,
     {
         'id'           : 'test',
         'type'         : 'U16',
         'min'          : '0',
         'max'          : '0xFFFF',
         'value'        : '0',
         'quantitytype' : 'Q_NO_UNIT',
         'verified'     : False,
     }
     ),
    (BoolDataPoint_Table,
     {
         'id'           : 'test',
         'value'        : 0,
     }
     ),
]
