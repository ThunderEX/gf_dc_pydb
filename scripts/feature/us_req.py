# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *
from ..models import *
from common import update_string

#1)	Have “Dry Running” as a selectable DO standard.  We have high level alarm as a DO, but here in the US, most customers also want to monitor the ‘Dry Running.”  This can be accomplished through user defined functions, but it is a pain in the rear to do and goes against my selling technique of an easy to use device
def dry_running_alarm_in_do():
    t = template('NewString')
    t.description = '''---------- 4.4.4.1 - Function of digital outputs页面里新加一行label:Dry running alarm ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.4.1 - Function of digital outputs          |
    +-----------------------------------------------+
    |                                               |
    |Function, DO1 (CU362)[71]                      |
    |  No function                          ☑       |
    |  Start, pump 1                        ☐       |
    |  Start, pump 2                        ☐       |
    |  Start, mixer                         ☐       |
    |  User-defined relay                   ☐       |
    |  High-level alarm                     ☐       |
--> |  Dry running alarm                    ☐       |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.define_name = 'SID_DO_DRY_RUNNING_ALARM'
    t.string_name = 'Dry running alarm'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_status_relay_func_alarm_relay_dry_running ----------'
    t.subject_name =  'relay_status_relay_func_alarm_relay_dry_running'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_ALARM_RELAY_DRY_RUNNING'
    t.bool_value = 0
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- any_alarm_relay_active与relay_status_relay_func_alarm_relay_dry_running挂接 ----------'
    t.subject_name =  'relay_status_relay_func_alarm_relay_dry_running'
    t.observer_name = 'any_alarm_relay_active'
    t.observer_type = 'BoolLogic'
    t.subject_relation_name = 'SOURCE'
    t.subject_access = 'Read'
    t.save()


    t = template('ObserverLinkSubject')
    t.description = '---------- alarm_control与relay_status_relay_func_alarm_relay_dry_running挂接 ----------'
    t.subject_name =  'relay_status_relay_func_alarm_relay_dry_running'
    t.observer_name = 'alarm_control'
    t.observer_type = 'AlarmControl'
    t.subject_relation_name = 'ALARM_RELAY_OUTPUT_VALUE_DRY_RUNNING'
    t.subject_access = 'Not decided'
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: alarm_relay_dry_running_auto_ack ----------'
    t.subject_name =  'alarm_relay_dry_running_auto_ack'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'alarm_control'
    t.observer_type = 'AlarmControl'
    t.subject_relation_name = 'ALARM_RELAY_ACK_DRY_RUNNING'
    t.bool_value = 0
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: alarm_relay_dry_running_manual_ack_present ----------'
    t.subject_name =  'alarm_relay_dry_running_manual_ack_present'
    t.subject_type_id = 'BoolDataPoint'
    t.subject_save = 'Value'
    t.flash_block = 'Config'
    t.observer_name = 'alarm_control'
    t.observer_type = 'AlarmControl'
    t.subject_relation_name = 'ALARM_RELAY_MANUAL_ACK_PRESENT_DRY_RUNNING'
    t.bool_value = 0
    t.save()


    t = template('NewSubject')
    t.description = '---------- 加Subject: relay_func_output_alarm_relay_dry_running ----------'
    t.subject_name =  'relay_func_output_alarm_relay_dry_running'
    t.subject_type_id = 'IntDataPoint'
    t.subject_save = '-'
    t.flash_block = '-'
    t.observer_name = 'relay_function_handler'
    t.observer_type = 'RelayFuncHandler'
    t.subject_relation_name = 'RELAY_FUNC_OUTPUT_ALARM_RELAY_DRY_RUNNING'

    t.int_value = '0'
    t.int_type = 'U32'
    t.int_min = '0'
    t.int_max = '16'
    t.int_quantity_type = 'Q_NO_UNIT'
    t.int_verified = True
    t.save()

    comment("AppTypeDefs.h里添加RELAY_FUNC_ALARM_RELAY_DRY_RUNNING")
    comment("DigitalOutputConfListView.cpp里FIRST_USER_IO_INDEX+1")
    comment("DigitalOutputConfListView.cpp里添加 { SID_DO_DRY_RUNNING_ALARM,          RELAY_FUNC_ALARM_RELAY_DRY_RUNNING               }, 注意放在SID_USERDEFINED_FUNCTION_1之前")
    comment("DigitalOutputFunctionState.cpp里添加{ RELAY_FUNC_ALARM_RELAY_DRY_RUNNING                  , SID_DO_DRY_RUNNING_ALARM                  }")
    comment("AlarmDef.h里ALARM_RELAY_TYPE添加ALARM_RELAY_DRY_RUNNING枚举")
    comment('''RelayFuncHandler.cpp里添加
    case SUBJECT_ID_RELAY_STATUS_RELAY_FUNC_ALARM_RELAY_DRY_RUNNING:
      mpRelayStatus[RELAY_FUNC_ALARM_RELAY_DRY_RUNNING].Update(pSubject);
      break;
    和
    case SP_RFH_RELAY_FUNC_ALARM_RELAY_DRY_RUNNING:
      mpRelayStatus[RELAY_FUNC_ALARM_RELAY_DRY_RUNNING].Attach(pSubject);
      break;
    case SP_RFH_RELAY_FUNC_OUTPUT_ALARM_RELAY_DRY_RUNNING:
      mpRelayFuncOutput[RELAY_FUNC_ALARM_RELAY_DRY_RUNNING].Attach(pSubject);
      break;
            ''')


    '''
    原来是5个listview，在一起正好把屏幕占满了，如果沿用现有的结构，下面新加一个listview：'4.4.6 AlarmRelay List 6'
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |Urgent alarms                                  |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |All alarms                                     |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |All alarms and warnings                        |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |User-defined alarms                            |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
    --> |Dry running alarm                              |
    --> |  Automatic reseting                    ☑      |
    --> |  Manual reseting                       ☐      |
        +-----------------------------------------------+
        这部分已经到屏幕下方看不见了，所以需要把AlarmRelay List 2~6的东西挪到List1里，再加上Dry running alarm，并把AlarmRelay List 2~6隐藏起来
        '''

    list1_id = DisplayComponent_Model.get(Name='4.4.6 AlarmRelay List 1').id
    DisplayListView().update(id=list1_id, PrevListId=0, NextListId=0)   #不需要4.4.6 AlarmRelay List 1指向其它List
    DisplayComponent().update(id=list1_id, x1=0, x2=239, y1=15, y2=271) #重新调整4.4.6 AlarmRelay List 1的尺寸

    #隐藏4.4.6 AlarmRelay List 2~5
    for i in range(2, 6):
        list_id = DisplayComponent_Model.get(Name='4.4.6 AlarmRelay List %d' % i).id
        DisplayComponent().update(id=list_id, ParentComponent=0, Visible=False, x1=0, x2=0, y1=0, y2=0)


    t = template('LabelBlank')
    t.description = '''---------- 4.4.6 Alarm relays 页面里新加一空行 ----------
    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.4.6 Alarm relays                             |
    +-----------------------------------------------+
    |                                               |
    |High-level alarm                               |
    |  Automatic reseting                    ☑      |
    |  Manual reseting                       ☐      |
