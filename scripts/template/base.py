# -*- coding: utf-8 -*-
from ..models import *
from ..tables import *

def save_decorator(parameters):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            rtn = []
            for index, para in enumerate(parameters):
                table = para[0]
                kwargs = para[1]
                x = table(**kwargs)
                func(x)
                rtn.append(x)
            return rtn
        return wrapper
    return decorator

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
