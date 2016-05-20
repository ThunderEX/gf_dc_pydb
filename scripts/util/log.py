# -*- coding: utf-8 -*-
import sys
import logging

py3 = sys.version_info[0] >= 3
if py3:
    unicode = str
    basestring = str
else: 
    uni_chr = unichr

def setup_logger(logger_name, log_file, level=logging.DEBUG):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s    %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w', encoding='UTF-8')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setLevel(logging.INFO)
    streamHandler.setFormatter(formatter)
    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)  

setup_logger('dc', 'dclog.log')
dclog = logging.getLogger('dc')

def log(str):
    if not isinstance(str, unicode):
        str = str.decode('utf-8')
    dclog.info(str)

def debug(str):
    if not isinstance(str, unicode):
        str = str.decode('utf-8')
    dclog.debug(str)

def comment(str):
    for s in str.split('\n'):
        if not isinstance(s, unicode):
            s = s.decode("utf-8")
        dclog.info(s)
