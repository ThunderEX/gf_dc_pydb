# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

#1)	Have “Dry Running” as a selectable DO standard.  We have high level alarm as a DO, but here in the US, most customers also want to monitor the ‘Dry Running.”  This can be accomplished through user defined functions, but it is a pain in the rear to do and goes against my selling technique of an easy to use device

def update_ptc_string():
    '''
    2)	Under “I/O Settings” > “PTC Inputs,” we can tag the “moisture” alarm from a digital input, and we can also assign the thermal as an input, but no one here knows what “PTC, Pump 1” stands for.  I understand that PTC stands for thermal, but that is because I work with this product all the time.  We have got to change the wording to show “PTC/Thermal, Pump 1” or some variant that actually says “thermal.”  We hook a lot of these systems up to existing pumps (non-grundfos) that simply have relay outputs for thermal/seal.  We end up having to use another digital input and a user defined function to create a thermal alarm because no one knows what the PTC means.  That would be a great and hopefully easy fix.
    '''
    str_list = [[2005, 2006], [2008, 2009], [2011, 2012], [2014, 2015], [2017, 2018], [2020, 2021]]
    for pump_num, id_list in enumerate(str_list):
        for ptc_num, _id in enumerate(id_list):
            update_string = 'PTC/Thermal %d, pump %d' % (ptc_num+1, pump_num+1)
            table = Strings()
            table.update(id=_id, language_id=0, String=update_string)
            table.update(id=_id, language_id=18, String=update_string)

