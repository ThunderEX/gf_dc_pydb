# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class NewSubject(object):

    ''' Add new subject and handle the relation with observer '''

    #below attributes need to be defined first
    subject_name = ''             #new subject name
    subject_type_id = ''          #which subject type to use
    geni_app_if = False
    subject_save = '-'
    flash_block = '-'
    verified = False
    observer_name = ''            #the corresponding observer name
    observer_type = ''            #the corresponding observer type
    subject_relation_name = ''
    subject_access = 'Read'

    #below attributes are for geni if geni_app_if is True
    geni_var_name = ''
    geni_class = 0
    geni_id = 0
    geni_convert_id = 'Dim. less with NA'
    auto_generate = True

    #different attributes according to different subject type
    #BoolDataPoint
    bool_value = 0
    #IntDataPoint
    int_value = '0'
    int_type = 'U32'
    int_min = '0'
    int_max = '99999999'
    int_quantity_type = 'Q_NO_UNIT'
    int_verified = False

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
