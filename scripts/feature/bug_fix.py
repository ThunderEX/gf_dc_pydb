# -*- coding: utf-8 -*-
from ..tables import *
from common import *

def update_alarm_205():
    '''
    Alarm 205 shown as alarm 215 in Russian: CU362 shows alarm “Soft pressure build up timeout (215) instead of ” inconsitency , float switch (205) “ when menu language is set to Russian.
    From Leif: text in Russian is 'Несоглас-ть, поплавк. выкл-ль (205)'
    '''
    correct_string = u'Несоглас-ть, поплавк. выкл-ль (205)'  # must place u before string
    update_string(537, 'Russian', correct_string)
