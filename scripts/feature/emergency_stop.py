# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def emergency_stop():
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
    |GRUNDFOS                       04-05-2015 11:13|
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

    for num in range(1, 7):
        t = template('ObserverLinkSubject')
        t.description = '---------- Pump与dig_in_func_state_emergency_stop挂接 ----------'
        t.subject_name =  'dig_in_func_state_emergency_stop'
        t.observer_name = 'pump_' + str(num)
        t.observer_type = 'Pump'
        t.subject_relation_name = 'EMERGENCY_STOP_DIG_IN_REQUEST'
        t.subject_access = 'Read'
        t.save()
