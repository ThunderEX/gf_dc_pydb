# -*- coding: utf-8 -*-
import os
import stat
import subprocess
import shutil
import time
import re
from .util.log import log, debug

def copy_database():

    """ Copy clean and original factory, DisplayFactory, language database to replace those in input directory. """

    f_database = r'.\backup\Factory.mdb'
    d_database = r'.\backup\DisplayFactory.mdb'
    l_database = r'.\backup\language.mdb'
    f_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
    d_dest = r'..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
    l_dest = r'..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'

    # if backup not exist, create them first
    if any(not os.path.isfile(path) for path in [f_database, d_database, l_database]):
        shutil.copy(f_dest, f_database)
        shutil.copy(d_dest, d_database)
        shutil.copy(l_dest, l_database)
        # remove read-only
        [os.chmod(path, stat.S_IWRITE) for path in [f_database, d_database, l_database]]

    # remove read-only
    [os.chmod(path, stat.S_IWRITE) for path in [f_dest, d_dest, l_dest]]
    shutil.copy(f_database, f_dest)
    shutil.copy(d_database, d_dest)
    shutil.copy(l_database, l_dest)
    debug('copy database done')


def change_software_version(new_version):
    if not new_version.startswith('V'):
        print('Only accept version format as V04.00.00 or Vx4.00.00, input %s' % new_version)
        raise ValueError
    setup_file = r'..\cu3x1AppPcSim_SRC\PcMrViewer\Setup\Setup.vdproj'
    os.chmod(setup_file, 644)
    key_word1 = r'(CU 362 DC Simulator )V[x\d]\d\.\d\d\.\d\d'
    key_word2 = r'(CU 362 Dedicated Controls Simulator )V[x\d]\d\.\d\d\.\d\d'
    # open file with r+b (allow write and binary mode)
    f = open(setup_file, 'r+')
    # read entire content of file into memory
    f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
    f_content = re.sub(key_word1, r'\1'+new_version, f_content)
    f_content = re.sub(key_word2, r'\1'+new_version, f_content)
    # return pointer to top of file so we can re-write the content with replaced string
    f.seek(0)
    # clear file content 
    f.truncate()
    # re-write the content with the updated content
    f.write(f_content)
    # close file
    f.close()

    firmware_version_file = r'..\cu3x1App_SRC\Control\source\util\SoftwareVersion.h'
    os.chmod(firmware_version_file, 644)
    key_word = r'(CPU_SW_VERSION_NO\s+0x00)([F\d]\d{5})'
    v = new_version.split('.')
    if new_version.startswith('Vx'):
        v[0] = 'F'+v[0][-1]      #e.g. F4
    else:
        v[0] = v[0][1:]  # remove 'V'
    new_version = ''.join(v)
    #print new_version
    f = open(firmware_version_file, 'r+')
    # read entire content of file into memory
    f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
    f_content = re.sub(key_word, r'CPU_SW_VERSION_NO 0x00'+new_version, f_content)
    # return pointer to top of file so we can re-write the content with replaced string
    f.seek(0)
    # clear file content 
    f.truncate()
    # re-write the content with the updated content
    f.write(f_content)
    # close file
    f.close()


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
