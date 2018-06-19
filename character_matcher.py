import magma
import mantle

def DefineCharacterMatcher(c : str):
    assert(len(c) == 1)
    CharType = magma.UInt(7)

    class _CharacterMatcher(magma.Circuit):
        name = "CharacterMatcher_" + c
        IO = ["char", magma.In(CharType),
              "match", magma.Out(magma.Bit)]

        @classmethod
        def definition(io):
            comp = mantle.EQ(7)
            magma.wire(io.char, comp.in0)
            magma.wire(io.char, comp.in1)
            magma.wire(comp.out, io.match)

    return _CharacterMatcher

def CharacterMatcher(c : str):
    assert(len(c) == 1)
    return DefineCharacterMatcher(c)()
