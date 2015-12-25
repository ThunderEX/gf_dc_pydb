# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *
from ..models import *
from common import *

def add_language():
    # 12 是"Don't translate"，但有单引号，sql报错，索性用数字，省得查询Foreign key
    lst = [
        ['Thai'       , 'SID_THAI'        , "State"] , # Thai 泰语
        ['Thai'       , 'SID_THAI_'       , 12]      , # Thai 泰语
        ['Indonesian' , 'SID_INDONESIAN'  , "State"] , # Indonesian 印度尼西亚
        ['Indonesian' , 'SID_INDONESIAN_' , 12]      , # Indonesian 印度尼西亚
        ['Latvia'     , 'SID_LATVIA'      , "State"] , # Latvia 拉脱维亚
        ['Latvia'     , 'SID_LATVIA_'     , 12]      , # Latvia 拉脱维亚
    ]
    for i in lst:
        t = template('NewString')
        t.description = '''---------- 新加语言的字符串: %s ----------''' % (i[0])
        t.string_name = i[0]
        t.define_name = i[1]
        t.define_type = i[2]
        t.save()

    lst = [
        [24 , 'Lithuanian' , 'lt' , 'SID_LITHUANIAN' , False] , # Lithuanian 立陶宛
        [25 , 'Thai'       , 'th' , 'SID_THAI'       , True]  , # Thai 泰语
        [26 , 'Indonesian' , 'id' , 'SID_INDONESIAN' , False] , # Indonesian 印度尼西亚
        [27 , 'Latvia'     , 'lv' , 'SID_LATVIA'     , False] , # Latvia 拉脱维亚
    ]
    for i in lst:
        t = template('LabelAndCheckbox')
        t.description = '''---------- 4.6.2 Display languages 页面里新加一行label and checkbox: %s ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.6.2 - Display languages                      |
        +-----------------------------------------------+
        |                                               |
        |Select language                                |
        |  British English                       ☑      |
        |  German                                ☐      |
        |  ...                                          |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        |
    --> |  %s                              ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[1], i[1])
        t.label_name = '4.6.2 LanguageSelection-%s' % i[2]
        t.checkbox_name = '4.6.2 LanguageSelection-%s cb' % i[2]
        t.checkbox_type = 'ModeCheckBox'
        t.check_state = i[0]
        t.label_column_index = 0
        t.checkbox_column_index = 1
        t.label_left_margin = 8
        t.label_right_margin = 0
        t.define_name = i[3]
        t.listview_id = '4.6.2 LanguageSelection list 1'
        t.exclude_from_factory = i[4]
        t.subject_id = 'display_language'
        t.save()

    # enable Croatian language
    DisplayListViewItem().update(id=2552, ExcludeFromFactory=False)
