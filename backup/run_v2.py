# -*- coding: utf-8 -*-
import shutil
from scripts.operations import *
from scripts.parameters import *
from scripts.tables import *
from scripts.util.log import *


def copy_database():
    f_database = r'.\backup\Factory.mdb'
    d_database = r'.\backup\DisplayFactory.mdb'
    l_database = r'.\backup\language.mdb'
    f_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
    d_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
    l_dest = r'..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'
    shutil.copy(f_database, f_dest)
    shutil.copy(d_database, d_dest)
    shutil.copy(l_database, l_dest)

if __name__ == '__main__':
    copy_database()

    comment('**************************** Factory Database部分 ****************************')
    comment('---------- 添加Observer: DDACtrl ----------')
    add_data(h2s_observer_parameters, 'observer')

    comment('---------- 添加Subject: dda_control_enabled ----------')
    add_data(h2s_subject_parameters)

    comment('---------- 连接Observer与Subject ----------')
    add_data(h2s_observer_subject_parameters)

    comment('---------- 添加Subject: h2s_level_act ----------')
    add_data(h2s_level_act_subject_parameters)

    comment('---------- 连接Observer与Subject ----------')
    add_data(h2s_level_act_observer_subject_parameters)

    comment('---------- GeniAppIf ----------')
    add_data(h2s_level_act_geni_if_parameters)

    comment('**************************** Display Database部分 ****************************')
    comment('---------- 添加label:h2s level于1.1 System Status ----------')
    add_data(h2s_level_quantity_parameters, 'quantity')
    add_data(h2s_level_label_parameters, 'label')

    comment('---------- 添加label:Chemical remaining于1.1 System Status ----------')
    add_data(chemical_remaining_label_parameters, 'label')

    comment('---------- 添加label:Chemical remaining于1.1 System Status ----------')
    add_data(chemical_dosed_label_parameters, 'label')

    comment('---------- 添加label:H2S Contol于4.2 Advanced Functions ----------')
    h2s_control_label_tables = add_data(h2s_control_label_parameters, 'label')
    h2s_control_group_tables = add_data(h2s_control_group_parameters)
    h2s_control_display_tables = add_data(h2s_control_display_parameters)
    h2s_control_listview_tables = add_data(h2s_control_listview_parameters)
    update_displayid(h2s_control_label_tables, h2s_control_display_tables)
    update_focus_component_id(h2s_control_listview_tables, h2s_control_display_tables)
    update_parent_component(h2s_control_group_tables, h2s_control_listview_tables)

    comment('---------- 添加label: Dosing pump于4.2.14 ----------')
    # 添加Dosing pump
    h2s_dosing_pump_label_tables = add_data(h2s_dosing_pump_label_parameters, 'label')

    comment('---------- 添加新页group: 4.2.14.1 Dosing pump ----------')
    h2s_dosing_pump_group_tables = add_data(h2s_dosing_pump_group_parameters)
    h2s_dosing_pump_display_tables = add_data(h2s_dosing_pump_display_parameters)
    #label跳转到新页
    update_displayid(h2s_dosing_pump_label_tables, h2s_dosing_pump_display_tables)

    comment('---------- 添加新的listview于页4.2.14.1 Dosing pump下 ----------')
    h2s_dosing_pump_listview_tables = add_data(h2s_dosing_pump_listview_parameters)
    update_focus_component_id(h2s_dosing_pump_listview_tables, h2s_dosing_pump_display_tables)
    update_parent_component(h2s_dosing_pump_group_tables, h2s_dosing_pump_listview_tables)

    comment('---------- 添加label: Go to modules installed于4.2.14 ----------')
    # 添加Go to modules installed
    add_data(h2s_go_to_modules_installed_label_parameters, 'label')

    comment('---------- 添加label:4.2.14.1 H2S dosing pump interface于4.2.14.1 Dosing pump ----------')
    add_data(h2s_dosing_pump_interface_label_parameters, 'label')

    comment('---------- 添加label和checkbox: Smart Digital DDA于4.2.14.1 H2S Dosing pump List ----------')
    add_data(h2s_dosing_pump_interface_smart_digital_dda_label_parameters, 'label')
    add_data(h2s_dosing_pump_interface_smart_digital_dda_checkbox_parameters)

    comment('---------- 添加label和checkbox: Analog dosing pump于4.2.14.1 H2S Dosing pump List ----------')
    add_data(h2s_dosing_pump_interface_analog_dosing_pump_label_parameters, 'label')
    add_data(h2s_dosing_pump_interface_analog_dosing_pump_checkbox_parameters)

    comment('---------- 添加label: Go to settting of Analog outputs于4.2.14.1 ----------')
    add_data(h2s_dosing_pump_go_to_ao_space_parameters)  # 空行
    add_data(h2s_dosing_pump_go_to_ao_label_parameters, 'label')

    comment('---------- 添加label: Go to settting of Digital outputs于4.2.14.1 ----------')
    add_data(h2s_dosing_pump_go_to_do_space_parameters)  # 空行
    add_data(h2s_dosing_pump_go_to_do_label_parameters, 'label')

    comment('---------- 添加label和checkbox: Dosing pump installed于4.1.7 ----------')
    add_data(h2s_dosing_pump_installed_space_parameters)  # 空行
    add_data(h2s_dosing_pump_installed_label_parameters, 'label')
    add_data(h2s_dosing_pump_installed_checkbox_parameters)
