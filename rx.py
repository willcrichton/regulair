from abc import ABC
import mantle
import magma as m
from character_matcher import CharacterMatcher

EPSILON = ''


def multi_wire(inp, out):
    for o in out:
        m.wire(inp, o)


class Expr(ABC):
    def to_circuit(self, charin):
        raise NotImplemented

    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)


class C(Expr):
    def __init__(self, c):
        self._c = c

    def to_circuit(self, charin):
        and_ = mantle.And(2)

        ff = mantle.DFF()
        m.wire(ff.O, and_.I0)

        matcher = CharacterMatcher(self._c)
        m.wire(charin, matcher.char)
        m.wire(matcher.match, and_.I1)

        return (ff.I, and_.O)


class Or(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

    def to_circuit(self, charin):
        (li, lo) = self._l.to_circuit(charin)
        (ri, ro) = self._l.to_circuit(charin)

        or_ = mantle.Or(2)
        or_(lo, ro)

        b = m.Bit()
        m.wire(b, li)
        m.wire(b, ri)

        return (b, or_.O)


class And(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

    def to_circuit(self, charin):
        (li, lo) = self._l.to_circuit(charin)
        (ri, ro) = self._l.to_circuit(charin)

        and_ = mantle.And(2)
        and_(lo, ro)

        b = m.Bit()
        m.wire(b, li)
        m.wire(b, ri)

        return (b, or_.O)


class Star(Expr):
    def __init__(self, rx):
        self._rx = rx

    def to_circuit(self, charin):
        (i, o) = self._rx.to_circuit(charin)

        andin = mantle.And(2)
        andout = mantle.And(2)

        m.wire(o, andin.I1)
        m.wire(o, andout.I1)
        m.wire(andin.O, i)

        b = m.Bit()
        m.wire(b, andin.I0)
        m.wire(b, andout.I0)

        return (b, andout.O)


if __name__ == '__main__':
    print(Star(C('x') | C('y')) & C('z'))
