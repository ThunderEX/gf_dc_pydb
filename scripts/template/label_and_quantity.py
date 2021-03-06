# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Label

class LabelAndQuantity(Label):
    '''
        New label and quantity
    '''
    label_name = ''               #: new label name that added in DisplayComponent
    label_readonly = True
    label_align = 'VCENTER_LEFT'
    label_left_margin = 0         #: left margin of label
    label_right_margin = 0        #: right margin of label
    quantity_name = ''            #: new quantity name that added in DisplayComponent
    quantity_type = 'Q_NO_UNIT'   #: quantity type in DisplayNumberQuantity
    quantity_readonly = True
    quantity_align = 'VCENTER_LEFT'
    quantity_left_margin = 0      #: left margin of quantity
    quantity_right_margin = 0     #: right margin of quantity
    define_name = ''              #: string define for new label
    label_string = ''             #: string for new label, multiple languages
    listview_id = ''              #: listview id which will include the new label and quantity
    subject_id = ''               #: link subject and quantity
    subject_access = 'Read'
    listviewitem_index = 0        #: label column index that to insert in the listview
    exclude_from_factory = False  #: hide the lable if true
    number_of_digits = 3          #: length of digital, 3 is int, 5 can display float

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
            ]

        self.label_parameters = [
            # 添加label
            (DisplayComponent,
             {
                 'Name': self.label_name,
                 'ComponentType': 'Label',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': self.label_readonly,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 添加数值
            (DisplayComponent,
             {
                 'Name': self.quantity_name,
                 'ComponentType': 'NumberQuantity',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': self.quantity_readonly,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 0,
                 'HelpString': 0,
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
                 'Align': self.label_align,
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': self.label_left_margin,
                 'RightMargin': self.label_right_margin,
                 'WordWrap': False,
             }
             ),
            # 定义数值的text排列方式
            (DisplayText,
             {
                 'id': self.quantity_name,
                 'Align': self.quantity_align,
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': self.quantity_left_margin,
                 'RightMargin': self.quantity_right_margin,
                 'WordWrap': False,
             }
             ),
            # 数值与新加单位对应
            (DisplayNumberQuantity,
             {
                 'id': self.quantity_name,
                 'QuantityType': self.quantity_type,
                 'NumberOfDigits': self.number_of_digits,
                 'NumberFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
                 'QuantityFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
             }
             ),
            # 数值与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.quantity_name,
                 'SubjectId': self.subject_id,
                 'SubjectAccess': self.subject_access,
             }
             ),           
        ]

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
            # 在新加的item下面添加数值
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.quantity_name,
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


    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        self.save_with_parameters(self.available_rule_parameters)
        self.increase_listview_item_index()

