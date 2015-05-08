# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *

def h2s_display():
    comment('**************************** Display Database部分 ****************************')
    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label:Start, dosing pump ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.4.1 - Function of digital outputs          |
    +-----------------------------------------------+
    |                                               |
    |Function, DO1 (CU362)[71]                      |
    |  No function                          ☑       |
    |  Start, pump 1                        ☐       |
    |  Start, pump 2                        ☐       |
    |  Start, mixer                         ☐       |
--> |  Start, dosing pump                   ☐       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    #由于该listview的ComponentType是DigitalOutputConfListView类型，只需要添加一个新字符串，并在AppTypeDefs.h和DigitalOutputConfListView.cpp里修改
    t.define_name = 'SID_DO_START_DOSING_PUMP'
    t.string_name = 'Start, dosing pump'
    t.save()
    
    t = template('LabelAndQuantity')
    t.description = '''---------- 添加label:h2s level于1.1 System Status ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |1.1 - System                                   |
    +-----------------------------------------------+
    |                                               |
    |  ------------+               +--------------  |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              +---------------+                |
    | Parallel-operation time           12:34h      |
    | Overflow time                     18:51h      |
    | Overflow volume                       0㎥     |
    | Number of overrflows                  6       |
    | Energy                              866kWh    |
--> | H2S level                            12PPM    |
    | Chemical remaining                  866l      |
    | Chemical dosed                      351l      |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 h2s level'
    t.quantity_name = '1.1 SystemStatus l1 h2s level nq'
    t.define_name = 'SID_H2S_LEVEL'
    t.string = 'H2S level'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'h2s_level_act'
    t.quantity_type =  'Q_PARTS_PER_MILLION'
    t.save()

    t = template('LabelAndQuantity')
    t.description = '''---------- 1.1 - System 页面里新加一行label:Chemical remaining和quantity:l ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |1.1 - System                                   |
    +-----------------------------------------------+
    |                                               |
    |  ------------+               +--------------  |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              +---------------+                |
    | Parallel-operation time           12:34h      |
    | Overflow time                     18:51h      |
    | Overflow volume                       0㎥     |
    | Number of overrflows                  6       |
    | Energy                              866kWh    |
    | H2S level                            12PPM    |
--> | Chemical remaining                  866l      |
    | Chemical dosed                      351l      |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 dosing feed tank level'
    t.quantity_name = '1.1 SystemStatus l1 dosing feed tank level nq'
    t.define_name = 'SID_DOSING_FEED_TANK_LEVEL'
    t.string = 'Dosing feed tank level'
    t.listview_id = '1.1 SystemStatus List 1'
    #TODO
    t.subject_id = 'dosing_feed_tank_level'
    t.quantity_type =  'Q_DEPTH'
    t.save()

    t = template('LabelAndQuantity')
    t.description = '''---------- 1.1 - System 页面里新加一行label:Chemical dosed和quantity:l ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |1.1 - System                                   |
    +-----------------------------------------------+
    |                                               |
    |  ------------+               +--------------  |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              |               |                |
    |              +---------------+                |
    | Parallel-operation time           12:34h      |
    | Overflow time                     18:51h      |
    | Overflow volume                       0㎥     |
    | Number of overrflows                  6       |
    | Energy                              866kWh    |
    | H2S level                            12PPM    |
    | Chemical remaining                  866l      |
--> | Chemical dosed                      351l      |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 chemical total dosed'
    t.quantity_name = '1.1 SystemStatus l1 chemical total dosed nq'
    t.define_name = 'SID_CHEMICAL_TOTAL_DOSED'
    t.string = 'Chemical total dosed'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'chemical_total_dosed'
    #TODO 改单位
    t.quantity_type = 'Q_VOLUME'
    t.save()

    t = template('LabelBlank')
    t.description = '''---------- 4.1.7 - Modules installed 页面里新加一行空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.1.7 - Modules installed                      |
    +-----------------------------------------------+
    |Number of IO351B modules               1       |
    |                                               |
    |IO 11X installed for                           |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
    |                                               |
    |MP 204 installed for                           |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
    |                                               |
    |VFD installed for                              |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
--> |                                               |
    |Dosing pump installed                  ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.listview_id = '4.1.7 pumpModules List'
    t.save()

    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.1.7 - Modules installed 页面里新加一行label和checkbox ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.1.7 - Modules installed                      |
    +-----------------------------------------------+
    |Number of IO351B modules               1       |
    |                                               |
    |IO 11X installed for                           |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
    |                                               |
    |MP 204 installed for                           |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
    |                                               |
    |VFD installed for                              |
    |  Pump 1                               ☑       |
    |  Pump 2                               ☐       |
    |                                               |
