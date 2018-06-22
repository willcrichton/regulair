import magma
import mantle
import regex


def DefineMatcher(regex: regex.Expr):
    CharType = magma.UInt(8)

    class _Matcher(magma.Circuit):
        name = "Matcher"
        IO = [
            "char", magma.In(CharType),
            "match", magma.Out(magma.Bit)
        ] + magma.ClockInterface()

        @classmethod
        def definition(io):
            (i, o) = regex.to_circuit(io.char)
            magma.wire(1, i)
            magma.wire(o, io.match)

    return _Matcher


def Matcher(regex: regex.Expr):
    return DefineMatcher(regex)()
