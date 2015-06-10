# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *

def h2s_factory():
    comment('**************************** Factory部分 ****************************')
    t = template('NewQuantity')
    t.description = '---------- 添加quantity:ppm ----------'
    t.type_name = 'Q_PARTS_PER_MILLION'
    t.define_name = 'SID_PPM'
    t.string = 'ppm'
    t.save()

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
    t.description = '---------- 添加quantity:l ----------'
    t.type_name = 'Q_LEVEL'
    t.define_name = 'SID_l'
    #t.string = 'l'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 为l加Subject: unit_level_actual ----------'
    t.subject_name = 'unit_level_actual'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'units'
    t.observer_type = 'MpcUnits'
    t.subject_access = 'Read/Write'
    t.subject_relation_name = 'Q_LEVEL'

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
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.short_name = 'DPC'
    t.save()

    t = template('NewObserver')
    t.description = '---------- 加Observer: DDA ----------'
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.short_name = 'DDA'
    t.save()

    ########################################## GENI Convert ###########################################
    t = template('NewGeniConvert')
    t.description = '---------- 加GeniConvert: PERCENTAGE_1PPM ----------'
    t.name = 'PERCENTAGE_1PPM'
    t.geni_info = 'COMMON_INFO + COM_INDEX_EXT_PERCENTAGE_1PPM'
    t.comment = 'Precentage 1ppm'
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
    t.description = '---------- 加Subject: dosing_pump_enabled ----------'
    #SP_DDA_dosing_pump_enabled
    t.subject_name =  'dosing_pump_enabled'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_pump_enabled'

    t.bool_value = 0
    t.save()

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_enabled挂接 ----------'
    t.subject_name =  'dosing_pump_enabled'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'dosing_pump_enabled'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewEnumData')
    t.description = '---------- 加Subject, EnumDataPoint: dosing_pump_type_dda, dosing_pump_type_analog ----------'
    #SP_DDA_DOSING_PUMP_TYPE_DDA, SP_DDA_DOSING_PUMP_TYPE_ANALOG
    #TODO 确认到底需要定义几个EnumDataPoint
    #t.enum_subject_names = ['dosing_pump_type_dda', 'dosing_pump_type_analog']
    t.enum_subject_names = ['dosing_pump_type']
    t.enum_geni_app_if = False
    t.enum_subject_save = 'Value'
    t.enum_flash_block = 'Config'
    t.enum_observer_name = 'dda_ctrl'
    t.enum_observer_type = 'DDACtrl'
    t.enum_subject_relation_names = ['dosing_pump_type']
    t.enum_subject_access = 'Read/Write'

    t.enum_type_name = 'DOSING_PUMP_TYPE'
    t.enum_values = ['DDA']

    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, str(t.enum_subject_names).upper()))

    t = template('ObserverLinkSubject')
    t.description = '---------- NonGFDosingPumpCtrl与dosing_pump_type挂接 ----------'
    t.subject_name =  'dosing_pump_type'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'NonGFDosingPumpCtrl'
    t.subject_relation_name = 'dosing_pump_type'
    t.subject_access = 'Read/Write'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_act ----------'
    #SP_DDA_H2S_LEVEL_ACT
    t.subject_name = 'h2s_level_act'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'h2s_level_act'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_PARTS_PER_MILLION'
    t.int_verified = False

    t.geni_var_name = 'h2s_level'
    t.geni_class = 14
    t.geni_id = 190
    t.subject_name = 'h2s_level_act'
    t.auto_generate = True
    t.geni_convert_id = 'Precentage 1ppm'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_feed_tank_level ----------'
    #SP_DDA_CHEMICAL_REMAINING
    t.subject_name = 'dosing_feed_tank_level'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_feed_tank_level'

    t.float_value = 0.1
    t.float_min = 0
    t.float_max = 999.9
    t.float_quantity_type = 'Q_DEPTH'

    t.geni_var_name = 'dosing_feed_tank_level'
    t.geni_class = 14
    t.geni_id = 193
    t.subject_name = 'dosing_feed_tank_level'
    t.auto_generate = True
    t.geni_convert_id = 'Dim. less with NA'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: chemical_total_dosed ----------'
    #SP_DDA_CHEMICAL_REMAINING
    t.subject_name = 'chemical_total_dosed'
    t.subject_type_id = 'FloatDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dda_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'chemical_total_dosed'

    t.float_value = 0.1
    t.float_min = 0
    t.float_max = 999.9
    t.float_quantity_type = 'Q_HEIGHT'

    t.geni_var_name = 'chemical_total_dosed'
    t.geni_class = 14
    t.geni_id = 194
    t.subject_name = 'chemical_total_dosed'
    t.auto_generate = True
    t.geni_convert_id = 'Volume 1mL'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: set_dosing_ref ----------'
    t.subject_name = 'set_dosing_ref'
    t.subject_type_id = 'FloatDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.geni_app_if = True
    t.observer_name = 'dda'
    t.observer_type = 'DDA'
    t.subject_relation_name = 'set_dosing_ref'
    t.subject_access = 'Write'

    t.float_value = 0
    t.float_min = 0
    t.float_max = 999
    # TODO set unit
    t.float_quantity_type = 'Q_HEIGHT'

    t.geni_var_name = 'set_dosing_ref'
    t.geni_class = 13
    t.geni_id = 6
    t.subject_name = 'set_dosing_ref'
    t.auto_generate = True
    t.geni_convert_id = 'Flow 0.1L/H'
    t.save()

