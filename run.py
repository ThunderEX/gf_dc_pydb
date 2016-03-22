# -*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *
import scripts.feature as f
from scripts.util.fw_upgrader.src.fw_upgrader import fw_upgrader, guess_local_ip

def update_database():
    copy_database()
    # f.h2s()
    f.change_profile_version_code(8)
    # f.mp204_io113()
    # f.dry_running_alarm_in_do()
    # f.update_ptc_string()
    # f.add_language()
    f.emergency_stop()
    run_generators(['Factory', 'Langguage'])

def build():
    vc_build()
    ghs_build('rebuild')
    generate_firmware()

def download():
    fw_upgrader('c:/local/Work/tools/tftpd64/', guess_local_ip(), '10.208.32.133')

if __name__ == '__main__':
    # change_software_version('Vx3.17.02')
    # update_database()
    # build()
    download()
