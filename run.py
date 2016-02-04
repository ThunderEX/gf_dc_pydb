# -*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *

def update_database():
    copy_database()
    #import在这里是因为一旦import下面的module，会连上数据库，要确保在copy_database之后
    import scripts.feature as f
    # f.h2s()
    # f.change_profile_version_code(7)
    # f.mp204_io113()
    # f.dry_running_alarm_in_do()
    # f.update_ptc_string()
    # f.add_language()
    # f.update_pump_string_for_italian()
    # f.mp204_current_numbers()
    f.factory_boot()
    run_generators(['Factory'])

def build():
    # vc_build()
    ghs_build('rebuild')
    generate_firmware()

if __name__ == '__main__':
    # change_software_version('V03.17.00')
    # update_database()
    build()
