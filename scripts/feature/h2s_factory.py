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

    t = template('NewObserver')
    t.description = '---------- 加Observer: DDACtrl ----------'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.short_name = 'DDA'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: dda_control_enabled ----------'
    #SP_DDA_DDA_CONTROL_ENABLED
    t.subject_name =  'dda_control_enabled'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dda_control_enabled'

    t.bool_value = 0
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
    t.enum_observer_name = 'dosing_pump_ctrl'
    t.enum_observer_type = 'DDACtrl'
    t.enum_subject_relation_names = ['dosing_pump_type']
    t.enum_subject_access = 'Read/Write'

    t.enum_type_name = 'DOSING_PUMP_TYPE'
    t.enum_values = ['DDA']

    t.save()
    comment('Note：在AppTypeDefs.h里加入枚举类型%s，值：%s' %(t.enum_type_name, str(t.enum_subject_names).upper()))

    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_act ----------'
    #SP_DDA_H2S_LEVEL_ACT
    t.subject_name = 'h2s_level_act'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dosing_pump_ctrl'
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
    t.geni_convert_id = 'Dim. less with NA'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: dosing_feed_tank_level ----------'
    #SP_DDA_CHEMICAL_REMAINING
    t.subject_name = 'dosing_feed_tank_level'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dosing_feed_tank_level'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_DEPTH'
    t.int_verified = False

    t.geni_var_name = 'dosing_feed_tank_level'
    t.geni_class = 13
    t.geni_id = 10
    t.subject_name = 'dosing_feed_tank_level'
    t.auto_generate = True
    t.geni_convert_id = 'Dim. less with NA'
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: chemical_total_dosed ----------'
    #SP_DDA_CHEMICAL_REMAINING
    t.subject_name = 'chemical_total_dosed'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'chemical_total_dosed'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_VOLUME'
    t.int_verified = False

    t.geni_var_name = 'chemical_total_dosed'
    t.geni_class = 13
    t.geni_id = 11
    t.subject_name = 'chemical_total_dosed'
    t.auto_generate = True
    t.geni_convert_id = 'Dim. less with NA'
    t.save()

'''
    t = template('NewAlarm')
    t.description = '----------- 加DDA Alarm ----------'

    t.alarm_define_name = 'SID_ALARM_254_DDA'
    t.alarm_string = 'DDA alarm (254)'

    #加alarm config
    t.alarm_config_subject_name = 'sys_alarm_dda_alarm_conf'
    t.alarm_config_subject_type_id = 'AlarmConfig'
    t.alarm_config_geni_app_if = False
    t.alarm_config_subject_save = 'Value'
    t.alarm_config_flash_block = 'Config'
    t.alarm_config_observer_name = 'display_alarm_slippoint'
    t.alarm_config_observer_type = 'DDACtrl'
    t.alarm_config_subject_relation_name = 'sys_alarm_dda'
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

    #SP_DDA_SYS_ALARM_DDA_ALARM_OBJ
    #加alarm
    t.alarm_subject_name = 'sys_alarm_dda_alarm_obj'
    t.alarm_subject_type_id = 'AlarmDataPoint'
    t.alarm_geni_app_if = False
    t.alarm_subject_save = '-'
    t.alarm_flash_block = '-'
    t.alarm_observer_name = 'dosing_pump_ctrl'
    t.alarm_observer_type = 'DDACtrl'
    t.alarm_subject_relation_name = 'sys_alarm_dda_alarm_obj'

    t.alarm_alarm_config_id = 'sys_alarm_dda_alarm_conf'
    t.alarm_alarm_config2_id = 'dummy_alarm_conf'
    t.alarm_erroneous_unit_type_id = 0
    t.alarm_erroneous_unit_number = 0
    t.alarm_alarm_id = 'SID_ALARM_254_DDA'

    t.save()
'''
