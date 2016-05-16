# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *
from .common import *

def grinder_func():
    ######################################### Observer ################################################
    t = template('NewObserver')
    t.description = '---------- 加Observer: GrinderCtrl ----------'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.short_name = 'GC'
    t.save()


    ######################################### Subject ################################################
    t = template('NewSubject')
    t.description = '---------- 加Subject: grinder_enabled ----------'
    t.subject_name =  'grinder_enabled'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'GRINDER_ENABLED'
    t.subject_access = 'Read/Write'
    t.bool_value = 0
    t.save()


    t = template('AvailableRule')
    t.description = '''---------- 添加一个Available rule: grinder enabled ---------- '''
    t.available_rule_name = 'Available rule: grinder enabled'
    t.available_rule_type = 'AvalibleIfSet'
    t.available_rule_checkstate = 1
    t.available_rule_subject_id = 'grinder_enabled'
    t.save()


    ######################################### Function ##################################################
    t = template('LabelAndNewPage')
    t.description = '''----------  添加label:Grinder Contol于4.2 Advanced Functions ----------
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
--> |Grinder control                                |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2 AdvancedFunc Grinder Contol'
    t.label_define_name = 'SID_GRINDER_CONTROL'
    t.label_string = 'Grinder control'
    t.listview_id = '4.2 AdvancedFunc List 1'

    t.group_name = '4.2.15 Grinder Contol Group'
    t.group_define_name = 'SID_GRINDER_CONTROL'

    t.root_group_id_name = '4.2.15 Grinder Contol Group'
    t.display_string_name = 'Grinder control'
    t.display_number = '4.2.15'

    t.listview_name = '4.2.15 Grinder Contol List'
    t.listview_column_width = [160, 64, 0]
    t.save()


    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.2.15 - Grinder control 页面里新加一行label和checkbox: 4.2.15 Grinder control enabled ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.15 - Grinder control                       |
    +-----------------------------------------------+
    |                                               |
--> |Grinder control enabled                ☑       |
    |                                               |
    |Go to setting of I/O                           |
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
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.15 Grinder control enabled'
    t.checkbox_name = '4.2.15 grinder control enabled cb'
    t.checkbox_type = 'OnOffCheckBox'
    t.label_column_index = 0
    t.checkbox_column_index = 1
    # 只有margin不等于0时，光标才能移到这一项
    t.label_left_margin = 2
    t.label_right_margin = 0
    t.define_name = 'SID_GRINDER_CONTROL_ENABLED'
    t.label_string = 'Grinder control enabled'
    t.listview_id = '4.2.15 Grinder Contol List'
    t.subject_id = 'grinder_enabled'
    t.save()


    t = template('LabelBlank')
    t.description = '''---------- 4.2.15 - Grinder control 页面里新加一行空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.15 - Grinder control                       |
    +-----------------------------------------------+
    |                                               |
    |Grinder control enabled                ☑       |
--> |                                               |
    |Go to setting of I/O                           |
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
    t.listview_id = '4.2.15 Grinder Contol List'
    t.save()


    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.15 - Grinder control 页面里新加一行label: Go to setting of I/O，点击进入4.4 I/O settings ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.15 - Grinder control                       |
    +-----------------------------------------------+
    |                                               |
    |Grinder control enabled                ☑       |
    |                                               |
--> |Go to setting of I/O                           |
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
    t.label_name = '4.2.15 Grinder control go to IO'
    t.label_string = 'Go to setting of I/O'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_IO'
    t.display_id = 47 # 4.4 IO Group
    t.listview_id = '4.2.15 Grinder Contol List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.save()