--> |Dosing pump installed                  ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.1.7 pumpModules dosing pump'
    t.checkbox_name = '4.1.7 pumpModules dosing pump cb'
    t.checkbox_type = 'OnOffCheckBox'
    t.label_column_index = 0
    t.checkbox_column_index = 1
    t.label_left_margin = 2
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_INSTALLED'
    t.label_string = 'Dosing pump installed'
    t.listview_id = '4.1.7 pumpModules List'
    t.subject_id = 'dda_control_enabled'
    t.save()

    t = template('LabelAndNewPage')
    t.description = '''----------  添加label:H2S Contol于4.2 Advanced Functions ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2 - Advanced Functions                       |
    +-----------------------------------------------+
    |                                               |
    |Anti-sezing                                    |
    |Daily emptying                                 |
    |Foam draining                                  |
    |Mixer configuration                            |
    |Adjustment of counters                         |
    |Resetting alarm log                            |
    |Pump groups                                    |
    |User-defined functions                         |
    |Variable-frequency drives                      |
    |Anti-blocking                                  |
    |Overflow                                       |
--> |H2S Control                                    |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2 AdvancedFunc H2S Contol'
    t.label_define_name = 'SID_H2S_CONTROL'
    t.label_string = 'H2S Control'
    t.listview_id = '4.2 AdvancedFunc List 1'

    t.group_name = '4.2.14 H2S Contol Group'
    t.group_define_name = 'SID_H2S_CONTROL'

    t.root_group_id_name = '4.2.14 H2S Contol Group'
    t.display_string_name = 'H2S Control'
    t.display_number = '4.2.14'

    t.listview_name = '4.2.14 H2S Contol List'
    t.listviewid_name = '4.2.14 H2S Contol List'
    t.listview_column_width = [160, 64, 0]
    t.save()

    t = template('LabelAndNewPage')
    t.description = '''---------- 4.2.14 - H2S Control 页面里新加一行label:Dosing pump，点击跳进4.2.14.1 Dosing pump group ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14 - H2S Control                           |
    +-----------------------------------------------+
    |                                               |
--> |Dosing pump                                    |
    |Go to Modules installed                        |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    #TODO add availabel条件
    t.label_name = '4.2.14 Dosing pump go to setting'
    t.label_define_name = 'SID_H2S_DOSING_PUMP_SETTING'
    t.label_string = 'Dosing pump'
    t.listview_id = '4.2.14 H2S Contol List'
    t.label_left_margin = 2
    t.label_right_margin = 1

    t.availabel_rule_name = 'Availabel rule: dosing pump installed'
    t.availabel_rule_type = 'AvalibleIfSet'
    t.availabel_rule_checkstate = 1
    t.availabel_rule_subject_id = 'dda_control_enabled'
    t.availabel_rule_column_index = 2

    t.group_name = '4.2.14.1 H2S Dosing pump group'
    t.group_define_name = 'SID_H2S_DOSING_PUMP_SETTING'

    t.root_group_id_name = '4.2.14.1 H2S Dosing pump group'
    t.display_string_name = 'Dosing pump'
    t.display_number = '4.2.14.1'

    t.listview_name = '4.2.14.1 H2S Dosing pump List'
    t.listviewid_name = '4.2.14.1 H2S Dosing pump List'
    t.listview_column_width = [164, 74, 0]
    t.save()

    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.14 - H2S Control 页面里新加一行label: go to modules installed，点击进入4.1.7 Modules installed ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14 - H2S Control                           |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump                                    |
--> |Go to Modules installed                        |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14 H2S go to modules installed'
    t.label_define_name = 'SID_GO_TO_MODULES_INSTALLED'
    t.display_id = 137
    t.listview_id = '4.2.14 H2S Contol List'
    t.label_left_margin = 2
    t.label_right_margin = 1
    t.save()

    t = template('LabelHeadline')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label:Dosing pump interface ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
--> |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
    |                                               |
    |Go to setting of analog outputs                |
    |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14.1 H2S dosing pump interface headline'
    t.define_name = 'SID_DOSING_PUMP_INTERFACE'
    t.label_string = 'Dosing pump interface'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()

    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Smart Digital DDA ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
--> |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
    |                                               |
    |Go to setting of analog outputs                |
    |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14.1 Smart Digital DDA'
    t.checkbox_name = '4.2.14.1 Smart Digital DDA cb'
    t.checkbox_type = 'ModeCheckBox'
    t.check_state = 0
    t.label_column_index = 0
    t.checkbox_column_index = 1
    t.label_left_margin = 4
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_SMART_DIGITAL_DDA'
    t.label_string = 'Smart Digital DDA'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.subject_id = 'dosing_pump_type'
    t.save()

    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Analog dosing pump ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
--> |  Analog dosing pump                   ☐       |
    |                                               |
    |Go to setting of analog outputs                |
    |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14.1 Analog dosing pump'
    t.checkbox_name = '4.2.14.1 Analog dosing pump cb'
    t.checkbox_type = 'ModeCheckBox'
    t.check_state = 1
    t.label_column_index = 0
    t.checkbox_column_index = 1
    t.label_left_margin = 4
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_ANALOG'
    t.label_string = 'Analog dosing pump'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.subject_id = 'dosing_pump_type'
    t.save()

    t = template('LabelBlank')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
--> |                                               |
    |Go to setting of analog outputs                |
    |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()

    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to setting of Analog outputs，点击进入4.4.3 Analog outputs ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
    |                                               |
--> |Go to setting of analog outputs                |
    |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14.1 Dosing pump go to AO'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_ANALOGUE_OUTPUTS'
    t.display_id = 143
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.save()

    t = template('LabelBlank')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
    |                                               |
    |Go to setting of analog outputs                |
--> |                                               |
    |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()

    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to setting of Digital outputs，点击进入4.4.4 Digital outputs ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump                         |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
    |                                               |
    |Go to setting of analog outputs                |
    |                                               |
--> |Go to setting of digital outputs               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.14.1 Dosing pump go to DO'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_DIGITAL_OUTPUTS'
    t.display_id = 35
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.save()
