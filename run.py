# -*- coding: utf-8 -*-
from scripts.misc import copy_database, run_generators, ghs_build, vc_build
from scripts.util.log import *
from scripts.tables import *
from scripts.feature.h2s import h2s
from scripts.feature.example import example



if __name__ == '__main__':
    copy_database()
    h2s()
    #example()
    run_generators()
    #ghs_build('rebuild')
    #vc_build()

    #x = DisplayComponent()
    #x.query(id=100)
    #x.query(Name__icontains='4.6', ComponentType=2)
    #x = AlarmDataPoint()
    #x.query()

    #x = Strings()
    #x.query(id=460)
    #x.query(String__icontains='level')
    #x = QuantityType()
    #x.query(Name__icontains='Q_L')
    #x = DisplayFont()
    #x.query(FontName__icontains='13')
    #x = AlarmDataPoint()
    #x.query()
    