--> |                                               |
    |Dry running alarm                              |
    |  Automatic reseting                    ☑      |
    |  Manual reseting                       ☐      |
    |                                               |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''
    t.listview_id = '4.4.6 AlarmRelay List 1'
    t.save()


    lst = [ # string, label_name, define_name, subject of auto reset
        ['Dry running alarm', '4.4.6 AlarmRelay dry running', 'SID_DO_DRY_RUNNING_ALARM', 'alarm_relay_dry_running_auto_ack'],
    ]
    for i in lst:
        t = template('LabelHeadline')
        t.description = '''---------- 4.4.6 Alarm relays 页面里新加一行label: %s ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
    --> |%s
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0], i[0])
        t.label_name = i[1]
        t.define_name = i[2]
        t.listview_id = '4.4.6 AlarmRelay List 1'
        t.foreground_colour = 'GUI_COLOUR_TEXT_HEADLINE_FOREGROUND'
        t.background_colour = 'GUI_COLOUR_DEFAULT_BACKGROUND'
        t.save()


        t = template('LabelAndCheckbox')
        t.description = '''---------- 4.4.6 Alarm relays 页面里新加一行label and checkbox: Automatic reseting ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |%s
    --> |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0])
        t.label_name = i[1] + ' auto'
        t.checkbox_name = i[1] + ' auto cb'
        t.checkbox_type = 'ModeCheckBox'
        t.check_state = 1
        t.label_column_index = 0
        t.checkbox_column_index = 1
        t.label_left_margin = 8
        t.label_right_margin = 0
        t.define_name = 'SID_AUTO_ACKNOWLEDGE'
        t.listview_id = '4.4.6 AlarmRelay List 1'
        t.subject_id = i[3]
        t.save()


        t = template('LabelAndCheckbox')
        t.description = '''---------- 4.4.6 Alarm relays 页面里新加一行label and checkbox: Manual reseting ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |%s
        |  Automatic reseting                    ☑      |
    --> |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0])
        t.label_name = i[1] + ' man'
        t.checkbox_name = i[1] + ' man cb'
        t.checkbox_type = 'ModeCheckBox'
        t.check_state = 0
        t.label_column_index = 0
        t.checkbox_column_index = 1
        t.label_left_margin = 8
        t.label_right_margin = 0
        t.define_name = 'SID_MANUAL_ACKNOWLEDGE'
        t.listview_id = '4.4.6 AlarmRelay List 1'
        t.subject_id = i[3]   #与auto使用同一个subject
        t.save()

        t = template('LabelBlank')
        t.description = '''---------- 4.4.6 Alarm relays 页面里新加一空行 ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |%s
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
    --> |                                               |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0])
        t.listview_id = '4.4.6 AlarmRelay List 1'
        t.save()
        

    #沿用base.py里用lable的基类方法处理listview
    def handle_listview(display_listview_item, display_listview_item_components_list):
        # index 从0开始遍历一遍
        for i in range(0, display_listview_item.model.Index):
            try:
                r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=i)
                if r:
                    # 通过id查询DisplayListViewItemComponents里是否已经有挂在该id下的
                    s = DisplayListViewItemComponents_Model.get(ListViewItemId=r.id)
                    if s:
                        for display_listview_item_components in display_listview_item_components_list:
                            if display_listview_item_components.model.ComponentId == s.ComponentId:
                                log(("DisplayListViewItemComponents已有该记录").decode('utf-8'))
                                return
            except:
                debug(("未找到记录").decode('utf-8'))
        display_listview_item.add()
        for x in display_listview_item_components_list:
            r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=display_listview_item.model.Index)
            x.model.ListViewItemId = r.id
            x.add()

    lst = [ # string, label_name, define_name, label name for auto reset, checkbox name for auto reset, subject of auto reset
        ['Urgent alarms', '4.4.6 AlarmRelay urgent', 'SID_DO_DRY_RUNNING_ALARM', 'alarm_relay_urgent_auto_ack'],
        ['All alarms', '4.4.6 AlarmRelay all', 'SID_DO_DRY_RUNNING_ALARM', 'alarm_relay_all_auto_ack'],
        ['All alarms and warnings', '4.4.6 AlarmRelay all+war', 'SID_DO_DRY_RUNNING_ALARM', 'alarm_relay_all_and_war_auto_ack'],
        ['User-defined alarms', '4.4.6 AlarmRelay custom', 'SID_DO_DRY_RUNNING_ALARM', 'alarm_relay_custom_auto_ack'],
    ]
    listview_id = '4.4.6 AlarmRelay List 1'
    for i in lst:
        comment('''---------- 4.4.6 Alarm relays 页面里新加一行label: %s ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
    --> |%s
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0], i[0]))
        table = DisplayListViewItem(ListViewId=listview_id)
        table.add()
        x = table
        l = []
        table = DisplayListViewItemComponents(ComponentId=i[1], ColumnIndex=0)
        table.add()
        l.append(table)
        handle_listview(x, l)


        comment('''---------- 4.4.6 Alarm relays 页面里新加一行label and checkbox: Automatic reseting ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |%s
    --> |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0]))
        # 在对应的listview下面新加一个item
        table = DisplayListViewItem(ListViewId=listview_id)
        table.add()
        x = table
        l = []
        # 在新加的item下面添加label
        table = DisplayListViewItemComponents(ComponentId=i[1]+' auto', ColumnIndex=0)
        table.add()
        l.append(table)
        table = DisplayListViewItemComponents(ComponentId=i[1]+' auto cb', ColumnIndex=1)
        table.add()
        l.append(table)
        handle_listview(x, l)


        comment('''---------- 4.4.6 Alarm relays 页面里新加一行label and checkbox: Manual reseting ----------
        +----------+-------------+---------+------------+
        |  Status  |  Operation  |  Alarm  |  Settings  |
        +----------+-------------+---------+------------+
        |4.4.6 Alarm relays                             |
        +-----------------------------------------------+
        |                                               |
        |High-level alarm                               |
        |  Automatic reseting                    ☑      |
        |  Manual reseting                       ☐      |
        |                                               |
        |%s
        |  Automatic reseting                    ☑      |
    --> |  Manual reseting                       ☐      |
        |                                               |
        +-----------------------------------------------+
        |GRUNDFOS                       04-05-2015 11:13|
        +-----------------------------------------------+
        ''' % (i[0]))
        # 在对应的listview下面新加一个item
        table = DisplayListViewItem(ListViewId=listview_id)
        table.add()
        x = table
        l = []
        # 在新加的item下面添加label
        table = DisplayListViewItemComponents(ComponentId=i[1]+' man', ColumnIndex=0)
        table.add()
        l.append(table)
        table = DisplayListViewItemComponents(ComponentId=i[1]+' man cb', ColumnIndex=1)
        table.add()
        l.append(table)
        handle_listview(x, l)

        if i != lst[-1]:
            t = template('LabelBlank')
            t.description = '''---------- 4.4.6 Alarm relays 页面里新加一空行 ----------
            +----------+-------------+---------+------------+
            |  Status  |  Operation  |  Alarm  |  Settings  |
            +----------+-------------+---------+------------+
            |4.4.6 Alarm relays                             |
            +-----------------------------------------------+
            |                                               |
            |High-level alarm                               |
            |  Automatic reseting                    ☑      |
            |  Manual reseting                       ☐      |
            |                                               |
            |%s
            |  Automatic reseting                    ☑      |
        --> |  Manual reseting                       ☐      |
            |                                               |
            +-----------------------------------------------+
            |GRUNDFOS                       04-05-2015 11:13|
            +-----------------------------------------------+
            ''' % (i[0])
            t.listview_id = '4.4.6 AlarmRelay List 1'
            t.save()


def update_ptc_string():
    '''
    2)	Under “I/O Settings” > “PTC Inputs,” we can tag the “moisture” alarm from a digital input, and we can also assign the thermal as an input, but no one here knows what “PTC, Pump 1” stands for.  I understand that PTC stands for thermal, but that is because I work with this product all the time.  We have got to change the wording to show “PTC/Thermal, Pump 1” or some variant that actually says “thermal.”  We hook a lot of these systems up to existing pumps (non-grundfos) that simply have relay outputs for thermal/seal.  We end up having to use another digital input and a user defined function to create a thermal alarm because no one knows what the PTC means.  That would be a great and hopefully easy fix.
    '''
    str_list = [[2005, 2006], [2008, 2009], [2011, 2012], [2014, 2015], [2017, 2018], [2020, 2021]]
    for pump_num, id_list in enumerate(str_list):
        for ptc_num, _id in enumerate(id_list):
            new_string = 'PTC/Thermal %d, pump %d' % (ptc_num+1, pump_num+1)
            update_string(_id, 'Developer', new_string)
            update_string(_id, 'English', new_string)

