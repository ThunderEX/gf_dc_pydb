# -*- coding: utf-8 -*-
import sys
import logging

py3 = sys.version_info[0] >= 3
if py3:
    unicode = str
    basestring = str
else: 
    uni_chr = unichr

# fn = 'dclog.log'
# logging.basicConfig(level=logging.DEBUG,
                    # format='%(asctime)s %(filename)s [line:%(lineno)d]    %(message)s',
                    # datefmt='%Y/%m/%d %H:%M:%S',
                    # encoding="UTF-8",
                    # filename=fn,
                    # filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
#formatter = logging.Formatter('%(filename)s [line:%(lineno)d]     %(message)s')
# formatter = logging.Formatter('%(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d]    %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w', encoding='UTF-8')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
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
