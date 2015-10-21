# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def change_string():
    table = Strings()
    table.update(id=2071, language_id=0, String='Accumulated overflow')
    table.update(id=2071, language_id=18, String='Accumulated overflow')

    table = Strings()
    table.update(id=2069, language_id=0, String='Block reply text messages')
    table.update(id=2069, language_id=18, String='Block reply text messages')
