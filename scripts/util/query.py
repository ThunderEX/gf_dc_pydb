# -*- coding: utf-8 -*-
from .log import *
from ..lib.prettytable import PrettyTable
from ..tables import *
from ..models import *

def create_table(model):
    field_dict = model.get_field_dict()
    field_names = list(field_dict)
    # 排序，让id在第一位
    if 'id' in field_names:
        id_index = field_names.index('id')
        if id_index is not 0:
            field_names[id_index] = field_names[0]
            field_names[0] = 'id'
    return PrettyTable(field_names), field_names

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
    table, field_names = create_table(model)

    results = ObserverSubjects_Model.select().where(SubjectRelationId=subject_relation_id)
    subject_list=[]
    for r in results:
        olist = [translate(field, getattr(r, field)) for field in field_names]
        table.add_row(olist)
        if 'SubjectId' in field_names:
            subject_list.append(getattr(r, 'SubjectId'))
    print(table)

    #print '\n'
    print('遍历所有由该SubjectRelation找出的subject')
    for subject_id in subject_list:
        table = PrettyTable(field_names)
        model = ObserverSubjects_Model()
        rs = model.select().where(SubjectId=subject_id)
        for r in rs:
            olist = [translate(field, getattr(r, field)) for field in field_names]
            table.add_row(olist)
        #print '\n'
        print(table)


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

def query_alarm():
    _id = id
    model = DisplayAlarmStrings_Model()
    string_model = StringDefines_Model()
    table, field_names = create_table(model)
    results = model.select()
    if results:
        for result in results:
            olist = []
            for field in field_names:
                #olist.append(str(getattr(result, field)))
                value = getattr(result, field)
                if field == 'StringId':
                    r = string_model.get(id=value)
                    value = r.DefineName
                olist.append(value)
            table.add_row(olist)
    log(table.get_string())
    return results


def query_observer_by_shortname(short_name):
    model = ObserverType_Model()
    print(model.__class__.__name__.replace('_Model', ''))
    table, field_names = create_table(model)
    result = ObserverType_Model.get(ShortName=short_name)
    type_id = getattr(result, 'id')
    olist = [getattr(result, field) for field in field_names]
    table.add_row(olist)
    print(table)

    model = Observer_Model()
    print(model.__class__.__name__.replace('_Model', ''))
    table, field_names = create_table(model)
    results = model.select().where(TypeId=type_id)
    for r in results:
        olist = [getattr(r, field) for field in field_names]
        table.add_row(olist)
    print(table)


if __name__ == '__main__':
    # query_alarm()
    query_by_subject_relation('SP_IO111_TEMPERATURE_SUPPORT_BEARING')
    # query_observer_by_shortname('PUMP')
