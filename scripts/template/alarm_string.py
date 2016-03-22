# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Base

class AlarmString(Base):

    ''' Add new alarm string'''

    #Alarm
    alarm_define_name = ''
    alarm_string = ''
    alarm_id = 0


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
            (DisplayAlarmStrings,
             {
                 'AlarmId': self.alarm_id,
                 'StringId': self.alarm_define_name,
             }
             ),
        ]

    def save(self):
        comment(self.description)
        self.update_parameters()
        rtn = []
        for index, para in enumerate(self.parameters):
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            if table == DisplayAlarmStrings:
                comment('添加AlarmId：%d' % (x.model.AlarmId))
                try:
                    result = x.model.get(AlarmId=x.model.AlarmId) #报错，说明没有
                    getattr(result, 'AlarmId')
                    comment('已有AlarmId：%d，不能重复加入' % (x.model.AlarmId))
                    raise NameError
                except:
                    pass
            x.add()
            rtn.append(x)
        return rtn
