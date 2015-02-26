# -*- coding: utf-8 -*-
import shutil
from operations import *
from parameters import *

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

if __name__ == '__main__':
    copy_database()
    add_data(h2s_quantity_parameters, type='quantity')
    add_data(h2s_label_parameters, type='label')
    add_data(h2s_subject_parameters)
    add_data(h2s_observer_parameters)
