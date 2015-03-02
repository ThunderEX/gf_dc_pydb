# -*- coding: utf-8 -*-
import shutil
from operations import *
from parameters import *
from tables import *

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
        if isinstance(x ,DisplayComponent_Table):
            h2scontol_label_table = x
            _focuscomponentid = x.model.id
    #找出group的parentcomponent供listview用
    for x in args[1]:
        if isinstance(x ,DisplayComponent_Table):
            h2scontol_group_table = x
            _parentcomponent = x.model.id
    for x in args[2]:
        if isinstance(x ,Display_Table):
            h2scontol_display_table = x
            _displayid = x.model.id
    for x in args[3]:
        if isinstance(x ,DisplayComponent_Table):
            h2scontol_listview_table = x
    h2scontol_label_table.update(h2scontol_label_table.model.id, displayid=_displayid)
    h2scontol_display_table.update(h2scontol_display_table.model.id, focuscomponentid=_focuscomponentid)
    h2scontol_listview_table.update(h2scontol_listview_table.model.id, parentcomponent=_parentcomponent)

if __name__ == '__main__':
    copy_database()
    add_data(h2s_level_quantity_parameters, type='quantity')
    #add_data(h2s_level_label_parameters, type='label')
    #add_data(h2s_subject_parameters)
    #add_data(h2s_observer_parameters)
    #添加h2scontol
    #h2scontol1 = add_data(h2s_control_label_parameters, type='label')
    #h2scontol2 = add_data(h2s_control_group_parameters)
    #h2scontol3 = add_data(h2s_control_display_parameters)
    #h2scontol4 = add_data(h2s_control_listview_parameters)
    #update_h2s_control([h2scontol1, h2scontol2, h2scontol3, h2scontol4])
    #x = DisplayListView_Table()
    #x.query(id=5838)
