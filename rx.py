from abc import ABC
import mantle
import magma as m

EPSILON = ''


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

        # comparator = ()
        # m.wire(charin, comparator.I)
        # m.wire(comparator.O, and_.I1)

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

        return ([li, ri], or_.O)


class And(Expr):
    def __init__(self, l, r):
        self._l = l
        self._r = r

    def to_circuit(self, charin):
        (li, lo) = self._l.to_circuit(charin)
        (ri, ro) = self._l.to_circuit(charin)

        and_ = mantle.And(2)
        and_(lo, ro)

        return ([li, ri], or_.O)


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

        return ([andin.I0, andout.I0], andout.O)


if __name__ == '__main__':
    print(Star(C('x') | C('y')) & C('z'))
