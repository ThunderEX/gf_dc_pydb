# -*- coding: utf-8 -*-
import shutil
from operations import *
from parameters import *
from tables import *
from util.log import *

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

def update_h2s_control(args):
    for x in args[0]:
        if isinstance(x ,DisplayComponent):
            h2scontol_label = x
    #找出group的parentcomponent供listview用
    for x in args[1]:
        if isinstance(x ,DisplayComponent):
            h2scontol_group = x
            _parentcomponent = x.model.id
    for x in args[2]:
        if isinstance(x ,Display):
            h2scontol_display = x
            _displayid = x.model.id
    #找出listview的focuscomponentid供display用
    for x in args[3]:
        if isinstance(x ,DisplayComponent):
            h2scontol_listview = x
            _focuscomponentid = x.model.id
    h2scontol_label.update(h2scontol_label.model.id, DisplayId=_displayid)
    h2scontol_display.update(h2scontol_display.model.id, FocusComponentId=_focuscomponentid)
    h2scontol_listview.update(h2scontol_listview.model.id, ParentComponent=_parentcomponent)


def update_h2s_dosing_pump_label(args):
    #找出DisplayComponent实例
    for x in args[0]:
        if isinstance(x ,DisplayComponent):
            display_component = x
    #找出Display的id
    for x in args[1]:
        if isinstance(x ,Display):
            _displayid = x.model.id
    display_component.update(display_component.model.id, DisplayId=_displayid)


if __name__ == '__main__':
    copy_database()

    comment('********** 添加h2s level label于1.1 System Status **********')
    add_data(h2s_level_quantity_parameters, type='quantity')
    add_data(h2s_level_label_parameters, type='label')

    comment('********** 添加H2S Contol于4.2 Advanced Functions **********')
    h2s_control_label_tables = add_data(h2s_control_label_parameters, type='label')
    h2s_control_group_tables = add_data(h2s_control_group_parameters)
    h2s_control_display_tables = add_data(h2s_control_display_parameters)
    h2s_control_listview_tables = add_data(h2s_control_listview_parameters)
    update_h2s_control([h2s_control_label_tables, h2s_control_group_tables, h2s_control_display_tables, h2s_control_listview_tables])

    comment('********** 添加label: Dosing pump于4.2.14 **********')
    #添加Dosing pump
    h2s_dosing_pump_label_tables = add_data(h2s_dosing_pump_label_parameters, 'label')
    h2s_dosing_pump_group_tables = add_data(h2s_control_group_parameters)
    h2s_dosing_pump_display_tables = add_data(h2s_control_display_parameters)
    h2s_dosing_pump_listview_tables = add_data(h2s_control_listview_parameters)
    update_h2s_control([h2s_dosing_pump_label_tables, h2s_dosing_pump_group_tables, h2s_dosing_pump_display_tables, h2s_dosing_pump_listview_tables])
    #update_h2s_dosing_pump_label([h2s_dosing_pump_label_tables, h2s_control_display_tables])

    """
    comment('********** 添加label: Go to modules installed于4.2.14 **********')
    #添加Go to modules installed
    add_data(h2s_go_to_modules_installed_label_parameters, 'label')

    comment('********** 添加label和checkbox: Dosing pump installed于4.1.7 **********')
    add_data(h2s_dosing_pump_installed_space_parameters)
    add_data(h2s_dosing_pump_installed_label_parameters, 'label')
    add_data(h2s_dosing_pump_installed_checkbox_parameters)

    comment('********** 添加Observer **********')
    add_data(h2s_observer_parameters, type='observer')

    comment('********** 添加Subject **********')
    add_data(h2s_subject_parameters)

    comment('********** 连接Observer与Subject **********')
    add_data(h2s_observer_subject_parameters)
    """
