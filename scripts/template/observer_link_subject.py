# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from .base import Base

class ObserverLinkSubject(Base):

    ''' Add new observer '''

    subject_name = ''            #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    observer_name = ''           #: new observer name, normally it is the instance of class
    observer_type = ''           #: new observer type, normally it is class name in application
    subject_relation_name = ''   #: subject relation name, must be all capitalized.
    subject_access = 'Read'      #: 'Not decided', 'Write', 'Read', 'Read/Write'

    def update_parameters(self):
        self.parameters = [
            # 添加SubjectRelation
            (SubjectRelation,
             {
                 'Name': self.subject_relation_name.upper(),  # 必须用大写字母
                 'ObserverTypeId': self.observer_type,
             }
             ),
            # 添加ObserverSubjects，会用到SubjectRelation添加的Name
            (ObserverSubjects,
             {
                 'SubjectId': self.subject_name,
                 'ObserverId': self.observer_name,
                 'SubjectRelationId': self.subject_relation_name.upper(),
                 'SubjectAccess': self.subject_access,
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
            if table == SubjectRelation:
                x.add()
                rtn.append(x)
                TypeId = x.model.id
                # 有时候会出现找到好几个SubjectRelation的情况，需要再进行一次精确查找，否则会在convert_foreignkey自动使用第一个匹配的id
                if not x.model.id:
                    temp_modle = x.get(Name=x.model.Name, ObserverTypeId=x.model.ObserverTypeId)
                    TypeId = temp_modle.id
                continue
            if table == ObserverSubjects:
                try:
                    if TypeId:
                        x.model.SubjectRelationId = TypeId
                    x.add()
                    rtn.append(x)
                except:
                    comment('需先定义添加ObserverType!!')
                    return
                continue
            x.add()
            rtn.append(x)
        return rtn
