# -*- coding: utf-8 -*-
from ..tables import *
from .common import *

def update_alarm_205():
    '''
    Alarm 205 shown as alarm 215 in Russian: CU362 shows alarm “Soft pressure build up timeout (215) instead of ” inconsitency , float switch (205) “ when menu language is set to Russian.
    From Leif: text in Russian is 'Несоглас-ть, поплавк. выкл-ль (205)'
    '''
    correct_string = u'Несоглас-ть, поплавк. выкл-ль (205)'  # must place u before string
    update_string(537, 'Russian', correct_string)

def update_pump_string_for_italian():
    '''
    A mistake in the Italian translation of menu 2.2 (see picture below). The text about Start and Stop level of pumps 1 and 2 is OK but from pump 3 to 6 it’s wrong.
    '''    
    correct_string = u'Livello di avvio 3'
    update_string(1570, 'Italian', correct_string)
    correct_string = u'Livello di avvio 4'
    update_string(1571, 'Italian', correct_string)
    correct_string = u'Livello di avvio 5'
    update_string(1572, 'Italian', correct_string)
    correct_string = u'Livello di avvio 6'
    update_string(1573, 'Italian', correct_string)
    correct_string = u'Livello di arresto 3'
    update_string(1574, 'Italian', correct_string)
    correct_string = u'Livello di arresto 4'
    update_string(1575, 'Italian', correct_string)
    correct_string = u'Livello di arresto 5'
    update_string(1576, 'Italian', correct_string)
    correct_string = u'Livello di arresto 6'
    update_string(1577, 'Italian', correct_string)


def mp204_current_numbers():
    '''
    MP204 current not show float value.
    '''
    _id = DisplayComponent().get(Name='1.2 PumpStatus1 l1 mp204 current NQ').id
    DisplayNumberQuantity().update(id=_id, NumberOfDigits=5)

def vfd_ao_available():
    table = DisplayListViewColumns(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", ColumnIndex=3, ColumnWidth=0)
    table.add()

    table = DisplayListViewItem(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", Index=3)
    r = table.get(ListViewId=table.model.ListViewId, Index=3)
    table = DisplayListViewItemComponents(ListViewItemId=r.id, ColumnIndex=3, ComponentId="Availability rule: VFD 2 installed")
    table.add()

    table = DisplayListViewItem(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", Index=4)
    r = table.get(ListViewId=table.model.ListViewId, Index=4)
    table = DisplayListViewItemComponents(ListViewItemId=r.id, ColumnIndex=3, ComponentId="Availability rule: VFD 3 installed")
    table.add()

    table = DisplayListViewItem(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", Index=5)
    r = table.get(ListViewId=table.model.ListViewId, Index=5)
    table = DisplayListViewItemComponents(ListViewItemId=r.id, ColumnIndex=3, ComponentId="Availability rule: VFD 4 installed")
    table.add()

    table = DisplayListViewItem(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", Index=6)
    r = table.get(ListViewId=table.model.ListViewId, Index=6)
    table = DisplayListViewItemComponents(ListViewItemId=r.id, ColumnIndex=3, ComponentId="Availability rule: VFD 5 installed")
    table.add()

    table = DisplayListViewItem(ListViewId="4.4.3.1 AnalogOutputSetup List 1 func", Index=7)
    r = table.get(ListViewId=table.model.ListViewId, Index=7)
    table = DisplayListViewItemComponents(ListViewItemId=r.id, ColumnIndex=3, ComponentId="Availability rule: VFD 6 installed")
    table.add()
