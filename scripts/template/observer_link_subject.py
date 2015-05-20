# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class ObserverLinkSubject(object):

    ''' Add new observer '''

    subject_name = ''            #: new subject name, this name will be used as SP_ + short_name + _ + subject_name (all capitalized) in application.
    observer_name = ''           #: new observer name, normally it is the instance of class
    observer_type = ''           #: new observer type, normally it is class name in application
    subject_relation_name = ''   #: subject relation name, must be all capitalized.
    subject_access = 'Read'      #: 'Not decided', 'Write', 'Read', 'Read/Write'

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

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
            #log(("处理第%d项" % (index + 1)).decode('utf-8'))
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            if table == SubjectRelation:
                x.add()
                rtn.append(x)
                TypeId = x.model.id
                continue
            if table == ObserverSubjects:
                try:
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
