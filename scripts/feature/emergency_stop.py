# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def emergency_stop():
    t = template('NewObserver')
    t.description = '---------- 加Observer: EmergencyStopCtrl ----------'
    t.observer_name = 'emergency_stop_ctrl'
    t.observer_type = 'EmergencyStopCtrl'
    t.observer_taskid = 'ControllerEventsTask'
    t.short_name = 'ESC'
    t.save()

    comment('**************************** Display Database部分 ****************************')

    t = template('NewString')
    t.description = '''---------- 4.4.2.4 - Digital inputs and functions页面里新加一行label:Emergency stop ----------
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
--> |  Emergency stop                       ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       2016-02-23 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DI_EMERGENCY_STOP'
    t.string_name = 'Emergency stop'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_emergency_stop ----------'
    t.subject_name = 'dig_in_func_input_emergency_stop'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_INPUT_EMERGENCY_STOP'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '30'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_emergency_stop ----------'
    t.subject_name = 'dig_in_func_state_emergency_stop'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = False
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'DIG_IN_FUNC_STATE_EMERGENCY_STOP'
    t.subject_access = 'Read/Write'

    t.enum_type_name = 'DIGITAL_INPUT_FUNC_STATE'
    t.enum_value = 'NOT_CONFIGURED'
    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, t.subject_name.upper()))
    comment('modified:   application/display/DigitalInputConfListView.cpp')
    comment('modified:   application/display/state/DigitalInputFunctionState.cpp')
    comment('modified:   application/driver/DiFuncHandler.cpp')
    comment('modified:   include/AppTypeDefs.h')

    for i in range(1,7):
        t = template('ObserverLinkSubject')
        t.description = '---------- Pump%d与dig_in_func_state_emergency_stop挂接 ----------' % (i)
        t.subject_name =  'dig_in_func_state_emergency_stop'
        t.observer_name = 'pump_' + str(i)
        t.observer_type = 'Pump'
        t.subject_relation_name = 'EMERGENCY_STOP_DIG_IN_REQUEST'
        t.subject_access = 'Read'
        t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- EmergencyStopCtrl与dig_in_func_state_emergency_stop挂接 ----------'
    t.subject_name =  'dig_in_func_state_emergency_stop'
    t.observer_name = 'emergency_stop_ctrl'
    t.observer_type = 'EmergencyStopCtrl'
    t.subject_relation_name = 'EMERGENCY_STOP_DIG_IN_REQUEST'
    t.subject_access = 'Read'
    t.save()

    t = template('NewString')
    t.description = '''---------- 新加alarm的string: System emergency stop is initiated (103) ----------'''
    t.define_name = 'SID_ALARM_103_EMERGENCY_STOP'
    t.string_name = 'System emergency stop is initiated (103)'
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
--> |  Emergency stop (103)                         |
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
    t.alarm_config_subject.subject_name = 'sys_alarm_emergency_stop_alarm_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.subject_access = 'Read/Write'
    t.alarm_config_subject.alarm_config_alarm_enabled = True
    #t.alarm_config_subject.alarm_config_warning_enabled = True
    t.alarm_config_subject.alarm_config_auto_ack = False
    t.alarm_config_subject.alarm_config_alarm_delay = 0
    t.alarm_config_subject.alarm_config_alarm_type = 'BoolDataPoint'
    t.alarm_config_subject.alarm_config_alarm_criteria = '='
    t.alarm_config_subject.alarm_config_alarm_limit = '1'
    t.alarm_config_subject.alarm_config_warning_limit = '0'
    t.alarm_config_subject.alarm_config_min_limit = '0'
    t.alarm_config_subject.alarm_config_max_limit = '1'
    t.alarm_config_subject.alarm_config_quantity_type_id = 'Q_NO_UNIT'
    t.alarm_config_subject.alarm_config_verified = False

    t.alarm_subject.subject_name = 'sys_alarm_emergency_stop_alarm_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'emergency_stop_ctrl'
    t.alarm_subject.observer_type = 'EmergencyStopCtrl'
    t.alarm_subject.subject_relation_name = 'SYS_ALARM_EMERGENCY_STOP_ALARM_OBJ'
    t.alarm_subject.alarm_alarm_config_id = 'sys_alarm_emergency_stop_alarm_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_103_EMERGENCY_STOP'
    t.alarm_define_name = 'SID_ALARM_103_EMERGENCY_STOP'
    t.alarm_id = 103
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- EmergencyStopCtrl与no_of_pumps挂接 ----------'
    t.subject_name =  'no_of_pumps'
    t.observer_name = 'emergency_stop_ctrl'
    t.observer_type = 'EmergencyStopCtrl'
    t.subject_relation_name = 'NO_OF_PUMPS'
    t.subject_access = 'Read'
    t.save()

    for i in range(1,7):
        t = template('ObserverLinkSubject')
        t.description = '---------- EmergencyStopCtrl与relay_status_relay_func_pump_%d挂接 ----------' % i
        t.subject_name =  'relay_status_relay_func_pump_%d' % i
        t.observer_name = 'emergency_stop_ctrl'
        t.observer_type = 'EmergencyStopCtrl'
        t.subject_relation_name = 'START_RELAY_PUMP_%d' % i
        t.subject_access = 'Write'
        t.save()

    for i in range(1,7):
        t = template('ObserverLinkSubject')
        t.description = '---------- EmergencyStopCtrl与vfd_%d_relay_status_relay_func_reverse挂接 ----------' % i
        t.subject_name =  'vfd_%d_relay_status_relay_func_reverse' % i
        t.observer_name = 'emergency_stop_ctrl'
        t.observer_type = 'EmergencyStopCtrl'
        t.subject_relation_name = 'REVERSE_RELAY_PUMP_%d' % i
        t.subject_access = 'Write'
        t.save()

    for i in range(1,7):
        t = template('ObserverLinkSubject')
        t.description = '---------- EmergencyStopCtrl与vfd_%d_pump_start_request挂接 ----------' % i
        t.subject_name =  'vfd_%d_pump_start_request' % i
        t.observer_name = 'emergency_stop_ctrl'
        t.observer_type = 'EmergencyStopCtrl'
        t.subject_relation_name = 'VFD_START_REQUEST_PUMP_%d' % i
        t.subject_access = 'Write'
        t.save()

    for i in range(1,7):
        t = template('ObserverLinkSubject')
        t.description = '---------- EmergencyStopCtrl与operation_mode_actual_pump_%d挂接 ----------' % i
        t.subject_name =  'operation_mode_actual_pump_%d' % i
        t.observer_name = 'emergency_stop_ctrl'
        t.observer_type = 'EmergencyStopCtrl'
        t.subject_relation_name = 'OPERATION_MODE_ACTUAL_PUMP_%d' % i
        t.subject_access = 'Write'
        t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- AppModeCtrl与sys_alarm_emergency_stop_alarm_obj挂接 ----------'
    t.subject_name =  'sys_alarm_emergency_stop_alarm_obj'
    t.observer_name = 'app_mode_ctrl'
    t.observer_type = 'AppModeCtrl'
    t.subject_relation_name = 'EMERGENCY_STOP_ALARM_OBJ'
    t.subject_access = 'Read'
    t.save()
