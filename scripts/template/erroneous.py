# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class Erroneous(Base):

    ''' Add new erroneous unit type '''

    id = 0                 #: id is not auto increase, need to define 
    name = ''              #: name for the new erroneous unit type
    string_id = ''
    unit_number = 0

    def update_parameters(self):
        self.parameters = [
            (ErroneousUnitType,
             {
                 'Id': self.id,
                 'Name': self.name,
             }
             ),
            #不同的unit number对应不同的标题字符串
            (DisplayUnitStrings,
             {
                 'UnitType': self.name,
                 'UnitName': self.unit_number,
                 'StringId': self.string_id,
             }
             ),
        ]
