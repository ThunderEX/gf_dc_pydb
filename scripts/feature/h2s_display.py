# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def h2s_display():
    comment('**************************** Display Database部分 ****************************')

    comment('因为加了两项在System Alarm里，导致后面的Pump Alarm等内容错位，需要将write_state>30的依次后推')
    # >30的都没有重复，批量更新
    table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
    results = table.query(WriteState__gte = 31)  #query >=30
    state_list = []
    for result in results:
        _id = getattr(result, 'id')
        value = getattr(result, 'WriteState')
        state_list.append([_id, value+2])
    for l in state_list:
        table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
        table.update(id=l[0], WriteState=l[1])
        comment('更新表WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay，id=%d, WriteState=%d' %(l[0], l[1]))
    #1464 | 4.5.2.x PumpAlarms (onoffauto) slippoint, WriteState=30, 有重复，拿出来单独处理
    table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
    table.update(id=1464, WriteState=32)
    
    #先加一个字符串'DDA alarm (254)'显示在'3.1 - current alarms'里
    t = template('NewString')
    t.description = '''---------- 3.1 - Current alarms页面里新加一个alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |3.1 - Current alarms                           |
    +-----------------------------------------------+
    |                                               |
    | (!)CU 362                                     |
--> |  DDA alarm (254)                              |
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
    t.define_name = 'SID_ALARM_254_DDA'
    t.string_name = 'DDA alarm (254)'
    t.save()

    t = template('SystemAlarm')
    t.description = '''---------- 4.5.1 - System alarms页面里新加一行label:DDA fault ----------
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
    |                                               |
--> |  DDA fault                                    |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.1 SystemAlarms (dda)'
    t.label_define_name = 'SID_DDA_FAULT'
    t.label_string = 'DDA fault'
    t.slippoint_name = '4.5.1 SystemAlarms (dda) slippoint'
    t.write_state = 30

    #加subject: sys_alarm_dda_fault_alarm_conf 类型为AlarmConfig
    t.alarm_config_subject_name = 'sys_alarm_dda_fault_alarm_conf'
    t.alarm_config_subject_type_id = 'AlarmConfig'
    t.alarm_config_geni_app_if = False
    t.alarm_config_subject_save = 'Value'
    t.alarm_config_flash_block = 'Config'
    t.alarm_config_observer_name = 'display_alarm_slippoint'
    t.alarm_config_observer_type = 'AlarmSlipPoint'
    t.alarm_config_subject_relation_name = 'sys_alarm_dda_fault'
    t.alarm_config_subject_access = 'Read/Write'

    t.alarm_config_alarm_enabled = True
    t.alarm_config_warning_enabled = True
    t.alarm_config_auto_ack = True
    t.alarm_config_alarm_delay = 5
    t.alarm_config_alarm_type = 'BoolDataPoint'
    t.alarm_config_alarm_criteria = '='
    t.alarm_config_alarm_limit = '1'
    t.alarm_config_warning_limit = '0'
    t.alarm_config_min_limit = '0'
    t.alarm_config_max_limit = '1'
    t.alarm_config_quantity_type_id = 'Q_NO_UNIT'
    t.alarm_config_verified = False

    #SP_DDA_SYS_ALARM_DDA_FAULT_ALARM_OBJ
    #加subject:sys_alarm_dda_fault_alarm_obj
    t.alarm_subject_name = 'sys_alarm_dda_fault_alarm_obj'
    t.alarm_subject_type_id = 'AlarmDataPoint'
    t.alarm_geni_app_if = False
    t.alarm_subject_save = '-'
    t.alarm_flash_block = '-'
    t.alarm_observer_name = 'dda_ctrl'
    t.alarm_observer_type = 'DDACtrl'
    t.alarm_subject_relation_name = 'sys_alarm_dda_fault_alarm_obj'

    t.alarm_alarm_config_id = 'sys_alarm_dda_fault_alarm_conf'
    t.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_erroneous_unit_number = 0
    t.alarm_alarm_id = 'SID_ALARM_254_DDA'

    comment('在AppTypeDefs.h里插入AC_SYS_ALARM_DDA_FAULT')
    comment('在AlarmState.cpp里插入一行{AC_SYS_ALARM_DDA_FAULT,                  SID_DDA_FAULT},')
    comment('''在AlarmSlipPoint.cpp里插入
    case SP_ASP_SYS_ALARM_DDA_FAULT:
      mpAlarmDP[AC_SYS_ALARM_DDA_FAULT][0].Attach(pSubject);
      break;
            ''')
    t.save()

    t = template('SystemAlarmStatus')
    t.description = '''---------- 4.5.5 - Status, system alarms页面里新加一行label:DDA fault ----------
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
--> |  DDA fault                               (!)  |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.5 SystemAlarms Status (dda)'
    t.label_define_name = 'SID_DDA_FAULT'
    t.label_string = 'DDA fault'
    t.alarm_icon_name = '4.5.5 SystemAlarms Status (dda) alarm icon'
    t.warning_icon_name = '4.5.5 SystemAlarms Status (dda) warning icon'
    t.subject_id = 'sys_alarm_dda_fault_alarm_conf'
    t.save()


    #先加一个字符串'Dosing pump alarm (255)'显示在'3.1 - current alarms'里
    t = template('NewString')
    t.description = '''---------- 3.1 - Current alarms页面里新加一个alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |3.1 - Current alarms                           |
    +-----------------------------------------------+
    |                                               |
    | (!)CU 362                                     |
