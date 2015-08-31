# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def h2s_factory():
    comment('**************************** Factory部分 ****************************')
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
    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_pump_installed ----------'
    #SP_DDA_dosing_pump_enabled
    t.subject_name =  'dosing_pump_installed'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_pump_installed'

    t.bool_value = 0
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_installed挂接 ----------'
    t.subject_name =  'dosing_pump_installed'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'dosing_pump_installed'
    t.subject_access = 'Read/Write'
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

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_type挂接 ----------'
    t.subject_name =  'dosing_pump_type'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'dosing_pump_type'
    t.subject_access = 'Read/Write'
    t.save()


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


    #--------------------------------------------------------------------------------------------------------#

    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_act ----------'
    #SP_DDAC_H2S_LEVEL_ACT
    t.subject_name = 'h2s_level_act'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = 'Value'
    t.flash_block = 'Log'
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
    t.float_quantity_type = 'Q_DEPTH'

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
    t.subject_save = '-'
    t.flash_block = '-'
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
    t.float_quantity_type = 'Q_VOLUME'

    t.geni_var_name = 'dosing_ref_act'
    t.geni_class = 14
    t.geni_id = 197
    t.auto_generate = True
    t.geni_convert_id = 'Flow 0.1L/H'
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
    t.float_quantity_type = 'Q_VOLUME'

    t.geni_var_name = 'set_dosing_ref'
    t.geni_class = 13
    t.geni_id = 6
    t.auto_generate = True
    t.geni_convert_id = 'Flow 0.1L/H'
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与set_dosing_ref挂接 ----------'
    t.subject_name =  'set_dosing_ref'
    t.observer_name = 'nongf_dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'set_dosing_ref'
    t.subject_access = 'Read/Write'
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
    t.int_max = '99999'
    t.int_quantity_type = 'Q_HEIGHT'
    t.int_verified = False
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- DDA与dda_reference挂接 ----------'
    t.subject_name =  'dda_reference'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'dda_reference'
    t.subject_access = 'Read/Write'
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
    t = template('Erroneous')
    t.description = '''---------- 新建一个alarm的类型: DOSING_PUMP ----------'''
    t.id = 18
    t.name = 'DOSING_PUMP'
    t.string_id = 'SID_UNIT_CU361'
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
    t.alarm_config_subject_name = 'h2s_sensor_fault_conf'
    t.alarm_config_subject_type_id = 'AlarmConfig'
    t.alarm_config_geni_app_if = False
    t.alarm_config_subject_save = 'Value'
    t.alarm_config_flash_block = 'Config'
    t.alarm_config_subject_access = 'Read/Write'

    t.alarm_config_alarm_enabled = True
    #t.alarm_config_warning_enabled = True
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

    t.alarm_subject_name = 'h2s_sensor_fault_obj'
    t.alarm_subject_type_id = 'AlarmDataPoint'
    t.alarm_geni_app_if = False
    t.alarm_subject_save = '-'
    t.alarm_flash_block = '-'
    t.alarm_observer_name = 'dda_ctrl'
    t.alarm_observer_type = 'DDACtrl'
    t.alarm_subject_relation_name = 'H2S_SENSOR_FAULT_OBJ'

    t.alarm_alarm_config_id = 'h2s_sensor_fault_conf'
    t.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_erroneous_unit_type_id = 'SYSTEM'       # in pit_alarm_3, so it is system alarm
    t.alarm_erroneous_unit_number = 0
    t.alarm_define_name = 'SID_ALARM_118_H2S_SENSOR_FAULT'
    t.alarm_id = 118

    t.save()

    #这里沿用已有的string，所以不需要新加string
    t = template('NewAlarm')
    t.description = '''---------- 新加alarm: dda_geni_comm_fault_obj ----------'''
    t.alarm_config_subject_name = 'dda_geni_comm_fault_conf'
    t.alarm_config_subject_type_id = 'AlarmConfig'
    t.alarm_config_geni_app_if = False
    t.alarm_config_subject_save = 'Value'
    t.alarm_config_flash_block = 'Config'
    t.alarm_config_subject_access = 'Read/Write'

    t.alarm_config_alarm_enabled = True
    #t.alarm_config_warning_enabled = True
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

    t.alarm_subject_name = 'dda_geni_comm_fault_obj'
    t.alarm_subject_type_id = 'AlarmDataPoint'
    t.alarm_geni_app_if = False
    t.alarm_subject_save = '-'
    t.alarm_flash_block = '-'
    t.alarm_observer_name = 'dda'
    t.alarm_observer_type = 'DDA'
    t.alarm_subject_relation_name = 'DDA_GENI_COMM_FAULT_OBJ'

    t.alarm_alarm_config_id = 'dda_geni_comm_fault_conf'
    t.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_erroneous_unit_type_id = 'SYSTEM'
    t.alarm_erroneous_unit_number = 0
    t.alarm_define_name = 'SID_ALARM_226_GENIBUS_ERROR'

    t.save()
