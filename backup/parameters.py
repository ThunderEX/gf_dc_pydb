# -*- coding: utf-8 -*-
from models import *
from tables import *

Yes = True
No = False
yes = True
no = False

"""
格式：
   （表名，
    {
            filed名1：参数，
            filed名2：参数，
    }
    ),
"""

#############################################################Display部分##########################################################

#--------------------------- 1.1 - System 页面里新加一行label:H2S level和quantity:ppm -------------------------------------------#
quantity_name = 'Q_PARTS_PER_MILLION'
string_define = 'SID_PPM'
string = 'ppm'
h2s_level_quantity_parameters = [
    # 1. 加新的单位类型
    (QuantityType,
     {
         'Name': quantity_name,
     }
     ),
    # 2. 加ppm的字符串定义
    (StringDefines,
     {
         "DefineName": string_define,
         "TypeId": "Quantity Unit",
     }
     ),
    # 3. 加ppm相应的字符串
    (Strings,
     {
         'String': string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 4. SubjectRelation里的MpcUnits要加上Q_PARTS_PER_MILLION
    (SubjectRelation,
     {
         'Name': quantity_name,
         'ObserverTypeId': 'MpcUnits',
     }
     ),
    # 5. 修改mpcunits.conf.cpp和mpcunits.cpp
]

label_component_name = '1.1 SystemStatus l1 h2s level'
quantity_component_name = '1.1 SystemStatus l1 h2s level nq'
string_define = 'SID_H2S_LEVEL'
string = 'H2S level'
listviewid_name = '1.1 SystemStatus List 1'
# TODO 先用已有的subject数据total_energy_j_for_display
subjectid = 'total_energy_j_for_display'

h2s_level_label_parameters = [
    # 1. 添加h2s label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加数值label
    (DisplayComponent,
     {
         'Name': quantity_component_name,
         'ComponentType': 'NumberQuantity',
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
         'DefineName': string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 7. 定义数值的text排列方式
    (DisplayText,
     {
         'id': quantity_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 0,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 8. 数值与新加单位'ppm'对应
    (DisplayNumberQuantity,
     {
         'id': quantity_component_name,
         'QuantityType': quantity_name,
         'NumberOfDigits': 3,
         'NumberFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
         'QuantityFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
     }
     ),
    # 9. 数值与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': quantity_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read',
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 0,
     }
     ),
    # 12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId': quantity_component_name,
         'ColumnIndex': 2,
     }
     ),
]

#--------------------------- 1.1 - System 页面里新加一行label:Chemical remaining和quantity:l -------------------------------------------#
label_component_name = '1.1 SystemStatus l1 chemical remaining'
quantity_component_name = '1.1 SystemStatus l1 chemical remaining nq'
string_define = 'SID_CHEMICAL_REMAINING'
string = 'Chemical remaining'
listviewid_name = '1.1 SystemStatus List 1'
quantity_name = 'Q_FLOW'
# TODO 试验新加subjectid
subjectid = 'h2s_level_act'

chemical_remaining_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加数值label
    (DisplayComponent,
     {
         'Name': quantity_component_name,
         'ComponentType': 'NumberQuantity',
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
         'DefineName': string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 7. 定义数值的text排列方式
    (DisplayText,
     {
         'id': quantity_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 0,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 8. 数值与单位对应
    (DisplayNumberQuantity,
     {
         'id': quantity_component_name,
         'QuantityType': quantity_name,
         'NumberOfDigits': 3,
         'NumberFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
         'QuantityFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
     }
     ),
    # 9. 数值与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': quantity_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read',
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 0,
     }
     ),
    # 12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId': quantity_component_name,
         'ColumnIndex': 2,
     }
     ),
]

#--------------------------- 1.1 - System 页面里新加一行label:Chemical dosed和quantity:l -------------------------------------------#
label_component_name = '1.1 SystemStatus l1 chemical dosed'
quantity_component_name = '1.1 SystemStatus l1 chemical dosed nq'
string_define = 'SID_CHEMICAL_DOSED'
string = 'Chemical dosed'
listviewid_name = '1.1 SystemStatus List 1'
quantity_name = 'Q_FLOW'
# TODO 试验新加subjectid
subjectid = 'h2s_level_act'

chemical_dosed_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加数值label
    (DisplayComponent,
     {
         'Name': quantity_component_name,
         'ComponentType': 'NumberQuantity',
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
         'DefineName': string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 7. 定义数值的text排列方式
    (DisplayText,
     {
         'id': quantity_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 0,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 8. 数值与单位对应
    (DisplayNumberQuantity,
     {
         'id': quantity_component_name,
         'QuantityType': quantity_name,
         'NumberOfDigits': 3,
         'NumberFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
         'QuantityFontId': 'DEFAULT_FONT_13_LANGUAGE_INDEP',
     }
     ),
    # 9. 数值与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': quantity_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read',
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 0,
     }
     ),
    # 12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId': quantity_component_name,
         'ColumnIndex': 2,
     }
     ),
]

