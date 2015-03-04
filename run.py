# -*- coding: utf-8 -*-
import shutil
from operations import *
from parameters import *
from tables import *
from util.log import *

def copy_database():
    f_database = r'.\v3.07\Factory.mdb'
    d_database = r'.\v3.07\DisplayFactory.mdb'
    l_database = r'.\v3.07\language.mdb'
    f_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
    d_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
    l_dest = r'..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'
    shutil.copy(f_database, f_dest)
    shutil.copy(d_database, d_dest)
    shutil.copy(l_database, l_dest)

def update_h2s_control(args):
    #找出label的focuscomponentid供display用
    for x in args[0]:
        if isinstance(x ,DisplayComponent):
            h2scontol_label = x
            _focuscomponentid = x.model.id
    #找出group的parentcomponent供listview用
    for x in args[1]:
        if isinstance(x ,DisplayComponent):
            h2scontol_group = x
            _parentcomponent = x.model.id
    for x in args[2]:
        if isinstance(x ,Display):
            h2scontol_display = x
            _displayid = x.model.id
    for x in args[3]:
        if isinstance(x ,DisplayComponent):
            h2scontol_listview = x
    h2scontol_label.update(h2scontol_label.model.id, DisplayId=_displayid)
    h2scontol_display.update(h2scontol_display.model.id, FocusComponentId=_focuscomponentid)
    h2scontol_listview.update(h2scontol_listview.model.id, ParentComponent=_parentcomponent)


if __name__ == '__main__':
    copy_database()
    comment('********** 添加h2s level label于1.1 System Status **********')
    add_data(h2s_level_quantity_parameters, type='quantity')
    add_data(h2s_level_label_parameters, type='label')
    comment('********** 添加h2scontol于4.2 Advanced Functions **********')
    h2scontol1 = add_data(h2s_control_label_parameters, type='label')
    h2scontol2 = add_data(h2s_control_group_parameters)
    h2scontol3 = add_data(h2s_control_display_parameters)
    h2scontol4 = add_data(h2s_control_listview_parameters)
    update_h2s_control([h2scontol1, h2scontol2, h2scontol3, h2scontol4])
    comment('********** 添加Observer **********')
    add_data(h2s_observer_parameters, type='observer')
    comment('********** 添加Subject **********')
    add_data(h2s_subject_parameters)
    comment('********** 连接Observer与Subject **********')
    add_data(h2s_observer_subject_parameters)
    print SP
    #x = DisplayListView()
    #x.query(id=5838)
