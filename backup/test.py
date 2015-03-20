# -*- coding: utf-8 -*-
import os, subprocess
from operations import *
from parameters import *
from tables import *
from util.log import *

def build():
    cmd = '"c:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\vcpackages\\vcbuild.exe" /build /M4 c:\\Local\\Workspace\\DCIII_V03.07.0a_int\\cu3x1AppPcSim_SRC\\PcMrViewer\\pc.sln  "Release362|Any CPU"'
    result = subprocess.call(cmd)


if __name__ == '__main__':
    #x = Strings()
    #x.query()
    build()
