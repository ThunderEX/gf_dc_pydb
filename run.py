# -*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *
import scripts.feature as f
from fw_upgrader import run as fw_upgrader
from fw_upgrader import guess_local_ip

def update_database():
    copy_database()
    # f.h2s()
    # f.change_profile_version_code(7)
    # f.mp204_io113()
    # f.dry_running_alarm_in_do()
    # f.update_ptc_string()
    # f.add_language()
    f.emergency_stop()
    run_generators(['Factory', 'Langguage'])

def build():
    vc_build()
    ghs_build()
    generate_firmware()

def download():
    fw_upgrader(guess_local_ip(), 'http://10.208.32.124', 10, 20, True)

if __name__ == '__main__':
    # change_software_version('Vx3.17.01')
    # update_database()
    # build()
    download()