#--------------------------- 4.2 - Advanced Functions 页面里新加一行label:H2S Control，点击可以跳进另一个页面 -------------------------------------------#
component_name = '4.2 AdvancedFunc H2S Contol'
string_define = 'SID_H2S_CONTROL'
string = 'H2S Control'
listviewid_name = '4.2 AdvancedFunc List 1'

h2s_control_label_parameters = [
    # 1. 添加h2s control label
    (DisplayComponent,
     {
         'Name': component_name,
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
         'DefineName': string_define,
         'TypeId': 'Display name',
     }
     ),
    # 3. label加相应的字符串
    (Strings,
     {
         'String': string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 4. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': string_define,
     }
     ),
    # 5. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 8,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 6. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 7. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]

component_name = '4.2.14 H2S Contol Group'
string_define = 'SID_H2S_CONTROL'
h2s_control_group_parameters = [
    # 1. 添加group，也就是另起一页
    (DisplayComponent,
     {
         'Name': component_name,
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
         'id': component_name,
         'StringId': string_define,
     }
     ),
    # 3. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 8,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
]

root_group_id_name = '4.2.14 H2S Contol Group',
string_name = 'H2S Control'
display_number = '4.2.14'
h2s_control_display_parameters = [
    # Display
    (Display,
     {
         'RootGroupId': root_group_id_name,
         'DisplayNumber': display_number,
         'Name': string_name,
         #'FocusComponentId'  : 0,   #set from listview later
         'AbleToShow': True,
         'Show': False,
         'FirstWizardDisplay': False,
     }
     ),
]

listview_name = '4.2.14 H2S Contol List'
listviewid_name = '4.2.14 H2S Contol List'

h2s_control_listview_parameters = [
    # 添加Listview
    (DisplayComponent,
     {
         'Name': listview_name,
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
         'id': listview_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 8,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    (DisplayListView,
     {
         'id': listviewid_name,
         'RowHeight': 15,
         'SelectedRow': 0,
         'NextListId': 0,  # - None -
         'PrevListId': 0,  # - None -
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 0,
         'ColumnWidth': 160,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 1,
         'ColumnWidth': 64,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 2,
         'ColumnWidth': 0,
     }
     ),
]

#--------------------------- 4.2.14 - H2S Control 页面里新加一行label:Dosing pump，点击跳进4.2.14.1 Dosing pump group -------------------------------------------#
component_name = '4.2.14 Dosing pump go to setting'
label_string_define = 'SID_H2S_DOSING_PUMP_SETTING'
label_string = 'Dosing pump',
listviewid_name = '4.2.14 H2S Contol List'

h2s_dosing_pump_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': component_name,
         'ComponentType': 'Label',
         'ParentComponent': 0,
         'Visible': True,
         'ReadOnly': True,
         'x1': 0,
         'y1': 0,
         'x2': 0,
         'y2': 0,
         #'DisplayId': 0,
         'HelpString': 0,
         'Transparent': False,
     }
     ),
    # 3. 加字符串定义
    (StringDefines,
     {
         'DefineName': label_string_define,
         'TypeId': 'Display name',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 1,
         'WordWrap': False,
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]

#--------------------------- 4.2.14 - H2S Control 页面里新加一行label: go to modules installed，点击进入4.1.7 Modules installed -------------------------------------------#
component_name = '4.2.14 H2S go to modules installed'
label_string_define = 'SID_GO_TO_MODULES_INSTALLED'
listviewid_name = '4.2.14 H2S Contol List'

h2s_go_to_modules_installed_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': component_name,
         'ComponentType': 'Label',
         'ParentComponent': 0,
         'Visible': True,
         'ReadOnly': True,
         'x1': 0,
         'y1': 0,
         'x2': 0,
         'y2': 0,
         'DisplayId': 137,       # 137 | Modules installed
         'HelpString': 0,
         'Transparent': False,
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 1,
         'WordWrap': False,
     }
     ),
        # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]

