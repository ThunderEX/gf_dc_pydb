# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *

def mp204_io113():
    comment('**************************** Display Database部分 ****************************')
    table = Strings()
    table.update(id=638, language_id=0, String='IO 11X, motor stator temperature')
    table.update(id=638, language_id=18, String='IO 11X, motor stator temperature')

    for i in range(1, 7):
        for j in range(1, 4):
            t = template('NewSubject')
            t.description = '---------- 为MP204加Subject: mp204_%d_phase_voltage_l%d ----------' % (i, j)
            t.subject_name = 'mp204_%d_phase_voltage_l%d' % (i, j)
            t.subject_type_id = 'FloatDataPoint'
            t.subject_save = '-'
            t.flash_block = '-'
            t.observer_name = 'mp204_module_%d' % (i)
            t.observer_type = 'MP204Module'
            t.subject_access = 'Read/Write'
            t.subject_relation_name = 'PHASE_VOLTAGE_L%d' % (j)

            t.float_value = 0.0
            t.float_min = 0
            t.float_max = 999
            t.float_quantity_type = 'Q_VOLTAGE'
            t.save()

    for i in range(1, 7):
        t = template('LabelAndQuantity')
        t.description = '''---------- 1.%d - Pump %d页面里新加一行MP204, phase voltage L1 ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |1.%d - Pump %d                                 |
        +-----------------------------------------------+
        | Status                             stopped    |
        | Controlled by            Auto/On/Off switch   |
        | Operating hours                     0:42h     |
        | Latest runtime                      0:00h     |
        | Time since service                  0:42h     |
        | Time for service                    9999h     |
        | Number of starts                    18        |
        | Number of starts/hours              0         |
    --> | MP204, phase voltage L1             0V        |
        | IO 11X, moisture in motor           Yes       |
        | IO 11X, support bearing             21°C      |
        | Start level                Alternating cycle  |
        | Stop level                          0.5m      |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i+1, i, i+1, i)
        t.label_name = '1.%d PumpStatus%d l1 MP204 phase voltage l1' % (i+1, i)
        t.label_left_margin = 2
        t.label_align = 'VCENTER_LEFT'
        t.quantity_name = '1.%d PumpStatus%d l1 MP204 phase voltage l1 nq' % (i+1, i)
        t.quantity_type = 'Q_VOLTAGE'
        t.quantity_readonly = True
        t.quantity_align = 'VCENTER_LEFT'
        t.define_name = 'SID_MP204_PHASE_VOLTAGE_L1'
        t.label_string = 'MP204, phase voltage L1'
        t.listview_id = '1.%d PumpStatus%d List 1' % (i+1, i)
        t.subject_id = 'mp204_%d_phase_voltage_l1' % (i)
        t.subject_access = 'Read'
        t.listviewitem_index = 36    #replace index 15 with new inserted item
        t.number_of_digits = 3
        t.available_rule_name = '1.%d PumpStatus%d l1 mp204 avail' % (i+1, i)
        t.available_rule_column_index = 4
        t.save()

        t = template('LabelAndQuantity')
        t.description = '''---------- 1.%d - Pump %d页面里新加一行MP204, phase voltage L2 ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |1.%d - Pump %d                                 |
        +-----------------------------------------------+
        | Status                             stopped    |
        | Controlled by            Auto/On/Off switch   |
        | Operating hours                     0:42h     |
        | Latest runtime                      0:00h     |
        | Time since service                  0:42h     |
        | Time for service                    9999h     |
        | Number of starts                    18        |
        | Number of starts/hours              0         |
        | MP204, phase voltage L1             0V        |
    --> | MP204, phase voltage L2             0V        |
        | IO 11X, moisture in motor           Yes       |
        | IO 11X, support bearing             21°C      |
        | Start level                Alternating cycle  |
        | Stop level                          0.5m      |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i+1, i, i+1, i)
        t.label_name = '1.%d PumpStatus%d l1 MP204 phase voltage l2' % (i+1, i)
        t.label_left_margin = 2
        t.label_align = 'VCENTER_LEFT'
        t.quantity_name = '1.%d PumpStatus%d l1 MP204 phase voltage l2 nq' % (i+1, i)
        t.quantity_type = 'Q_VOLTAGE'
        t.quantity_readonly = True
        t.quantity_align = 'VCENTER_LEFT'
        t.define_name = 'SID_MP204_PHASE_VOLTAGE_L2'
        t.label_string = 'MP204, phase voltage L2'
        t.listview_id = '1.%d PumpStatus%d List 1' % (i+1, i)
        t.subject_id = 'mp204_%d_phase_voltage_l2' % (i)
        t.subject_access = 'Read'
        t.listviewitem_index = 37    #replace index 15 with new inserted item
        t.number_of_digits = 3
        t.available_rule_name = '1.%d PumpStatus%d l1 mp204 avail' % (i+1, i)
        t.available_rule_column_index = 4
        t.save()


        t = template('LabelAndQuantity')
        t.description = '''---------- 1.%d - Pump %d页面里新加一行MP204, phase voltage L3 ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |1.%d - Pump %d                                 |
        +-----------------------------------------------+
        | Status                             stopped    |
        | Controlled by            Auto/On/Off switch   |
        | Operating hours                     0:42h     |
        | Latest runtime                      0:00h     |
        | Time since service                  0:42h     |
        | Time for service                    9999h     |
        | Number of starts                    18        |
        | Number of starts/hours              0         |
        | MP204, phase voltage L1             0V        |
        | MP204, phase voltage L2             0V        |
    --> | MP204, phase voltage L3             0V        |
        | IO 11X, moisture in motor           Yes       |
        | IO 11X, support bearing             21°C      |
        | Start level                Alternating cycle  |
        | Stop level                          0.5m      |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i+1, i, i+1, i)
        t.label_name = '1.%d PumpStatus%d l1 MP204 phase voltage l3' % (i+1, i)
        t.label_left_margin = 2
        t.label_align = 'VCENTER_LEFT'
        t.quantity_name = '1.%d PumpStatus%d l1 MP204 phase voltage l3 nq' % (i+1, i)
        t.quantity_type = 'Q_VOLTAGE'
        t.quantity_readonly = True
        t.quantity_align = 'VCENTER_LEFT'
        t.define_name = 'SID_MP204_PHASE_VOLTAGE_L3'
        t.label_string = 'MP204, phase voltage L3'
        t.listview_id = '1.%d PumpStatus%d List 1' % (i+1, i)
        t.subject_id = 'mp204_%d_phase_voltage_l3' % (i)
        t.subject_access = 'Read'
        t.listviewitem_index = 38    #replace index 15 with new inserted item
        t.number_of_digits = 3
        t.available_rule_name = '1.%d PumpStatus%d l1 mp204 avail' % (i+1, i)
        t.available_rule_column_index = 4
        t.save()


        t = template('LabelAndQuantity')
        t.description = '''---------- 1.%d - Pump %d页面里新加一行IO113, support bearing ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |1.%d - Pump %d                                 |
        +-----------------------------------------------+
        | Status                             stopped    |
        | Controlled by            Auto/On/Off switch   |
        | Operating hours                     0:42h     |
        | Latest runtime                      0:00h     |
        | Time since service                  0:42h     |
        | Time for service                    9999h     |
        | Number of starts                    18        |
        | Number of starts/hours              0         |
        | IO 11X, moisture in motor           Yes       |
    --> | IO 11X, support bearing             21°C      |
        | Start level                Alternating cycle  |
        | Stop level                          0.5m      |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i+1, i, i+1, i)
        t.label_name = '1.%d PumpStatus%d l1 IO113 support bearing' % (i+1, i)
        t.label_left_margin = 2
        t.label_align = 'VCENTER_LEFT'
        t.quantity_name = '1.%d PumpStatus%d l1 IO113 support bearing nq' % (i+1, i)
        t.quantity_type = 'Q_TEMPERATURE'
        t.quantity_readonly = True
        t.quantity_align = 'VCENTER_LEFT'
        t.define_name = 'SID_IO111_SUPPORT_BEARING'
        t.label_string = 'IO 11X, support bearing'
        t.listview_id = '1.%d PumpStatus%d List 1' % (i+1, i)
        t.subject_id = 'io111_pump_%d_temperature_support_bearing' % (i)
        t.subject_access = 'Read'
        t.listviewitem_index = 15    #replace index 15 with new inserted item
        t.number_of_digits = 3
        t.save()
    
    
        t = template('LabelAndQuantity')
        t.description = '''---------- 1.%d - Pump %d页面里新加一行IO113, support bearing ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |1.%d - Pump %d                                 |
        +-----------------------------------------------+
        | Status                             stopped    |
        | Controlled by            Auto/On/Off switch   |
        | Operating hours                     0:42h     |
        | Latest runtime                      0:00h     |
        | Time since service                  0:42h     |
        | Time for service                    9999h     |
        | Number of starts                    18        |
        | Number of starts/hours              0         |
        | IO 11X, moisture in motor           Yes       |
        | IO 11X, support bearing             21°C      |
    --> | IO 11X, main bearing                21°C      |
        | Start level                Alternating cycle  |
        | Stop level                          0.5m      |
        |                                               |
        |                                               |
        |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i+1, i, i+1, i)
        t.label_name = '1.%d PumpStatus%d l1 IO113 main bearing' % (i+1, i)
        t.label_left_margin = 2
        t.label_align = 'VCENTER_LEFT'
        t.quantity_name = '1.%d PumpStatus%d l1 IO113 main bearing nq' % (i+1, i)
        t.quantity_type = 'Q_TEMPERATURE'
        t.quantity_readonly = True
        t.quantity_align = 'VCENTER_LEFT'
        t.define_name = 'SID_IO111_MAIN_BEARING'
        t.label_string = 'IO 11X, main bearing'
        t.listview_id = '1.%d PumpStatus%d List 1' % (i+1, i)
        t.subject_id = 'io111_pump_%d_temperature_main_bearing' % (i)
        t.subject_access = 'Read'
        t.listviewitem_index = 16    #replace index 16 with new inserted item
        t.number_of_digits = 3
        t.save()

