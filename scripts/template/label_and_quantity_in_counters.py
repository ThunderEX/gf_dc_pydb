# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Label

class LabelAndQuantityInCounters(Label):

    ''' New label and checkbox in 4.2.5 - Adjustment of counters.  '''

    label_name = ''               #: new label name that added in DisplayComponent
    quantity_name = ''            #: new quantity name that added in DisplayComponent
    quantity_type = 'Q_NO_UNIT'   #: quantity type in DisplayNumberQuantity
    define_name = ''              #: string define for new label
    label_string = ''             #: string for new label, multiple languages
    listview_id = '4.2.5 AdjustCounters List'              #: listview id which will include the new label and quantity
    subject_id = ''               #: link subject and quantity
    listviewitem_index = 0        #: label column index that to insert in the listview
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
            # 添加label
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
            # 添加数值
            (DisplayComponent,
             {
                 'Name': self.quantity_name,
                 'ComponentType': 'NumberQuantity',
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
                 'LeftMargin': 8,
                 'RightMargin': 0,
                 'WordWrap': False,
             }
             ),
            # 定义数值的text排列方式
            (DisplayText,
             {
                 'id': self.quantity_name,
                 'Align': 'VCENTER_HCENTER',
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': 0,
                 'RightMargin': 0,
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
                 'SubjectAccess': 'Read/Write',
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


    def increase_listview_item_index(self):
        '''
            把新加的listviewitem的Index改成中间的Index，并把大于这个值的Index都加1
        :return: 
        '''
        table = DisplayListViewItem(ListViewId=self.listview_id)
        max_idx = table.model.Index - 1
        listviewitem_model = DisplayListViewItem_Model()
        r = listviewitem_model.select().where(ListViewId=table.model.ListViewId)
        id_idx_list = [(i.id, i.Index) for i in r]
        for item in id_idx_list:
            if item[1] == max_idx:       # 新加入的item的Index是最大的，将其改为指定的index
                table.update(id=item[0], Index=self.listviewitem_index)
                continue
            if item[1] >= self.listviewitem_index:  # 其它大于指定index的item，将其index加1
                table.update(id=item[0], Index=item[1]+1)
        
    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        self.save_with_parameters(self.available_rule_parameters)
        self.increase_listview_item_index()