def grinder_alarm():
    ######################################### Alarm ##################################################
    # TODO specify alarm code

    t = template('NewString')
    t.description = '''---------- 新加alarm的string: Grinder blocked (???) ----------'''
    t.define_name = 'SID_ALARM_108_GRINDER_BLOCKED'
    t.string_name = 'Grinder blocked (108)'
    t.save()

    t = template('NewAlarm')
    t.description = '''---------- 3.1 - Current alarms页面里新加一个alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |3.1 - Current alarms                           |
    +-----------------------------------------------+
    |                                               |
    | (!)CU 362                                     |
--> |  Grinder blocked (???)                        |
    |  Occured at                   2015-05-15 14:01|
    |  Disappeared at                     --   --   |
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
    |GRUNDFOS                       2016-02-23 11:13|
    +-----------------------------------------------+
    '''
    t.alarm_config_subject.subject_name = 'sys_alarm_grinder_blocked_alarm_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.subject_access = 'Read/Write'
    t.alarm_config_subject.alarm_config_alarm_enabled = True
    #t.alarm_config_subject.alarm_config_warning_enabled = True
    t.alarm_config_subject.alarm_config_auto_ack = False
    t.alarm_config_subject.alarm_config_alarm_delay = 1
    t.alarm_config_subject.alarm_config_alarm_type = 'BoolDataPoint'
    t.alarm_config_subject.alarm_config_alarm_criteria = '='
    t.alarm_config_subject.alarm_config_alarm_limit = '1'
    t.alarm_config_subject.alarm_config_warning_limit = '0'
    t.alarm_config_subject.alarm_config_min_limit = '0'
    t.alarm_config_subject.alarm_config_max_limit = '1'
    t.alarm_config_subject.alarm_config_quantity_type_id = 'Q_NO_UNIT'
    t.alarm_config_subject.alarm_config_verified = False

    t.alarm_subject.subject_name = 'sys_alarm_grinder_blocked_alarm_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'grinder_ctrl'
    t.alarm_subject.observer_type = 'GrinderCtrl'
    t.alarm_subject.subject_relation_name = 'SYSTEM_ALARM_GRINDER_BLOCKED'
    t.alarm_subject.subject_access = 'Write'
    t.alarm_subject.alarm_alarm_config_id = 'sys_alarm_grinder_blocked_alarm_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_108_GRINDER_BLOCKED'
    t.alarm_define_name = 'SID_ALARM_108_GRINDER_BLOCKED'
    t.alarm_id = 108
    t.save()

