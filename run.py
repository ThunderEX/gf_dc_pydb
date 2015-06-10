# -*- coding: utf-8 -*-
from scripts.misc import copy_database, run_generators, ghs_build, vc_build
from scripts.util.log import *
from scripts.tables import *
from scripts.feature.h2s_factory import h2s_factory
from scripts.feature.h2s_display import h2s_display
from scripts.feature.example import example


if __name__ == '__main__':
    copy_database()
    h2s_factory()
    h2s_display()
    run_generators()
    #vc_build()
    #ghs_build('rebuild')
    #example()

    #x = DisplayAlarmStrings()
    #x.query()
