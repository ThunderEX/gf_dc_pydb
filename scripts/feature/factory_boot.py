# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def factory_boot():
    t = template('NewSubject')
    t.description = '---------- 加Subject: factory_boot ----------'
    #SP_DDAC_H2S_LEVEL_ACT
    t.subject_name = 'factory_boot'
    t.subject_type_id = 'IntDataPoint'
    t.geni_app_if = True
    t.geni_comment = 'factory boot'
    t.subject_save = '-'
    t.flash_block = '-'

    t.int_value = '0xFFFFFFFF'
    t.int_type = 'U32'
    t.int_min = '0xFFFFFFFF'
    t.int_max = '0xFFFFFFFF'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = False

    t.geni_var_name = 'factory_boot'
    t.geni_class = 3
    t.geni_id = 3
    t.auto_generate = False
    t.geni_convert_id = '<none>'
    t.save()
   
