# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class LabelAndCheckboxInAO(object):

    ''' New label and checkbox in AO.  '''

    label_name = ''               #: new label name that added in DisplayComponent
    checkbox_name = ''            #: new checkbox name that added in DisplayComponent
    checkbox_type = 'ModeCheckBox'            #: new checkbox type, ModeCheckBox or OnOffCheckBox
    define_name = ''              #: string define for new label
    label_string = ''             #: string for new label, multiple languages
    listview_id = '4.4.3.1 AnalogOutputSetup List 1 func'              #: listview id which will include the new label and quantity
    subject_id = 'display_ao_slippoint_virtual_func'               #: link subject and quantity
    check_state = 0               #: ModeCheckBox use this, value means enum define values in AppTypeDefs.h
    label_column_index = 0        #: label column index in the listview
    checkbox_column_index = 1     #: checkbox column index in the listview
    label_left_margin = 8         #: left margin of label
    label_right_margin = 0        #: right margin of label
    listviewitem_index = 11       #: the index for new label and checkbox, which is blank line before

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
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
            # 3. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.define_name,
                 'TypeId': 'Value type',
             }
             ),
            # 4. label加相应的字符串
            (Strings,
             {
                 'String': self.label_string,
                 'LanguageId': 'DEV_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (Strings,
             {
                 'String': self.label_string,
                 'LanguageId': 'UK_LANGUAGE',
                 'Status': 'UnEdit',
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
            # 10. 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
 
            (DisplayModeCheckBox,
             {
                 'id': self.checkbox_name,
                 'CheckState': self.check_state,
             }
             ),
            # checkbox与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.checkbox_name,
                 'SubjectId': self.subject_id,
                 'SubjectAccess': 'Read/Write',
             }
             ),
        ]

    def save(self):
        comment(self.description)
        self.update_parameters()
        rtn = []
        for index, para in enumerate(self.parameters):
            #log(("处理第%d项" % (index + 1)).decode('utf-8'))
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            x.add()
            rtn.append(x)
        self.handle_ao_setting_items()
        self.replace_blank_line_with_new_added_label_and_checkbox()
        return rtn

    def replace_blank_line_with_new_added_label_and_checkbox(self):
        listviewitem_model = DisplayListViewItem_Model()
        table = DisplayListViewItemComponents()
        # 4.4.3.1 AnalogOutputSetup List 1 func = 5139
        r = listviewitem_model.get(ListViewId=5139, Index=self.listviewitem_index)
        if r:
            listviewitem_id = r.id
        else:
            debug(("未找到记录").decode('utf-8'))
            raise NameError
        table = DisplayListViewItemComponents(ListViewItemId=listviewitem_id, ComponentId=self.label_name, ColumnIndex=self.label_column_index)
        table.add()
        table = DisplayListViewItemComponents(ListViewItemId=listviewitem_id, ComponentId=self.checkbox_name, ColumnIndex=self.checkbox_column_index)
        table.add()
        

    def handle_ao_setting_items(self):
        listviewitem_model = DisplayListViewItem_Model()
        listviewitemcomponents_model = DisplayListViewItemComponents_Model()
        table = DisplayListViewItemComponents()
        
        #4183-4190是headline，min和max等setting
        for _id in range(4183, 4190+1):
            #先找出在DisplayListViewItem里的id
            r = listviewitemcomponents_model.get(id=_id)
            if r:
                listviewitem_id = r.ListViewItemId
            else:
                debug(("未找到记录").decode('utf-8'))
                raise NameError
            #再找出该id在DisplayListViewItem里对应的index
            r = listviewitem_model.get(id=listviewitem_id)
            if r:
                listview_id = r.ListViewId
                index = r.Index
            else:
                debug(("未找到记录").decode('utf-8'))
                raise NameError
            new_index = index + 1
            #最后还要在DisplayListViewItem里找到index+1后的新id
            r = listviewitem_model.get(ListViewId=listview_id, Index=new_index)
            if r:
                new_listviewitem_id = r.id
            else:
                debug(("未找到记录").decode('utf-8'))
                raise NameError
            #用新的id更新DisplayListViewItemComponents表
            table.update(id=_id, ListViewItemId=new_listviewitem_id)
            
            '''
                   # 11. 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ListViewItemId': 1903
                 'ComponentId': self.label_name,
                 'ColumnIndex': self.label_column_index,
             }
             ),
            # 12. 在新加的item下面添加数值
            (DisplayListViewItemComponents,
             {
                 'ListViewItemId': 1903
                 'ComponentId': self.checkbox_name,
                 'ColumnIndex': self.checkbox_column_index,
             }
             ),
            '''

