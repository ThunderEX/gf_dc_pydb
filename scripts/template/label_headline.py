# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class LabelHeadline(object):
    label_name = ''               #new label name that added in DisplayComponent
    define_name = ''              #string define for new label
    string = ''                   #string for new label, in many languages
    listview_id = ''              #listview id which will include the new label and quantity
    label_left_margin = 0
    label_right_margin = 0

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
            (DisplayComponent,
             {
                 'Name': self.label_name,
                 'ComponentType': 'Label',
                 'ParentComponent': 0,
                 'Visible': True,
                 'ReadOnly': True,
                 'x1': 1,
                 'y1': 0,
                 'x2': 239,
                 'y2': 29,
                 'DisplayId': 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            # 3. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.define_name,
                 'TypeId': 'Display name',
             }
             ),
            # 4. label加相应的字符串
            (Strings,
             {
                 'String': self.string,
                 'LanguageId': 'DEV_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (Strings,
             {
                 'String': self.string,
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
            # 7. 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
            # 8. 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
             }
             ),
        ]

    def save(self):
        comment(self.description)
        self.update_parameters()
        rtn = []
        display_listview_item_components_list = []
        for index, para in enumerate(self.parameters):
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




