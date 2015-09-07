# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from subject import NewSubject
from base import Base

class NewAlarm(Base):

    ''' Add new alarm '''

    alarm_config_subject = NewSubject()
    alarm_subject = NewSubject()

    #Alarm
    alarm_define_name = ''
    alarm_id = 0

    def update_parameters(self):
        self.parameters = []
        if self.alarm_id:
            self.parameters.append(
                (DisplayAlarmStrings,
                 {
                     'AlarmId': self.alarm_id,
                     'StringId': self.alarm_define_name,
                 }
                 ),
            )

    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.parameters)
        self.alarm_config_subject.save()
        self.alarm_subject.save()