#--------------------------- 新加页面4.2.14.1 - Dosing pump -------------------------------------------#
component_name = '4.2.14.1 H2S Dosing pump group'
string_define = 'SID_H2S_DOSING_PUMP_SETTING'
h2s_dosing_pump_group_parameters = [
    # 1. 添加group，也就是另起一页
    (DisplayComponent,
     {
         'Name': component_name,
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
         'id': component_name,
         'StringId': string_define,
     }
     ),
    # 3. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 8,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
]

root_group_id_name = '4.2.14.1 H2S Dosing pump group',
string_name = 'Dosing pump',
display_number = '4.2.14.1'
h2s_dosing_pump_display_parameters = [
    # Display
    (Display,
     {
         'RootGroupId': root_group_id_name,
         'DisplayNumber': display_number,
         'Name': string_name,
         #'FocusComponentId'  : 0,   #set from listview later
         'AbleToShow': True,
         'Show': False,
         'FirstWizardDisplay': False,
     }
     ),
]

listview_name = '4.2.14.1 H2S Dosing pump List'
listviewid_name = '4.2.14.1 H2S Dosing pump List'

h2s_dosing_pump_listview_parameters = [
    # 添加Listview
    (DisplayComponent,
     {
         'Name': listview_name,
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
    (DisplayListView,
     {
         'id': listviewid_name,
         'RowHeight': 15,
         'SelectedRow': 0,
         'NextListId': 0,  # - None -
         'PrevListId': 0,  # - None -
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 0,
         'ColumnWidth': 0,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 1,
         'ColumnWidth': 164,
     }
     ),
    (DisplayListViewColumns,
     {
         'ListViewId': listviewid_name,
         'ColumnIndex': 2,
         'ColumnWidth': 74,
     }
     ),
]


#--------------------------- 4.2.14.1 - Dosing pump 页面里新加一行label:Dosing pump interface -------------------------------------------#
component_name = '4.2.14.1 H2S dosing pump interface headline'
label_string_define = 'SID_DOSING_PUMP_INTERFACE'
label_string = 'Dosing pump interface',
listviewid_name = '4.2.14.1 H2S Dosing pump List'

h2s_dosing_pump_interface_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': component_name,
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
         'DefineName': label_string_define,
         'TypeId': 'Display name',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 0,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]


#--------------------------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Smart Digital DDA -------------------------------------------#
label_component_name = '4.2.14.1 Smart Digital DDA'
cb_component_name = '4.2.14.1 Smart Digital DDA cb'
label_string_define = 'SID_H2S_DOSING_PUMP_SMART_DIGITAL_DDA'
label_string = 'Smart Digital DDA',
listviewid_name = '4.2.14.1 H2S Dosing pump List'
# TODO 先用已有的subject数据pit_level_ctrl_type，是个枚举类型
subjectid = 'pit_level_ctrl_type'

h2s_dosing_pump_interface_smart_digital_dda_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加OnOffCheckBox
    (DisplayComponent,
     {
         'Name': cb_component_name,
         'ComponentType': 'ModeCheckBox',
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
         'DefineName': label_string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 4,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 1,
     }
     ),
    # 12. 在新加的item下面添加checkbox
    (DisplayListViewItemComponents,
     {
         'ComponentId': cb_component_name,
         'ColumnIndex': 2,
     }
     ),
]

h2s_dosing_pump_interface_smart_digital_dda_checkbox_parameters = [
    (DisplayModeCheckBox,
     {
         'id': cb_component_name,
         'CheckState': 0,
     }
     ),
    # checkbox与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': cb_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read/Write',
     }
     ),
]

#--------------------------- 4.2.14.1 - Dosing pump 页面里新加一行label和checkbox: 4.2.14.1 Analog dosing pump -------------------------------------------#
label_component_name = '4.2.14.1 Analog dosing pump'
cb_component_name = '4.2.14.1 Analog dosing pump cb'
label_string_define = 'SID_H2S_DOSING_PUMP_ANALOG'
label_string = 'Analog dosing pump',
listviewid_name = '4.2.14.1 H2S Dosing pump List'
# TODO 先用已有的subject数据pit_level_ctrl_type，是个枚举类型
subjectid = 'pit_level_ctrl_type'

h2s_dosing_pump_interface_analog_dosing_pump_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加OnOffCheckBox
    (DisplayComponent,
     {
         'Name': cb_component_name,
         'ComponentType': 'ModeCheckBox',
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
         'DefineName': label_string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 4,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 1,
     }
     ),
    # 12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId': cb_component_name,
         'ColumnIndex': 2,
     }
     ),
]

