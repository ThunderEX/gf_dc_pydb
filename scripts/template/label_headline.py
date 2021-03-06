# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Label

class LabelHeadline(Label):

    ''' New label that only one line text '''

    label_name = ''               #: new label name that added in DisplayComponent
    define_name = ''              #: string define for new label
    label_string = ''             #: string for new label, multiple languages
    listview_id = ''              #: listview id which will include the new label and quantity
    exclude_from_factory = False  #: hide the lable if true
    label_left_margin = 0         #: left margin of label
    label_right_margin = 0        #: right margin of label
    label_x1 = 1
    label_y1 = 0
    label_x2 = 239
    label_y2 = 29
    help_string = 0
    foreground_colour = None
    background_colour = None

    available_rule_name = ''                #: specify the available rule name, this rule should be pre-defined
    available_rule_column_index = 0         #: the column width should be 0

    def update_parameters(self):
        if self.label_string:
            self.string_parameters = [
                # 加字符串定义
                (StringDefines,
                 {
                     'DefineName': self.define_name,
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
            (DisplayComponent,
             {
                 'Name': self.label_name,
                 'ComponentType': 'Label',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': True,
                 'x1': self.label_x1,
                 'y1': self.label_y1,
                 'x2': self.label_x2,
                 'y2': self.label_y2,
                 'DisplayId': 0,
                 'HelpString': self.help_string,
                 'Transparent': False,
             }
             ),
            
            # 将字符串和label对应起来
            (DisplayLabel,
             {
                 'id': self.label_name,
                 'StringId': self.define_name,
             }
             ),
            # 定义label的text排列方式
            (DisplayText,
             {
                 'id': self.label_name,
                 'Align': 'VCENTER_LEFT',
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': self.label_left_margin,
                 'RightMargin': self.label_right_margin,
                 'WordWrap': False,
             }
             ),
        ]
        if self.foreground_colour:
            self.label_parameters.append(
                (DisplayComponentColour,
                 {
                     'id': self.label_name,
                     'ForegroundColour': self.foreground_colour,
                     'BackgroundColour': self.background_colour,
                 }
                 ),
            )

        self.display_listview_parameters = [
            # 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
                 'ExcludeFromFactory': self.exclude_from_factory,
             }
             ),
            # 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
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

