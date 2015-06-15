# -*- coding: utf-8 -*-
import logging
fn = 'dclog.log'
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s [line:%(lineno)d]    %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S',
                    encoding="UTF-8",
                    filename=fn,
                    filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
#formatter = logging.Formatter('%(filename)s [line:%(lineno)d]     %(message)s')
formatter = logging.Formatter('%(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

log = logging.info
debug = logging.debug


def comment(str):
    for s in str.split('\n'):
        s = s.decode("utf-8")
        logging.info(s)