h2s_dosing_pump_interface_analog_dosing_pump_checkbox_parameters = [
    (DisplayModeCheckBox,
     {
         'id': cb_component_name,
         'CheckState': 1,
     }
     ),
    # checkbox与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': cb_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read/Write',
     }
     ),
]

#--------------------------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to settting of Analog outputs，点击进入4.4.3 Analog outputs -------------------------------------------#
component_name = '4.2.14.1 Dosing pump go to AO'
label_string_define = 'SID_GO_TO_SETTING_OF_ANALOGUE_OUTPUTS'
listviewid_name = '4.2.14.1 H2S Dosing pump List'

h2s_dosing_pump_go_to_ao_space_parameters = [
    # 为了美观，需要在listview下加一行空格
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
]

h2s_dosing_pump_go_to_ao_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': component_name,
         'ComponentType': 'Label',
         'ParentComponent': 0,
         'Visible': True,
         'ReadOnly': True,
         'x1': 0,
         'y1': 0,
         'x2': 0,
         'y2': 0,
         'DisplayId': 143,       # 143 | Analog outputs
         'HelpString': 0,
         'Transparent': False,
     }
     ),
    # 2. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': label_string_define,
     }
     ),
    # 3. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 1,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 4. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 5. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]

#--------------------------- 4.2.14.1 - Dosing pump 页面里新加一行label: Go to settting of Digital outputs，点击进入4.4.4 Digital outputs -------------------------------------------#
component_name = '4.2.14.1 Dosing pump go to DO'
label_string_define = 'SID_GO_TO_SETTING_OF_DIGITAL_OUTPUTS'
listviewid_name = '4.2.14.1 H2S Dosing pump List'

h2s_dosing_pump_go_to_do_space_parameters = [
    # 为了美观，需要在listview下加一行空格
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
]

h2s_dosing_pump_go_to_do_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': component_name,
         'ComponentType': 'Label',
         'ParentComponent': 0,
         'Visible': True,
         'ReadOnly': True,
         'x1': 0,
         'y1': 0,
         'x2': 0,
         'y2': 0,
         'DisplayId': 35,       # 35 | Digital outputs
         'HelpString': 0,
         'Transparent': False,
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 1,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
        # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': component_name,
         'ColumnIndex': 0,
     }
     ),
]

#--------------------------- 4.1.7 - Modules installed 页面里新加一行label和checkbox -------------------------------------------#
label_component_name = '4.1.7 pumpModules dosing pump'
cb_component_name = '4.1.7 pumpModules dosing pump cb'
label_string_define = 'SID_H2S_DOSING_PUMP_INSTALLED'
label_string = 'Dosing pump installed',
listviewid_name = '4.1.7 pumpModules List'
# TODO 先用已有的subject数据io111_pump_1_installed
subjectid = 'io111_pump_1_installed'

h2s_dosing_pump_installed_space_parameters = [
    # 为了美观，需要在listview下加一行空格
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
]

