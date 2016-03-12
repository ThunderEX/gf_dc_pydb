# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *
from common import *

def h2s_factory():
    comment('**************************** Factory部分 ****************************')
    change_profile_version_code(6)

    comment('添加语言Latvia')
    table = Languages(id=27, Language='LV_LANGUAGE', iso_name='lv-LV', uk_name='Latvia')
    table.add()

    t = template('NewQuantity')
    t.description = '---------- 添加quantity:ppm ----------'
    t.type_name = 'Q_PARTS_PER_MILLION'
    t.define_name = 'SID_PPM'
    t.string = 'ppm'
    t.save()
    comment('Note: 需要修改UnitTypes.h, mpcunits.conf.cpp和mpcunits.cpp')


    t = template('NewSubject')
    t.description = '---------- 为ppm加Subject: unit_ppm_actual ----------'
    t.subject_name = 'unit_ppm_actual'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'units'
    t.observer_type = 'MpcUnits'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'Q_PARTS_PER_MILLION'

    t.int_value = '0'
    t.int_type = 'I32'
    t.int_min = '0'
    t.int_max = '10'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()


    t = template('NewQuantity')
    t.description = '---------- 添加quantity:ml/h ----------'
    t.type_name = 'Q_SMALL_FLOW'
    t.define_name = 'SID_ml_h'
    t.string = 'ml/h'
    t.save()
    comment('Note: 需要修改UnitTypes.h, mpcunits.conf.cpp和mpcunits.cpp')


    t = template('NewSubject')
    t.description = '---------- 为ml/h加Subject: unit_small_flow ----------'
    t.subject_name = 'unit_small_flow_actual'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'units'
    t.observer_type = 'MpcUnits'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'Q_SMALL_FLOW'

    t.int_value = '0'
    t.int_type = 'I32'
    t.int_min = '0'
    t.int_max = '10'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False
    t.save()

    
    ######################################### Observer ################################################
    t = template('NewObserver')
    t.description = '---------- 加Observer: DDACtrl ----------'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.short_name = 'DDAC'
    t.save()


    t = template('NewObserver')
    t.description = '---------- 加Observer: NonGFDosingPumpCtrl ----------'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.short_name = 'DPC'
    t.save()


    t = template('NewObserver')
    t.description = '---------- 加Observer: DDA ----------'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.short_name = 'DDA'
    t.constructor_args = 'DDA_NO_1'
    t.save()


    ########################################## GENI Convert ###########################################
    t = template('NewGeniConvert')
    t.description = '---------- 加GeniConvert: PERCENTAGE_1PPM ----------'
    t.name = 'PERCENTAGE_1PPM'
    t.geni_info = 'COMMON_INFO + COM_INDEX_EXT_PERCENTAGE_1PPM'
    t.comment = 'Percentage 1ppm'
    t.save()


    t = template('NewGeniConvert')
    t.description = '---------- 加GeniConvert: FLOW_DOT1LH ----------'
    t.name = 'FLOW_DOT1LH'
    t.geni_info = 'COMMON_INFO + COM_INDEX_EXT_FLOW_DOT1LH'
    t.comment = 'Flow 0.1L/H'
    t.save()


    t = template('NewGeniConvert')
    t.description = '---------- 加GeniConvert: VOLUME_1ML ----------'
    t.name = 'VOLUME_1ML'
    t.geni_info = 'COMMON_INFO + COM_INDEX_EXT_VOLUME_1ML'
    t.comment = 'Volume 1mL'
    t.save()


    ######################################### Subject ################################################
    t = template('ObserverLinkSubject')
    t.description = '---------- DDACtrl与any_pump_running挂接 ----------'
    t.subject_name =  'any_pump_running'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'ANY_PUMP_RUNNING'
    t.subject_access = 'Read'
    t.save()

    
    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_pump_installed ----------'
    t.subject_name =  'dosing_pump_installed'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_pump_installed'
    t.subject_access = 'Read/Write'
    t.bool_value = 0
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: analog_dosing_pump_installed ----------'
    t.subject_name =  'analog_dosing_pump_installed'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'ANALOG_DOSING_PUMP_INSTALLED'
    t.bool_value = 0
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与analog_dosing_pump_installed挂接 ----------'
    t.subject_name =  'analog_dosing_pump_installed'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'ANALOG_DOSING_PUMP_INSTALLED'
    t.subject_access = 'Read'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dda_installed ----------'
    #SP_DDA_dda_installed
    t.subject_name =  'dda_installed'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dda_installed'

    t.bool_value = 0
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- DDA与dda_installed挂接 ----------'
    t.subject_name =  'dda_installed'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'dda_installed'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dosing_pump_type ----------'
    t.subject_name = 'dosing_pump_type'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_pump_type'
    t.subject_access = 'Read/Write'
    t.enum_type_name = 'DOSING_PUMP_TYPE'
    t.enum_value = 'DDA'
    t.subject_access = 'Read/Write'

    t.geni_var_name = 'pit_pump_conn_type'
    t.geni_class = 11
    t.geni_id = 35
    t.auto_generate = False
    t.geni_convert_id = 'Bits without NA'
    t.geni_comment = 'pit_pump_conn_type'
    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, t.subject_name.upper()))


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dosing_pump_operating_mode ----------'
    t.subject_name = 'dosing_pump_operating_mode'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'OPERATION_MODE_DOSING_PUMP'
    t.subject_access = 'Write'
    t.enum_type_name = 'ACTUAL_OPERATION_MODE'
    t.enum_value = 'NOT_INSTALLED'

    t.geni_var_name = 'pit_pump_mode'
    t.geni_class = 11
    t.geni_id = 32
    t.auto_generate = False
    t.geni_convert_id = 'Bits without NA'
    t.geni_comment = 'pit_pump_mode'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_operating_mode挂接 ----------'
    t.subject_name =  'dosing_pump_operating_mode'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'OPERATION_MODE_DOSING_PUMP'
    t.subject_access = 'Write'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_operating_mode挂接 ----------'
    t.subject_name =  'dosing_pump_operating_mode'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'OPERATION_MODE_DOSING_PUMP'
    t.subject_access = 'Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_act ----------'
    #SP_DDAC_H2S_LEVEL_ACT
    t.subject_name = 'h2s_level_act'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'h2s_level_act'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_PARTS_PER_MILLION'
    t.int_verified = False

    t.geni_var_name = 'h2s_level_act'
    t.geni_class = 14
    t.geni_id = 190
    t.auto_generate = True
    t.geni_convert_id = 'Percentage 1ppm'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- LoggingCtrl与h2s_level_act挂接 ----------'
    t.subject_name =  'h2s_level_act'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_relation_name = 'H2S_LEVEL_ACT'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_today_log ----------'
    t.subject_name = 'h2s_level_today_log'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Log'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_relation_name = 'H2S_LEVEL_TODAY_LOG'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_PARTS_PER_MILLION'
    t.int_verified = False

    t.geni_var_name = 'h2s_level_today_log'
    t.geni_class = 14
    t.geni_id = 191
    t.auto_generate = True
    t.geni_convert_id = 'Percentage 1ppm'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_yesterday_log ----------'
    t.subject_name = 'h2s_level_yesterday_log'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_relation_name = 'H2S_LEVEL_YESTERDAY_LOG'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_PARTS_PER_MILLION'
    t.int_verified = False

    t.geni_var_name = 'h2s_level_yesterday_log'
    t.geni_class = 14
    t.geni_id = 192
    t.auto_generate = True
    t.geni_convert_id = 'Percentage 1ppm'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_72h_log ----------'
    t.subject_name = 'h2s_level_72h_log'
    t.subject_type_id = 'VectorDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'H2S_LEVEL_72H_LOG'

    t.vector_type = 'I32'
    t.vector_initial_size = 72
    t.vector_max_size = 72
    t.vector_default_value = '-1'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_feed_tank_level ----------'
    t.subject_name = 'dosing_feed_tank_level'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_feed_tank_level'
    t.subject_access = 'Read/Write'

    t.float_value = 0.0
    t.float_min = 0
    t.float_max = 999.9
    t.float_quantity_type = 'Q_HEIGHT'

    t.geni_var_name = 'dosing_feed_tank_level'
    t.geni_class = 14
    t.geni_id = 193
    t.auto_generate = True
    t.geni_convert_id = 'Head/Distance, 0.01 m'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: chemical_total_dosed, 显示在HMI上 ----------'
    t.subject_name = 'chemical_total_dosed'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'CHEMICAL_TOTAL_DOSED'
    t.subject_access = 'Read/Write'

    t.float_value = 0.0
    t.float_min = 0
    #t.float_max = 999999.9
    t.float_max = 999.999
    t.float_quantity_type = 'Q_VOLUME'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与chemical_total_dosed挂接 ----------'
    t.subject_name =  'chemical_total_dosed'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'CHEMICAL_TOTAL_DOSED'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: running_dosing_volume ----------'
    t.subject_name = 'running_dosing_volume'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'RUNNING_DOSING_VOLUME'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '0xFFFFFFFF'
    t.int_quantity_type = 'Q_VOLUME'
    t.int_verified = False
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与running_dosing_volume挂接 ----------'
    t.subject_name =  'running_dosing_volume'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'RUNNING_DOSING_VOLUME'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- LoggingCtrl与running_dosing_volume挂接 ----------'
    t.subject_name =  'running_dosing_volume'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_relation_name = 'RUNNING_DOSING_VOLUME'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_volume_total_log ----------'
    t.subject_name = 'dosing_volume_total_log'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'DOSING_VOLUME_TOTAL_LOG'

    t.float_value = 0.0
    t.float_min = 0.0
    t.float_max = 999999.9999
    t.float_quantity_type = 'Q_VOLUME'

    t.geni_var_name = 'dosing_volume_total_log'
    t.geni_class = 14
    t.geni_id = 194
    t.auto_generate = True
    t.geni_convert_id = 'Volume 1mL'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_volume_total_log挂接 ----------'
    t.subject_name =  'dosing_volume_total_log'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'DOSING_VOLUME_TOTAL_LOG'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_volume_today_log ----------'
    t.subject_name = 'dosing_volume_today_log'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Log'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'DOSING_VOLUME_TODAY_LOG'

    t.float_value = 0.0
    t.float_min = 0.0
    t.float_max = 999999.9999
    t.float_quantity_type = 'Q_VOLUME'

    t.geni_var_name = 'dosing_volume_today_log'
    t.geni_class = 14
    t.geni_id = 195
    t.auto_generate = True
    t.geni_convert_id = 'Volume 1mL'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_volume_yesterday_log ----------'
    t.subject_name = 'dosing_volume_yesterday_log'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'DOSING_VOLUME_YESTERDAY_LOG'

    t.float_value = 0.0
    t.float_min = 0.0
    t.float_max = 999999.9999
    t.float_quantity_type = 'Q_VOLUME'

    t.geni_var_name = 'dosing_volume_yesterday_log'
    t.geni_class = 14
    t.geni_id = 196
    t.auto_generate = True
    t.geni_convert_id = 'Volume 1mL'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_volume_1h_acc ----------'
    t.subject_name = 'dosing_volume_1h_acc'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Log'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'DOSING_VOLUME_1H_ACC'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '10000000'
    t.int_quantity_type = 'Q_VOLUME'
    t.int_verified = False
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_volume_72h_log ----------'
    t.subject_name = 'dosing_volume_72h_log'
    t.subject_type_id = 'VectorDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'logging_ctrl'
    t.observer_type = 'LoggingCtrl'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'DOSING_VOLUME_72H_LOG'

    t.vector_type = 'I32'
    t.vector_initial_size = 72
    t.vector_max_size = 72
    t.vector_default_value = '-1'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_ref_act ----------'
    t.subject_name = 'dosing_ref_act'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.geni_app_if = True
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_ref_act'
    t.subject_access = 'Write'

    t.float_value = 0
    t.float_min = 0
    t.float_max = 999999
    t.float_quantity_type = 'Q_SMALL_FLOW'

    t.geni_var_name = 'dosing_ref_act'
    t.geni_class = 14
    t.geni_id = 197
    t.auto_generate = True
    t.geni_convert_id = 'Flow 0.1L/H'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- DDA与dosing_ref_act挂接 ----------'
    t.subject_name =  'dosing_ref_act'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'DOSING_REF_ACT'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_ref_act挂接 ----------'
    t.subject_name =  'dosing_ref_act'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'DOSING_REF_ACT'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: set_h2s_level ----------'
    t.subject_name = 'set_h2s_level'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.geni_app_if = True
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'set_h2s_level'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_PARTS_PER_MILLION'
    t.int_verified = False

    t.geni_var_name = 'set_h2s_level'
    t.geni_class = 13
    t.geni_id = 4
    t.auto_generate = True
    t.geni_convert_id = 'Percentage 1ppm'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: set_h2s_fault ----------'
    t.subject_name = 'set_h2s_fault'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.geni_app_if = True
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'set_h2s_fault'
    t.subject_access = 'Read/Write'

    t.int_value = '0'
    t.int_type = 'U16'
    t.int_min = '0'
    t.int_max = '0xFFFF'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False

    t.geni_var_name = 'set_h2s_fault'
    t.geni_class = 13
    t.geni_id = 5
    t.auto_generate = True
    t.geni_convert_id = 'Bits without NA'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: set_dosing_ref ----------'
    t.subject_name = 'set_dosing_ref'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.geni_app_if = True
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'set_dosing_ref'
    t.subject_access = 'Write'

    t.float_value = 0
    t.float_min = 0
    t.float_max = 999999
    t.float_quantity_type = 'Q_SMALL_FLOW'

    t.geni_var_name = 'set_dosing_ref'
    t.geni_class = 13
    t.geni_id = 6
    t.auto_generate = True
    t.geni_convert_id = 'Flow 0.1L/H'
    t.save()
    

    t = template('NewSubject')
    t.description = '---------- 加Subject: dda_reference，DDA driver和DDACtrl交换数据用----------'
    #SP_DDA_dda_reference
    t.subject_name =  'dda_reference'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dda_reference'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '9999999'
    t.int_quantity_type = 'Q_SMALL_FLOW'
    t.int_verified = False
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- DDA与alarm_reset_event挂接 ----------'
    t.subject_name =  'alarm_reset_event'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'SYSTEM_ALARM_RESET_EVENT'
    t.subject_access = 'Read/Write'
    t.save()


    ######################################### Alarm ################################################
    t = template('NewString')
    t.description = '''---------- 新加alarm 类型的string: Dosing pump ----------'''
    t.define_name = 'SID_UNIT_DOSING_PUMP'
    t.string_name = 'Dosing pump'
    t.save()


    t = template('Erroneous')
    t.description = '''---------- 新建一个alarm的类型: DOSING_PUMP ----------'''
    t.id = 18
    t.name = 'DOSING_PUMP'
    t.string_id = 'SID_UNIT_DOSING_PUMP'
    t.unit_number = 0
    t.save()


    #原来system_alarm_status_4和system_warning_status_4是个dummy值，要把它加到GeniAppIf里
    table = GeniAppIf(**{'GeniVarName':'pit_alarms4', 'GeniClass':11, 'GeniId':55, 'SubjectId':'system_alarm_status_4', 'GeniConvertId':'Bits without NA', 'AutoGenerate':True, })
    table.add()
    table = GeniAppIf(**{'GeniVarName':'pit_warn4', 'GeniClass':11, 'GeniId':56, 'SubjectId':'system_warning_status_4', 'GeniConvertId':'Bits without NA', 'AutoGenerate':True, })
    table.add()
    

    #先加一个字符串'Dosing pump alarm'显示在'3.1 - current alarms'里
    t = template('NewString')
    t.description = '''---------- 新加alarm的string: H2S sensor fault (118) ----------'''
    t.define_name = 'SID_ALARM_118_H2S_SENSOR_FAULT'
    t.string_name = 'H2S sensor fault (118)'
    t.save()


    t = template('NewAlarm')
    t.description = '''---------- 新加alarm: h2s_sensor_fault_obj ----------'''
    t.alarm_config_subject.subject_name = 'h2s_sensor_fault_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.subject_access = 'Read/Write'
    t.alarm_config_subject.alarm_config_alarm_enabled = True
    #t.alarm_config_subject.alarm_config_warning_enabled = True
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

    t.alarm_subject.subject_name = 'h2s_sensor_fault_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'dda_ctrl'
    t.alarm_subject.observer_type = 'DDACtrl'
    t.alarm_subject.subject_relation_name = 'H2S_SENSOR_FAULT_OBJ'
    t.alarm_subject.alarm_alarm_config_id = 'h2s_sensor_fault_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'SYSTEM'       # in pit_alarm_3, so it is system alarm
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_118_H2S_SENSOR_FAULT'
    t.alarm_define_name = 'SID_ALARM_118_H2S_SENSOR_FAULT'
    t.alarm_id = 118
    t.save()


    #这里沿用已有的string，所以不需要新加string
    t = template('NewAlarm')
    t.description = '''---------- 新加alarm: dda_geni_comm_fault_obj ----------'''
    t.alarm_config_subject.subject_name = 'dda_geni_comm_fault_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.subject_access = 'Read/Write'
    t.alarm_config_subject.alarm_config_alarm_enabled = True
    #t.alarm_config_subject.alarm_config_warning_enabled = True
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

    t.alarm_subject.subject_name = 'dda_geni_comm_fault_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'dda'
    t.alarm_subject.observer_type = 'DDA'
    t.alarm_subject.subject_relation_name = 'DDA_GENI_COMM_FAULT_OBJ'
    t.alarm_subject.alarm_alarm_config_id = 'dda_geni_comm_fault_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'DOSING_PUMP'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_226_GENIBUS_ERROR'
    t.alarm_define_name = 'SID_ALARM_226_GENIBUS_ERROR'
    t.save()


