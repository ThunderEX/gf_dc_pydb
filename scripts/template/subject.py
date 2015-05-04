# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class NewSubject(object):

    ''' Add new subject and handle the relation with observer '''

    #below attributes need to be defined first
    subject_name = ''                       #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    subject_type_id = ''                    #: which subject type to use, IntDataPoint, BoolDataPoint or something else.
    geni_app_if = False                     #: True - geni interface, False - not geni interface.
    subject_save = '-'                      #: '-', 'All', 'Value'.
    flash_block = '-'                       #: '-', 'Config', 'Log', 'GSC', 'No boot', 'Log series 1', 'Log series 2', 'Log series 3', 'Log series 4', 'Log series 5'.
    verified = False                        #: verified.
    observer_name = ''                      #: the corresponding observer name.
    observer_type = ''                      #: the corresponding observer type.
    subject_relation_name = ''              #: subject relation name, must be all capitalized.
    subject_access = 'Read'                 #: 'Not decided', 'Write', 'Read', 'Read/Write'

    # below attributes are for geni if geni_app_if is True
    geni_var_name = ''                      #: geni variable name
    geni_class = 0                          #: geni class
    geni_id = 0                             #: geni id
    geni_convert_id = 'Dim. less with NA'   #: geni convert id, defined in GeniConvert table
    auto_generate = True                    #: auto generate geni data for this subject

    ''' different attributes according to different subject type '''

    #: BoolDataPoint
    bool_value = 0                          #: 0 or 1

    #IntDataPoint
    int_value = '0'                         #: set value
    int_type = 'U32'                        #: int data type, 'I16', 'I32', 'U16', 'U32', 'U8'
    int_min = '0'                           #: minimum value
    int_max = '99999999'                    #: maximum value
    int_quantity_type = 'Q_NO_UNIT'         #: quantity type for this int data
    int_verified = False                    #: verified

    #EnumDataPoint
    enum_enum_type_name = ''
    enum_value = ''

    #AlarmConfig
    alarm_config_sms_1_enabled = False
    alarm_config_sms_2_enabled = False
    alarm_config_sms_3_enabled = False
    alarm_config_scada_enabled = False
    alarm_config_custom_relay_for_alarm_enabled = False
    alarm_config_custom_relay_for_warning_enabled = False
    alarm_config_alarm_enabled = False
    alarm_config_warning_enabled = False
    alarm_config_auto_ack = False
    alarm_config_alarm_delay = 1
    alarm_config_alarm_type = 'BoolDataPoint'
    alarm_config_alarm_criteria = '='
    alarm_config_alarm_limit = 1
    alarm_config_warning_limit = 1
    alarm_config_min_limit = 0
    alarm_config_max_limit = 1
    alarm_config_quantity_type_id = 'Q_NO_UNIT'
    alarm_config_verified = False

    #AlarmDataPoint
    alarm_alarm_config_id = ''
    alarm_alarm_config2_id = 'dummy_alarm_conf'
    alarm_erroneous_unit_type_id = 0
    alarm_erroneous_unit_number = 0
    alarm_alarm_id = ''                         #: SID_ALARM_XXXX

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
            # 1. 加Subject
            (Subject,
             {
                 'Name': self.subject_name,
                 'TypeId': self.subject_type_id,
                 'GeniAppIf': self.geni_app_if,
                 'Save': self.subject_save,
                 'FlashBlock': self.flash_block,
                 'Verified': self.verified,
             }
             ),
        ]
        if self.subject_type_id == 'BoolDataPoint':
            self.parameters.append(
                (BoolDataPoint,
                 {
                     'id': self.subject_name,
                     'Value': self.bool_value,
                 }
                 ),
            )
        elif self.subject_type_id == 'IntDataPoint':
            self.parameters.append(
                (IntDataPoint,
                 {
                     'id': self.subject_name,
                     'Value': self.int_value,
                     'Type': self.int_type,
                     'Min': self.int_min,
                     'Max': self.int_max,
                     'QuantityType': self.int_quantity_type,
                     'Verified': self.int_verified,
                 }
                 ),
            )
        elif self.subject_type_id == 'EnumDataPoint':
            self.parameters.append(
                (EnumDataPoint,
                 {
                     'id': self.subject_name,
                     'EnumTypeName': self.enum_enum_type_name.upper(),
                     'Value': self.enum_value.upper(),
                 }
                 ),
            )
        elif self.subject_type_id == 'AlarmConfig':
            self.parameters.append(
                (AlarmConfig,
                 {
                     'AlarmConfigId'                : self.subject_name,
                     'Sms1Enabled'                  : self.alarm_config_sms_1_enabled,
                     'Sms2Enabled'                  : self.alarm_config_sms_2_enabled,
                     'Sms3Enabled'                  : self.alarm_config_sms_3_enabled,
                     'ScadaEnabled'                 : self.alarm_config_scada_enabled,
                     'CustomRelayForAlarmEnabled'   : self.alarm_config_custom_relay_for_alarm_enabled,
                     'CustomRelayForWarningEnabled' : self.alarm_config_custom_relay_for_warning_enabled,
                     'AlarmEnabled'                 : self.alarm_config_alarm_enabled,
                     'WarningEnabled'               : self.alarm_config_warning_enabled,
                     'AutoAck'                      : self.alarm_config_auto_ack,
                     'AlarmDelay'                   : self.alarm_config_alarm_delay,
                     'AlarmType'                    : self.alarm_config_alarm_type,
                     'AlarmCriteria'                : self.alarm_config_alarm_criteria,
                     'AlarmLimit'                   : self.alarm_config_alarm_limit,
                     'WarningLimit'                 : self.alarm_config_warning_limit,
                     'MinLimit'                     : self.alarm_config_min_limit,
                     'MaxLimit'                     : self.alarm_config_max_limit,
                     'QuantityTypeId'               : self.alarm_config_quantity_type_id,
                     'Verified'                     : self.alarm_config_verified,
                 }
                 ),
            )
        elif self.subject_type_id == 'AlarmDataPoint':
            self.parameters.append(
                (AlarmDataPoint,
                 {
                     'id'                  : self.subject_name,
                     'AlarmConfigId'       : self.alarm_alarm_config_id,
                     'AlarmConfig2Id'      : self.alarm_alarm_config2_id,
                     'ErroneousUnitTypeId' : self.alarm_erroneous_unit_type_id,
                     'ErroneousUnitNumber' : self.alarm_erroneous_unit_number,
                     'AlarmId'             : self.alarm_alarm_id,
                 }
                 ),
            )
        else:
            comment('Not supported datapoint type')
            raise NameError

        # 添加SubjectRelation
        self.parameters.append(
            (SubjectRelation,
             {
                 'Name': self.subject_relation_name.upper(),  # 必须用大写字母
                 'ObserverTypeId': self.observer_type,
             }
             ),
        )
        # 添加ObserverSubjects，会用到SubjectRelation添加的Name
        self.parameters.append(
            (ObserverSubjects,
             {
                 'SubjectId': self.subject_name,
                 'ObserverId': self.observer_name,
                 'SubjectRelationId': self.subject_relation_name.upper(),
                 'SubjectAccess': self.subject_access,
             }
             )
        )

        #Geni
        if self.geni_app_if:
            self.parameters.append(
                (GeniAppIf,
                 {
                     'GeniVarName': self.geni_var_name,
                     'GeniClass': self.geni_class,
                     'GeniId': self.geni_id,
                     'SubjectId': self.subject_name,
                     'GeniConvertId': self.geni_convert_id,
                     'AutoGenerate': self.auto_generate,
                     #'Comment': self.geni_comment,
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
        #SP = 'SP_' + self.short_name + '_' + self.subject_name.upper()
        #comment('Use %s in application' %(SP))
        return rtn
