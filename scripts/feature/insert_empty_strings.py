# -*- coding: utf-8 -*-

from ..template.tpl import template
from ..util.log import *
from ..tables import *
from ..models import *

def insert_empty_strings(language_id):
    result = Languages_Model.get(id=language_id)
    lang = result.uk_name.encode('ascii', 'ignore')
    comment('为所有字符串的%s语言插入空值' % (lang))
    comment('过程缓慢，请耐心等待...')
    table = Strings()
    sql = "INSERT INTO Strings ( Id, LanguageId, [String] ) SELECT Strings.Id, Languages.Id, '' AS Expr1 FROM Strings, Languages WHERE (((Languages.Id)=%d) AND ((Strings.LanguageId)=0) AND (([Strings].[Id]*100+[Languages].[Id]) Not In (select id_lang from id_lang)));" % language_id
    table.model.raw_execute(sql)


def insert_empty_strings_for_all_languages(min_id, max_id):
    comment('为id从%d到%d的字符串插入所有语言的空值' % (min_id, max_id))
    comment('过程缓慢，请耐心等待...')
    table = Strings()
    sql = "INSERT INTO Strings ( Id, LanguageId, [String] ) SELECT Strings.Id, Languages.Id, '' AS Expr1 FROM Strings, Languages WHERE ( ((Strings.LanguageId)=0) AND (Strings.Id BETWEEN %d AND %d) AND (([Strings].[Id]*100+[Languages].[Id]) Not In (select id_lang from id_lang)));" % (min_id, max_id)
    table.model.raw_execute(sql)
