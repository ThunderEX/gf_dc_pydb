# -*- coding: utf-8 -*-
import os, sys
from peewee import *

factory_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/Factory.mdb'
display_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/DisplayFactory.mdb'
language_database = '../cu3x1App_SRC/Control/LangGenerator/input/language.mdb'

class FBaseModel(Model):
    database = Database(factory_database)

class DBaseModel(Model):
    database = Database(display_database)

class LBaseModel(Model):
    database = Database(language_database)

#Factor Database Models
class AlarmConfig(FBaseModel):
    alarmconfigid = IntegerField()
    sms1enabled = BooleanField()
    sms2enabled = BooleanField()
    sms3enabled = BooleanField()
    scadaenabled = BooleanField()
    customrelayforalarmenabled = BooleanField()
    customrelayforwarningenabled = BooleanField()
    alarmenabled = BooleanField()
    warningenabled = BooleanField()
    autoack = BooleanField()
    alarmtype = CharField()
    alarmcriteria = CharField()
    alarmlimit = CharField()
    warninglimit = CharField()
    minlimit = CharField()
    maxlimit = CharField()
    quantitytypeid = IntegerField()
    verified = BooleanField()
    comment = CharField()

class AlarmDataPoint(FBaseModel):
    id = IntegerField()
    alarmconfigid = IntegerField()
    alarmconfig2id = IntegerField()
    erroneousunittypeid = IntegerField()
    erroneousunitnumber = IntegerField()
    alarmid = IntegerField()
    comment = CharField()

class BoolDataPoint(FBaseModel):
    id = IntegerField()
    value = IntegerField()
    comment = CharField()

class EnumDataPoint(FBaseModel):
    id = IntegerField()
    enumtypename = CharField()
    value = CharField()
    comment = CharField()

