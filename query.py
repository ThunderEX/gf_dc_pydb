# -*- coding: utf-8 -*-
from scripts.util.log import *
from scripts.util.prettytable import PrettyTable
from scripts.template.tpl import template
from scripts.tables import *

def query_by_subject_relation(str):
    s = ""
    if not str.startswith('SP_'):
        raise NameError
    s = str.split('_')
    sp = s[0]
    short_name = s[1]
    result = ObserverType_Model.get(ShortName=short_name)
    observer_type_id = result.id
    s = s[2:]
    relation = '_'.join(s)
    result = SubjectRelation_Model.get(ObserverTypeId=observer_type_id, Name=relation)
    subject_relation_id = result.id

    model = ObserverSubjects_Model()
    field_dict = model.get_field_dict()
    field_names = field_dict.keys()
    #简单排序，让id在第一位
    if 'id' in field_names:
        id_index = field_names.index('id')
        if id_index is not 0:
            field_names[id_index] = field_names[0]
            field_names[0] = 'id'
    table = PrettyTable(field_names)

    results = ObserverSubjects_Model.select().where(SubjectRelationId=subject_relation_id)
    subject_list=[]
    for r in results:
        olist = []
        for field in field_names:
            value = getattr(r, field)
            if field == 'SubjectId':
                subject_list.append(value)
            item = translate(field, value)
            olist.append(item)
        table.add_row(olist)
    print table

    print '\n'
    print '遍历所有由该SubjectRelation找出的subject'
    for subject_id in subject_list:
        table = PrettyTable(field_names)
        model = ObserverSubjects_Model()
        rs = model.select().where(SubjectId=subject_id)
        for r in rs:
            olist = []
            for field in field_names:
                value = getattr(r, field)
                item = translate(field, value)
                olist.append(item)
            table.add_row(olist)
        print '\n'
        print table


def translate(field, value):
    if field == 'SubjectId':
        model = Subject_Model
    elif field == 'SubjectRelationId':
        model = SubjectRelation_Model
    elif field == 'ObserverId':
        model = Observer_Model
    elif field == 'SubjectAccess':
        model = SubjectAccessType_Model
    else:
        return value
    result = model.get(id=value)
    return getattr(result, 'Name')
    

if __name__ == '__main__':
    #x = DisplayAlarmStrings()
    #x.query()

    query_by_subject_relation('SP_CUE_ALARM_FAULT_OBJ')
