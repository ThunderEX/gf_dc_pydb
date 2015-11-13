# -*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *


def update_database():
    copy_database()
    #import在这里是因为一旦import下面的module，会连上数据库，要确保在copy_database之后
    from scripts.feature.h2s import h2s
    h2s()

    run_generators(['Factory', 'Langguage'])

def build():
    vc_build()
    ghs_build()
    generate_firmware()

if __name__ == '__main__':
    change_software_version('Vx4.00.05')
    update_database()
    #build()
