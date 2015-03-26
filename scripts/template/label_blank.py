# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

class LabelBlank(object):
    '''
        Add new blank line in speific listview
    '''
    listview_id = ''              #: listview id which will include the new blank line

    def __init__(self):
        self.parameters = []
        self.description = 'No description'

    def update_parameters(self):
        self.parameters = [
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
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
            x.add()
            rtn.append(x)
        return rtn
