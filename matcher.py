import magma
import rx

def DefineMatcher(regex : rx.Expr):
    CharType = magma.UInt(7)

    class _Matcher(magma.Circuit):
        name = "Matcher"
        IO = ["char", magma.In(CharType),
              "done", magma.Out(magma.Bit),
              "match", magma.Out(magma.Bit)]

        @classmethod
        def definition(io):
            magma.wire(io.char[0], io.done)
            magma.wire(0, io.match)

    return _Matcher

def Matcher(regex : rx.Expr):
    return DefineMatcher(regex)()
