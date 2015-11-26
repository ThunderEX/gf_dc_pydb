# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Label
from subject import NewSubject

class SystemAlarm(Label):

    ''' 
    Add new system alarm in 4.5.1 - System alarms 

    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.5.1 - System alarms                          |
    +-----------------------------------------------+
    |                                               |
    |Select system alarm                            |
    |  Overflow                                     |
    |  High level                                   |
    |  Alarm level                                  |
    |  Dry running                                  |
    |  Float switch                                 |
    |  Level sensor                                 |
    |  ......                                       |
    |                                               |
    |                                               |
--> |  DDA fault                                    |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''

    label_name = ''                                 # : new label name that added in DisplayComponent.
    label_define_name = ''                          # : string define for new label.
    label_string = ''                               # : string for new label, multiple languages
    slippoint_name = ''                             # : system alarm is pair of label and slippoint
    subject_id = 'display_configalarm_slippoint_no' # : link subject and slippoint
    write_state = 0                                 # : write state can help render to new alarm config page, the value should equal the new enum value defined in ALARM_CONFIG_TYPE in AppTypeDefs.h
    listview_id = '4.5.1 SystemAlarms List'         # : listview id which will include the new label and slippoint

    available_rule_name = ''                        #: specify the available rule name, this rule should be pre-defined
    available_rule_column_index = 0                 #: the column width should be 0

    alarm_alarm_id = 0                              #: specify the id of alarm, which is also the event code in geni profile
    alarm_alarm_string_id = ''                      #: SID_ALARM_XXXX

    alarm_config_subject = NewSubject()
    alarm_subject = NewSubject()

    def update_parameters(self):
        if self.label_string:
            self.string_parameters = [
                # 加字符串定义
                (StringDefines,
                 {
                     'DefineName': self.label_define_name,
                     'TypeId': 'Display name',
                 }
                 ),
                # label加相应的字符串
                (Strings,
                 {
                     'String': self.label_string,
                     'LanguageId': 'DEV_LANGUAGE',
                     'Status': 'UnEdit',
                 }
                 ),
            ]

        self.label_parameters = [
            # 1. 添加label
            (DisplayComponent,
             {
                 'Name': self.label_name,
                 'ComponentType': 'Label',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': True,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 0,
                 'HelpString': 'SID_HELP_4_5_1_LINE_5',
                 'Transparent': False,
             }
             ),
            # 2. 添加slippoint
            (DisplayComponent,
             {
                 'Name': self.slippoint_name,
                 'ComponentType': 'WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay',
                 'ParentComponent': 0,
                 'Visible': False,
                 'ReadOnly': False,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 67,           #Digital outputs
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 5. 将字符串和label对应起来
            (DisplayLabel,
             {
                 'id': self.label_name,
                 'StringId': self.label_define_name,
             }
             ),
            # 6. 定义label的text排列方式
            (DisplayText,
             {
                 'id': self.label_name,
                 'Align': 'VCENTER_LEFT',
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': 8,
                 'RightMargin': 0,
                 'WordWrap': False,
             }
             ),
            # 9. slippoint与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.slippoint_name,
                 'SubjectId': self.subject_id,         #fixed to display_configalarm_slippoint_no
                 'SubjectAccess': 'Write',
             }
             ),
            # 13. 在WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay表里添加WriteState
            # TODO 用正则找出同样是'4.5.1 SystemAlarms'的最大WriteState
            (WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay,
             {
                 'id': self.slippoint_name,
                 'WriteState': self.write_state,
             }
             ),
        ]

        self.display_listview_parameters = [
            # 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
            # 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
             }
             ),
            # 在新加的item下面添加slippoint
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.slippoint_name,
                 'ColumnIndex': 1,
             }
             ),
        ]

        if self.available_rule_name:
            self.available_rule_parameters = [
                    (DisplayListViewItemComponents,
                     {
                         'ListViewItemId': 0,  #在handle_DisplayListViewItemAndComponents里更新，与label的ListViewItemId相等，而不是外部输入
                         'ComponentId': self.available_rule_name,
                         'ColumnIndex': self.available_rule_column_index,      #TODO, 需要判断哪个ColumnWidth为0
                     }
                     ),
                ]

        if self.alarm_alarm_id:
            self.label_parameters.append(
            (DisplayAlarmStrings,
             {
                'AlarmId': self.alarm_alarm_id,
                'StringId': self.alarm_alarm_string_id,
             }
             ),
            )


    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        self.save_with_parameters(self.available_rule_parameters)
        self.alarm_config_subject.save()
        self.alarm_subject.save()
