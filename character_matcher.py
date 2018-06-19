import magma
import mantle


def DefineCharacterMatcher(c: str):
    assert (len(c) == 1)
    CharType = magma.UInt(8)

    class _CharacterMatcher(magma.Circuit):
        name = "CharacterMatcher_" + c
        IO = ["char", magma.In(CharType), "match", magma.Out(magma.Bit)]

        @classmethod
        def definition(io):
            comp = mantle.EQ(8)
            magma.wire(magma.uint(ord(c[0]), 8), comp.I0)
            magma.wire(io.char, comp.I1)
            magma.wire(comp.O, io.match)

    return _CharacterMatcher


def CharacterMatcher(c: str):
    assert (len(c) == 1)
    return DefineCharacterMatcher(c)()
