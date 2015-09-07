# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class Base(object):

    ''' Base class '''
    parameters = []
    description = 'No description'

    def update_parameters(self):
        pass

    def save_with_parameters(self, parameters):
        #必须先add，然后后面的table才会找到某些键值，所以不能用下面这种写法
        #rtn = map(lambda x: x[0](**x[1]), parameters)
        #[f.add() for f in rtn]
        rtn = []
        for index, para in enumerate(parameters):
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            x.add()
            rtn.append(x)
        return rtn

    def save(self):
        comment(self.description)
        self.update_parameters()
        return self.save_with_parameters(self.parameters)


class Label(Base):

    label_parameters = []
    string_parameters = []
    display_listview_parameters = []
    available_rule_parameters = []

    def handle_DisplayListViewItemAndComponents(self, display_listview_parameters):
        """DisplayListViewItem和DisplayListViewItemComponents是相互关联的，用本函数处理一下"""
        display_listview_item_components_list = []
        for para in display_listview_parameters:
            table = para[0]
            kwargs = para[1]
            x = table(**kwargs)
            if table == DisplayListViewItem:
                display_listview_item = x
            if table == DisplayListViewItemComponents:
                display_listview_item_components_list.append(x)

        # index 从0开始遍历一遍
        for i in range(0, display_listview_item.model.Index):
            try:
                r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=i)
                if r:
                    # 通过id查询DisplayListViewItemComponents里是否已经有挂在该id下的
                    s = DisplayListViewItemComponents_Model.get(ListViewItemId=r.id)
                    if s:
                        for display_listview_item_components in display_listview_item_components_list:
                            if display_listview_item_components.model.ComponentId == s.ComponentId:
                                log(("DisplayListViewItemComponents已有该记录").decode('utf-8'))
                                return
            except:
                debug(("未找到记录").decode('utf-8'))
        display_listview_item.add()
        for x in display_listview_item_components_list:
            r = DisplayListViewItem_Model.get(ListViewId=display_listview_item.model.ListViewId, Index=display_listview_item.model.Index)
            x.model.ListViewItemId = r.id
            if self.available_rule_name:
                for index, para in enumerate(self.available_rule_parameters):
                    if para[0] == DisplayListViewItemComponents:
                        self.available_rule_parameters[index][1]['ListViewItemId'] = r.id        #确保rule里的listviewitemid和label的一样，TODO 这里实现可以，但总觉得扩展性不好
            x.add()

    def increase_listview_item_index(self):
        ''' 把新加的listviewitem的Index改成中间的Index，并把大于这个值的Index都加1 '''
        if hasattr(self, 'listviewitem_index') and self.listviewitem_index is not 0:
            table = DisplayListViewItem(ListViewId=self.listview_id)
            max_idx = table.model.Index - 1
            listviewitem_model = DisplayListViewItem_Model()
            r = listviewitem_model.select().where(ListViewId=table.model.ListViewId)
            id_idx_list = [(i.id, i.Index) for i in r]
            for item in id_idx_list:
                if item[1] == max_idx:       # 新加入的item的Index是最大的，将其改为指定的index
                    table.update(id=item[0], Index=self.listviewitem_index)
                    continue
                if item[1] >= self.listviewitem_index:  # 其它大于指定index的item，将其index加1
                    table.update(id=item[0], Index=item[1]+1)


    def save(self):
        comment(self.description)
        self.update_parameters()
        self.save_with_parameters(self.string_parameters)
        self.save_with_parameters(self.label_parameters)
        self.handle_DisplayListViewItemAndComponents(self.display_listview_parameters)
        self.save_with_parameters(self.available_rule_parameters)
