# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from subject import NewSubject

class NewAlarm(object):

    ''' Add new alarm '''

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
    alarm_erroneous_unit_type_id = 0
    alarm_erroneous_unit_number = 0
    #alarm_alarm_id = ''                           #: SID_ALARM_XXXX

    #Alarm
    alarm_define_name = ''
    alarm_id = 0


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


        self.alarm_subject.subject_name                                  = self.alarm_subject_name
        self.alarm_subject.subject_type_id                               = self.alarm_subject_type_id
        self.alarm_subject.geni_app_if                                   = self.alarm_geni_app_if
        self.alarm_subject.subject_save                                  = self.alarm_subject_save
        self.alarm_subject.flash_block                                   = self.alarm_flash_block
        self.alarm_subject.verified                                      = self.alarm_verified
        self.alarm_subject.observer_name                                 = self.alarm_observer_name
        self.alarm_subject.observer_type                                 = self.alarm_observer_type
        self.alarm_subject.subject_relation_name                         = self.alarm_subject_relation_name
        self.alarm_subject.subject_access                                = self.alarm_subject_access
        self.alarm_subject.geni_var_name                                 = self.alarm_geni_var_name
        self.alarm_subject.geni_class                                    = self.alarm_geni_class
        self.alarm_subject.geni_id                                       = self.alarm_geni_id
        self.alarm_subject.geni_convert_id                               = self.alarm_geni_convert_id
        self.alarm_subject.auto_generate                                 = self.alarm_auto_generate

        self.alarm_subject.alarm_alarm_config_id        = self.alarm_alarm_config_id
        self.alarm_subject.alarm_alarm_config2_id       = self.alarm_alarm_config2_id
        self.alarm_subject.alarm_erroneous_unit_type_id = self.alarm_erroneous_unit_type_id
        self.alarm_subject.alarm_erroneous_unit_number  = self.alarm_erroneous_unit_number
        self.alarm_subject.alarm_alarm_id               = self.alarm_define_name

        self.parameters = []
        if self.alarm_id:
            self.parameters.append(
                (DisplayAlarmStrings,
                 {
                     'AlarmId': self.alarm_id,
                     'StringId': self.alarm_define_name,
                 }
                 ),
            )

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
        self.alarm_config_subject.save()
        self.alarm_subject.save()
        return rtn
