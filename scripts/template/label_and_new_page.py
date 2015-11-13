# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Label

class LabelAndNewPage(Label):

    ''' Add new label and click this label will render to a new page. New page combines with a group and display. Under the group, it is a listview. '''

    label_name = ''                         #: new label name that added in DisplayComponent.
    label_define_name = ''                  #: string define for new label.
    label_string = ''                       #: string for new label, multiple languages
    listview_id = ''                        #: listview id which will include the new label
    label_left_margin = 8                   #: left margin of label
    label_right_margin = 0                  #: right margin of label

    available_rule_name = ''                #: specify the available rule name, this rule should be pre-defined
    available_rule_column_index = 0         #: the column width should be 0

    group_name = ''                         #: new group name that added in DisplayComponent.
    group_define_name = ''                  #: string define for new group.

    root_group_id_name = ''                 #: group id name in Display table, should be same with group_name
    display_string_name = ''                #: should be same with label_string
    display_number = ''                     #: the index number of group

    listview_name = ''                      #: new listview name that added in DisplayComponent.
    listview_column_width = [160, 64, 0]    #: list of column width of new listview.
    next_list_id = 0                        # next listview to the new listview, 0 is '- None -'
    prev_list_id = 0                        # previous listview to the new listview, 0 is '- None -'
    exclude_from_factory = False            #: hide the lable if true
    
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
                 #'DisplayId'       : 0,         #DisplayComponent里DisplayId为0，需要指向要显示的group
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 将字符串和label对应起来
            (DisplayLabel,
             {
                 'id': self.label_name,
                 'StringId': self.label_define_name,
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
                         'ListViewItemId': 0,                                  #在handle_DisplayListViewItemAndComponents里更新，与label的ListViewItemId相等，而不是外部输入
                         'ComponentId': self.available_rule_name,
                         'ColumnIndex': self.available_rule_column_index,      #TODO, 需要判断哪个ColumnWidth为0
                     }
                     ),
                ]

        self.group_parameters = [
            # 1. 添加group，也就是另起一页
            (DisplayComponent,
             {
                 'Name': self.group_name,
                 'ComponentType': 'Group',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': False,
                 'x1': 0,
                 'y1': 33,
                 'x2': 239,
                 'y2': 305,
                 'DisplayId': 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 2. 将字符串和label对应起来
            (DisplayLabel,
             {
                 'id': self.group_name,
                 'StringId': self.group_define_name,
             }
             ),
            # 3. 定义label的text排列方式
            (DisplayText,
             {
                 'id': self.group_name,
                 'Align': 'VCENTER_LEFT',
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': 8,
                 'RightMargin': 0,
                 'WordWrap': False,
             }
             ),
        ]

        self.display_parameters = [
            # Display
            (Display,
             {
                 'RootGroupId': self.root_group_id_name,
                 'DisplayNumber': self.display_number,
                 'Name': self.display_string_name,
                 #'FocusComponentId'  : 0,   #set from listview later
                 'AbleToShow': True,
                 'Show': False,
                 'FirstWizardDisplay': False,
             }
             ),
        ]

        self.listview_parameters = [
            # 添加Listview
            (DisplayComponent,
             {
                 'Name': self.listview_name,
                 'ComponentType': 'ListView',
                 #'ParentComponent' : 0,                          #set later
                 'Visible': True,
                 'ReadOnly': False,
                 'x1': 0,
                 'y1': 15,
                 'x2': 239,
                 'y2': 271,
                 'DisplayId': 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 2. 定义label的text排列方式
            (DisplayText,
             {
                 'id': self.listview_name,
                 'Align': 'VCENTER_LEFT',
                 'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
                 'LeftMargin': 8,
                 'RightMargin': 0,
                 'WordWrap': False,
             }
             ),
            (DisplayListView,
             {
                 'id': self.listview_name,
                 'RowHeight': 15,
                 'SelectedRow': 0,
                 'NextListId': self.next_list_id,
                 'PrevListId': self.prev_list_id,  # - None -
             }
             ),
        ]
        for index, column in enumerate(self.listview_column_width):
            self.listview_parameters.append(
                (DisplayListViewColumns, 
                 { 
                     'ListViewId': self.listview_name, 
                     'ColumnIndex': index, 
                     'ColumnWidth': column, 
                  }
                 )
            )

    def update_displayid(self, display_component_tables, display_tables):
        '''
            更新DisplayComponent表里的DisplayId，指向一个新的页

        :param display_component_tables: 添加label等形成的table实例列表
        :param display_tables: 添加display形成的table列表
        '''
        # 找出DisplayComponent实例
        for x in display_component_tables:
            if isinstance(x, DisplayComponent):
                display_component = x
        # 找出Display的id
        for x in display_tables:
            if isinstance(x, Display):
                _displayid = x.model.id
        display_component.update(display_component.model.id, DisplayId=_displayid)

    def update_focus_component_id(self, display_component_tables, display_tables):
        '''
            更新display表里的FocusComponentId，指向listview等的id

        :param display_component_tables: 添加listview，label等形成的table实例列表
        :param display_tables: 添加display形成的table列表
        '''
        # 找出DisplayComponent的id
        for x in display_component_tables:
            if isinstance(x, DisplayComponent):
                _focuscomponentid = x.model.id
        # 找出Display
        for x in display_tables:
            if isinstance(x, Display):
                display = x
        display.update(display.model.id, FocusComponentId=_focuscomponentid)

    def update_parent_component(self, group_tables, display_component_tables):
        '''
            更新DisplayComponent表里的ParentComponent，指向group的id

        :param group_tables: 添加group形成的table实例列表
        :param display_component_tables: 添加listview，label等形成的table实例列表
        '''
        for x in group_tables:
            if isinstance(x, DisplayComponent):
                group_component = x
                _parentcomponent = x.model.id
        # 找出Display的id
        for x in display_component_tables:
            if isinstance(x, DisplayComponent):
                display_component = x
        display_component.update(display_component.model.id, ParentComponent=_parentcomponent)

    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        label_tables = self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        available_rule_tables = self.save_with_parameters(self.available_rule_parameters)
        group_tables = self.save_with_parameters(self.group_parameters)
        display_tables = self.save_with_parameters(self.display_parameters)
        listview_tables = self.save_with_parameters(self.listview_parameters)
        self.update_displayid(label_tables, display_tables)
        self.update_focus_component_id(listview_tables, display_tables)
        self.update_parent_component(group_tables, listview_tables)
        
