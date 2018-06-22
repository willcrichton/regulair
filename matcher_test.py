import magma as m
from magma.bit_vector import BitVector
from magma.simulator.python_simulator import PythonSimulator
import matcher
from regex import *


def char_to_bv(c):
    assert(len(c) == 1)
    return BitVector(ord(c), num_bits=8)


if __name__ == "__main__":
    rx = C('x')
    my_matcher = matcher.DefineMatcher(rx)
    simulator = PythonSimulator(my_matcher, clock=my_matcher.CLK)

    def simulate(s):
        for c in s:
            print ("####  c = %s  ####" % c)
            simulator.set_value(my_matcher.char, c)
            simulator.advance(2)
            print (simulator.get_value(my_matcher.match))

    string = ".x"
    s = [char_to_bv(c) for c in string]

    simulate(s)
