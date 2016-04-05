#-*- coding: utf-8 -*-
from scripts.misc import *
from scripts.util.log import *
import scripts.feature as f
# from scripts.util.fw_upgrader.src.fw_upgrader import fw_upgrader, guess_local_ip
from scripts.util.fw_gen.fw_gen_wrapper import gen
from scripts.util.merge_excel import Cu361Texts as texts


def update_database():
    copy_database()
    f.change_profile_version_code(8)
    f.emergency_stop()
    f.factory_boot()
    # f.h2s()
    # run_generators(['Factory', 'Langguage'])


def build():
    vc_build()
    ghs_build('rebuild')
    # generate_firmware()


# def download():
    # exe_path = os.path.join(os.path.relpath('..'), r'cu3x1App_SRC\Control\source\exe')
    # fw_upgrader(exe_path, guess_local_ip(), '10.208.32.125')
    # fw_upgrader(exe_path, server_ip='192.168.0.1', client_ip='192.168.0.2', timeout=20, web_response_timeout=20)

if __name__ == '__main__':
    change_software_version('V03.18.00')
    update_database()
    texts(r'..\cu3x1App_SRC\Control\LangGenerator\input\Cu361Texts.xls').export_range(2005, 2021)
    build()
    gen(os.path.relpath('..'))
    # download()
