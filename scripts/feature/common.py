# -*- coding: utf-8 -*-
import os, re
from ..template.tpl import template
from ..util.log import *
from ..tables import *
from ..models import *

languages = {
    "Developer"  : 0,
    "Danish"     : 1,
    "German"     : 2,
    "French"     : 3,
    "Italian"    : 4,
    "Spanish"    : 5,
    "Portuguese" : 6,
    "Greek"      : 7,
    "Dutch"      : 8,
    "Swedish"    : 9,
    "Finnish"    : 10,
    "Polish"     : 11,
    "Russian"    : 12,
    "Korean"     : 13,
    "Chinese"    : 14,
    "Japanese"   : 15,
    "Turkish"    : 16,
    "Czech"      : 17,
    "English"    : 18,
    "Hungarian"  : 19,
    "Estonian"   : 20,
    "Bulgarian"  : 21,
    "Slovenian"  : 22,
    "Croatian"   : 23,
    "Lithuanian" : 24,
    "Thai"       : 25,
    "Indonesian" : 26,
    "Latvia"     : 27,
}

def update_string(_id, _language, string):
    if _language not in languages.keys():
        log('Unrecognized language!!')
        raise NameError
    table = Strings()
    table.update(id=_id, language_id=languages[_language], String=string)


def insert_empty_strings(_language):
    if _language not in languages.keys():
        log('Unrecognized language!!')
        raise NameError
    language_id = languages[_language]
    result = Languages().get(id=language_id)
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


def append_sys_alarm(num_of_added_items):
    comment('在4.5.x里，因为加了一项在4.5.1 System Alarm里，导致后面的4.5.2 Pump Alarm等内容错位，需要先将write_state依次后推')
    #1464 | 4.5.2.x PumpAlarms (onoffauto) slippoint, WriteState=30是Pump alarm里第一项
    table = WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay()
    result = table.get(id=1464)
    first_write_state_in_pump_alarm = result.WriteState
    new_write_state_in_sys_alarm = first_write_state_in_pump_alarm
    comment("新加System Alarm位置为：%d" % (new_write_state_in_sys_alarm))

    results = table.query(WriteState__gte = first_write_state_in_pump_alarm, suppress_log=True)  #query >= first_write_state_in_pump_alarm
    state_list = []
    for result in results:
        _id = getattr(result, 'id')
        # 4293 | 4.4.2 DigitalInputs DI9 IO351-43 WDP WriteState=30
        # 4375 | wizard.14 DigitalInputs DI9 IO351-43 WDP WriteState=30
        if _id in [4293, 4375]:
            continue
        value = getattr(result, 'WriteState')
        # 都向后移num_of_added_items个位置
        state_list.append([_id, value + num_of_added_items])
    for l in state_list:
        table.update(id=l[0], WriteState=l[1])
        # comment('更新表WriteValueToDataPointAtKeyPressAndJumpToSpecificDisplay，id=%d, WriteState=%d' %(l[0], l[1]))
    return new_write_state_in_sys_alarm

def change_profile_version_code(new_ver_code):
    new_ver_code = str(new_ver_code)
    comment('更新版本号为%s' % (new_ver_code))
    table = IntDataPoint(id='profile_ver_code', Type='U8', QuantityType='Q_NO_UNIT')
    _id = table.model.id
    table.update(id=_id, Min=new_ver_code, Max=new_ver_code, Value=new_ver_code)   
