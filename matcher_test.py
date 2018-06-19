from magma.bit_vector import BitVector
from magma.simulator.python_simulator import PythonSimulator
import matcher
from rx import *

import magma

def char_to_bv(c):
    assert(len(c) == 1)
    return BitVector(ord(c), num_bits=8)


if __name__ == "__main__":


    '''
    from character_matcher import *
    ma = DefineCharacterMatcher("x")
    simulator = PythonSimulator(ma)
    simulator.set_value(ma.char, BitVector(120, 8))
    simulator.evaluate()
    print (simulator.get_value(ma.match))
    exit(0)
    '''

    '''
    class Foo(magma.Circuit):
        name = "Foo"
        IO = ["inp", magma.In(magma.Bit), "out", magma.Out(magma.Bit)] + magma.ClockInterface()

        @classmethod
        def definition(io):
            val = m.uint(ord('x'), 8)
            (i, o) = C('x').to_circuit(val)
            magma.wire(io.inp, i)
            magma.wire(o, io.out)
    
    simulator = PythonSimulator(Foo, clock=Foo.CLK)

    simulator.set_value(Foo.inp, 1)
    simulator.advance(2)
    print (simulator.get_value(Foo.out))
    #print (simulator.get_value(Foo.tmp))

    simulator.set_value(Foo.inp, 1)
    simulator.advance(2)
    print (simulator.get_value(Foo.out))
    #print (simulator.get_value(Foo.tmp))

    exit(0)
    '''

    rx = C('x') #| C('y')
    my_matcher = matcher.DefineMatcher(rx)
    simulator = PythonSimulator(my_matcher, clock=my_matcher.CLK)

    def simulate(s):
        for c in s:
            print ("###############################################")
            simulator.set_value(my_matcher.char, c)
            simulator.advance(2)
            print (
                #simulator.get_value(my_matcher.done),
                simulator.get_value(my_matcher.match),
                #simulator.get_value(my_matcher.o_debug),
                #simulator.get_value(my_matcher.char),
                #simulator.get_value(my_matcher.done_bit_debug),
            )

    string = ".x"
    s = [char_to_bv(c) for c in string]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [BitVector(0, 8)]
    s += [char_to_bv(c) for c in "afafasdfdasf"]
    
    simulate(s)

    #assert simulator.get_value(Adder4.out) == int2seq(6, 4)
    #assert simulator.get_value(Adder4.out) == BitVector(6, num_bits=4)
    #assert simulator.get_value(Adder4.cout) == False
    #print("Success!")
