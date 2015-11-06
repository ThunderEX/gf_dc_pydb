# -*- coding: utf-8 -*-
from scripts.misc import copy_database, run_generators, ghs_build, vc_build, generate_firmware
from scripts.util.log import *


if __name__ == '__main__':
    #option = 'update_database'
    option = 'build'
    #from scripts.feature.change_software_version import change_software_version
    #change_software_version(simulator_version='Vx4.00.04', controller_version='Vx4.00.04')

    if option == 'update_database':
        #copy_database()
        #import在这里是因为一旦import下面的module，会连上数据库，要确保在copy_database之后
        #from scripts.feature.h2s_factory import h2s_factory
        #from scripts.feature.h2s_display import h2s_display
        #h2s_factory()
        #h2s_display()
        #from scripts.feature.change_string import change_string
        #change_string()
        #from scripts.feature.insert_empty_strings import *
        #insert_empty_strings_for_all_languages(2060, 2101)
        #insert_empty_strings(24)
        #insert_empty_strings(25)
        #insert_empty_strings(26)
        #insert_empty_strings(27)

        run_generators(['Factory', 'Langguage'])
    else:
        vc_build()
        #ghs_build()
        #generate_firmware()
