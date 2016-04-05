# -*- coding: utf-8 -*-

import os, sys
from .fw_gen import buildone, loadlayout

def gen(src_path):
    curpath = os.path.dirname(os.path.realpath(__file__))  # path of current script
    exe_path = os.path.join(src_path, r'cu3x1App_SRC\Control\source\exe')
    bin_path = os.path.join(src_path, r'cu3x1Platform_SRC\FirmwareGenerator\input')
    mpc_path = os.path.join(exe_path, r'MPC')
    if not os.path.isdir(mpc_path):
        os.mkdir(mpc_path)
    # print(bin_path)
    filler, segments = loadlayout(os.path.join(curpath, 'flashfile/cu362FlashFile.txt'))
    outputfile = os.path.join(exe_path, r'MPC\cu362_firmware.bin')
    # print('generating %s' % outputfile)
    new_segments = []
    for s in segments:
        # use build bin file in src folder
        s['filename'] = (os.path.join(exe_path, os.path.basename(s['filename'])))
        new_segments.append(s)
    buildone(outputfile, filler, new_segments)

    filler, segments = loadlayout(os.path.join(curpath, 'flashfile/cu362FlashFile16MB.txt'))
    outputfile = os.path.join(exe_path, r'MPC\98149206.bin')
    # print('generating %s' % outputfile)
    new_segments = []
    
    for s in segments:
        # use cu3x1Platform_SRC\FirmwareGenerator\input\ instead of the specified folder in flash file
        temp_path = bin_path
        # use build bin file in src folder
        if os.path.basename(s['filename']) == 'cu362.bin':
            temp_path = exe_path
        # cu352_bootloader is special case since there is no such file in cu3x1Platform_SRC\FirmwareGenerator\input\
        if os.path.basename(s['filename']) == 'cu352_bootloader.bin':
            temp_path = os.path.join(curpath, 'common_input')
        s['filename'] = (os.path.join(temp_path, os.path.basename(s['filename'])))
        new_segments.append(s)
    # for s in new_segments:
        # print(s['filename'])
    buildone(outputfile, filler, new_segments)

if __name__ == '__main__':
    gen(r'c:\local\Workspace\55602_DC_V04.01.00_dev')
