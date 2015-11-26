# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Label
from subject import NewSubject

class SystemAlarmStatus(Label):

    '''
    Add new system alarm status in 4.5.5 - System alarms 

    +----------+-------------+---------+------------+
    |  Status  |  Operation  |  Alarm  |  Settings  |
    +----------+-------------+---------+------------+
    |4.5.5 - Status, system alarms                  |
    +-----------------------------------------------+
    |                                               |
    |  Overflow                                (!)  |
    |  High level                              (!)  |
    |  Alarm level                             (!)  |
    |  Dry running                             (!)  |
    |  Float switch                            (!)  |
    |  Level sensor                            (!)  |
    |  ......                                       |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
    |                                               |
--> |  DDA fault                               (!)  |
    +-----------------------------------------------+
    |GRUNDFOS                       04-05-2015 11:13|
    +-----------------------------------------------+
    '''

    label_name = ''                                 # : new label name that added in DisplayComponent.
    label_define_name = ''                          # : string define for new label.
    label_string = ''                               # : string for new label, multiple languages
    alarm_icon_name = ''                            # : new alarm icon name that added in DisplayComponent.
    warning_icon_name = ''                          # : new warning icon name that added in DisplayComponent.
    subject_id = ''                                 # : link subject and alarm icon and warning icon, should be a AlarmConfig type subject
    listview_id = '4.5.5 SystemAlarms Status List'  # : listview id which will include the new label and icons

    available_rule_name = ''                #: specify the available rule name, this rule should be pre-defined
    available_rule_column_index = 0         #: the column width should be 0

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
                 'HelpString': 'SID_HELP_4_5_1_LINE_5',      #TODO define new help string
                 'Transparent': False,
             }
             ),
            # 2. 添加alarm icon
            (DisplayComponent,
             {
                 'Name': self.alarm_icon_name,
                 'ComponentType': 'AlarmEnabledIconState',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': True,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 2. 添加warning icon
            (DisplayComponent,
             {
                 'Name': self.warning_icon_name,
                 'ComponentType': 'WarningEnabledIconState',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': True,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 0,
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
            # 7. alarm icon与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.alarm_icon_name,
                 'SubjectId': self.subject_id,
                 'SubjectAccess': 'Write',
             }
             ),
            # 7. warning icon与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.warning_icon_name,
                 'SubjectId': self.subject_id,
                 'SubjectAccess': 'Read',
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
             # 在新加的item下面添加alarm icon
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.alarm_icon_name,
                 'ColumnIndex': 1,
             }
             ),
            # 在新加的item下面添加warning icon
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.warning_icon_name,
                 'ColumnIndex': 2,
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

