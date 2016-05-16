#-*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *
from scripts.util.query import *
import scripts.feature as f
from scripts.util.fw_upgrader.src.fw_upgrader import fw_upgrader, guess_local_ip
from scripts.util.fw_gen.fw_gen_wrapper import gen
from scripts.util.merge_excel import Cu361Texts as texts
from scripts.util.query import *


def update_database():
    copy_database()
    f.change_profile_version_code(9)
    f.anti_stealing()
    f.grinder()
    run_generators(['Factory', 'Langguage'])


def build():
    vc_build()
    ghs_build('rebuild')
    # generate_firmware()


def download():
    exe_path = os.path.join(os.path.relpath('..'), r'cu3x1App_SRC\Control\source\exe')
    # fw_upgrader(exe_path, guess_local_ip(), '10.208.32.125')
    fw_upgrader(exe_path, server_ip='192.168.0.1', client_ip='192.168.0.2', timeout=20, web_response_timeout=20)

if __name__ == '__main__':
    # query_alarm()
    # query_by_subject_relation('SP_WIO_MEASURED_VALUE_WATER_IN_OIL')
    # change_software_version('Vx3.18.01')
    update_database()
    # build()
    # gen(os.path.relpath('..'))
    # download()
