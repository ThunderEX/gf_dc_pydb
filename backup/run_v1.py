# -*- coding: utf-8 -*-
import os, sys
import shutil
from util.peewee import *
from models import *


def add_DisplayComponent(component_name, component_type_name):
    #################### 操作表DisplayComponent ####################
    display_component = DisplayComponent()
    r = DisplayComponentTypes.get(name=component_type_name)
    display_component.componenttype = r.id
    display_component.name = component_name
    display_component.parentcomponent = 0
    display_component.visible = True
    display_component.readonly = True
    display_component.x1 = 0
    display_component.x2 = 0
    display_component.y1 = 0
    display_component.y1 = 0
    display_component.displayId = 0
    display_component.helpstring = 0
    display_component.transparent = False
    display_component.comment = ' '
    display_component.save()

def add_StringDefines(string_definename, type_name):
    #################### 操作表StringDefines ####################
    # 添加DefineName，都是以'SID_'开头
    string_defines = StringDefines()
    r = StringDefines.select()
    id_list = []
    for i in r:
        id_list.append(i.id)
    string_defines.id = max(id_list) + 1
    log("max id in StringDefines table is %d" %max(id_list))
        
    string_defines.definename = string_definename

    r = StringTypes.get(type=type_name)   #查找StringTypes中的id
    string_defines.typeid = r.id

    string_defines.location = " "
    string_defines.ukdescription = " "
    string_defines.displaynumbers = " "
    string_defines.save()

def add_Strings(str, langs=['DEV_LANGUAGE', 'UK_LANGUAGE']):
    #################### 操作表Strings ####################
    # 默认添加DEV_LANGUAGE和UK_LANGUAGE
    strings = Strings()
    r = Strings.select()
    id_list = []
    for i in r:
        id_list.append(i.id)
    log("max id in Strings table is %d" %max(id_list))

    for lang in langs:
        strings.id = max(id_list) + 1
        strings.string = str
        strings.status = "UnEdit"
        r = Languages.get(language=lang)
        strings.languageid = r.id
        strings.save(force_insert=True)

def add_DisplayLabel(lable_name, string_definename):
    #################### 操作表DisplayLabel ####################
    display_label = DisplayLabel()
    #1. 从DisplayComponent中取出label的id
    r = DisplayComponent.get(name=lable_name)
    display_label.id = r.id
    #2. 从StringDefines中取出刚才加的string
    r = StringDefines.get(definename=string_definename)
    display_label.stringid = r.id

    display_label.comment = ' '
    display_label.save()

def add_DisplayText(component_name, align_method, left_margin=0, right_margin=0, font='DEFAULT_FONT_13_LANGUAGE_DEP'):
    align = {
            "TOP_LEFT"        : 0,
            "TOP_RIGHT"       : 1,
            "TOP_HCENTER"     : 2,
            "BOTTOM_LEFT"     : 4,
            "BOTTOM_RIGHT"    : 5,
            "BOTTOM_HCENTER"  : 6,
            "VCENTER_LEFT"    : 12,
            "VCENTER_RIGHT"   : 13,
            "VCENTER_HCENTER" : 14,
            }
    display_text = DisplayText()

    #1. 从DisplayComponent中取出刚才加的label的id
    r = DisplayComponent.get(name=component_name)
    display_text.id = r.id
    r = DisplayFont.get(fontname=font)
    display_text.fontid = r.id      #字体id

    display_text.texttoshow = ' '
    display_text.align = align[align_method]
    display_text.leftmargin = left_margin
    display_text.rightmargin = right_margin
    display_text.wordwrap = False
    display_text.comment = ' '
    display_text.save()

def add_DisplayNumberQuantity(nq_name, unit, digits, number_font = 'DEFAULT_FONT_13_LANGUAGE_DEP', quantity_font = 'DEFAULT_FONT_13_LANGUAGE_DEP'):
    #################### 操作表DisplayNumberQuantity ####################
    display_number_quantity = DisplayNumberQuantity()

    #1. 从DisplayComponent中取出刚才加的nq的id
    r = DisplayComponent.get(name=nq_name)
    display_number_quantity.id = r.id
    #2. 从QuantityType中取出相应单位的id
    r = QuantityType.get(name=unit)
    display_number_quantity.quantitytype = r.id
    #3. 从DisplayFont中取出相应字体的id
    r = DisplayFont.get(fontname=number_font)
    display_number_quantity.numberfontid = r.id      #数量字体
    r = DisplayFont.get(fontname=quantity_font)
    display_number_quantity.quantityfontid = r.id    #单位字体

    display_number_quantity.numberofdigits = digits
    display_number_quantity.comment = ' '
    display_number_quantity.save()

def add_DisplayObserverSingleSubject(nq_name, subject_name, access):
    #################### 操作表DisplayObserverSingleSubject ####################
    display_observer_single_subject = DisplayObserverSingleSubject()
    #1. 从DisplayComponent中取出刚才加的nq的id
    r = DisplayComponent.get(name=nq_name)
    display_observer_single_subject.id = r.id
    #2. 从Subject中取出id
    r = Subject.get(name=subject_name)
    display_observer_single_subject.subjectid = r.id
    #3. 从SubjectAccessType中取出类型对应的id
    r = SubjectAccessType.get(name=access)
    display_observer_single_subject.subjectaccess = r.id

    display_observer_single_subject.comment = ' '
    display_observer_single_subject.save()

