# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
import re

def change_software_version(simulator_version='', controller_version=''):
    setup_file = r'..\cu3x1AppPcSim_SRC\PcMrViewer\Setup\Setup.vdproj'
    key_word1 = r'(CU 362 DC Simulator )V[x\d]\d\.\d\d\.\d\d'
    key_word2 = r'(CU 362 Dedicated Controls Simulator )V[x\d]\d\.\d\d\.\d\d'
    # open file with r+b (allow write and binary mode)
    f = open(setup_file, 'r+b')   
    # read entire content of file into memory
    f_content = f.read()
    # basically match middle line and replace it with itself and the extra line
    f_content = re.sub(key_word1, r'\1'+simulator_version, f_content)
    f_content = re.sub(key_word2, r'\1'+simulator_version, f_content)
    # return pointer to top of file so we can re-write the content with replaced string
    f.seek(0)
    # clear file content 
    f.truncate()
    # re-write the content with the updated content
    f.write(f_content)
    # close file
    f.close()

    firmware_version_file = r'..\cu3x1App_SRC\Control\source\util\SoftwareVersion.h'
    key_word = r'(CPU_SW_VERSION_NO\s+0x00)([F\d]\d{5})'
    v = controller_version.split('.')
    if controller_version.startswith('Vx'):
        v[0] = 'F'+v[0][-1]      #e.g. F4
    else:
        v[0] = v[0][1:]  # remove 'V'
    new_version = ''.join(v)
    print new_version
    f = open(firmware_version_file, 'r+b')   
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
