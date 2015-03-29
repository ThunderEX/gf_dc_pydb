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

    # different attributes according to different subject type
    #: BoolDataPoint, if subject_type_id=BoolDataPoint
    bool_value = 0                          #: 0 or 1
    #IntDataPoint, if subject_type_id=IntDataPoint
    int_value = '0'                         #: set value
    int_type = 'U32'                        #: int data type, 'I16', 'I32', 'U16', 'U32', 'U8'
    int_min = '0'                           #: minimum value
    int_max = '99999999'                    #: maximum value
    int_quantity_type = 'Q_NO_UNIT'         #: quantity type for this int data
    int_verified = False                    #: verified

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
                 'ObserverTypeId': self.observer_type,
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
