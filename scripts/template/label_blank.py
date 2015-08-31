# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *
from base import Base

class LabelBlank(Base):

    ''' Add new blank line in speific listview '''

    listview_id = ''              #: listview id which will include the new blank line

    def update_parameters(self):
        self.parameters = [
            (DisplayListViewItem,
             {
                 'ListViewId': self.listview_id,
             }
             ),
        ]
