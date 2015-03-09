# -*- coding: utf-8 -*-
import os
import sys
from util.peewee import *

factory_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/Factory.mdb'
display_database = '../cu3x1App_SRC/Control/FactoryGenerator/input/DisplayFactory.mdb'
language_database = '../cu3x1App_SRC/Control/LangGenerator/input/language.mdb'


class FBaseModel(Model):
    database = Database(factory_database)


class DBaseModel(Model):
    database = Database(display_database)


class LBaseModel(Model):
    database = Database(language_database)

# Factor Database Models


class AlarmConfig_Model(FBaseModel):
    AlarmConfigId = IntegerField()
    Sms1Enabled = BooleanField()
    Sms2Enabled = BooleanField()
    Sms3Enabled = BooleanField()
    ScadaEnabled = BooleanField()
    CustomRelayForAlarmEnabled = BooleanField()
    CustomRelayForWarningEnabled = BooleanField()
    AlarmEnabled = BooleanField()
    WarningEnabled = BooleanField()
    AutoAck = BooleanField()
    AlarmType = CharField()
    AlarmCriteria = CharField()
    AlarmLimit = CharField()
    WarningLimit = CharField()
    MinLimit = CharField()
    MaxLimit = CharField()
    QuantityTypeId = IntegerField()
    Verified = BooleanField()
    Comment = CharField()


class AlarmDataPoint_Model(FBaseModel):
    id = IntegerField()
    AlarmConfigId = IntegerField()
    AlarmConfig2Id = IntegerField()
    ErroneousUnitTypeId = IntegerField()
    ErroneousUnitNumber = IntegerField()
    AlarmId = IntegerField()
    Comment = CharField()


class BoolDataPoint_Model(FBaseModel):
    id = IntegerField()
    Value = IntegerField()
    Comment = CharField()


class EnumDataPoint_Model(FBaseModel):
    id = IntegerField()
    EnumTypeName = CharField()
    Value = CharField()
    Comment = CharField()


class EnumTypes_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class ErroneousUnitType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class FlashBlockTypes_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class FloatDataPoint_Model(FBaseModel):
    id = IntegerField()
    QuantityType = IntegerField()
    Comment = CharField()


class GeniAppIf_Model(FBaseModel):
    GeniVarName = CharField()
    GeniClass = IntegerField()
    GeniId = IntegerField()
    SubjectId = IntegerField()
    GeniConvertId = IntegerField()
    AutoGenerate = BooleanField()
    Comment = CharField()


class GeniConvert_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()
    GeniNASupport = BooleanField()
    GeniInfo = CharField()


class IntDataPoint_Model(FBaseModel):
    id = IntegerField()
    Type = CharField()
    Min = CharField()
    Max = CharField()
    Value = CharField()
    QuantityType = IntegerField()
    Comment = CharField()
    Verified = BooleanField()


class IntDataPointTypes_Model(FBaseModel):
    Type = CharField()
    Comment = CharField()


class Observer_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    TypeId = IntegerField()
    ConstructorArgs = CharField()
    TaskId = IntegerField()
    TaskOrder = IntegerField()
    SubjectId = IntegerField()
    Comment = CharField()


class ObserverSubjects_Model(FBaseModel):
    id = IntegerField()
    SubjectId = IntegerField()
    ObserverId = IntegerField()
    SubjectRelationId = IntegerField()
    SubjectAccess = IntegerField()
    Comment = CharField()


class ObserverType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    ShortName = CharField()
    NameSpace = CharField()
    IsSingleton = BooleanField()
    IsSubject = BooleanField()
    Comment = CharField()


class QuantityType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class ResetType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class SaveTypes_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class StringDataPoint_Model(FBaseModel):
    id = IntegerField()
    Value = CharField()
    MaxLen = IntegerField()
    Comment = CharField()


class Subject_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    TypeId = IntegerField()
    GeniAppIf = BooleanField()
    Save = IntegerField()
    FlashBlock = IntegerField()
    Verified = BooleanField()
    Comment = CharField()


class SubjectRelation_Model(FBaseModel):
    id = IntegerField()
    ObserverTypeId = IntegerField()
    Name = CharField()
    Comment = CharField()


class SubjectTypes_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class SubjectAccessType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class Task_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Type = IntegerField()
    Comment = CharField()


