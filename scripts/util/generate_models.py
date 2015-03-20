# -*- coding: utf-8 -*-
import os
import sys
import pypyodbc

DisplayFactory_TableNames = [
    "Colours",
    "Display",
    "DisplayAlarmStrings",
    "DisplayAvailable",
    "DisplayComponent",
    "DisplayComponentColour",
    "DisplayComponentTypes",
    "DisplayFont",
    "DisplayFrame",
    "DisplayImage",
    "DisplayImages",
    "DisplayLabel",
    "DisplayListView",
    "DisplayListViewColumns",
    "DisplayListViewItem",
    "DisplayListViewItemComponents",
    "DisplayMenuTab",
    "DisplayModeCheckBox",
    "DisplayMultiNumber",
    "DisplayNumber",
    "DisplayNumberQuantity",
    "DisplayObserver",
    "DisplayObserverSingleSubject",
    "DisplayOnOffCheckBox",
    "DisplayText",
    "DisplayUnitStrings",
    "display_ids",
    #"Paste Errors",            #这张表名有空格
    "WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay",
]

Factory_TablesNames = [
    "AlarmConfig",
    "AlarmDataPoint",
    #"AlarmStateType",  #不存在
    "BoolDataPoint",
    "EnumDataPoint",
    "EnumTypes",
    "ErroneousUnitType",
    "FlashBlockTypes",
    "FloatDataPoint",
    "GeniAppIf",
    "GeniConvert",
    "IntDataPoint",
    "IntDataPointTypes",
    "Observer",
    "ObserverSubjects",
    "ObserverType",
    "QuantityType",
    "ResetType",
    "SaveTypes",
    "StringDataPoint",
    "Subject",
    "SubjectRelation",
    "SubjectTypes",
    "SubjectAccessType",
    "Task",
    "TaskType",
    "VectorDataPoint",
    "VectorDataPointTypes",
    #"zzz_subjectid_relations subform",  #这张表名有空格
]

Language_TableNames = [
    "excel_import",
    "Languages",
    "StringDefines",
    "Strings",
    "StringTypes",
]

sqls = {
    "get_all_tables": "SELECT [Name] FROM MSysObjects WHERE Type In (1,4,6) AND Left([Name] , 4) <> 'MSys' ORDER BY [Name]",  # 没法运行，权限不够
}

INT_TYPE = type(1)
STRING_TYPE = type("string")
UNICODE_TYPE = type(u"string")
BOOL_TYPE = type(True)

field_types = {
    UNICODE_TYPE: "CharField()",
    INT_TYPE: "IntegerField()",
    BOOL_TYPE: "BooleanField()",
}

# factory数据库
factory_connection = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=../../../cu3x1App_SRC/Control/FactoryGenerator/input/Factory.mdb'
# DisplayFactory数据库
display_connection = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=../../../cu3x1App_SRC/Control/FactoryGenerator/input/DisplayFactory.mdb'
# language数据库
language_connection = 'Driver={Microsoft Access Driver (*.mdb)};DBQ=../../../cu3x1App_SRC/Control/LangGenerator/input/language.mdb'

output_file = open('../models.py', 'w')
template = """# -*- coding: utf-8 -*-
import os, sys
from util.peewee import *

factory_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/Factory.mdb'
display_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/DisplayFactory.mdb'
language_database ='../cu3x1App_SRC/Control/LangGenerator/input/language.mdb'

class FBaseModel(Model):
    database = Database(factory_database)

class DBaseModel(Model):
    database = Database(display_database)

class LBaseModel(Model):
    database = Database(language_database)
"""
output_file.write(template)
output_file.write('\n')
cls = "class %s_Model(%sBaseModel):"

output_file.write('#Factor Database Models')
output_file.write('\n')
connection = pypyodbc.connect(factory_connection)
cur = connection.cursor()
for tb in Factory_TablesNames:
    output_file.write(cls % (tb, 'F'))
    output_file.write('\n')
    sql = "SELECT * FROM %s" % (tb)
    cur.execute(sql)
    for descrip in cur.description:
        name = descrip[0]
        type = descrip[1]
        # 这个域虽然定义了，但不能写，不知道为什么
        if name == 'field1':
            continue
        if name in ['id', 'ID', 'iD', 'Id']:
            name = name.lower()
        if type in field_types.keys():
            str = "    " + name + " = " + field_types[type] + "\n"
            output_file.write(str)
    output_file.write('\n')

output_file.write('#Display Database Models')
output_file.write('\n')
connection = pypyodbc.connect(display_connection)
cur = connection.cursor()
for tb in DisplayFactory_TableNames:
    output_file.write(cls % (tb, 'D'))
    output_file.write('\n')
    sql = "SELECT * FROM %s" % (tb)
    cur.execute(sql)
    for descrip in cur.description:
        name = descrip[0]
        type = descrip[1]
        if name in ['id', 'ID', 'iD', 'Id']:
            name = name.lower()
        if type in field_types.keys():
            str = "    " + name + " = " + field_types[type] + "\n"
            output_file.write(str)
    output_file.write('\n')

output_file.write('#Language Database Models')
output_file.write('\n')
connection = pypyodbc.connect(language_connection)
cur = connection.cursor()
for tb in Language_TableNames:
    output_file.write(cls % (tb, 'L'))
    output_file.write('\n')
    sql = "SELECT * FROM %s" % (tb)
    cur.execute(sql)
    for descrip in cur.description:
        name = descrip[0]
        type = descrip[1]
        if name in ['id', 'ID', 'iD', 'Id']:
            name = name.lower()
        if type in field_types.keys():
            str = "    " + name + " = " + field_types[type] + "\n"
            output_file.write(str)
    output_file.write('\n')
