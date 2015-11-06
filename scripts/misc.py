# -*- coding: utf-8 -*-
import os
import subprocess
import shutil
import time
from util.log import log, debug

def copy_database():

    ''' Copy clean and original factory, DisplayFactory, language database to replace those in input directory. '''

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
        debug('copy database done')
    except:
        log('Set backup database please')
        raise NameError


def run_generators(generators=['Factory', 'Langguage', 'WebPage']):

    ''' Run factory, displayfactory, language generators '''

    current_dir = os.getcwd()
    FactoryGenerator = r'FactoryGenerator.exe  -generate'
    LangGenerator = r'LangGenerator.exe  -generate'
    WebPageGenerator = r'WebPageGenerator.exe  -generate'
    os.chdir(current_dir)
    if 'Factory' in generators:
        os.chdir(r'..\cu3x1App_SRC\Control\FactoryGenerator')
        subprocess.call(FactoryGenerator)
        os.chdir(current_dir)
    if 'Langguage' in generators:
        os.chdir(r'..\cu3x1App_SRC\Control\LangGenerator')
        subprocess.call(LangGenerator)
        os.chdir(current_dir)
    if 'WebPage' in generators:
        os.chdir(r'..\cu3x1App_SRC\Control\WebPageGenerator')
        subprocess.call(WebPageGenerator)
        os.chdir(current_dir)


def ghs_build(opt=''):
    '''
        Run GreenHill build command.
    
    :param opt: rebuild
    :return: 
    '''

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
    if result != 0:
        log('编译错误')
        raise NameError


def vc_build():

    ''' Run Visual Studio build command '''

    start_time = time.time()
    current_dir = os.getcwd()
    tft_cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\vcpackages\\vcbuild.exe" /rebuild Tft.vcproj "Release362|Win32"'
    displayviewer_cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\vcpackages\\vcbuild.exe" /rebuild DisplayViewer\\src\\DisplayViewer.csproj "Release362|Win32"'
    cu_cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\vcpackages\\vcbuild.exe" ControlUnit.vcproj "Release362|Win32"'
    setup_cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\Common7\\IDE\\devenv.com" pc.sln /Build "Release362|Win32" Setup.vdproj'
    os.chdir(r'..\cu3x1AppPcSim_SRC\PcMrViewer')
    result = subprocess.call(tft_cmd)
    result = subprocess.call(displayviewer_cmd)
    result = subprocess.call(cu_cmd)
    result = subprocess.call(setup_cmd)
    os.chdir(current_dir)
    elapsed_time = time.time() - start_time
    log('Elapsed time for building VC project: %s' % (elapsed_time))

def generate_firmware():

    source = r'..\cu3x1App_SRC\Control\source\exe\CU362.bin'
    dest = r'c:\Local\Workspace\FirmwareGenerator\36x_DC\input\CU362.bin'
    try:
        shutil.copy(source, dest)
        debug('copy firmware done')
    except:
        raise NameError

    generator_dir = r'c:\Local\Workspace\FirmwareGenerator'
    os.chdir(generator_dir)
    try:
        subprocess.call('Generate DC_362 firmware.bat')
    except:
        raise NameError

    dest = r'c:\local\Work\tools\tftpd64\MPC\cu362_firmware.bin'
    source = r'c:\Local\Workspace\FirmwareGenerator\36x_DC\output\cu362_firmware.bin'
    
    try:
        shutil.copy(source, dest)
        debug('copy firmware to tftp done')
    except:
        raise NameError