h2s_dosing_pump_installed_label_parameters = [
    # 1. 添加label
    (DisplayComponent,
     {
         'Name': label_component_name,
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
    # 2. 添加OnOffCheckBox
    (DisplayComponent,
     {
         'Name': cb_component_name,
         'ComponentType': 'OnOffCheckBox',
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
         'DefineName': label_string_define,
         'TypeId': 'Value type',
     }
     ),
    # 4. label加相应的字符串
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'DEV_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    (Strings,
     {
         'String': label_string,
         'LanguageId': 'UK_LANGUAGE',
         'Status': 'UnEdit',
     }
     ),
    # 5. 将字符串和label对应起来
    (DisplayLabel,
     {
         'id': label_component_name,
         'StringId': label_string_define,
     }
     ),
    # 6. 定义label的text排列方式
    (DisplayText,
     {
         'id': label_component_name,
         'Align': 'VCENTER_LEFT',
         'FontId': 'DEFAULT_FONT_13_LANGUAGE_DEP',
         'LeftMargin': 2,
         'RightMargin': 0,
         'WordWrap': False,
     }
     ),
    # 10. 在对应的listview下面新加一个item
    (DisplayListViewItem,
     {
         'ListViewId': listviewid_name,
     }
     ),
    # 11. 在新加的item下面添加label
    (DisplayListViewItemComponents,
     {
         'ComponentId': label_component_name,
         'ColumnIndex': 0,
     }
     ),
    # 12. 在新加的item下面添加数值
    (DisplayListViewItemComponents,
     {
         'ComponentId': cb_component_name,
         'ColumnIndex': 1,
     }
     ),
]

h2s_dosing_pump_installed_checkbox_parameters = [
    (DisplayOnOffCheckBox,
     {
         'id': cb_component_name,
         'OnValue': 1,
         'OffValue': 0,
     }
     ),
    # checkbox与subject对应
    (DisplayObserverSingleSubject,
     {
         'id': cb_component_name,
         'SubjectId': subjectid,
         'SubjectAccess': 'Read/Write',
     }
     ),
]

#############################################################Factor部分##########################################################
#--------------------------- 加Observer: DDACtrl -------------------------------------------#
observer_name = 'dosing_pump_ctrl'
observer_type = 'DDACtrl'
short_name = 'DDA'
h2s_observer_parameters = [
    # 1. 加ObserverType
    (ObserverType,
     {
         'Name': observer_type,
         'ShortName': short_name,
         'IsSingleton': False,
         'IsSubject': False,
     }
     ),
    # 2. 加Observer
    (Observer,
     {
         'Name': observer_name,
         #'TypeId'          : 96,      #set from ObserverType
         'TaskId': 'LowPrioPeriodicTask',
         #'TaskOrder'       : None,
         #'SubjectId'       : None,
         #'ConstructorArgs' : None,
     }
     ),
]

#--------------------------- 加Subject: dda_control_enabled -------------------------------------------#
subject_name =  'dda_control_enabled'
observer_name = 'dosing_pump_ctrl'
observer_type = 'DDACtrl'
h2s_subject_parameters = [
    # 1. 加Subject
    (Subject,
     {
         'Name': subject_name,
         'TypeId': 'BoolDataPoint',
         'GeniAppIf': False,
         'Save': 'Value',
         'FlashBlock': 'Config',
         'Verified': False,
     }
     ),
    # 2. 对应的DataPoint也要添加
    (BoolDataPoint,
     {
         'id': subject_name,
         'Value': 0,
     }
     ),
]

h2s_observer_subject_parameters = [
    # 1. 先添加SubjectRelation
    (SubjectRelation,
     {
         'Name':subject_name.upper(),  # 必须用大写字母
         'ObserverTypeId': observer_type,
     }
     ),
    # 2. 再添加ObserverSubjects，会用到SubjectRelation添加的Name
    (ObserverSubjects,
     {
         'SubjectId': subject_name,
         'ObserverId': observer_name,
         'ObserverTypeId': observer_type,
         'SubjectRelationId': subject_name.upper(),
         'SubjectAccess': 'Read',
     }
     ),
]
# 用到的SubjectPtr名字SP_DDA_DDA_CONTROL_ENABLED
SP = 'SP_' + short_name + '_' + subject_name.upper()

#--------------------------- 加Subject: h2s_level_act -------------------------------------------#
subject_name = 'h2s_level_act'
quantity_type = 'Q_FLOW'
observer_name = 'dosing_pump_ctrl'
observer_type = 'DDACtrl'
h2s_level_act_subject_parameters = [
    # 1. 加Subject
    (Subject,
     {
         'Name': subject_name,
         'TypeId': 'IntDataPoint',
         'GeniAppIf': True,
         'Save': '-',
         'FlashBlock': '-',
         'Verified': False,
     }
     ),
    # 2. 对应的DataPoint也要添加
    (IntDataPoint,
     {
         'id': subject_name,
         'Value': '0',
         'Type': 'U32',
         'Min': '0',
         'Max': '99999999',
         'QuantityType': quantity_type,
         'Verified': False,
     }
     ),
]

h2s_level_act_observer_subject_parameters = [
    # 1. 先添加SubjectRelation
    (SubjectRelation,
     {
         'Name': subject_name.upper(),  # 必须用大写字母
         'ObserverTypeId': observer_type,
     }
     ),
    # 2. 再添加ObserverSubjects，会用到SubjectRelation添加的Name
    (ObserverSubjects,
     {
         'SubjectId': subject_name,
         'ObserverId': observer_name,
         'ObserverTypeId': observer_type,
         'SubjectRelationId': subject_name.upper(),
         'SubjectAccess': 'Read',
     }
     ),
]

geni_var_name = 'h2s_level'
geni_class = 14
geni_id = 190
subject_name = 'h2s_level_act'
geni_convert_id = 'Dim. less with NA'

h2s_level_act_geni_if_parameters = [
    (GeniAppIf,
     {
         'GeniVarName': geni_var_name,
         'GeniClass': geni_class,
         'GeniId': geni_id,
         'SubjectId': subject_name,
         'GeniConvertId': geni_convert_id,
         'AutoGenerate': True,
         'Comment': 'h2s level actual',
     }
     ),
]
