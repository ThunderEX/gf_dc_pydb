# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class NewString(Base):

    ''' Add new string '''

    define_name = ''
    string_name = ''
    define_type = 'Value type'


    def update_parameters(self):
        self.parameters = [
            # 1. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.define_name,
                 'TypeId': self.define_type,
             }
             ),
            # 2. label加相应的字符串
            (Strings,
             {
                 'String': self.string_name,
                 'LanguageId': 'DEV_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (Strings,
             {
                 'String': self.string_name,
                 'LanguageId': 'UK_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
        ]
