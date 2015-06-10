# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class NewGeniConvert(object):

    ''' Add new geni convert'''

    #Alarm
    name = ''
    geni_na_support = True
    geni_info = 'DIMLESS_255'
    comment = ''


    def __init__(self):
        self.parameters = []
        self.description = 'No description'

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
