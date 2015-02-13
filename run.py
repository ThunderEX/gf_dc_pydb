# -*- coding: utf-8 -*-
import os, sys
from peewee import *
from tables import *


def add_DisplayComponent(component_name, component_type_name):
    #################### 操作表DisplayComponent ####################
    dc_label = DisplayComponent()
    r = DisplayComponentTypes.select().where(name=component_type_name)   #返回结果集
    for i in r:
        dc_label.componenttype = i.id
    dc_label.name = component_name
    dc_label.parentcomponent = 0
    dc_label.visible = True
    dc_label.readonly = True
    dc_label.x1 = 0
    dc_label.x2 = 0
    dc_label.y1 = 0
    dc_label.y1 = 0
    dc_label.displayId = 0
    dc_label.helpstring = 0
    dc_label.transparent = False
    dc_label.comment = ' '
    try:
        dc_label.save()
        log("成功加入DisplayComponent: " + component_name)
    except Exception as e:
        log("错误！！！无法加入DisplayComponent")
        raise e

def add_StringDefines(string_definename, type_name):
    #################### 操作表StringDefines ####################
    # 添加DefineName，都是以'SID_'开头
    sd_string = StringDefines()
    r = StringDefines.select()
    id_list = []
    for i in r:
        id_list.append(i.id)
    sd_string.id = max(id_list) + 1
    log("max id in StringDefines table is %d" %max(id_list))
        
    sd_string.definename = string_definename
    r = StringTypes.select().where(type=type_name)   #查找StringTypes中的id
    for i in r:
        sd_string.typeid = i.id
    sd_string.location = " "
    sd_string.ukdescription = " "
    sd_string.displaynumbers = " "
    try:
        sd_string.save()
        log("成功加入string definename: " + string_definename)
    except Exception as e:
        log("错误！！！无法加入string definename: " + string_definename)
        raise e

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
        r = Languages.select().where(language=lang)
        for i in r:
            strings.languageid = i.id
        try:
            strings.save(force_insert=True)
            log("成功加入string: " + str)
        except Exception as e:
            log("错误！！！无法加入string: " + str)
            raise e

def add_DisplayLabel(lable_name, string_definename):
    #################### 操作表DisplayLabel ####################
    displaylabel = DisplayLabel()
    #1. 从DisplayComponent中取出刚才加的label的id
    r = DisplayComponent.select().where(name=lable_name)
    for i in r:
        displaylabel.id = i.id
    #2. 从StringDefines中取出刚才加的string
    r = StringDefines.select().where(definename=string_definename)
    for i in r:
        displaylabel.stringid = i.id
    displaylabel.comment = ' '
    try:
        displaylabel.save()
        log("成功加入display label")
    except Exception as e:
        log("错误！！！无法加入display label")
        raise e

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
    displaytext = DisplayText()
    #1. 从DisplayComponent中取出刚才加的label的id
    r = DisplayComponent.select().where(name=component_name)
    for i in r:
        displaytext.id = i.id
    displaytext.texttoshow = ' '
    displaytext.align = align[align_method]
    r = DisplayFont.select().where(fontname=font)
    for i in r:
        displaytext.fontid = i.id      #字体id
    displaytext.leftmargin = left_margin
    displaytext.rightmargin = right_margin
    displaytext.wordwrap = False
    displaytext.comment = ' '
    try:
        displaytext.save()
        log("成功加入DisplayText")
    except Exception as e:
        log("错误！！！无法加入DisplayText")
        raise e


def add_DisplayNumberQuantity(nq_name, unit, digits, number_font = 'DEFAULT_FONT_13_LANGUAGE_DEP', quantity_font = 'DEFAULT_FONT_13_LANGUAGE_DEP'):
    #################### 操作表DisplayNumberQuantity ####################
    displaynumberquantity = DisplayNumberQuantity()
    #1. 从DisplayComponent中取出刚才加的nq的id
    r = DisplayComponent.select().where(name=nq_name)
    for i in r:
        displaynumberquantity.id = i.id
    #2. 从QuantityType中取出相应单位的id
    r = QuantityType.select().where(name=unit)
    for i in r:
        displaynumberquantity.quantitytype = i.id
    displaynumberquantity.numberofdigits = digits
    #3. 从DisplayFont中取出相应字体的id
    r = DisplayFont.select().where(fontname=number_font)
    for i in r:
        displaynumberquantity.numberfontid = i.id      #数量字体
    r = DisplayFont.select().where(fontname=quantity_font)
    for i in r:
        displaynumberquantity.quantityfontid = i.id    #单位字体
    displaynumberquantity.comment = ' '
    try:
        displaynumberquantity.save()
        log("成功加入DisplayNumberQuantity")
    except Exception as e:
        log("错误！！！无法加入DisplayNumberQuantity")
        raise e

