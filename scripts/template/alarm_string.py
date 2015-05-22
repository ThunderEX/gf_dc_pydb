# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class AlarmString(object):

    ''' Add new alarm string'''

    #Alarm
    alarm_define_name = ''
    alarm_string = ''


    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
            # 1. 加字符串定义
            (StringDefines,
             {
                 'DefineName': self.alarm_define_name,
                 'TypeId': 'Alarm',
             }
             ),
            # 2. alarm加相应的字符串
            (Strings,
             {
                 'String': self.alarm_string,
                 'LanguageId': 'DEV_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (Strings,
             {
                 'String': self.alarm_string,
                 'LanguageId': 'UK_LANGUAGE',
                 'Status': 'UnEdit',
             }
             ),
            (DisplayAlarmStrings,
             {
                 'StringId': self.alarm_define_name,
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
            if table == DisplayAlarmStrings:
                comment('新加入AlarmString的AlarmId 为：%d' % (x.model.AlarmId))
            rtn.append(x)
        return rtn
