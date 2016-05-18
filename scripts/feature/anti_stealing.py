# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def anti_stealing():
    """
    Anti stealing: flowchart

                                        +---------------------+
    dig_in_func_state_anti_stealing --> |anti_stealing_ctrl   |
                                        |DigitalInputAlarmCtrl|
                                        +---------------------+
                                                |
                                                |  sys_alarm_anti_stealing_alarm_obj
                                                v
                                        +---------------------+
                                        |anti_stealing_detect |
                                        |  AlarmDetectCtrl    |
                                        +---------------------+
                                                |
                                                |  anti_stealing_alarm_flag
                                                v
                                        +----------------------+
                                        |anti_stealing_alarm_do|
                                        |      BoolLogic       |
                                        +----------------------+
                                                |
                                                |  relay_status_relay_func_anti_stealing_alarm
                                                v
                                        +----------------------+
                                        |relay_function_handler| --> relay_func_output_anti_stealing_alarm
                                        |   RelayFuncHandler   |
                                        +----------------------+
    """

    t = template('NewObserver')
    t.description = '---------- 加Observer: anti_stealing_ctrl ----------'
    t.observer_name = 'anti_stealing_ctrl'
    t.observer_type = 'DigitalInputAlarmCtrl'
    t.observer_taskid = 'ControllerEventsTask'
    t.constructor_args = 'false'
    t.short_name = 'DIAC'
    t.save()

    t = template('NewString')
    t.description = '''---------- 4.4.2.4 - Digital inputs and functions页面里新加一行label:Anti stealing ----------
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
--> |  Anti stealing                        ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       2016-02-23 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DI_ANTI_STEALING'
    t.string_name = 'Anti stealing'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_anti_stealing ----------'
    t.subject_name = 'dig_in_func_input_anti_stealing'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_INPUT_ANTI_STEALING'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '30'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_anti_stealing ----------'
    t.subject_name = 'dig_in_func_state_anti_stealing'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = False
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_STATE_ANTI_STEALING'
    t.subject_access = 'Read/Write'

    t.enum_type_name = 'DIGITAL_INPUT_FUNC_STATE'
    t.enum_value = 'NOT_CONFIGURED'
    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, t.subject_name.upper()))
    comment('modified:   application/display/DigitalInputConfListView.cpp')
    comment('modified:   application/display/state/DigitalInputFunctionState.cpp')
    comment('modified:   application/driver/DiFuncHandler.cpp')
    comment('modified:   include/AppTypeDefs.h')


    t = template('ObserverLinkSubject')
    t.description = '---------- DigitalInputAlarmCtrl与dig_in_func_state_anti_stealing挂接 ----------'
    t.subject_name =  'dig_in_func_state_anti_stealing'
    t.observer_name = 'anti_stealing_ctrl'
    t.observer_type = 'DigitalInputAlarmCtrl'
    t.subject_relation_name = 'DIG_IN_FUNC_STATE'
    t.subject_access = 'Read'
    t.save()

    ####################################### anti_stealing_alarm #########################################

    comment('在4.5.x里，因为加了一项在4.5.1 System Alarm里，导致后面的4.5.2 Pump Alarm等内容错位，需要先将write_state依次后推')
    num_of_added_items = 1
    #1464 | 4.5.2.x PumpAlarms (onoffauto) slippoint, WriteState=30是Pump alarm里第一项
    table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
    result = table.get(id=1464)
    first_write_state_in_pump_alarm = result.WriteState
    new_write_state_in_sys_alarm = first_write_state_in_pump_alarm
    comment("新加System Alarm位置为：%d" % (new_write_state_in_sys_alarm))

    results = table.query(WriteState__gte = first_write_state_in_pump_alarm, suppress_log=True)  #query >= first_write_state_in_pump_alarm
    state_list = []
    for result in results:
        _id = getattr(result, 'id')
        # 4293 | 4.4.2 DigitalInputs DI9 IO351-43 WDP WriteState=30
        # 4375 | wizard.14 DigitalInputs DI9 IO351-43 WDP WriteState=30
        if _id in [4293, 4375]:
            continue
        value = getattr(result, 'WriteState')
        # 都向后移num_of_added_items个位置
        state_list.append([_id, value + num_of_added_items])
    for l in state_list:
        table.update(id=l[0], WriteState=l[1])
        # comment('更新表WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay，id=%d, WriteState=%d' %(l[0], l[1]))


    # 104已经被占用了，SID_ALARM_104_SOFTWARE_SHUT_DOWN_REQUEST
    t = template('NewString')
    t.description = '''---------- 3.1 - Current alarms页面里新加一个alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |3.1 - Current alarms                           |
    +-----------------------------------------------+
    |                                               |
    | (!)CU 362                                     |
