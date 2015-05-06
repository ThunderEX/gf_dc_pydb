# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class NewString(object):

    ''' Add new string '''

    define_name = ''
    string_name = ''

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
            # 1. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.define_name,
                 'TypeId': 'Value type',
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
        return rtn
