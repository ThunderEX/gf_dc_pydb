# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class NewQuantity(object):

    ''' New quantity '''

    type_name = ''          #: new quantity type name, start with Q_
    define_name = ''        #: string define for new quantity
    string = ''             #: display string on screen, multiple languages

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

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
            # 4. SubjectRelation里的MpcUnits要加上单位类型
            #(SubjectRelation,
             #{
                 #'Name': self.type_name,
                 #'ObserverTypeId': 'MpcUnits',
             #}
             #),
            # 5. 修改mpcunits.conf.cpp和mpcunits.cpp
        ])

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
        comment('Note: 需要修改UnitTypes.h, mpcunits.conf.cpp和mpcunits.cpp')
        return rtn
