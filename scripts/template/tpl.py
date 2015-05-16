# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

from label_and_quantity import *
from label_and_new_page import *
from label_and_exist_page import *
from label_headline import *
from label_and_checkbox import *
from label_blank import *
from quantity import *
from observer import *
from subject import *
from alarm import *
from enum_data import *
from string import *
from system_alarm import *
from system_alarm_status import *

class Template(object):
    def __init__(self, ):
        pass

    @staticmethod
    def get(tpl):
        try:
            instance = globals()[tpl]()
            return instance
        except:
            print 'Not defined template!!'
            raise NameError

def template(tpl):
    try:
        instance = globals()[tpl]()
        return instance
    except:
        print 'Not defined template!!'
        raise NameError
