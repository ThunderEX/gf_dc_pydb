# -*- coding: utf-8 -*-

from util.log import *
from models import *
from tables import *
from parameters import *


def handle_DisplayListViewItemAndComponents(display_listview_item, display_listview_item_components_list):
    """DisplayListViewItem和DisplayListViewItemComponents是相互关联的，用本函数处理一下"""
    #index 从0开始遍历一遍
    for i in range(0, display_listview_item.model.Index):
        try:
            r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=i)
            if r:
                #通过id查询DisplayListViewItemComponents里是否已经有挂在该id下的
                s = DisplayListViewItemComponents_Model.get(ListViewItemId=r.id)
                if s:
                    for display_listview_item_components in display_listview_item_components_list:
                        if display_listview_item_components.model.ComponentId == s.ComponentId:
                            log(("DisplayListViewItemComponents已有该记录").decode('utf-8'))
                            return
        except :
            log(("未找到记录").decode('utf-8'))
    display_listview_item.add()
    for x in display_listview_item_components_list:
        r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=display_listview_item.model.Index)
        x.model.ListViewItemId = r.id
        x.add()


def add_label(label_parameters):
    rtn = []
    display_listview_item_components_list = []
    for para in label_parameters:
        table = para[0]
        kwargs = para[1]
        x = table(**kwargs)
        if table == DisplayListViewItem:
            display_listview_item = x
            continue
        if table == DisplayListViewItemComponents:
            display_listview_item_components_list.append(x)
            continue
        x.add()
        rtn.append(x)
    handle_DisplayListViewItemAndComponents(display_listview_item, display_listview_item_components_list)
    return rtn


def add_observer(parameters):
    rtn = []
    for para in parameters:
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


def add_data(parameters, type='normal'):
    '''
        数据库添加数据
    
    :param parameters: 参数list
    :param type: 类型
    :return: tables实例形成的list
    '''
    rtn = []
    if type.lower() == 'label':
        rtn = add_label(parameters)
    elif type.lower() == 'observer':
        rtn = add_observer(parameters)
    else:
        for para in parameters:
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            x.add()
            rtn.append(x)
    return rtn