class EnumTypes(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class ErroneousUnitType(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class FloatDataPoint(FBaseModel):
    id = IntegerField()
    quantitytype = IntegerField()
    comment = CharField()

class GeniAppIf(FBaseModel):
    genivarname = CharField()
    geniclass = IntegerField()
    geniid = IntegerField()
    subjectid = IntegerField()
    geniconvertid = IntegerField()
    autogenerate = BooleanField()
    comment = CharField()

class GeniConvert(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()
    geninasupport = BooleanField()
    geniinfo = CharField()

class IntDataPoint(FBaseModel):
    id = IntegerField()
    type = CharField()
    min = CharField()
    max = CharField()
    value = CharField()
    quantitytype = IntegerField()
    comment = CharField()
    verified = BooleanField()

class IntDataPointTypes(FBaseModel):
    type = CharField()
    comment = CharField()

class Observer(FBaseModel):
    id = IntegerField()
    name = CharField()
    typeid = IntegerField()
    constructorargs = CharField()
    taskid = IntegerField()
    taskorder = IntegerField()
    subjectid = IntegerField()
    comment = CharField()

class ObserverSubjects(FBaseModel):
    id = IntegerField()
    subjectid = IntegerField()
    observerid = IntegerField()
    subjectrelationid = IntegerField()
    subjectaccess = IntegerField()
    comment = CharField()

class ObserverType(FBaseModel):
    id = IntegerField()
    name = CharField()
    shortname = CharField()
    namespace = CharField()
    issingleton = BooleanField()
    issubject = BooleanField()
    comment = CharField()

class QuantityType(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class ResetType(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class StringDataPoint(FBaseModel):
    id = IntegerField()
    value = CharField()
    maxlen = IntegerField()
    comment = CharField()

class Subject(FBaseModel):
    id = IntegerField()
    name = CharField()
    typeid = IntegerField()
    geniappif = BooleanField()
    save = IntegerField()
    flashblock = IntegerField()
    verified = BooleanField()
    comment = CharField()

class SubjectRelation(FBaseModel):
    id = IntegerField()
    observertypeid = IntegerField()
    name = CharField()
    comment = CharField()

class SubjectTypes(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class SubjectAccessType(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class Task(FBaseModel):
    id = IntegerField()
    name = CharField()
    type = IntegerField()
    comment = CharField()

class TaskType(FBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class VectorDataPoint(FBaseModel):
    id = IntegerField()
    type = CharField()
    initialsize = IntegerField()
    maxsize = IntegerField()
    defaultvalue = CharField()
    comment = CharField()

class VectorDataPointTypes(FBaseModel):
    type = CharField()
    comment = CharField()

#Display Database Models
class Colours(DBaseModel):
    colour = CharField()

class Display(DBaseModel):
    id = IntegerField()
    rootgroupid = IntegerField()
    displaynumber = CharField()
    name = IntegerField()
    focuscomponentid = IntegerField()
    abletoshow = BooleanField()
    show = BooleanField()
    firstwizarddisplay = BooleanField()
    comment = CharField()

class DisplayAlarmStrings(DBaseModel):
    alarmid = IntegerField()
    stringid = IntegerField()
    comment = CharField()

class DisplayAvailable(DBaseModel):
    id = IntegerField()
    checkstate = IntegerField()
    comment = CharField()

class DisplayComponent(DBaseModel):
    id = IntegerField()
    name = CharField()
    componenttype = IntegerField()
    parentcomponent = IntegerField()
    visible = BooleanField()
    readonly = BooleanField()
    x1 = IntegerField()
    y1 = IntegerField()
    x2 = IntegerField()
    y2 = IntegerField()
    displayid = IntegerField()
    helpstring = IntegerField()
    transparent = BooleanField()
    comment = CharField()

class DisplayComponentColour(DBaseModel):
    id = IntegerField()
    foregroundcolour = CharField()
    backgroundcolour = CharField()

class DisplayComponentTypes(DBaseModel):
    id = IntegerField()
    name = CharField()
    isobserver = BooleanField()
    hassinglesubject = BooleanField()
    comment = CharField()

class DisplayFont(DBaseModel):
    id = IntegerField()
    fontname = CharField()
    comment = CharField()

class DisplayFrame(DBaseModel):
    id = IntegerField()
    drawframe = BooleanField()
    fillbackground = BooleanField()
    comment = CharField()

class DisplayImage(DBaseModel):
    componentid = IntegerField()
    imagesid = IntegerField()
    comment = CharField()

class DisplayImages(DBaseModel):
    id = IntegerField()
    name = CharField()
    comment = CharField()

class DisplayLabel(DBaseModel):
    id = IntegerField()
    stringid = IntegerField()
    comment = CharField()

class DisplayListView(DBaseModel):
    id = IntegerField()
    rowheight = IntegerField()
    selectedrow = IntegerField()
    nextlistid = IntegerField()
    prevlistid = IntegerField()
    comment = CharField()

class DisplayListViewColumns(DBaseModel):
    columnindex = IntegerField()
    listviewid = IntegerField()
    columnwidth = IntegerField()
    comment = CharField()

class DisplayListViewItem(DBaseModel):
    id = IntegerField()
    listviewid = IntegerField()
    index = IntegerField()
    excludefromfactory = BooleanField()
    comment = CharField()

class DisplayListViewItemComponents(DBaseModel):
    id = IntegerField()
    listviewitemid = IntegerField()
    columnindex = IntegerField()
    componentid = IntegerField()
    comment = CharField()

class DisplayMenuTab(DBaseModel):
    id = IntegerField()
    stringid = IntegerField()
    selectioncolour = IntegerField()
    selectionbackgroundcolour = IntegerField()
    comment = CharField()

class DisplayModeCheckBox(DBaseModel):
    id = IntegerField()
    checkstate = IntegerField()
    comment = CharField()

class DisplayMultiNumber(DBaseModel):
    id = IntegerField()
    fieldcount = IntegerField()
    fieldminvalue = IntegerField()
    fieldmaxvalue = IntegerField()
    comment = CharField()

class DisplayNumber(DBaseModel):
    id = IntegerField()
    numberofdigits = IntegerField()
    comment = CharField()

class DisplayNumberQuantity(DBaseModel):
    id = IntegerField()
    quantitytype = IntegerField()
    numberofdigits = IntegerField()
    numberfontid = IntegerField()
    quantityfontid = IntegerField()
    comment = CharField()

class DisplayObserver(DBaseModel):
    id = IntegerField()
    observerid = IntegerField()
    comment = CharField()

class DisplayObserverSingleSubject(DBaseModel):
    id = IntegerField()
    subjectid = IntegerField()
    subjectaccess = IntegerField()
    comment = CharField()

class DisplayOnOffCheckBox(DBaseModel):
    id = IntegerField()
    onvalue = IntegerField()
    offvalue = IntegerField()
    comment = CharField()

class DisplayText(DBaseModel):
    id = IntegerField()
    texttoshow = CharField()
    align = IntegerField()
    fontid = IntegerField()
    leftmargin = IntegerField()
    rightmargin = IntegerField()
    wordwrap = BooleanField()
    comment = CharField()

class DisplayUnitStrings(DBaseModel):
    unittype = IntegerField()
    unitnumber = IntegerField()
    stringid = IntegerField()
    comment = CharField()

class WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay(DBaseModel):
    id = IntegerField()
    writestate = IntegerField()
    comment = CharField()

#Language Database Models
class excel_import(LBaseModel):
    l_0 = CharField()
    l_1 = CharField()
    l_2 = CharField()
    l_3 = CharField()
    l_4 = CharField()
    l_5 = CharField()
    l_6 = CharField()
    l_7 = CharField()
    l_8 = CharField()
    l_9 = CharField()
    l_10 = CharField()
    l_11 = CharField()
    l_12 = CharField()
    l_13 = CharField()
    l_14 = CharField()
    l_15 = CharField()
    l_16 = CharField()
    l_17 = CharField()
    l_18 = CharField()
    l_19 = CharField()
    l_20 = CharField()
    l_21 = CharField()
    l_22 = CharField()
    l_23 = CharField()

class Languages(LBaseModel):
    id = IntegerField()
    language = CharField()
    iso_name = CharField()
    uk_name = CharField()

class StringDefines(LBaseModel):
    id = IntegerField()
    definename = CharField()
    location = CharField()
    ukdescription = CharField()
    typeid = IntegerField()
    displaynumbers = CharField()

class Strings(LBaseModel):
    id = IntegerField()
    languageid = IntegerField()
    string = CharField()
    status = CharField()

class StringTypes(LBaseModel):
    id = IntegerField()
    type = CharField()
    description = CharField()

