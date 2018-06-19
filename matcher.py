import magma
import mantle
import rx


def DefineMatcher(regex: rx.Expr):
    CharType = magma.UInt(8)

    class _Matcher(magma.Circuit):
        name = "Matcher"
        IO = [
            #"o_debug", magma.Out(magma.Bit),
            #"done_bit_debug", magma.Out(magma.Bit),
            "char", magma.In(CharType),
            #"done", magma.Out(magma.Bit),
            "match", magma.Out(magma.Bit)
        ] + magma.ClockInterface()

        @classmethod
        def definition(io):
            (i, o) = regex.to_circuit(io.char)

            magma.wire(1, i)

            magma.wire(o, io.match)

            #match_ff = mantle.DFF(init=0, has_ce=True)
            #done_ff = mantle.DFF(init=0, has_ce=True)

            #magma.wire(o, match_ff.I)
            #done_bit = mantle.eq(io.char, magma.uint(0, 8))
            #magma.wire(done_bit, done_ff.I)

            #magma.wire(done_ff.O, io.done)
            #magma.wire(match_ff.O, io.match)

            #magma.wire(~done_bit, done_ff.CE)
            #magma.wire(~(done_bit | done_ff.O), match_ff.CE)

            #magma.wire(o, io.o_debug)
            #magma.wire(done_bit, io.done_bit_debug)

    return _Matcher


def Matcher(regex: rx.Expr):
    return DefineMatcher(regex)()
