# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Base

class NewSubject(Base):

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
    geni_comment = ''

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

    #FloatDataPoint
    float_value = 0                         #: set value
    float_min = 0                           #: minimum value
    float_max = 99999999                    #: maximum value
    float_quantity_type = 'Q_NO_UNIT'       #: quantity type for this float data

    #VectorDataPoint
    vector_type = ''
    vector_initial_size = 0
    vector_max_size = 0
    vector_default_value = '-1'

    #EnumDataPoint
    enum_type_name = ''
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
        elif self.subject_type_id == 'FloatDataPoint':
            self.parameters.append(
                (FloatDataPoint,
                 {
                     'id': self.subject_name,
                     'Value': self.float_value,
                     'Min': self.float_min,
                     'Max': self.float_max,
                     'QuantityType': self.float_quantity_type,
                 }
                 ),
            )
        elif self.subject_type_id == 'VectorDataPoint':
            self.parameters.append(
                (VectorDataPoint,
                 {
                     'id': self.subject_name,
                     'Type': self.vector_type,
                     'InitialSize': self.vector_initial_size,
                     'MaxSize': self.vector_max_size,
                     'DefaultValue': self.vector_default_value,
                 }
                 ),
            )
        elif self.subject_type_id == 'EnumDataPoint':
            self.parameters.extend(
                [(EnumDataPoint,
                 {
                     'id': self.subject_name,
                     'EnumTypeName': self.enum_type_name.upper(),
                     'Value': self.enum_value.upper(),
                 }
                 ),
                (EnumTypes,
                 {
                     'Name': self.enum_type_name,
                 }
                 ),]
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

        #只有在有Relation时才添加这两张表，有些DataPoint用不到，比如AlarmConfig
        if len(self.subject_relation_name):
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
                     'Comment': self.geni_comment,
                 }
                 ),
            )
