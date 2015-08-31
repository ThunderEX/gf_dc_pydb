# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class NewQuantity(Base):

    ''' New quantity '''

    type_name = ''          #: new quantity type name, start with Q_
    define_name = ''        #: string define for new quantity
    string = ''             #: display string on screen, multiple languages

    def update_parameters(self):
        self.parameters = [
            # 1. 加新的单位类型
            (QuantityType,
             {
                 'Name': self.type_name,
             }
             ),
            # 2. 单位的字符串定义
            (StringDefines,
             {
                 "DefineName": self.define_name,
                 "TypeId": "Quantity Unit",
             }
             ),
        ]
        if self.string:
            self.parameters.extend([
            # 3. 单位的字符串
            (Strings,
             {
                 'String': self.string,
                 'LanguageId': 'DEV_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (Strings,
             {
                 'String': self.string,
                 'LanguageId': 'UK_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
        ])
