# -*- coding: utf-8 -*-
from scripts.misc import copy_database, run_generators, ghs_build, vc_build
from scripts.util.log import *
from scripts.tables import *
from scripts.feature.h2s import h2s
from scripts.feature.example import example



if __name__ == '__main__':
    #copy_database()
    #h2s()
    x = DisplayComponent()
    x.query(Name__icontains='4.6', ComponentType=2)
    #example()
    #run_generators()
    #ghs_build()
    #vc_build()