--> |  Anti stealing has been initiated (107)       |
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
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_ALARM_107_ANTI_STEALING'
    t.string_name = 'Anti stealing has been initiated (107)'
    t.save()
    

    t = template('SystemAlarm')
    t.description = '''---------- 4.5.1 - System alarms页面里新加一行label:Anti stealing ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.5.1 - System alarms                          |
    +-----------------------------------------------+
    |                                               |
    |Select system alarm                            |
    |  Overflow                                     |
    |  High level                                   |
    |  Alarm level                                  |
    |  Dry running                                  |
    |  Float switch                                 |
    |  Level sensor                                 |
    |  ......                                       |
    |                                               |
--> |  Anti stealing                                |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.1 SystemAlarms (anti stealing)'
    t.label_define_name = 'SID_ANTI_STEALING'
    t.label_string = 'Anti stealing'
    t.slippoint_name = '4.5.1 SystemAlarms (anti stealing) slippoint'
    t.write_state = new_write_state_in_sys_alarm

    t.alarm_config_subject.subject_name = 'sys_alarm_anti_stealing_alarm_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.observer_name = 'display_alarm_slippoint'
    t.alarm_config_subject.observer_type = 'AlarmSlipPoint'
    t.alarm_config_subject.subject_relation_name = 'SYS_ALARM_ANTI_STEALING'
    t.alarm_config_subject.subject_access = 'Read/Write'

    t.alarm_config_subject.alarm_config_alarm_enabled = True
    t.alarm_config_subject.alarm_config_warning_enabled = False
    t.alarm_config_subject.alarm_config_auto_ack = True
    t.alarm_config_subject.alarm_config_alarm_delay = 1
    t.alarm_config_subject.alarm_config_alarm_type = 'BoolDataPoint'
    t.alarm_config_subject.alarm_config_alarm_criteria = '='
    t.alarm_config_subject.alarm_config_alarm_limit = '1'
    t.alarm_config_subject.alarm_config_warning_limit = '0'
    t.alarm_config_subject.alarm_config_min_limit = '0'
    t.alarm_config_subject.alarm_config_max_limit = '1'
    t.alarm_config_subject.alarm_config_quantity_type_id = 'Q_NO_UNIT'
    t.alarm_config_subject.alarm_config_verified = False

    t.alarm_subject.subject_name = 'sys_alarm_anti_stealing_alarm_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'anti_stealing_ctrl'
    t.alarm_subject.observer_type = 'DigitalInputAlarmCtrl'
    t.alarm_subject.subject_relation_name = 'FAULT_OBJ'
    t.alarm_subject.subject_access = 'Write'
    t.alarm_subject.alarm_alarm_config_id = 'sys_alarm_anti_stealing_alarm_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    # 104已经被占用了，SID_ALARM_104_SOFTWARE_SHUT_DOWN_REQUEST
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_107_ANTI_STEALING'
    t.alarm_alarm_string_id = 'SID_ALARM_107_ANTI_STEALING'
    t.alarm_alarm_id = 107
    t.save()

    comment('在AppTypeDefs.h里插入AC_SYS_ALARM_ANTI_STEALING')
    comment('在AlarmState.cpp里插入一行{AC_SYS_ALARM_ANTI_STEALING,                  SID_DI_ANTI_STEALING},')
    comment('''在AlarmSlipPoint.cpp里插入
    case SP_ASP_SYS_ALARM_ANTI_STEALING:
      mpAlarmDP[AC_SYS_ALARM_ANTI_STEALING][0].Attach(pSubject);
      break;
            ''')


    t = template('SystemAlarmStatus')
    t.description = '''---------- 4.5.5 - Status, system alarms页面里新加一行label:Anti stealing ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.5.5 - Status, system alarms                  |
    +-----------------------------------------------+
    |                                               |
    |  Overflow                                (!)  |
    |  High level                              (!)  |
    |  Alarm level                             (!)  |
    |  Dry running                             (!)  |
    |  Float switch                            (!)  |
    |  Level sensor                            (!)  |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Anti stealing                           (!)  |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.5 SystemAlarms Status (anti stealing)'
    t.label_define_name = 'SID_ANTI_STEALING'
    t.label_string = 'Anti stealing'
    t.alarm_icon_name = '4.5.5 SystemAlarms Status (anti stealing) alarm icon'
    t.warning_icon_name = '4.5.5 SystemAlarms Status (anti stealing) warning icon'
    t.subject_id = 'sys_alarm_anti_stealing_alarm_conf'
    t.save()


    ####################################### anti_stealing_detect #########################################
    t = template('NewObserver')
    t.description = '---------- 加Observer: anti_stealing_detect ----------'
    t.observer_name = 'anti_stealing_detect'
    t.observer_type = 'AlarmDetectCtrl'
    t.observer_taskid = 'ControllerEventsTask'
    t.short_name = 'ADC'
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- AlarmDetectCtrl与sys_alarm_anti_stealing_alarm_obj挂接 ----------'
    t.subject_name =  'sys_alarm_anti_stealing_alarm_obj'
    t.observer_name = 'anti_stealing_detect'
    t.observer_type = 'AlarmDetectCtrl'
    t.subject_relation_name = 'ALARM_OBJ'
    t.subject_access = 'Not decided'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: anti_stealing_alarm_flag ----------'
    t.subject_name =  'anti_stealing_alarm_flag'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'anti_stealing_detect'
    t.observer_type = 'AlarmDetectCtrl'
    t.subject_relation_name = 'ALARM_PRESENT'
    t.subject_access = 'Not decided'
    t.bool_value = 0
    t.save()

    ####################################### active anti_stealing in DO #########################################
    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label:Anti stealing alarm ----------
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
--> |  Anti stealing alarm                  ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_ANTI_STEALING_ALARM'
    t.string_name = 'Anti stealing alarm'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_anti_stealing_alarm ----------'
    t.subject_name =  'relay_status_relay_func_anti_stealing_alarm'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_ANTI_STEALING_ALARM'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_anti_stealing_alarm ----------'
    t.subject_name =  'relay_func_output_anti_stealing_alarm'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_ANTI_STEALING_ALARM'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()
    comment("AppTypeDefs.h里添加RELAY_FUNC_ANTI_STEALING")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_ANTI_STEALING_ALARM,          RELAY_FUNC_ANTI_STEALING_ALARM               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp.cpp里添加{ RELAY_FUNC_ANTI_STEALING_ALARM                  , SID_DO_ANTI_STEALING_ALARM                  }")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_ANTI_STEALING_ALARM:
      mpRelayStatus[RELAY_FUNC_ANTI_STEALING_ALARM].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_ANTI_STEALING_ALARM:
      mpRelayStatus[RELAY_FUNC_ANTI_STEALING_ALARM].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_ANTI_STEALING_ALARM:
      mpRelayFuncOutput[RELAY_FUNC_ANTI_STEALING_ALARM].Attach(pSubject);
      break;
            ''')

    t = template('NewObserver')
    t.description = '---------- 加Observer: anti_stealing_alarm_do ----------'
    t.observer_name = 'anti_stealing_alarm_do'
    t.observer_type = 'BoolLogic'
    t.observer_taskid = 'ControllerEventsTask'
    t.constructor_args = 'BOOL_LOGIC_OPERATOR_OR'
    t.short_name = 'BL'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- anti_stealing_alarm_do与anti_stealing_alarm_flag挂接 ----------'
    t.subject_name =  'anti_stealing_alarm_flag'
    t.observer_name = 'anti_stealing_alarm_do'
    t.observer_type = 'BoolLogic'
    t.subject_relation_name = 'SOURCE'
    t.subject_access = 'Read'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- anti_stealing_alarm_do与relay_status_relay_func_anti_stealing_alarm挂接 ----------'
    t.subject_name =  'relay_status_relay_func_anti_stealing_alarm'
    t.observer_name = 'anti_stealing_alarm_do'
    t.observer_type = 'BoolLogic'
    t.subject_relation_name = 'OUTPUT'
    t.subject_access = 'Write'
    t.save()
