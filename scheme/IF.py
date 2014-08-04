__author__ = 'perkins'

from scheme.macro import Macro
from scheme.Globals import Globals
from zope.interface import implements


class IF(object):
    implements(Macro)
    def __init__(self):
        pass
    def __call__(self, processer, params):
        conditional = params[0]
        if_true = params[1]
        if_false = params[2] if len(params) == 3 else None
        env = processer.cenv.parent
        if isinstance(conditional, list):
            if processer.process(conditional, env):
                return if_true
            else:
                return if_false
        else:
            if conditional.toObject(env):
                return if_true
            else:
                return if_false


Globals['if'] = IF()