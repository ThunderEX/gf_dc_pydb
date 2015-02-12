import os, sys
import shutil

f_database = 'Factory.mdb'
d_database = 'DisplayFactory.mdb'
l_database = 'language.mdb'

f_dest = r'..\..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
d_dest = r'..\..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
l_dest = r'..\..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'

if __name__ == '__main__':
    shutil.copy(f_database, f_dest)
    shutil.copy(d_database, d_dest)
    shutil.copy(l_database, l_dest)
