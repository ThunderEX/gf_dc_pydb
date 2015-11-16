# -*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *


def update_database():
    copy_database()
    #import在这里是因为一旦import下面的module，会连上数据库，要确保在copy_database之后
    from scripts.feature import *
    h2s()
    # mp204_io113()
    # dry_running_alarm_in_do()
    # update_ptc_string()
    # add_language()
    run_generators(['Factory', 'Langguage', 'WebPage'])

def build():
    vc_build()
    ghs_build()
    generate_firmware()

if __name__ == '__main__':
    change_software_version('Vx4.00.05')
    update_database()
    #build()
