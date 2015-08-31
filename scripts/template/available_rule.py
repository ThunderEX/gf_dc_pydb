# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class AvailableRule(Base):

    ''' Add new available rule '''

    available_rule_name = ''                #: set available rule for this label
    available_rule_type = 'AvalibleIfSet'   #: available rule type
    available_rule_checkstate = 0           #: available rule is set if checkstate equal this value
    available_rule_subject_id = ''          #: corresponding subject (checkbox), link the subject to available rule

    def update_parameters(self):
        self.parameters = [
            # 1. 添加rule
            (DisplayComponent,
             {
                 'Name': self.available_rule_name,
                 'ComponentType': self.available_rule_type,
                 'ParentComponent': 0,
                 'Visible': False,
                 'ReadOnly': True,
                 'x1': 0,
                 'y1': 0,
                 'x2': 0,
                 'y2': 0,
                 'DisplayId' : 0,
                 'HelpString': 0,
                 'Transparent': False,
             }
             ),
            (DisplayAvailable,
             {
                 'id': self.available_rule_name,
                 'CheckState': self.available_rule_checkstate,
             }
             ),
            (DisplayObserverSingleSubject,
             {
                 'id': self.available_rule_name,
                 'SubjectId': self.available_rule_subject_id,
                 'SubjectAccess': 'Read',
             }
             ),
        ]