def h2s_display():
    comment('**************************** Display Database部分 ****************************')

    t = template('AvailableRule')
    t.description = '''---------- 添加一个Available rule: dosing pump installed ---------- '''
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_type = 'AvalibleIfSet'
    t.available_rule_checkstate = 1
    t.available_rule_subject_id = 'dosing_pump_installed'
    t.save()
    
    
    t = template('AvailableRule')
    t.description = '''---------- 添加一个Available rule: analog dosing pump selected ---------- '''
    t.available_rule_name = 'Available rule: analog dosing pump selected'
    t.available_rule_type = 'AvalibleIfSet'
    t.available_rule_checkstate = 1
    t.available_rule_subject_id = 'analog_dosing_pump_installed'
    t.save()   
    

    comment('在4.5.x里，因为加了两项在4.5.1 System Alarm里，导致后面的4.5.2 Pump Alarm等内容错位，需要先将write_state>30的依次后推')
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
        #comment('更新表WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay，id=%d, WriteState=%d' %(l[0], l[1]))
    #1464 | 4.5.2.x PumpAlarms (onoffauto) slippoint, WriteState=30, 有重复，拿出来单独处理
    table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
    table.update(id=1464, WriteState=32)


    comment('加DDA的一系列Alarm')
    dda_alram_strings = [
        #(210, 'SID_ALARM_210_DDA_OVER_PRESSURE'                   , 'Over pressure (210)'),   #已有
        #(211, 'SID_ALARM_211_DDA_MEAN_PRESSURE_TO_LOW'            , 'Mean pressure to low (211)'),   #已有
        (35,  'SID_ALARM_035_DDA_GAS_IN_PUMP_HEAD'                 , 'Gas in pump head, deaerating problem (35)'),
        #(208, 'SID_ALARM_208_DDA_CAVITATIONS'                     , 'Cavitations (208)'),   #已有
        (36,  'SID_ALARM_036_DDA_PRESSURE_VALVE_LEAKAGE'           , 'Discharge valve leakage (36)'),
        (37,  'SID_ALARM_037_DDA_SUCTION_VALVE_LEAKAGE'            , 'Suction valve leakage (37)'),
        (38,  'SID_ALARM_038_DDA_VENTING_VALVE_DEFECT'             , 'Vent valve defective (38)'),
        #(12, 'SID_ALARM_12_DDA_TIME_FOR_SERVICE_IS_EXCEED'       , 'Time for service is exceed (12)'),   #已有
        (33,  'SID_ALARM_033_DDA_SOON_TIME_FOR_SERVICE'            , 'Soon time for service (33)'),
        #(17,  'SID_ALARM_17_DDA_CAPACITY_TOO_LOW'                 , 'Capacity too low (17)'),   #已有
        #(19,  'SID_ALARM_19_DDA_DIAPHRAGM_BREAK'                  , 'Diaphragm break (19)'),
        #(51, 'SID_ALARM_51_DDA_BLOCKED_MOTOR_OR_PUMP'            , 'Blocked motor/pump (51)'),   #已有
        #(206, 'SID_ALARM_206_DDA_PRE_EMPTY_TANK'                  , 'Pre empty tank (206)'),   #已有
        #(57, 'SID_ALARM_57_DDA_EMPTY_TANK'                       , 'Empty tank (57)'),   #已有
        #(169,'SID_ALARM_169_DDA_CABLE_BREAKDOWN_ON_FLOW_MONITOR' , 'Cable breakdown on Flow Monitor (169)'),   #已有
        (47,  'SID_ALARM_047_DDA_CABLE_BREAKDOWN_ON_ANALOGUE'      , 'Fault, analog input (47)'),
    ]
    for alarm_string in dda_alram_strings:
        t = template('AlarmString')
        t.description = '---------- 加Alarm String: %s ----------' % (alarm_string[1])
        t.alarm_id = alarm_string[0]
        t.alarm_define_name = alarm_string[1]
        t.alarm_string = alarm_string[2]
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
    t.alarm_config_subject.subject_name = 'sys_alarm_dda_fault_alarm_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.observer_name = 'display_alarm_slippoint'
    t.alarm_config_subject.observer_type = 'AlarmSlipPoint'
    t.alarm_config_subject.subject_relation_name = 'sys_alarm_dda_fault'
    t.alarm_config_subject.subject_access = 'Read/Write'

    t.alarm_config_subject.alarm_config_alarm_enabled = True
    t.alarm_config_subject.alarm_config_warning_enabled = True
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

    #加subject:sys_alarm_dda_fault_alarm_obj
    t.alarm_subject.subject_name = 'sys_alarm_dda_fault_alarm_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'dda'
    t.alarm_subject.observer_type = 'DDA'
    t.alarm_subject.subject_relation_name = 'sys_alarm_dda_fault_alarm_obj'

    t.alarm_subject.alarm_alarm_config_id = 'sys_alarm_dda_fault_alarm_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'DOSING_PUMP'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_016_OTHER'

    t.alarm_alarm_string_id = 'SID_ALARM_016_OTHER'    #默认是Other，实际使用时会SetValue一个Alarm_ID

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


    #先加一个字符串'Dosing pump alarm'显示在'3.1 - current alarms'里
    t = template('NewString')
    t.description = '''---------- 3.1 - Current alarms页面里新加一个alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |3.1 - Current alarms                           |
    +-----------------------------------------------+
    |                                               |
    | (!)CU 362                                     |
--> |  Dosing pump not ready (102)                  |
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
    t.define_name = 'SID_ALARM_102_DOSING_PUMP'
    t.string_name = 'Dosing pump not ready (102)'
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
--> |  Analog dosing pump                           |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.5.1 SystemAlarms (analog dosing pump)'
    t.label_define_name = 'SID_ANALOG_DOSING_PUMP'
    t.label_string = 'Analog dosing pump'
    t.slippoint_name = '4.5.1 SystemAlarms (analog dosing pump) slippoint'
    t.write_state = 31

    #加subject: sys_alarm_dosing_pump_alarm_conf 类型为AlarmConfig
    t.alarm_config_subject.subject_name = 'sys_alarm_dosing_pump_alarm_conf'
    t.alarm_config_subject.subject_type_id = 'AlarmConfig'
    t.alarm_config_subject.geni_app_if = False
    t.alarm_config_subject.subject_save = 'Value'
    t.alarm_config_subject.flash_block = 'Config'
    t.alarm_config_subject.observer_name = 'display_alarm_slippoint'
    t.alarm_config_subject.observer_type = 'AlarmSlipPoint'
    t.alarm_config_subject.subject_relation_name = 'sys_alarm_dosing_pump'
    t.alarm_config_subject.subject_access = 'Read/Write'

    t.alarm_config_subject.alarm_config_alarm_enabled = True
    t.alarm_config_subject.alarm_config_warning_enabled = True
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

    #SP_DDA_SYS_ALARM_DOSING_PUMP_ALARM_OBJ
    #加subject:sys_alarm_dosing_pump_alarm_obj
    t.alarm_subject.subject_name = 'sys_alarm_dosing_pump_alarm_obj'
    t.alarm_subject.subject_type_id = 'AlarmDataPoint'
    t.alarm_subject.geni_app_if = False
    t.alarm_subject.subject_save = '-'
    t.alarm_subject.flash_block = '-'
    t.alarm_subject.observer_name = 'nongf_dosing_pump_ctrl'
    t.alarm_subject.observer_type = 'NonGFDosingPumpCtrl'
    t.alarm_subject.subject_relation_name = 'sys_alarm_dosing_pump_alarm_obj'

    t.alarm_subject.alarm_alarm_config_id = 'sys_alarm_dosing_pump_alarm_conf'
    t.alarm_subject.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_subject.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_subject.alarm_erroneous_unit_number = 0
    t.alarm_subject.alarm_alarm_id = 'SID_ALARM_102_DOSING_PUMP'

    t.alarm_alarm_id = 102
    t.alarm_alarm_string_id = 'SID_ALARM_102_DOSING_PUMP'      #不同于DDA的Alarm，这里只有一个Alarm，所以新加一个字串，固定显示

    comment('在AppTypeDefs.h里插入AC_SYS_ALARM_DOSING_PUMP')
    comment('在AlarmState.cpp里插入一行{AC_SYS_ALARM_DOSING_PUMP,                  SID_ANALOG_DOSING_PUMP},')
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
    t.label_define_name = 'SID_ANALOG_DOSING_PUMP'
    t.label_string = 'Analog dosing pump'
    t.alarm_icon_name = '4.5.5 SystemAlarms Status (dosing pump) alarm icon'
    t.warning_icon_name = '4.5.5 SystemAlarms Status (dosing pump) warning icon'
    t.subject_id = 'sys_alarm_dosing_pump_alarm_conf'
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


    t = template('NewSubject')
    t.description = '---------- 加Subject, EnumDataPoint: dig_in_func_state_dosing_pump ----------'
    t.subject_name = 'dig_in_func_state_dosing_pump'
    t.subject_type_id = 'EnumDataPoint'
    t.geni_app_if = False
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'digital_input_function_handler'
    t.observer_type = 'DiFuncHandler'
    t.subject_relation_name = 'dig_in_func_state_dosing_pump'
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
    t.description = '---------- DigitalInputConfListView与analog_dosing_pump_installed挂接 ----------'
    t.subject_name =  'analog_dosing_pump_installed'
    t.observer_name = 'display_dig_in_conf_listview'
    t.observer_type = 'DigitalInputConfListView'
    t.subject_relation_name = 'ANALOG_DOSING_PUMP_INSTALLED'
    t.subject_access = 'Read/Write'
    t.save()
    

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dig_in_func_state_dosing_pump挂接 ----------'
    t.subject_name =  'dig_in_func_state_dosing_pump'
    t.observer_name = 'nongf_dosing_pump_ctrl'
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


    t = template('ObserverLinkSubject')
    t.description = '---------- DigitalOutputConfListView与analog_dosing_pump_installed挂接 ----------'
    t.subject_name =  'analog_dosing_pump_installed'
    t.observer_name = 'display_dig_out_conf_listview'
    t.observer_type = 'DigitalOutputConfListView'
    t.subject_relation_name = 'ANALOG_DOSING_PUMP_INSTALLED'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与relay_status_relay_func_dosing_pump挂接 ----------'
    t.subject_name =  'relay_status_relay_func_dosing_pump'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'RELAY_STATUS_RELAY_FUNC_DOSING_PUMP'
    t.subject_access = 'Write'
    t.save()


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
    t.description = '---------- 加Subject: measured_value_chemical_container ----------'
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
    t.description = '---------- AnalogInputConfListView与dosing_pump_installed挂接，作为AvailableRule ----------'
    t.subject_name =  'dosing_pump_installed'
    t.observer_name = 'display_ana_in_conf_listview'
    t.observer_type = 'AnalogInputConfListView'
    t.subject_relation_name = 'DOSING_PUMP_INSTALLED'
    t.subject_access = 'Read'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- DDACtrl与measured_value_chemical_container挂接 ----------'
    t.subject_name =  'measured_value_chemical_container'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'measured_value_chemical_container'
    t.subject_access = 'Read'
    t.save()
    comment("modified:   application/AnaInConfigCtrl/AnaInMeasureValueCtrl.cpp")
    comment("modified:   application/DosingPumpCtrl/NonGFDosingPumpCtrl.cpp")
    comment("modified:   application/DosingPumpCtrl/NonGFDosingPumpCtrl.h")
    comment("modified:   application/display/AnalogInputConfListView.cpp")
    comment("modified:   application/display/state/AnalogInputFunctionState.cpp")
    comment("modified:   include/AppTypeDefs.h")


    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.4.3.x - Function of analog output页面里新加一行Dosing pump setpoint ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.3.1 - Function of analog output            |
    +-----------------------------------------------+
    |                                               |
    |Function, AO1 (IO351B-41)                      |
    |  Not used                             ☐       |
    |  Surface level                        ☐       |
    |  VFD frequency, pump 1                ☐       |
    |  User-defined output 1                ☐       |
    |  User-defined output 2                ☐       |
    |  User-defined output 3                ☐       |
--> |  Dosing pump setpoint                 ☐       |
    |                                               |
    |                                               |
    |Output range                                   |
    | Min. (0V)                              0m     |
    | Max. (10V)                             5m     |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.4.3.1 AnalogOutputSetup func dosing pump'
    t.checkbox_name = '4.4.3.1 AnalogOutputSetup func dosing pump cb'
    t.checkbox_type = 'ModeCheckBox'
    t.define_name = 'SID_AO_DOSING_PUMP_SETPOINT'
    t.label_string = 'Dosing pump setpoint'
    t.listview_id = '4.4.3.1 AnalogOutputSetup List 1 func'
    t.subject_id = 'display_ao_slippoint_virtual_func'
    t.check_state = 11
    t.label_left_margin = 8
    t.label_right_margin = 0
    t.listviewitem_index = 11
    t.available_rule_name = 'Available rule: analog dosing pump selected'
    t.available_rule_column_index = 2
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: ao_dosing_pump_setpoint ----------'
    t.subject_name = 'ao_dosing_pump_setpoint'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'ana_out_ctrl'
    t.observer_type = 'AnaOutCtrl'
    t.subject_relation_name = 'ANA_OUT_FUNC_DOSING_PUMP'
    t.subject_access = 'Read'

    t.float_value = 0
    t.float_min = 0
    t.float_max = 999999.0
    t.float_quantity_type = 'Q_SMALL_FLOW'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与ao_dosing_pump_setpoint挂接 ----------'
    t.subject_name =  'ao_dosing_pump_setpoint'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'AO_DOSING_PUMP_SETPOINT'
    t.subject_access = 'Write'
    t.save()

    comment("modified:   include/AppTypeDefs.h")
    comment("modified:   AnaOutCtrl/AnaOutCtrl.cpp")
    comment("modified:   display/state/AnalogOutputFunctionState.cpp")


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
    | Dosing feed tank level             23.1m      |
    | Dosed in total                     32.5㎥     |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 h2s level'
    t.label_left_margin = 2
    t.quantity_name = '1.1 SystemStatus l1 h2s level nq'
    t.define_name = 'SID_H2S_LEVEL'
    t.label_string = 'H2S level'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'h2s_level_act'
    t.quantity_type =  'Q_PARTS_PER_MILLION'
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 4
    t.save()


    t = template('LabelAndQuantity')
    t.description = '''---------- 1.1 - System 页面里新加一行label:Dosing feed tank level ----------
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
--> | Dosing feed tank level             23.1m      |
    | Dosed in total                     32.5㎥     |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 dosing feed tank level'
    t.label_left_margin = 2
    t.quantity_name = '1.1 SystemStatus l1 dosing feed tank level nq'
    t.define_name = 'SID_DOSING_FEED_TANK_LEVEL'
    t.label_string = 'Dosing feed tank level'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'dosing_feed_tank_level'
    t.quantity_type =  'Q_HEIGHT'
    t.number_of_digits = 5
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 4
    t.save()


    t = template('LabelAndQuantity')
    t.description = '''---------- 1.1 - System 页面里新加一行label:Chemical dosed----------
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
    | Dosing feed tank level             23.1m      |
--> | Dosed in total                     32.5㎥     |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 chemical total dosed'
    t.label_left_margin = 2
    t.quantity_name = '1.1 SystemStatus l1 chemical total dosed nq'
    t.define_name = 'SID_CHEMICAL_TOTAL_DOSED'
    t.label_string = 'Dosed in total'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'chemical_total_dosed'
    t.quantity_type = 'Q_VOLUME'
    t.number_of_digits = 7
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 4
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
    t.subject_id = 'dosing_pump_installed'
    t.save()


    t = template('LabelAndQuantity')
    t.description = '''---------- 4.2.5 - Adjustment of counters页面里新加一行Dosed in total ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.5 - Adjustment of counters                 |
    +-----------------------------------------------+
    |System                                         |
    |  Operating hours                   2:02h      |
    |  Parallel-operation time           0:00h      |
    |  Overflow time                     0:00h      |
    |  Number of overflows                  0       |
    |  Total Volume Overrun Cn              0       |
