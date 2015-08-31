# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class NewGeniConvert(Base):

    ''' Add new geni convert'''

    #Alarm
    name = ''
    geni_na_support = True
    geni_info = 'DIMLESS_255'
    comment = ''

    def update_parameters(self):
        self.parameters = [
            # 1. 加字符串定义
            (GeniConvert,
             {
                 'Name': self.name,
                 'GeniNASupport': self.geni_na_support,
                 'GeniInfo': self.geni_info,
                 'Comment': self.comment,
             }
             ),
        ]
