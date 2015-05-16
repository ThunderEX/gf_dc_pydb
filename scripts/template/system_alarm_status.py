# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from subject import NewSubject

class SystemAlarmStatus(object):

    ''' Add new system alarm in 4.5.1 - System alarms '''

    label_name = ''                                 # : new label name that added in DisplayComponent.
    label_define_name = ''                          # : string define for new label.
    label_string = ''                               # : string for new label, multiple languages
    alarm_icon_name = ''                            # : new alarm icon name that added in DisplayComponent.
    warning_icon_name = ''                          # : new warning icon name that added in DisplayComponent.
    subject_id = ''                                 # : link subject and alarm icon and warning icon, should be a AlarmConfig type subject
    listview_id = '4.5.5 SystemAlarms Status List'  # : listview id which will include the new label and icons

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
            # 3. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.label_define_name,
                 'TypeId': 'Display name',
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
            # 8. 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
            # 9. 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
             }
             ),
             # 10. 在新加的item下面添加alarm icon
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.alarm_icon_name,
                 'ColumnIndex': 1,
             }
             ),
            # 10. 在新加的item下面添加warning icon
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.warning_icon_name,
                 'ColumnIndex': 2,
             }
             ),
        ]


    def add_alarm(self, parameters):
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

    def save(self):
        comment(self.description)
        self.update_parameters()
        self.add_alarm(self.parameters)
