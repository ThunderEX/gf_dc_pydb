# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Label

class LabelAndCheckbox(Label):

    ''' New label and checkbox.  '''

    label_name = ''               #: new label name that added in DisplayComponent
    checkbox_name = ''            #: new checkbox name that added in DisplayComponent
    checkbox_type = ''            #: new checkbox type, ModeCheckBox or OnOffCheckBox
    define_name = ''              #: string define for new label
    label_string = ''             #: string for new label, multiple languages
    listview_id = ''              #: listview id which will include the new label and quantity
    subject_id = ''               #: link subject and checkbox
    check_state = 0               #: ModeCheckBox use this, value means enum define values in AppTypeDefs.h
    label_column_index = 0        #: label column index in the listview
    checkbox_column_index = 1     #: checkbox column index in the listview
    label_left_margin = 0         #: left margin of label
    label_right_margin = 0        #: right margin of label
    listviewitem_index = 0        #: the index for new label and checkbox, which is blank line before

    available_rule_name = ''                #: specify the available rule name, this rule should be pre-defined
    available_rule_column_index = 0         #: the column width should be 0

    def update_parameters(self):
        if self.label_string:
            self.string_parameters = [
                # 加字符串定义
                (StringDefines,
                 {
                     'DefineName': self.define_name,
                     'TypeId': 'Value type',
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
                # label加相应的字符串
                (Strings,
                 {
                     'String': self.label_string,
                     'LanguageId': 'UK_LANGUAGE',
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
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 2. 添加CheckBox
            (DisplayComponent,
             {
                 'Name': self.checkbox_name,
                 'ComponentType': self.checkbox_type,
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': False,
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
                 'StringId': self.define_name,
             }
             ),
            # 6. 定义label的text排列方式
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
        if self.checkbox_type == 'ModeCheckBox':
            self.label_parameters.append(
                (DisplayModeCheckBox,
                 {
                     'id': self.checkbox_name,
                     'CheckState': self.check_state,
                 }
                 ),
            )
        elif self.checkbox_type == 'OnOffCheckBox':
            self.label_parameters.append(
                (DisplayOnOffCheckBox,
                 {
                     'id': self.checkbox_name,
                     'OnValue': 1,
                     'OffValue': 0,
                 }
                 ),
            )

        self.label_parameters.append(
            # checkbox与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.checkbox_name,
                 'SubjectId': self.subject_id,
                 'SubjectAccess': 'Read/Write',
             }
             ),
        )

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
                 'ColumnIndex': self.label_column_index,
             }
             ),
            # 在新加的item下面添加数值
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.checkbox_name,
                 'ColumnIndex': self.checkbox_column_index,
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


    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        self.save_with_parameters(self.available_rule_parameters)
        self.increase_listview_item_index()