def grinder_io():
    ######################################### I/O ##################################################
    #---------------------------------------- DI --------------------------------------------------
    t = template('NewString')
    t.description = '''---------- 4.4.2.4 - Digital inputs and functions页面里新加一行label: Flow switch, grinder ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.2.4 - Digital iutputs and functions        |
    +-----------------------------------------------+
    |Select input logic                             |
    |  NO (normally open)                   ☑       |
    |  NC (normally closed)                 ☐       |
    |                                               |
    |Function, DI1 (IO351B-41)                      |
    |  Not used                             ☐       |
    |  Automatic/manual, pump 1             ☐       |
    |  Manual start, pump 1                 ☐       |
    |  Automatic/manual, pump 2             ☐       |
    |  Manual start, pump 2                 ☐       |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Flow switch, grinder                 ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       2016-02-23 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DI_GRINDER_FLOW_SWITCH'
    t.string_name = 'Flow switch, grinder'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_grinder_flow_switch ----------'
    t.subject_name = 'dig_in_func_input_grinder_flow_switch'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_INPUT_GRINDER_FLOW_SWITCH'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '30'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_grinder_flow_switch ----------'
    t.subject_name = 'dig_in_func_state_grinder_flow_switch'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = False
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_STATE_GRINDER_FLOW_SWITCH'
    t.subject_access = 'Read/Write'

    t.enum_type_name = 'DIGITAL_INPUT_FUNC_STATE'
    t.enum_value = 'NOT_CONFIGURED'
    t.save()
    comment('Note：在AppTypeDefs.h里枚举DIGITAL_INPUT_FUNC_TYPE里加入：DIGITAL_INPUT_FUNC_GRINDER_FLOW_SWITCH')
    comment('''application/display/DigitalInputConfListView.cpp 添加：
            {SID_DI_GRINDER_FLOW_SWITCH, DIGITAL_INPUT_FUNC_GRINDER_FLOW_SWITCH},''')
    comment('''application/display/state/DigitalInputFunctionState.cpp 添加：
            {DIGITAL_INPUT_FUNC_GRINDER_FLOW_SWITCH, SID_DI_GRINDER_FLOW_SWITCH},''')
    comment('''application/driver/DiFuncHandler.cpp 的SetSubjectPointer里添加：
    case SP_DIFH_DIG_IN_FUNC_STATE_GRINDER_FLOW_SWITCH:
      mpDiFuncState[DIGITAL_INPUT_FUNC_GRINDER_FLOW_SWITCH].Attach(pSubject);
      break;
    case SP_DIFH_DIG_IN_FUNC_INPUT_GRINDER_FLOW_SWITCH:
      mpDiFuncInput[DIGITAL_INPUT_FUNC_GRINDER_FLOW_SWITCH].Attach(pSubject);
      break;''')


    t = template('ObserverLinkSubject')
    t.description = '---------- GrinderCtrl与dig_in_func_state_grinder_flow_switch挂接 ----------'
    t.subject_name =  'dig_in_func_state_grinder_flow_switch'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'GRINDER_FLOW_SWITCH_DIG_IN_REQUEST'
    t.subject_access = 'Read'
    t.save()

    t = template('NewString')
    t.description = '''---------- 4.4.2.4 - Digital inputs and functions页面里新加一行label: Current overload, grinder ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.2.4 - Digital iutputs and functions        |
    +-----------------------------------------------+
    |Select input logic                             |
    |  NO (normally open)                   ☑       |
    |  NC (normally closed)                 ☐       |
    |                                               |
    |Function, DI1 (IO351B-41)                      |
    |  Not used                             ☐       |
    |  Automatic/manual, pump 1             ☐       |
    |  Manual start, pump 1                 ☐       |
    |  Automatic/manual, pump 2             ☐       |
    |  Manual start, pump 2                 ☐       |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Current overload, grinder            ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       2016-02-23 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DI_GRINDER_CURRENT_OVERLOAD'
    t.string_name = 'Current overload, grinder'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_grinder_current_overload ----------'
    t.subject_name = 'dig_in_func_input_grinder_current_overload'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_INPUT_GRINDER_CURRENT_OVERLOAD'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '30'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_grinder_current_overload ----------'
    t.subject_name = 'dig_in_func_state_grinder_current_overload'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = False
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_STATE_GRINDER_CURRENT_OVERLOAD'
    t.subject_access = 'Read/Write'

    t.enum_type_name = 'DIGITAL_INPUT_FUNC_STATE'
    t.enum_value = 'NOT_CONFIGURED'
    t.save()
    comment('Note：在AppTypeDefs.h里枚举DIGITAL_INPUT_FUNC_TYPE里加入：DIGITAL_INPUT_FUNC_GRINDER_CURRENT_OVERLOAD')
    comment('''application/display/DigitalInputConfListView.cpp 添加：
            {SID_DI_GRINDER_CURRENT_OVERLOAD, DIGITAL_INPUT_FUNC_GRINDER_CURRENT_OVERLOAD},''')
    comment('''application/display/state/DigitalInputFunctionState.cpp 添加：
            {DIGITAL_INPUT_FUNC_GRINDER_CURRENT_OVERLOAD, SID_DI_GRINDER_CURRENT_OVERLOAD},''')
    comment('''application/driver/DiFuncHandler.cpp 的SetSubjectPointer里添加：
    case SP_DIFH_DIG_IN_FUNC_STATE_GRINDER_CURRENT_OVERLOAD:
      mpDiFuncState[DIGITAL_INPUT_FUNC_GRINDER_CURRENT_OVERLOAD].Attach(pSubject);
      break;
    case SP_DIFH_DIG_IN_FUNC_INPUT_GRINDER_CURRENT_OVERLOAD:
      mpDiFuncInput[DIGITAL_INPUT_FUNC_GRINDER_CURRENT_OVERLOAD].Attach(pSubject);
      break;''')


    t = template('ObserverLinkSubject')
    t.description = '---------- GrinderCtrl与dig_in_func_state_grinder_current_overload挂接 ----------'
    t.subject_name =  'dig_in_func_state_grinder_current_overload'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'GRINDER_CURRENT_OVERLOAD_DIG_IN_REQUEST'
    t.subject_access = 'Read'
    t.save()


    # subject to set availabel rule in DI
    t = template('ObserverLinkSubject')
    t.description = '---------- DigitalInputConfListView与grinder_enabled挂接 ----------'
    t.subject_name =  'grinder_enabled'
    t.observer_name = 'display_dig_in_conf_listview'
    t.observer_type = 'DigitalInputConfListView'
    t.subject_relation_name = 'GRINDER_ENABLED'
    t.subject_access = 'Read/Write'
    t.save()
    comment("修改DigitalInputConfListView.cpp，添加available")


    #---------------------------------------- DO --------------------------------------------------
    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label: Start, grinder ----------
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
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Start, grinder                       ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_GRINDER_START'
    t.string_name = 'Start, grinder'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_grinder_start ----------'
    t.subject_name =  'relay_status_relay_func_grinder_start'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_GRINDER_START'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_grinder_start ----------'
    t.subject_name =  'relay_func_output_grinder_start'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_GRINDER_START'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()
    comment("AppTypeDefs.h里添加RELAY_FUNC_GRINDER_START")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_GRINDER_START,          RELAY_FUNC_GRINDER_START               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp.cpp里添加{ RELAY_FUNC_GRINDER_START                  , SID_DO_GRINDER_START                  }")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_GRINDER_START:
      mpRelayStatus[RELAY_FUNC_GRINDER_START].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_GRINDER_START:
      mpRelayStatus[RELAY_FUNC_GRINDER_START].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_GRINDER_START:
      mpRelayFuncOutput[RELAY_FUNC_GRINDER_START].Attach(pSubject);
      break;
            ''')


    t = template('ObserverLinkSubject')
    t.description = '---------- grinder_ctrl与relay_status_relay_func_grinder_start挂接 ----------'
    t.subject_name =  'relay_status_relay_func_grinder_start'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'RELAY_STATUS_RELAY_FUNC_GRINDER_START'
    t.subject_access = 'Write'
    t.save()


    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label: reverse, grinder ----------
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
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Reverse, grinder                     ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_GRINDER_REVERSE'
    t.string_name = 'Reverse, grinder'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_grinder_reverse ----------'
    t.subject_name =  'relay_status_relay_func_grinder_reverse'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_GRINDER_REVERSE'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_grinder_reverse ----------'
    t.subject_name =  'relay_func_output_grinder_reverse'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_GRINDER_REVERSE'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()
    comment("AppTypeDefs.h里添加RELAY_FUNC_GRINDER_REVERSE")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_GRINDER_REVERSE,          RELAY_FUNC_GRINDER_REVERSE               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp.cpp里添加{ RELAY_FUNC_GRINDER_REVERSE                  , SID_DO_GRINDER_REVERSE                  }")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_GRINDER_REVERSE:
      mpRelayStatus[RELAY_FUNC_GRINDER_REVERSE].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_GRINDER_REVERSE:
      mpRelayStatus[RELAY_FUNC_GRINDER_REVERSE].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_GRINDER_REVERSE:
      mpRelayFuncOutput[RELAY_FUNC_GRINDER_REVERSE].Attach(pSubject);
      break;
            ''')


    t = template('ObserverLinkSubject')
    t.description = '---------- grinder_ctrl与relay_status_relay_func_grinder_reverse挂接 ----------'
    t.subject_name =  'relay_status_relay_func_grinder_reverse'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'RELAY_STATUS_RELAY_FUNC_GRINDER_REVERSE'
    t.subject_access = 'Write'
    t.save()


    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label: Grinder blocked alarm ----------
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
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> | Grinder blocked alarm                 ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_GRINDER_BLOCKED_ALARM'
    t.string_name = 'Grinder blocked alarm'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_grinder_blocked_alarm ----------'
    t.subject_name =  'relay_status_relay_func_grinder_blocked_alarm'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_GRINDER_BLOCKED_ALARM'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_grinder_blocked_alarm ----------'
    t.subject_name =  'relay_func_output_grinder_blocked_alarm'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_GRINDER_BLOCKED_ALARM'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()
    comment("AppTypeDefs.h里添加RELAY_FUNC_GRINDER_BLOCKED_ALARM")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_GRINDER_BLOCKED_ALARM,          RELAY_FUNC_GRINDER_BLOCKED_ALARM               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp.cpp里添加{ RELAY_FUNC_GRINDER_BLOCKED_ALARM                  , SID_DO_GRINDER_BLOCKED_ALARM                  }")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_GRINDER_BLOCKED_ALARM:
      mpRelayStatus[RELAY_FUNC_GRINDER_BLOCKED_ALARM].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_GRINDER_BLOCKED_ALARM:
      mpRelayStatus[RELAY_FUNC_GRINDER_BLOCKED_ALARM].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_GRINDER_BLOCKED_ALARM:
      mpRelayFuncOutput[RELAY_FUNC_GRINDER_BLOCKED_ALARM].Attach(pSubject);
      break;
            ''')


    t = template('ObserverLinkSubject')
    t.description = '---------- grinder_ctrl与relay_status_relay_func_grinder_blocked_alarm挂接 ----------'
    t.subject_name =  'relay_status_relay_func_grinder_blocked_alarm'
    t.observer_name = 'grinder_ctrl'
    t.observer_type = 'GrinderCtrl'
    t.subject_relation_name = 'RELAY_STATUS_RELAY_FUNC_GRINDER_BLOCKED_ALARM'
    t.subject_access = 'Write'
    t.save()


def grinder_io_bak():
    # subject to set availabel rule in DO
    t = template('ObserverLinkSubject')
    t.description = '---------- DigitalOutputConfListView与grinder_enabled挂接 ----------'
    t.subject_name =  'grinder_enabled'
    t.observer_name = 'display_dig_out_conf_listview'
    t.observer_type = 'DigitalOutputConfListView'
    t.subject_relation_name = 'GRINDER_ENABLED'
    t.subject_access = 'Read/Write'
    t.save()
    comment("修改DigitalOutputConfListView.cpp，添加available")

def grinder():
    grinder_func()
    grinder_io()