def add_DisplayListViewItem(listview_str):
    #################### 操作表DisplayListViewItem ####################
    display_listview_item = DisplayListViewItem()
    #1. 找出listview的id
    r = DisplayComponent.get(name=listview_str)
    display_listview_item.listviewid = r.id
    #2. 找出同一个listview下的item有多少个，选出最大的index
    r = DisplayListViewItem.select().where(listviewid=display_listview_item.listviewid)
    idx_list = []
    for i in r:
        idx_list.append(i.index)
    max_idx = max(idx_list)
    log("max index in DisplayListViewItem table and id=%d is %d" %(display_listview_item.listviewid, max_idx))
    display_listview_item.index = max_idx + 1      #在最大index基础上+1
    display_listview_item.excludefromfactory = False
    display_listview_item.comment = ' '
    display_listview_item.save()
    return display_listview_item

def add_DisplayListViewItemComponents(component_name, dlvi):
    #################### 操作表DisplayListViewItemComponents ####################
    display_listview_item_components = DisplayListViewItemComponents()
    #这里应该能唯一确定id
    r = DisplayListViewItem.get(listviewid=dlvi.listviewid, index=dlvi.index)
    display_listview_item_components.listviewitemid = r.id
    r = DisplayComponent.get(name=component_name)
    display_listview_item_components.componentid = r.id

    display_listview_item_components.columnindex = 0
    #display_listview_item_components.componentid
    display_listview_item_components.comment = ' '
    display_listview_item_components.save()

def add_QuantityType(quantity_name):
    quantity_type = QuantityType()
    r = QuantityType.select()
    id_list = []
    for i in r:
        id_list.append(i.id)
    id_list.sort()
    #最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
    quantity_type.id = id_list[-2] + 1
    log("new quantitytype id is: %d" %(quantity_type.id))
    quantity_type.name = quantity_name
    quantity_type.comment = ' '
    quantity_type.save()

def add_SubjectRelation(observer_type_name, name):
    """ 
    observer_type_name - ObserverType里对应的name
    name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
    """
    subject_relation = SubjectRelation()
    r = ObserverType.get(name=observer_type_name)
    subject_relation.observertypeid = r.id
    subject_relation.name = name
    subject_relation.comment = ' '
    subject_relation.save()

def copy_database():
    f_database = r'.\v3.07\Factory.mdb'
    d_database = r'.\v3.07\DisplayFactory.mdb'
    l_database = r'.\v3.07\language.mdb'
    f_dest = r'..\..\cu3x1App_SRC\Control\FactoryGenerator\input\Factory.mdb'
    d_dest = r'..\..\cu3x1App_SRC\Control\FactoryGenerator\input\DisplayFactory.mdb'
    l_dest = r'..\..\cu3x1App_SRC\Control\LangGenerator\input\language.mdb'
    shutil.copy(f_database, f_dest)
    shutil.copy(d_database, d_dest)
    shutil.copy(l_database, l_dest)

if __name__ == '__main__':
    #copy_database()
    ppm_quantity_name = 'Q_PARTS_PER_MILLION'
    ppm_string_define = 'SID_PPM'
    ppm_string = 'ppm'
    #1. 加新的单位类型
    add_QuantityType(ppm_quantity_name)
    #2. 加ppm的字符串定义
    add_StringDefines(ppm_string_define, 'Quantity Unit')
    #3. 加ppm相应的字符串
    add_Strings(ppm_string)
    #4. SubjectRelation里的MpcUnits要加上Q_PARTS_PER_MILLION
    add_SubjectRelation('MpcUnits', ppm_quantity_name)

    #表ObserverSubjects
    #SubjectId	        ObserverId	SubjectRelationId	Subject Access	Text10	Comment
    #unit_energy_actual	units	    Q_ENERGY	        Read/Write	    129	
    #要有对应的observer才能生成SP_UNITS_XXX
    #这里我先改成Q_PARTS_PER_MILLION，看看energy能不能把单位改成ppm

    #Note
    #改mpcunits.conf.cpp
    #改mpcunits.cpp，SetSubjectPointer加
    #case SP_UNITS_Q_PARTS_PER_MILLION        : mUnitsDataPoints[Q_PARTS_PER_MILLION].Attach(pSubject); break;

    h2s_label_name = '1.1 SystemStatus l1 h2s level'
    h2s_nq_name = '1.1 SystemStatus l1 h2s level nq'
    h2s_string_define = 'SID_H2S_LEVEL' 
    h2s_string = 'H2S level'
    #1. 添加label
    add_DisplayComponent(h2s_label_name, 'Label')
    #2. 添加数值
    add_DisplayComponent(h2s_nq_name, 'NumberQuantity')
    #3. 加字符串定义
    add_StringDefines(h2s_string_define, 'Value type')
    #4. label加相应的字符串
    add_Strings(h2s_string)
    #5. 将字符串和label对应起来
    add_DisplayLabel(h2s_label_name, h2s_string_define)
    #6. 定义label的text排列方式
    add_DisplayText(h2s_label_name, 'VCENTER_LEFT', 2, 0)
    #7. 定义数值的text排列方式
    add_DisplayText(h2s_nq_name, 'VCENTER_LEFT', 0, 0)
    #8. 数值与新加单位'ppm'对应
    add_DisplayNumberQuantity(h2s_nq_name, ppm_quantity_name, 3, 'DEFAULT_FONT_13_LANGUAGE_INDEP', 'DEFAULT_FONT_13_LANGUAGE_INDEP')
    #9. 数值与subject对应
    #TODO 先用已有的subject数据total_energy_j_for_display
    add_DisplayObserverSingleSubject(h2s_nq_name, 'total_energy_j_for_display', 'Read')

    #10. 在对应的listview下面新加一个item
    listview_name = '1.1 SystemStatus List 1'
    dlvi = add_DisplayListViewItem(listview_name)
    #11. 在新加的item下面添加label
    add_DisplayListViewItemComponents(h2s_label_name, dlvi)
    #12. 在新加的item下面添加数值
    add_DisplayListViewItemComponents(h2s_nq_name, dlvi)
