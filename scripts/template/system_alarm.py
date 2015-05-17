# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from subject import NewSubject

class SystemAlarm(object):

    ''' Add new system alarm in 4.5.1 - System alarms '''

    label_name = ''                                 # : new label name that added in DisplayComponent.
    label_define_name = ''                          # : string define for new label.
    label_string = ''                               # : string for new label, multiple languages
    slippoint_name = ''                             # : system alarm is pair of label and slippoint
    subject_id = 'display_configalarm_slippoint_no' # : link subject and slippoint
    write_state = 0                                 # : write state can help render to new alarm config page, the value should equal the new enum value defined in ALARM_CONFIG_TYPE in AppTypeDefs.h
    listview_id = '4.5.1 SystemAlarms List'         # : listview id which will include the new label and slippoint

    #AlarmConfig
    alarm_config_subject_name          = ''            #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    alarm_config_subject_type_id       = ''            #: which subject type to use, IntDataPoint, BoolDataPoint or something else.
    alarm_config_geni_app_if           = False         #: True - geni interface, False - not geni interface.
    alarm_config_subject_save          = '-'           #: '-', 'All', 'Value'.
    alarm_config_flash_block           = '-'           #: '-', 'Config', 'Log', 'GSC', 'No boot', 'Log series 1', 'Log series 2', 'Log series 3', 'Log series 4', 'Log series 5'.
    alarm_config_verified              = False         #: verified.
    alarm_config_observer_name         = ''            #: the corresponding observer name.
    alarm_config_observer_type         = ''            #: the corresponding observer type.
    alarm_config_subject_relation_name = ''            #: subject relation name, must be all capitalized.
    alarm_config_subject_access        = 'Read'        #: 'Not decided', 'Write', 'Read', 'Read/Write'

    # below attributes are for geni if geni_app_if is True
    alarm_config_geni_var_name   = ''                  #: geni variable name
    alarm_config_geni_class      = 0                   #: geni class
    alarm_config_geni_id         = 0                   #: geni id
    alarm_config_geni_convert_id = 'Dim. less with NA' #: geni convert id, defined in GeniConvert table
    alarm_config_auto_generate   = True                #: auto generate geni data for this subject

    alarm_config_sms_1_enabled                    = False
    alarm_config_sms_2_enabled                    = False
    alarm_config_sms_3_enabled                    = False
    alarm_config_scada_enabled                    = False
    alarm_config_custom_relay_for_alarm_enabled   = False
    alarm_config_custom_relay_for_warning_enabled = False
    alarm_config_alarm_enabled                    = False
    alarm_config_warning_enabled                  = False
    alarm_config_auto_ack                         = False
    alarm_config_alarm_delay                      = 1
    alarm_config_alarm_type                       = 'BoolDataPoint'
    alarm_config_alarm_criteria                   = '='
    alarm_config_alarm_limit                      = 1
    alarm_config_warning_limit                    = 1
    alarm_config_min_limit                        = 0
    alarm_config_max_limit                        = 1
    alarm_config_quantity_type_id                 = 'Q_NO_UNIT'
    alarm_config_verified                         = False

    #AlarmDataPoint
    alarm_subject_name              = ''          #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    alarm_subject_type_id           = ''          #: which subject type to use, IntDataPoint, BoolDataPoint or something else.
    alarm_geni_app_if               = False       #: True - geni interface, False - not geni interface.
    alarm_subject_save              = '-'         #: '-', 'All', 'Value'.
    alarm_flash_block               = '-'         #: '-', 'Config', 'Log', 'GSC', 'No boot', 'Log series 1', 'Log series 2', 'Log series 3', 'Log series 4', 'Log series 5'.
    alarm_verified                  = False       #: verified.
    alarm_observer_name             = ''          #: the corresponding observer name.
    alarm_observer_type             = ''          #: the corresponding observer type.
    alarm_subject_relation_name     = ''          #: subject relation name, must be all capitalized.
    alarm_subject_access            = 'Read'      #: 'Not decided', 'Write', 'Read', 'Read/Write'

    # below attributes are for geni if geni_app_if is True
    alarm_geni_var_name   = ''                    #: geni variable name
    alarm_geni_class      = 0                     #: geni class
    alarm_geni_id         = 0                     #: geni id
    alarm_geni_convert_id = 'Dim. less with NA'   #: geni convert id, defined in GeniConvert table
    alarm_auto_generate   = True                  #: auto generate geni data for this subject

    alarm_alarm_config_id = ''
    alarm_alarm_config2_id = ''
    alarm_erroneous_unit_type_id = 0              #: error type, defined in ErroneousUnitType table, 0 = system
    alarm_erroneous_unit_number = 0               #: error title string, defined in DisplayUnitStrings table
    alarm_alarm_id = ''                           #: SID_ALARM_XXXX

    def __init__(self):
        self.parameters = []
        self.alarm_config_subject = NewSubject()
        self.alarm_subject = NewSubject()
        self.description = 'No description'

    def update_parameters(self):
        self.alarm_config_subject.subject_name                                  = self.alarm_config_subject_name
        self.alarm_config_subject.subject_type_id                               = self.alarm_config_subject_type_id
        self.alarm_config_subject.geni_app_if                                   = self.alarm_config_geni_app_if
        self.alarm_config_subject.subject_save                                  = self.alarm_config_subject_save
        self.alarm_config_subject.flash_block                                   = self.alarm_config_flash_block
        self.alarm_config_subject.verified                                      = self.alarm_config_verified
        self.alarm_config_subject.observer_name                                 = self.alarm_config_observer_name
        self.alarm_config_subject.observer_type                                 = self.alarm_config_observer_type
        self.alarm_config_subject.subject_relation_name                         = self.alarm_config_subject_relation_name
        self.alarm_config_subject.subject_access                                = self.alarm_config_subject_access
        self.alarm_config_subject.geni_var_name                                 = self.alarm_config_geni_var_name
        self.alarm_config_subject.geni_class                                    = self.alarm_config_geni_class
        self.alarm_config_subject.geni_id                                       = self.alarm_config_geni_id
        self.alarm_config_subject.geni_convert_id                               = self.alarm_config_geni_convert_id
        self.alarm_config_subject.auto_generate                                 = self.alarm_config_auto_generate

        self.alarm_config_subject.alarm_config_sms_1_enabled                    = self.alarm_config_sms_1_enabled
        self.alarm_config_subject.alarm_config_sms_2_enabled                    = self.alarm_config_sms_2_enabled
        self.alarm_config_subject.alarm_config_sms_3_enabled                    = self.alarm_config_sms_3_enabled
        self.alarm_config_subject.alarm_config_scada_enabled                    = self.alarm_config_scada_enabled
        self.alarm_config_subject.alarm_config_custom_relay_for_alarm_enabled   = self.alarm_config_custom_relay_for_alarm_enabled
        self.alarm_config_subject.alarm_config_custom_relay_for_warning_enabled = self.alarm_config_custom_relay_for_warning_enabled
        self.alarm_config_subject.alarm_config_alarm_enabled                    = self.alarm_config_alarm_enabled
        self.alarm_config_subject.alarm_config_warning_enabled                  = self.alarm_config_warning_enabled
        self.alarm_config_subject.alarm_config_auto_ack                         = self.alarm_config_auto_ack
        self.alarm_config_subject.alarm_config_alarm_delay                      = self.alarm_config_alarm_delay
        self.alarm_config_subject.alarm_config_alarm_type                       = self.alarm_config_alarm_type
        self.alarm_config_subject.alarm_config_alarm_criteria                   = self.alarm_config_alarm_criteria
        self.alarm_config_subject.alarm_config_alarm_limit                      = self.alarm_config_alarm_limit
        self.alarm_config_subject.alarm_config_warning_limit                    = self.alarm_config_warning_limit
        self.alarm_config_subject.alarm_config_min_limit                        = self.alarm_config_min_limit
        self.alarm_config_subject.alarm_config_max_limit                        = self.alarm_config_max_limit
        self.alarm_config_subject.alarm_config_quantity_type_id                 = self.alarm_config_quantity_type_id
        self.alarm_config_subject.alarm_config_verified                         = self.alarm_config_verified


        self.alarm_subject.subject_name                 = self.alarm_subject_name
        self.alarm_subject.subject_type_id              = self.alarm_subject_type_id
        self.alarm_subject.geni_app_if                  = self.alarm_geni_app_if
        self.alarm_subject.subject_save                 = self.alarm_subject_save
        self.alarm_subject.flash_block                  = self.alarm_flash_block
        self.alarm_subject.verified                     = self.alarm_verified
        self.alarm_subject.observer_name                = self.alarm_observer_name
        self.alarm_subject.observer_type                = self.alarm_observer_type
        self.alarm_subject.subject_relation_name        = self.alarm_subject_relation_name
        self.alarm_subject.subject_access               = self.alarm_subject_access
        self.alarm_subject.geni_var_name                = self.alarm_geni_var_name
        self.alarm_subject.geni_class                   = self.alarm_geni_class
        self.alarm_subject.geni_id                      = self.alarm_geni_id
        self.alarm_subject.geni_convert_id              = self.alarm_geni_convert_id
        self.alarm_subject.auto_generate                = self.alarm_auto_generate

        self.alarm_subject.alarm_alarm_config_id        = self.alarm_alarm_config_id
        self.alarm_subject.alarm_alarm_config2_id       = self.alarm_alarm_config2_id
        self.alarm_subject.alarm_erroneous_unit_type_id = self.alarm_erroneous_unit_type_id
        self.alarm_subject.alarm_erroneous_unit_number  = self.alarm_erroneous_unit_number
        self.alarm_subject.alarm_alarm_id               = self.alarm_alarm_id

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
                 'HelpString': 'SID_HELP_4_5_1_LINE_5',
                 'Transparent': False,
             }
             ),
            # 2. 添加slippoint
            (DisplayComponent,
             {
                 'Name': self.slippoint_name,
                 'ComponentType': 'WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay',
                 'ParentComponent': 0,
                 'Visible': False,
                 'ReadOnly': False,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId': 67,           #Digital outputs
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
            (DisplayAlarmStrings,
             {
                 'StringId': self.alarm_alarm_id,
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
            # 9. slippoint与subject对应
            (DisplayObserverSingleSubject,
             {
                 'id': self.slippoint_name,
                 'SubjectId': self.subject_id,         #fixed to display_configalarm_slippoint_no
                 'SubjectAccess': 'Write',
             }
             ),
            # 10. 在对应的listview下面新加一个item
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
            # 11. 在新加的item下面添加label
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.label_name,
                 'ColumnIndex': 0,
             }
             ),
             # 12. 在新加的item下面添加slippoint
            (DisplayListViewItemComponents,
             {
                 'ComponentId': self.slippoint_name,
                 'ColumnIndex': 1,
             }
             ),
            # 13. 在WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay表里添加WriteState
            # TODO 用正则找出同样是'4.5.1 SystemAlarms'的最大WriteState
            (WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay,
             {
                 'id': self.slippoint_name,
                 'WriteState': self.write_state,
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
        self.alarm_config_subject.save()
        self.alarm_subject.save()
