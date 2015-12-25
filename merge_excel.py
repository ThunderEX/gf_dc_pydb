# -*- coding: utf-8 -*-

import xlrd
from scripts.util.log import *
from scripts.util.prettytable import PrettyTable
from scripts.template.tpl import template
from scripts.tables import *
from scripts.models import *
from scripts.feature.common import *

ID_COLUMN = 10

class Cu361Texts(object):
    def __init__(self,):
        self.data = xlrd.open_workbook(r'..\cu3x1App_SRC\Control\LangGenerator\input\Cu361Texts.xls')
        self.table = self.data.sheet_by_name(u'Strings for translation')
        self.languages = [
            #language,    column, id
            ["Developer"  , 11   , 0  ,],     #L
            ["Danish"     , 12   , 1  ,],     #M
            ["German"     , 13   , 2  ,],     #N
            ["French"     , 14   , 3  ,],     #O
            ["Italian"    , 15   , 4  ,],     #P
            ["Spanish"    , 16   , 5  ,],     #Q
            ["Portuguese" , 17   , 6  ,],     #R
            ["Greek"      , 18   , 7  ,],     #S
            ["Dutch"      , 19   , 8  ,],     #T
            ["Swedish"    , 20   , 9  ,],     #U
            ["Finnish"    , 21   , 10 ,],     #V
            ["Polish"     , 22   , 11 ,],     #W
            ["Russian"    , 23   , 12 ,],     #X
            ["Korean"     , 24   , 13 ,],     #Y
            ["Chinese"    , 25   , 14 ,],     #Z
            ["Japanese"   , 26   , 15 ,],     #AA
            ["Turkish"    , 27   , 16 ,],     #AB
            ["Czech"      , 28   , 17 ,],     #AC
            ["English"    , 29   , 18 ,],     #AD
            ["Hungarian"  , 30   , 19 ,],     #AE
            ["Estonian"   , 31   , 20 ,],     #AF
            ["Bulgarian"  , 32   , 21 ,],     #AG
            ["Slovenian"  , 33   , 22 ,],     #AH
            ["Croatian"   , 34   , 23 ,],     #AI
            ["Lithuanian" , 35   , 24 ,],     #AJ
            # ["Thai"       , None , 25 ,],     
            ["Indonesian" , 36   , 26 ,],     #AK
            ["Latvia"     , 37   , 27 ,],     #AL
        ]

    def export(self, id):
        cell_row = id + 7
        cell_id = self.table.cell(cell_row, ID_COLUMN).value
        cell_type = self.table.cell(cell_row, 0).value
        if cell_type == u"Don't translate":
            log("id:%d 不需要翻译" % int(cell_id))
            return
        for i in self.languages:
            cell_value = self.table.cell(cell_row, i[1]).value
            if '"' in cell_value:
                log("id:%d,语言%s- 注意，有双引号，请手动合并" %(cell_id, i[0]))
                continue
            update_string(id, i[0], cell_value)

    def export_range(self, start_id, end_id):
        for i in range(start_id, end_id+1):
            self.export(i)

    def export_all(self):
        rows = self.table.nrows
        max_id = rows - 7
        self.export_range(0, max_id)
        

if __name__ == '__main__':
    texts = Cu361Texts()
    texts.export(638)
    texts.export_range(2005, 2021)
    texts.export_range(2076, 2087)
