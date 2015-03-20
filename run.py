# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import time
from scripts.example.h2s import h2s
from scripts.util.log import *


def copy_database():
    f_database = r'.\backup\Factory.mdb'
    d_database = r'.\backup\DisplayFactory.mdb'
    l_database = r'.\backup\language.mdb'
    f_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
    d_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
    l_dest = r'..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'
    try:
        shutil.copy(f_database, f_dest)
        shutil.copy(d_database, d_dest)
        shutil.copy(l_database, l_dest)
    except:
        log('Set backup database please')
        raise NameError


def run_generators():
    current_dir = os.getcwd()
    FactoryGenerator = r'FactoryGenerator.exe  -generate'
    LangGenerator = r'LangGenerator.exe  -generate'
    WebPageGenerator = r'WebPageGenerator.exe  -generate'
    os.chdir(current_dir)
    os.chdir(r'..\cu3x1App_SRC\Control\FactoryGenerator')
    subprocess.call(FactoryGenerator)
    os.chdir(current_dir)
    os.chdir(r'..\cu3x1App_SRC\Control\LangGenerator')
    subprocess.call(LangGenerator)
    os.chdir(current_dir)
    os.chdir(r'..\cu3x1App_SRC\Control\WebPageGenerator')
    subprocess.call(WebPageGenerator)
    os.chdir(current_dir)


def ghs_build(opt=''):
    start_time = time.time()
    current_dir = os.getcwd()
    clean_cmd = r'c:\GHS\V35\mips35\build.exe -clean Main_362.bld'
    all_build_cmd = r'c:\GHS\V35\mips35\build.exe -all -nowarnings Main_362.bld'
    build_cmd = r'c:\GHS\V35\mips35\build.exe -nowarnings Main_362.bld'
    os.chdir(r'..\cu3x1App_SRC\Control\source')
    if opt == 'rebuild':
        result = subprocess.call(clean_cmd)
        result = subprocess.call(all_build_cmd)
    else:
        result = subprocess.call(build_cmd)
    os.chdir(current_dir)
    elapsed_time = time.time() - start_time
    log('Elapsed time for building Multi2000 project: %s' % (elapsed_time))


def vc_build():
    start_time = time.time()
    current_dir = os.getcwd()
    cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\vcpackages\\vcbuild.exe" /build /M4 pc.sln  "Release362|Any CPU"'
    os.chdir(r'..\cu3x1AppPcSim_SRC\PcMrViewer')
    result = subprocess.call(cmd)
    os.chdir(current_dir)
    elapsed_time = time.time() - start_time
    log('Elapsed time for building VC project: %s' % (elapsed_time))


if __name__ == '__main__':
    #copy_database()
    #h2s()
    run_generators()
    #ghs_build()
    #vc_build()
