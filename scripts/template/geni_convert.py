# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Base

class NewGeniConvert(Base):

    ''' Add new geni convert'''

    name = ''
    geni_na_support = True
    geni_info = 'DIMLESS_255'
    comment = ''

    def update_parameters(self):
        self.parameters = [
            (GeniConvert,
             {
                 'Name': self.name,
                 'GeniNASupport': self.geni_na_support,
                 'GeniInfo': self.geni_info,
                 'Comment': self.comment,
             }
             ),
        ]