--> |  Dosing pump alarm (255)                      |
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
    t.define_name = 'SID_ALARM_255_DOSING_PUMP'
    t.string_name = 'Dosing pump alarm (255)'
    t.save()

    t = template('SystemAlarm')
    t.description = '''---------- 4.5.1 - System alarms页面里新加一行label:Dosing pump ----------
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
    |  DDA fault                                    |
--> |  Dosing pump                                  |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.1 SystemAlarms (dosing pump)'
    t.label_define_name = 'SID_DOSING_PUMP'
    t.label_string = 'Dosing pump'
    t.slippoint_name = '4.5.1 SystemAlarms (dosing pump) slippoint'
    t.write_state = 31

    #加subject: sys_alarm_dosing_pump_alarm_conf 类型为AlarmConfig
    t.alarm_config_subject_name = 'sys_alarm_dosing_pump_alarm_conf'
    t.alarm_config_subject_type_id = 'AlarmConfig'
    t.alarm_config_geni_app_if = False
    t.alarm_config_subject_save = 'Value'
    t.alarm_config_flash_block = 'Config'
    t.alarm_config_observer_name = 'display_alarm_slippoint'
    t.alarm_config_observer_type = 'AlarmSlipPoint'
    t.alarm_config_subject_relation_name = 'sys_alarm_dosing_pump'
    t.alarm_config_subject_access = 'Read/Write'

    t.alarm_config_alarm_enabled = True
    t.alarm_config_warning_enabled = True
    t.alarm_config_auto_ack = True
    t.alarm_config_alarm_delay = 5
    t.alarm_config_alarm_type = 'BoolDataPoint'
    t.alarm_config_alarm_criteria = '='
    t.alarm_config_alarm_limit = '1'
    t.alarm_config_warning_limit = '0'
    t.alarm_config_min_limit = '0'
    t.alarm_config_max_limit = '1'
    t.alarm_config_quantity_type_id = 'Q_NO_UNIT'
    t.alarm_config_verified = False

    #SP_DDA_SYS_ALARM_DOSING_PUMP_ALARM_OBJ
    #加subject:sys_alarm_dosing_pump_alarm_obj
    t.alarm_subject_name = 'sys_alarm_dosing_pump_alarm_obj'
    t.alarm_subject_type_id = 'AlarmDataPoint'
    t.alarm_geni_app_if = False
    t.alarm_subject_save = '-'
    t.alarm_flash_block = '-'
    t.alarm_observer_name = 'dosing_pump_ctrl'
    t.alarm_observer_type = 'NonGFDosingPumpCtrl'
    t.alarm_subject_relation_name = 'sys_alarm_dosing_pump_alarm_obj'

    t.alarm_alarm_config_id = 'sys_alarm_dosing_pump_alarm_conf'
    t.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_erroneous_unit_number = 0
    t.alarm_alarm_id = 'SID_ALARM_255_DOSING_PUMP'

    comment('在AppTypeDefs.h里插入AC_SYS_ALARM_DOSING_PUMP')
    comment('在AlarmState.cpp里插入一行{AC_SYS_ALARM_DOSING_PUMP,                  SID_DOSING_PUMP},')
    comment('''在AlarmSlipPoint.cpp里插入
    case SP_ASP_SYS_ALARM_DOSING_PUMP:
      mpAlarmDP[AC_SYS_ALARM_DOSING_PUMP][0].Attach(pSubject);
      break;
            ''')
    t.save()

    

    t = template('SystemAlarmStatus')
    t.description = '''---------- 4.5.5 - Status, system alarms页面里新加一行label:Dosing pump ----------
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
--> |  Dosing pump                             (!)  |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.5 SystemAlarms Status (dosing pump)'
    t.label_define_name = 'SID_DOSING_PUMP'
    t.label_string = 'Dosing pump'
    t.alarm_icon_name = '4.5.5 SystemAlarms Status (dosing pump) alarm icon'
    t.warning_icon_name = '4.5.5 SystemAlarms Status (dosing pump) warning icon'
    t.subject_id = 'sys_alarm_dosing_pump_alarm_conf'
    t.save()


    comment('加DDA的一系列Alarm')
    dda_alram_strings = [
        ('SID_ALARM_256_DDA_OVER_PRESSURE'                   , 'Over pressure (256)'),
        ('SID_ALARM_257_DDA_MEAN_PRESSURE_TO_LOW'            , 'Mean pressure to low (257)'),
        ('SID_ALARM_258_DDA_GAS_IN_PUMP_HEAD'                , 'Gas in pump head, deaerating problem (258)'),
        ('SID_ALARM_259_DDA_CAVITATIONS'                     , 'Cavitations (259)'),
        ('SID_ALARM_260_DDA_PRESSURE_VALVE_LEAKAGE'          , 'Pressure valve leakage (260)'),
        ('SID_ALARM_261_DDA_SUCTION_VALVE_LEAKAGE'           , 'Suction valve leakage (261)'),
        ('SID_ALARM_262_DDA_VENTING_VALVE_DEFECT'            , 'Venting valve defect (262)'),
        ('SID_ALARM_263_DDA_TIME_FOR_SERVICE_IS_EXCEED'      , 'Time for service is exceed (263)'),
        ('SID_ALARM_264_DDA_SOON_TIME_FOR_SERVICE'           , 'Soon time for service (264)'),
        ('SID_ALARM_265_DDA_CAPACITY_TOO_LOW'                , 'Capacity too low (265)'),
        ('SID_ALARM_266_DDA_DIAPHRAGM_BREAK'                 , 'Diaphragm break (266)'),
        ('SID_ALARM_267_DDA_BLOCKED_MOTOR_OR_PUMP'           , 'Blocked motor/pump (267)'),
        ('SID_ALARM_268_DDA_PRE_EMPTY_TANK'                  , 'Pre empty tank (268)'),
        ('SID_ALARM_269_DDA_EMPTY_TANK'                      , 'Empty tank (269)'),
        ('SID_ALARM_270_DDA_CABLE_BREAKDOWN_ON_FLOW_MONITOR' , 'Cable breakdown on Flow Monitor (270)'),
        ('SID_ALARM_271_DDA_CABLE_BREAKDOWN_ON_ANALOGUE'     , 'Cable breakdown on Analogue (271)'),
    ]
    for alarm_string in dda_alram_strings:
        t = template('AlarmString')
        t.description = '---------- 加Alarm String: %s ----------' % (alarm_string[1])
        t.alarm_define_name = alarm_string[0]
        t.alarm_string = alarm_string[1]
        t.save()
    

    t = template('NewString')
    t.description = '''---------- 4.4.2.4 - Digital inputs and functions页面里新加一行label:Dosing pump ready ----------
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
--> |  Dosing pump ready                    ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DI_DOSING_PUMP_READY'
    t.string_name = 'Dosing pump ready'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_dosing_pump ----------'
    t.subject_name = 'dig_in_func_input_dosing_pump'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'dig_in_func_input_dosing_pump'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '30'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewEnumData')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_dosing_pump ----------'
    t.enum_subject_names = ['dig_in_func_state_dosing_pump']
    t.enum_geni_app_if = False
    t.enum_subject_save = '-'
    t.enum_flash_block = '-'
    t.enum_observer_name = 'digital_input_function_handler'
    t.enum_observer_type = 'DiFuncHandler'
    t.enum_subject_relation_names = ['dig_in_func_state_dosing_pump']
    t.enum_subject_access = 'Read/Write'

    t.enum_type_name = 'DIGITAL_INPUT_FUNC_STATE'
    t.enum_values = ['NOT_CONFIGURED']
    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, str(t.enum_subject_names).upper()))
    comment('modified:   application/display/DigitalInputConfListView.cpp')
    comment('modified:   application/display/state/DigitalInputFunctionState.cpp')
    comment('modified:   application/driver/DiFuncHandler.cpp')
    comment('modified:   include/AppTypeDefs.h')

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dig_in_func_state_dosing_pump挂接 ----------'
    t.subject_name =  'dig_in_func_state_dosing_pump'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'DOSING_PUMP_DIG_IN_REQUEST'
    t.subject_access = 'Read'
    t.save()


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
--> |  Start, dosing pump                   ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_START_DOSING_PUMP'
    t.string_name = 'Start, dosing pump'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_dosing_pump ----------'
    #SP_DDA_dosing_pump_enabled
    t.subject_name =  'relay_status_relay_func_dosing_pump'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_DOSING_PUMP'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_dosing_pump ----------'
    t.subject_name =  'relay_func_output_dosing_pump'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_DOSING_PUMP'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()

    comment("AppTypeDefs.h里添加RELAY_FUNC_DOSING_PUMP")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_START_DOSING_PUMP,          RELAY_FUNC_DOSING_PUMP               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp.cpp里添加{ RELAY_FUNC_DOSING_PUMP                  , SID_DO_START_DOSING_PUMP                  }")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_DOSING_PUMP:
      mpRelayStatus[RELAY_FUNC_DOSING_PUMP].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_DOSING_PUMP:
      mpRelayStatus[RELAY_FUNC_DOSING_PUMP].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_DOSING_PUMP:
      mpRelayFuncOutput[RELAY_FUNC_DOSING_PUMP].Attach(pSubject);
      break;
            ''')

    
    t = template('NewString')
    t.description = '''---------- 4.4.1.x.1 - Analog inputs and measured value页面里新加一行Level, chemical container ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.1.1.1 - Analog iutputs and measuered value |
    +-----------------------------------------------+
    |                                               |
    |Function, AI1 (CU 362)                         |
    |  Not used                             ☐       |
    |  Flow rate                            ☐       |
    |  Level, ultrasound                    ☐       |
    |  Level, pressure                      ☐       |
    |  Pres, sensor, discharge              ☐       |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  Level, chemical container            ☐       |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_AI_LEVEL_CHEMICAL_CONTAINER'
    t.string_name = 'Level, chemical container'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: dig_in_func_input_dosing_pump ----------'
    t.subject_name = 'measured_value_chemical_container'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'ana_in_measure_value_ctrl'
    t.observer_type = 'AnaInMeasureValueCtrl'
    t.subject_relation_name = 'measured_value_chemical_container'
    t.subject_access = 'Write'

    t.float_value = 0
    t.float_min = 0
    t.float_max = 100
    t.float_quantity_type = 'Q_HEIGHT'
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与measured_value_chemical_container挂接 ----------'
    t.subject_name =  'measured_value_chemical_container'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'measured_value_chemical_container'
    t.subject_access = 'Read'
    t.save()
    comment("modified:   application/AnaInConfigCtrl/AnaInMeasureValueCtrl.cpp")
    comment("modified:   application/DosingPumpCtrl/NonGFDosingPumpCtrl.cpp")
    comment("modified:   application/DosingPumpCtrl/NonGFDosingPumpCtrl.h")
    comment("modified:   application/display/AnalogInputConfListView.cpp")
    comment("modified:   application/display/state/AnalogInputFunctionState.cpp")
    comment("modified:   include/AppTypeDefs.h")



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
    t.subject_id = 'dosing_pump_enabled'
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
    t.label_name = '4.2.14 Dosing pump go to setting'
    t.label_define_name = 'SID_H2S_DOSING_PUMP_SETTING'
    t.label_string = 'Dosing pump setting'
    t.listview_id = '4.2.14 H2S Contol List'
    t.label_left_margin = 2
    t.label_right_margin = 1

    t.availabel_rule_name = 'Availabel rule: dosing pump installed'
    t.availabel_rule_type = 'AvalibleIfSet'
    t.availabel_rule_checkstate = 1
    t.availabel_rule_subject_id = 'dosing_pump_enabled'
    t.availabel_rule_column_index = 2

    t.group_name = '4.2.14.1 H2S Dosing pump group'
    t.group_define_name = 'SID_H2S_DOSING_PUMP_SETTING'

    t.root_group_id_name = '4.2.14.1 H2S Dosing pump group'
    t.display_string_name = 'Dosing pump setting'
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