--> |  Dosed in total                    32.5㎥     |
    |                                               |
    |Pump 1                                         |
    |  Operating hours                   2:02h      |
    |  Time since service                0:00h      |
    |  Number of starts                     0       |
    |                                               |
    |Pump 1                                         |
    |  Operating hours                   2:02h      |
    |  Time since service                0:00h      |
    |  Number of starts                     0       |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2.5 AdjustCounters total chemical dosed'
    t.label_left_margin = 8
    t.quantity_name = '4.2.5 AdjustCounters total chemical dosed nq'
    t.quantity_type = 'Q_VOLUME'
    t.quantity_readonly = False
    t.quantity_align = 'VCENTER_HCENTER'
    t.define_name = 'SID_CHEMICAL_TOTAL_DOSED'
    #t.label_string = 'Total chemical dosed'
    t.listview_id = '4.2.5 AdjustCounters List'
    t.subject_id = 'chemical_total_dosed'
    t.subject_access = 'Read/Write'
    t.listviewitem_index = 7    #replace index 7 with new inserted item
    t.number_of_digits = 7
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 4
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
--> |H2S control                                    |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '4.2 AdvancedFunc H2S Contol'
    t.label_define_name = 'SID_H2S_CONTROL'
    t.label_string = 'H2S control'
    t.listview_id = '4.2 AdvancedFunc List 1'

    t.group_name = '4.2.14 H2S Contol Group'
    t.group_define_name = 'SID_H2S_CONTROL'

    t.root_group_id_name = '4.2.14 H2S Contol Group'
    t.display_string_name = 'H2S control'
    t.display_number = '4.2.14'

    t.listview_name = '4.2.14 H2S Contol List'
    t.listview_column_width = [160, 64, 0]
    t.save()


    t = template('LabelAndNewPage')
    t.description = '''---------- 4.2.14 - H2S control 页面里新加一行label:Dosing pump，点击跳进4.2.14.1 Dosing pump group ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14 - H2S control                           |
    +-----------------------------------------------+
    |                                               |
--> |Dosing pump setting                            |
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
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 2
    t.group_name = '4.2.14.1 H2S Dosing pump group'
    t.group_define_name = 'SID_H2S_DOSING_PUMP_SETTING'
    t.root_group_id_name = '4.2.14.1 H2S Dosing pump group'
    t.display_string_name = 'Dosing pump setting'
    t.display_number = '4.2.14.1'
    t.listview_name = '4.2.14.1 H2S Dosing pump List'
    t.listview_column_width = [164, 74, 0]
    t.save()


    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.14 - H2S control 页面里新加一行label: go to modules installed，点击进入4.1.7 Modules installed ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14 - H2S control                           |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump setting                            |
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
    |4.2.14.1 - Dosing pump setting                 |
    +-----------------------------------------------+
    |                                               |
--> |Dosing pump interface                          |
    |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
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
    t.label_name = '4.2.14.1 H2S dosing pump interface headline'
    t.define_name = 'SID_DOSING_PUMP_INTERFACE'
    t.label_string = 'Dosing pump interface'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.foreground_colour = 'GUI_COLOUR_TEXT_HEADLINE_FOREGROUND'
    t.background_colour = 'GUI_COLOUR_DEFAULT_BACKGROUND'
    t.save()


    t = template('LabelAndCheckbox')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Smart Digital DDA ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump setting                 |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
--> |  Smart Digital DDA                    ☑       |
    |  Analog dosing pump                   ☐       |
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
    |4.2.14.1 - Dosing pump setting                 |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☐       |
--> |  Analog dosing pump                   ☑       |
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
    t.define_name = 'SID_ANALOG_DOSING_PUMP'
    #t.label_string = 'Analog dosing pump'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.subject_id = 'dosing_pump_type'
    t.save()


    t = template('LabelBlank')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump setting                 |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☐       |
    |  Analog dosing pump                   ☑       |
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
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()


    t = template('LabelAndExistPage')
    t.description = '''---------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to setting of Analog outputs，点击进入4.4.3 Analog outputs ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.2.14.1 - Dosing pump setting                 |
    +-----------------------------------------------+
    |                                               |
    |Dosing pump interface                          |
    |  Smart Digital DDA                    ☐       |
    |  Analog dosing pump                   ☑       |
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
    t.label_name = '4.2.14.1 Dosing pump go to IO'
    t.label_string = 'Go to setting of I/O'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_IO'
    t.display_id = 47 # 4.4 IO Group
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.available_rule_name = 'Available rule: analog dosing pump selected'
    t.available_rule_column_index = 2
    t.save()


    t = template('LabelAndQuantity')
    t.description = '''---------- 1.1 - System 页面里新加一行label:Dosing pump setpoint ----------
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
    | Dosing feed tank level             23.1m      |
    | Dosed in total                     32.5㎥     |
--> | Dosing pump setpoint               5000ml/h   |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.label_name = '1.1 SystemStatus l1 dosing pump setpoint'
    t.label_left_margin = 2
    t.quantity_name = '1.1 SystemStatus l1 h2s dosing pump nq'
    t.define_name = 'SID_AO_DOSING_PUMP_SETPOINT'
    #t.label_string = 'Dosing pump setpoint'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'dda_reference'
    t.quantity_type =  'Q_SMALL_FLOW'
    t.number_of_digits = 5
    t.available_rule_name = 'Available rule: dosing pump installed'
    t.available_rule_column_index = 4
    t.save()


def h2s():
    h2s_factory()
    h2s_display()
