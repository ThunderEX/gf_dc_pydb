# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class NewObserver(Base):

    ''' Add new observer '''

    observer_name = ''           #: new observer name, normally it is the instance of class
    observer_type = ''           #: new observer type, normally it is class name in application
    short_name = ''              #: short name for new observer
    constructor_args = None

    def update_parameters(self):
        self.parameters = [
            # 1. 加ObserverType
            (ObserverType,
             {
                 'Name': self.observer_type,
                 'ShortName': self.short_name,
                 'IsSingleton': False,
                 'IsSubject': False,
             }
             ),
            # 2. 加Observer
            (Observer,
             {
                 'Name': self.observer_name,
                 #'TypeId'          : 96,      #set from ObserverType
                 'TaskId': 'LowPrioPeriodicTask',
                 #'TaskOrder'       : None,
                 #'SubjectId'       : None,
                 'ConstructorArgs' : self.constructor_args,
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
            if table == ObserverType:
                x.add()
                rtn.append(x)
                TypeId = x.model.id
                continue
            if table == Observer:
                try:
                    x.model.TypeId = TypeId
                    x.add()
                    rtn.append(x)
                except:
                    comment('需先定义添加ObserverType!!')
                    return
                continue
            x.add()
            rtn.append(x)
        return rtn
