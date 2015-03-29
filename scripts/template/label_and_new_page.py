# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class LabelAndNewPage(object):

    ''' Add new label and click this label will render to a new page. New page combines with a group and display. Under the group, it is a listview. '''

    label_name = ''                         #: new label name that added in DisplayComponent.
    label_define_name = ''                  #: string define for new label.
    label_string = ''                       #: string for new label, multiple languages
    listview_id = ''                        #: listview id which will include the new label and quantity
    label_left_margin = 8                   #: left margin of label
    label_right_margin = 0                  #: right margin of label

    group_name = ''                         #: new group name that added in DisplayComponent.
    group_define_name = ''                  #: string define for new group.

    root_group_id_name = ''                 #: group id name in Display table, should be same with group_name
    display_string_name = ''                #: should be same with label_string
    display_number = ''                     #: the index number of group

    listview_name = ''                      #: new listview name that added in DisplayComponent.
    listviewid_name = ''                    #: the name same as listview_name, used in DisplayListView
    listview_column_width = [160, 64, 0]    #: list of column width of new listview.
    next_list_id = 0                        # next listview to the new listview, 0 is '- None -'
    prev_list_id = 0                        # previous listview to the new listview, 0 is '- None -'
    
    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
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
                 #'DisplayId'       : 0,         #DisplayComponent里DisplayId为0，需要指向要显示的group
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 2. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.label_define_name,
                 'TypeId': 'Display name',
             }
             ),
            # 3. label加相应的字符串
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
            # 4. 将字符串和label对应起来
            (DisplayLabel,
             {
                 'id': self.label_name,
                 'StringId': self.label_define_name,
             }
             ),
            # 5. 定义label的text排列方式
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
            # 6. 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
            # 7. 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
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
                 'id': self.listviewid_name,
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
                     'ListViewId': self.listviewid_name, 
                     'ColumnIndex': index, 
                     'ColumnWidth': column, 
                  }
                 )
            )

    def add(self, parameters):
        rtn = []
        for index, para in enumerate(parameters):
            #log(("处理第%d项" % (index + 1)).decode('utf-8'))
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            x.add()
            rtn.append(x)
        return rtn

    def add_label(self, parameters):
        rtn = []
        display_listview_item_components_list = []
        for index, para in enumerate(parameters):
            #log(("处理第%d项" % (index + 1)).decode('utf-8'))
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            if table == DisplayListViewItem:
                display_listview_item = x
                continue
            if table == DisplayListViewItemComponents:
                display_listview_item_components_list.append(x)
                continue
            x.add()
            rtn.append(x)
        self.handle_DisplayListViewItemAndComponents(display_listview_item, display_listview_item_components_list)
        return rtn

    def handle_DisplayListViewItemAndComponents(self, display_listview_item, display_listview_item_components_list):
        """DisplayListViewItem和DisplayListViewItemComponents是相互关联的，用本函数处理一下"""
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
        label_tables = self.add_label(self.label_parameters)
        group_tables = self.add(self.group_parameters)
        display_tables = self.add(self.display_parameters)
        listview_tables = self.add(self.listview_parameters)
        self.update_displayid(label_tables, display_tables)
        self.update_focus_component_id(listview_tables, display_tables)
        self.update_parent_component(group_tables, listview_tables)
        