class TaskType_Model(FBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class VectorDataPoint_Model(FBaseModel):
    id = IntegerField()
    Type = CharField()
    InitialSize = IntegerField()
    MaxSize = IntegerField()
    DefaultValue = CharField()
    Comment = CharField()


class VectorDataPointTypes_Model(FBaseModel):
    Type = CharField()
    Comment = CharField()

# Display Database Models


class Colours_Model(DBaseModel):
    Colour = CharField()


class Display_Model(DBaseModel):
    id = IntegerField()
    RootGroupId = IntegerField()
    DisplayNumber = CharField()
    Name = IntegerField()
    FocusComponentId = IntegerField()
    AbleToShow = BooleanField()
    Show = BooleanField()
    FirstWizardDisplay = BooleanField()
    Comment = CharField()


class DisplayAlarmStrings_Model(DBaseModel):
    AlarmId = IntegerField()
    StringId = IntegerField()
    Comment = CharField()


class DisplayAvailable_Model(DBaseModel):
    id = IntegerField()
    CheckState = IntegerField()
    Comment = CharField()


class DisplayComponent_Model(DBaseModel):
    id = IntegerField()
    Name = CharField()
    ComponentType = IntegerField()
    ParentComponent = IntegerField()
    Visible = BooleanField()
    ReadOnly = BooleanField()
    x1 = IntegerField()
    y1 = IntegerField()
    x2 = IntegerField()
    y2 = IntegerField()
    DisplayId = IntegerField()
    HelpString = IntegerField()
    Transparent = BooleanField()
    Comment = CharField()


class DisplayComponentColour_Model(DBaseModel):
    id = IntegerField()
    ForegroundColour = CharField()
    BackgroundColour = CharField()


class DisplayComponentTypes_Model(DBaseModel):
    id = IntegerField()
    Name = CharField()
    IsObserver = BooleanField()
    HasSingleSubject = BooleanField()
    Comment = CharField()


class DisplayFont_Model(DBaseModel):
    id = IntegerField()
    FontName = CharField()
    Comment = CharField()


class DisplayFrame_Model(DBaseModel):
    id = IntegerField()
    DrawFrame = BooleanField()
    FillBackground = BooleanField()
    Comment = CharField()


class DisplayImage_Model(DBaseModel):
    ComponentId = IntegerField()
    ImagesId = IntegerField()
    Comment = CharField()


class DisplayImages_Model(DBaseModel):
    id = IntegerField()
    Name = CharField()
    Comment = CharField()


class DisplayLabel_Model(DBaseModel):
    id = IntegerField()
    StringId = IntegerField()
    Comment = CharField()


class DisplayListView_Model(DBaseModel):
    id = IntegerField()
    RowHeight = IntegerField()
    SelectedRow = IntegerField()
    NextListId = IntegerField()
    PrevListId = IntegerField()
    Comment = CharField()


class DisplayListViewColumns_Model(DBaseModel):
    ColumnIndex = IntegerField()
    ListViewId = IntegerField()
    ColumnWidth = IntegerField()
    Comment = CharField()


class DisplayListViewItem_Model(DBaseModel):
    id = IntegerField()
    ListViewId = IntegerField()
    Index = IntegerField()
    ExcludeFromFactory = BooleanField()
    Comment = CharField()


class DisplayListViewItemComponents_Model(DBaseModel):
    id = IntegerField()
    ListViewItemId = IntegerField()
    ColumnIndex = IntegerField()
    ComponentId = IntegerField()
    Comment = CharField()


class DisplayMenuTab_Model(DBaseModel):
    id = IntegerField()
    StringId = IntegerField()
    SelectionColour = IntegerField()
    SelectionBackgroundColour = IntegerField()
    Comment = CharField()


class DisplayModeCheckBox_Model(DBaseModel):
    id = IntegerField()
    CheckState = IntegerField()
    Comment = CharField()


class DisplayMultiNumber_Model(DBaseModel):
    id = IntegerField()
    FieldCount = IntegerField()
    FieldMinValue = IntegerField()
    FieldMaxValue = IntegerField()
    Comment = CharField()


class DisplayNumber_Model(DBaseModel):
    id = IntegerField()
    NumberOfDigits = IntegerField()
    Comment = CharField()


class DisplayNumberQuantity_Model(DBaseModel):
    id = IntegerField()
    QuantityType = IntegerField()
    NumberOfDigits = IntegerField()
    NumberFontId = IntegerField()
    QuantityFontId = IntegerField()
    Comment = CharField()


class DisplayObserver_Model(DBaseModel):
    id = IntegerField()
    ObserverId = IntegerField()
    Comment = CharField()


class DisplayObserverSingleSubject_Model(DBaseModel):
    id = IntegerField()
    SubjectId = IntegerField()
    SubjectAccess = IntegerField()
    Comment = CharField()


class DisplayOnOffCheckBox_Model(DBaseModel):
    id = IntegerField()
    OnValue = IntegerField()
    OffValue = IntegerField()
    Comment = CharField()


class DisplayText_Model(DBaseModel):
    id = IntegerField()
    TextToShow = CharField()
    Align = IntegerField()
    FontId = IntegerField()
    LeftMargin = IntegerField()
    RightMargin = IntegerField()
    WordWrap = BooleanField()
    Comment = CharField()


class DisplayUnitStrings_Model(DBaseModel):
    UnitType = IntegerField()
    UnitNumber = IntegerField()
    StringId = IntegerField()
    Comment = CharField()


class display_ids_Model(DBaseModel):
    Expr1000 = IntegerField()
    Expr1001 = CharField()


class WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay_Model(DBaseModel):
    id = IntegerField()
    WriteState = IntegerField()
    Comment = CharField()

# Language Database Models


class excel_import_Model(LBaseModel):
    L_0 = CharField()
    L_1 = CharField()
    L_2 = CharField()
    L_3 = CharField()
    L_4 = CharField()
    L_5 = CharField()
    L_6 = CharField()
    L_7 = CharField()
    L_8 = CharField()
    L_9 = CharField()
    L_10 = CharField()
    L_11 = CharField()
    L_12 = CharField()
    L_13 = CharField()
    L_14 = CharField()
    L_15 = CharField()
    L_16 = CharField()
    L_17 = CharField()
    L_18 = CharField()
    L_19 = CharField()
    L_20 = CharField()
    L_21 = CharField()
    L_22 = CharField()
    L_23 = CharField()


class Languages_Model(LBaseModel):
    id = IntegerField()
    Language = CharField()
    iso_name = CharField()
    uk_name = CharField()


class StringDefines_Model(LBaseModel):
    id = IntegerField()
    DefineName = CharField()
    Location = CharField()
    UKDescription = CharField()
    TypeId = IntegerField()
    DisplayNumbers = CharField()


class Strings_Model(LBaseModel):
    id = IntegerField()
    LanguageId = IntegerField()
    String = CharField()
    Status = CharField()


class StringTypes_Model(LBaseModel):
    id = IntegerField()
    Type = CharField()
    Description = CharField()
