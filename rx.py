from abc import ABC

EPSILON = ''

class Expr(ABC):
    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

    
class C(Expr):
    def __init__(self, c):
        self._c = c

class Or(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

class And(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

class Star(Expr):
    def __init__(self, rx):
        self._rx = rx

if __name__ == '__main__':
    print(Star(C('x') | C('y')) & C('z'))