def add_DisplayObserverSingleSubject(nq_name, subject_name, access):
    #################### 操作表DisplayObserverSingleSubject ####################
    displayobserversinglesubject = DisplayObserverSingleSubject()
    #1. 从DisplayComponent中取出刚才加的nq的id
    r = DisplayComponent.select().where(name=nq_name)
    for i in r:
        displayobserversinglesubject.id = i.id
    #2. 从Subject中取出id
    r = Subject.select().where(name=subject_name)
    for i in r:
        displayobserversinglesubject.subjectid = i.id
    #2. 从SubjectAccessType中取出类型对应的id
    r = SubjectAccessType.select().where(name=access)
    for i in r:
        displayobserversinglesubject.subjectaccess = i.id
    displayobserversinglesubject.comment = ' '
    try:
        displayobserversinglesubject.save()
        log("成功加入DisplayObserverSingleSubject")
    except Exception as e:
        log("错误！！！无法加入DisplayObserverSingleSubject")
        raise e

def add_DisplayListViewItem(listview_str):
    #################### 操作表DisplayListViewItem ####################
    displaylistviewitem = DisplayListViewItem()
    #1. 找出listview的id
    r = DisplayComponent.select().where(name=listview_str)
    for i in r:
        displaylistviewitem.listviewid = i.id
    r = DisplayListViewItem.select().where(listviewid=displaylistviewitem.listviewid)
    #2. 找出同一个listview下的item有多少个，选出最大的index
    idx_list = []
    for i in r:
        idx_list.append(i.index)
    max_idx = max(idx_list)
    log("max index in DisplayListViewItem table and id=%d is %d" %(displaylistviewitem.listviewid, max_idx))
    displaylistviewitem.index = max_idx + 1      #在最大index基础上+1
    displaylistviewitem.excludefromfactory = False
    displaylistviewitem.comment = ' '
    try:
        displaylistviewitem.save()
        log("成功加入DisplayListViewItem")
    except Exception as e:
        log("错误！！！无法加入DisplayListViewItem")
        raise e
    return displaylistviewitem

def add_DisplayListViewItemComponents(component_name, dlvi):
    #################### 操作表DisplayListViewItemComponents ####################
    displaylistviewitemcomponents = DisplayListViewItemComponents()
    #这里应该能唯一确定id
    r = DisplayListViewItem.select().where(listviewid=dlvi.listviewid, index=dlvi.index)
    for i in r:
        displaylistviewitemcomponents.listviewitemid = i.id
    displaylistviewitemcomponents.columnindex = 0
    displaylistviewitemcomponents.componentid
    r = DisplayComponent.select().where(name=component_name)
    for i in r:
        displaylistviewitemcomponents.componentid = i.id
    displaylistviewitemcomponents.comment = ' '
    try:
        displaylistviewitemcomponents.save()
        log("成功加入DisplayListViewItemComponents")
    except Exception as e:
        log("错误！！！无法加入DisplayListViewItemComponents")
        raise e

def add_QuantityType(quantity_name):
    quantitytype = QuantityType()
    r = QuantityType.select()
    id_list = []
    for i in r:
        id_list.append(i.id)
    id_list.sort()
    #最后一个是Q_LAST_UNIT，100，要从倒数第二个+1
    quantitytype.id = id_list[-2] + 1
    log("new quantitytype id is: %d" %(quantitytype.id))
    quantitytype.name = quantity_name
    quantitytype.comment = ' '
    try:
        quantitytype.save()
        log("成功加入QuantityType")
    except Exception as e:
        log("错误！！！无法加入QuantityType")
        raise e

def add_SubjectRelation(observer_type_name, name):
    """ 
    observer_type_name - ObserverType里对应的name
    name - 用于组成SubjectPointer，前面加SP_和ObserverType里的ShortName，如SP_UNITS_XXX
    """
    subjectrelation = SubjectRelation()
    r = ObserverType.select().where(name=observer_type_name)
    for i in r:
        subjectrelation.observertypeid = i.id
    subjectrelation.name = name
    subjectrelation.comment = ' '
    try:
        subjectrelation.save()
        log("成功加入SubjectRelation")
    except Exception as e:
        log("错误！！！无法加入SubjectRelation")
        raise e
    

if __name__ == '__main__':
    ppm_quantity_name = 'Q_PARTS_PER_MILLION'
    ppm_string_define = 'SID_PPM'
    ppm_string = 'ppm'
    #加新的单位类型
    add_QuantityType(ppm_quantity_name)
    #加ppm的字符串定义
    add_StringDefines(ppm_string_define, 'Quantity Unit')
    #加ppm相应的字符串
    add_Strings(ppm_string)
    #SubjectRelation里的MpcUnits要加上Q_PARTS_PER_MILLION
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
