# -*- coding: utf-8 -*-
from scripts.misc import copy_database, run_generators, ghs_build, vc_build, generate_firmware
from scripts.util.log import *


if __name__ == '__main__':
    #example()
    option = 'update_database'
    option = 'build'

    if option == 'update_database':
        copy_database()
        #import在这里是因为一旦import下面的module，会连上数据库，要确保在copy_database之后
        from scripts.tables import *
        from scripts.feature.h2s_factory import h2s_factory
        from scripts.feature.h2s_display import h2s_display
        from scripts.feature.example import *
        h2s_factory()
        h2s_display()
        run_generators(['Factory', 'Langguage'])
    else:
        #vc_build()
        ghs_build()
        generate_firmware()
