# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from subject import NewSubject

class NewEnumData(object):

    ''' Add new enum data '''

    #AlarmConfig
    enum_subject_names          = []            #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    enum_subject_type_id       = 'EnumDataPoint'            #: which subject type to use, IntDataPoint, BoolDataPoint or something else.
    enum_geni_app_if           = False         #: True - geni interface, False - not geni interface.
    enum_subject_save          = '-'           #: '-', 'All', 'Value'.
    enum_flash_block           = '-'           #: '-', 'Config', 'Log', 'GSC', 'No boot', 'Log series 1', 'Log series 2', 'Log series 3', 'Log series 4', 'Log series 5'.
    enum_verified              = False         #: verified.
    enum_observer_name         = ''            #: the corresponding observer name.
    enum_observer_type         = ''            #: the corresponding observer type.
    enum_subject_relation_names = []            #: subject relation name, must be all capitalized.
    enum_subject_access        = 'Read'        #: 'Not decided', 'Write', 'Read', 'Read/Write'

    # below attributes are for geni if geni_app_if is True
    enum_geni_var_name   = ''                  #: geni variable name
    enum_geni_class      = 0                   #: geni class
    enum_geni_id         = 0                   #: geni id
    enum_geni_convert_id = 'Dim. less with NA' #: geni convert id, defined in GeniConvert table
    enum_auto_generate   = True                #: auto generate geni data for this subject

    enum_type_name = ''
    enum_values = []

    def __init__(self):
        self.parameters = []
        self.enum_subjects = []
        self.description = 'No description'

    def update_parameters(self):
        for i in range(len(self.enum_subject_names)):
            enum_subject = NewSubject()
            enum_subject.subject_name           = self.enum_subject_names[i]
            enum_subject.subject_type_id        = self.enum_subject_type_id
            enum_subject.geni_app_if            = self.enum_geni_app_if
            enum_subject.subject_save           = self.enum_subject_save
            enum_subject.flash_block            = self.enum_flash_block
            enum_subject.verified               = self.enum_verified
            enum_subject.observer_name          = self.enum_observer_name
            enum_subject.observer_type          = self.enum_observer_type
            enum_subject.subject_relation_name  = self.enum_subject_relation_names[i]
            enum_subject.subject_access         = self.enum_subject_access
            enum_subject.geni_var_name          = self.enum_geni_var_name
            enum_subject.geni_class             = self.enum_geni_class
            enum_subject.geni_id                = self.enum_geni_id
            enum_subject.geni_convert_id        = self.enum_geni_convert_id
            enum_subject.auto_generate          = self.enum_auto_generate

            enum_subject.enum_enum_type_name    = self.enum_type_name
            enum_subject.enum_value             = self.enum_values[i]

            self.enum_subjects.append(enum_subject)

        self.parameters = [
            (EnumTypes,
             {
                 'Name': self.enum_type_name,
             }
             ),
        ]

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
        for subject in self.enum_subjects:
            subject.save()
        return rtn
