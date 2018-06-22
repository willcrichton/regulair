from abc import ABC
import magma as m
import mantle
from character_matcher import CharacterMatcher


EPSILON = ''


class Expr(ABC):
    def to_circuit(self, char_in):
        raise NotImplemented

    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)


class C(Expr):
    def __init__(self, c):
        self._c = c

    def to_circuit(self, char_in):
        and_ = mantle.And(2)

        ff = mantle.DFF()
        m.wire(ff.O, and_.I0)

        matcher = CharacterMatcher(self._c)
        m.wire(char_in, matcher.char)
        m.wire(matcher.match, and_.I1)

        return (ff.I, and_.O)


class Or(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

    def to_circuit(self, char_in):
        (li, lo) = self._l.to_circuit(char_in)
        (ri, ro) = self._l.to_circuit(char_in)

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

    def to_circuit(self, char_in):
        (li, lo) = self._l.to_circuit(char_in)
        (ri, ro) = self._l.to_circuit(char_in)

        and_ = mantle.And(2)
        and_(lo, ro)

        b = m.Bit()
        m.wire(b, li)
        m.wire(b, ri)

        return (b, and_.O)


class Star(Expr):
    def __init__(self, regex):
        self._regex = regex

    def to_circuit(self, char_in):
        (i, o) = self._regex.to_circuit(char_in)

        orin = mantle.Or(2)
        orout = mantle.Or(2)

        m.wire(o, orin.I1)
        m.wire(o, orout.I1)
        m.wire(orin.O, i)

        b = m.Bit()
        m.wire(b, orin.I0)
        m.wire(b, orout.I0)

        return (b, orout.O)


if __name__ == '__main__':
    print(Star(C('x') | C('y')) & C('z'))
