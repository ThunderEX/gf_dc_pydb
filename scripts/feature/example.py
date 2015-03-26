# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *

def example():
    comment('This is an example')
    t = template('LabelHeadline')
    t.description = '---------- Add headline text in 4. Settings ----------'
    t.label_name = '4. test headline'
    t.define_name = 'SID_TEST_HEADLINE'
    t.string = 'test headline'
    t.listview_id = '4. Settings List 1'
    t.save()
