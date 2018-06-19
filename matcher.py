import magma
import rx


def DefineMatcher(regex: rx.Expr):
    CharType = magma.UInt(8)

    class _Matcher(magma.Circuit):
        name = "Matcher"
        IO = [
            "char",
            magma.In(CharType), "done",
            magma.Out(magma.Bit), "match",
            magma.Out(magma.Bit)
        ]

        @classmethod
        def definition(io):
            (i, o) = regex.to_circuit(io.char)

            magma.wire(1, i)
            magma.wire(o, io.match)

            # TODO
            magma.wire(io.char[0], io.done)

    return _Matcher


def Matcher(regex: rx.Expr):
    return DefineMatcher(regex)()
