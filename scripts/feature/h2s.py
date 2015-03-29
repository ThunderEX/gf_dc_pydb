# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *

def h2s():
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
    t.subject_name =  'dda_control_enabled'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'dda_control_enabled'

    t.bool_value = 0
    t.save()

    t = template('NewSubject')
    t.description = '---------- 加Subject: h2s_level_act ----------'
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
    t.description = '---------- 加Subject: chemical_remaining ----------'
    t.subject_name = 'chemical_remaining'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'dosing_pump_ctrl'
    t.observer_type = 'DDACtrl'
    t.subject_relation_name = 'chemical_remaining'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '99999999'
    t.int_quantity_type = 'Q_LEVEL'
    t.int_verified = False

    t.geni_var_name = 'chemical_remaining'
    t.geni_class = 13
    t.geni_id = 10
    t.subject_name = 'chemical_remaining'
    t.auto_generate = True
    t.geni_convert_id = 'Dim. less with NA'
    t.save()

    comment('**************************** Display Database部分 ****************************')
    
    t = template('LabelAndQuantity')
    t.description = '---------- 添加label:h2s level于1.1 System Status ----------'
    t.label_name = '1.1 SystemStatus l1 h2s level'
    t.quantity_name = '1.1 SystemStatus l1 h2s level nq'
    t.define_name = 'SID_H2S_LEVEL'
    t.string = 'H2S level'
    t.listview_id = '1.1 SystemStatus List 1'
    t.subject_id = 'h2s_level_act'
    t.quantity_type =  'Q_PARTS_PER_MILLION'
    t.save()
    
    t = template('LabelAndQuantity')
    t.description = '---------- 1.1 - System 页面里新加一行label:Chemical remaining和quantity:l ----------'
    t.label_name = '1.1 SystemStatus l1 chemical remaining'
    t.quantity_name = '1.1 SystemStatus l1 chemical remaining nq'
    t.define_name = 'SID_CHEMICAL_REMAINING'
    t.string = 'Chemical remaining'
    t.listview_id = '1.1 SystemStatus List 1'
    #TODO
    t.subject_id = 'chemical_remaining'
    t.quantity_type =  'Q_LEVEL'
    t.save()

    t = template('LabelAndQuantity')
    t.description = '---------- 1.1 - System 页面里新加一行label:Chemical dosed和quantity:l ----------'
    t.label_name = '1.1 SystemStatus l1 chemical dosed'
    t.quantity_name = '1.1 SystemStatus l1 chemical dosed nq'
    t.define_name = 'SID_CHEMICAL_DOSED'
    t.string = 'Chemical dosed'
    t.listview_id = '1.1 SystemStatus List 1'
    #TODO
    t.subject_id = 'chemical_remaining'
    t.quantity_type = 'Q_LEVEL'
    t.save()
    
    t = template('LabelAndNewPage')
    t.description = '----------  添加label:H2S Contol于4.2 Advanced Functions ----------'
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
    t.save()

    t = template('LabelAndNewPage')
    t.description = '---------- 4.2.14 - H2S Control 页面里新加一行label:Dosing pump，点击跳进4.2.14.1 Dosing pump group ----------'
    t.label_name = '4.2.14 Dosing pump go to setting'
    t.label_define_name = 'SID_H2S_DOSING_PUMP_SETTING'
    t.label_string = 'Dosing pump'
    t.listview_id = '4.2.14 H2S Contol List'
    t.label_left_margin = 2
    t.label_right_margin = 1

    t.group_name = '4.2.14.1 H2S Dosing pump group'
    t.group_define_name = 'SID_H2S_DOSING_PUMP_SETTING'

    t.root_group_id_name = '4.2.14.1 H2S Dosing pump group'
    t.display_string_name = 'Dosing pump'
    t.display_number = '4.2.14.1'

    t.listview_name = '4.2.14.1 H2S Dosing pump List'
    t.listviewid_name = '4.2.14.1 H2S Dosing pump List'
    t.listview_column_width = [0, 164, 74]
    t.save()
    
    t = template('LabelAndExistPage')
    t.description = '---------- 4.2.14 - H2S Control 页面里新加一行label: go to modules installed，点击进入4.1.7 Modules installed ----------'
    t.label_name = '4.2.14 H2S go to modules installed'
    t.label_define_name = 'SID_GO_TO_MODULES_INSTALLED'
    t.display_id = 137
    t.listview_id = '4.2.14 H2S Contol List'
    t.label_left_margin = 2
    t.label_right_margin = 1
    t.save()

    t = template('LabelHeadline')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行label:Dosing pump interface ----------'
    t.label_name = '4.2.14.1 H2S dosing pump interface headline'
    t.define_name = 'SID_DOSING_PUMP_INTERFACE'
    t.label_string = 'Dosing pump interface'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()
    
    t = template('LabelAndCheckbox')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Smart Digital DDA ----------'
    t.label_name = '4.2.14.1 Smart Digital DDA'
    t.checkbox_name = '4.2.14.1 Smart Digital DDA cb'
    t.checkbox_type = 'ModeCheckBox'
    t.check_state = 1
    t.label_column_index = 1
    t.checkbox_column = 2
    t.label_left_margin = 4
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_SMART_DIGITAL_DDA'
    t.label_string = 'Smart Digital DDA'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    # TODO 先用已有的subject数据pit_level_ctrl_type，是个枚举类型
    t.subject_id = 'pit_level_ctrl_type'
    t.save()
    
    t = template('LabelAndCheckbox')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Analog dosing pump ----------'
    t.label_name = '4.2.14.1 Analog dosing pump'
    t.checkbox_name = '4.2.14.1 Analog dosing pump cb'
    t.checkbox_type = 'ModeCheckBox'
    t.check_state = 0
    t.label_column_index = 1
    t.checkbox_column = 2
    t.label_left_margin = 4
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_ANALOG'
    t.label_string = 'Analog dosing pump'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    # TODO 先用已有的subject数据pit_level_ctrl_type，是个枚举类型
    t.subject_id = 'pit_level_ctrl_type'
    t.save()
    
    t = template('LabelBlank')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行空行 ----------'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()

    t = template('LabelAndExistPage')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to settting of Analog outputs，点击进入4.4.3 Analog outputs ----------'
    t.label_name = '4.2.14.1 Dosing pump go to AO'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_ANALOGUE_OUTPUTS'
    t.display_id = 143
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.save()
    
    t = template('LabelBlank')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行空行 ----------'
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.save()

    t = template('LabelAndExistPage')
    t.description = '---------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to settting of Digital outputs，点击进入4.4.4 Digital outputs ----------'
    t.label_name = '4.2.14.1 Dosing pump go to DO'
    t.label_define_name = 'SID_GO_TO_SETTING_OF_DIGITAL_OUTPUTS'
    t.display_id = 143
    t.listview_id = '4.2.14.1 H2S Dosing pump List'
    t.label_left_margin = 1
    t.label_right_margin = 0
    t.save()

    t = template('LabelBlank')
    t.description = '---------- 4.1.7 - Modules installed 页面里新加一行空行 ----------'
    t.listview_id = '4.1.7 pumpModules List'
    t.save()

    t = template('LabelAndCheckbox')
    t.description = '---------- 4.1.7 - Modules installed 页面里新加一行label和checkbox ----------'
    t.label_name = '4.1.7 pumpModules dosing pump'
    t.checkbox_name = '4.1.7 pumpModules dosing pump cb'
    t.checkbox_type = 'OnOffCheckBox'
    t.label_column_index = 0
    t.checkbox_column = 1
    t.label_left_margin = 2
    t.label_right_margin = 0
    t.define_name = 'SID_H2S_DOSING_PUMP_INSTALLED'
    t.label_string = 'Dosing pump installed'
    t.listview_id = '4.1.7 pumpModules List'
    # TODO 先用已有的subject数据io111_pump_1_installed
    t.subject_id = 'io111_pump_1_installed'
    t.save()
    
