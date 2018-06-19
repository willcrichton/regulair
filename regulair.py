import magma as m
m.set_mantle_target("ice40")

import mantle
from mantle import Counter, Memory
from loam.boards.icestick import IceStick

from rx import *
from nfa import *
from matcher import Matcher


def char_input(string):
    string += '\0'
    counter = Counter(9)
    tab = [ord(string[i]) for i in range(len(string))]
    rom = Memory(height=512, width=8, rom=tab, readonly=True)
    return rom(counter)


def to_fpga(rx):

    icestick = IceStick()
    icestick.Clock.on()

    main = icestick.DefineMain()

    inp = char_input('zzxy')
    matcher = Matcher(rx)

    m.wire(inp, matcher.char)

    m.wire(matcher.match, ??)
    m.wire(matcher.done, ??)

    m.EndDefine()

    m.compile('regulair', main)


if __name__ == '__main__':
    #rx = Star(C('x') | C('y')) & C('z')
    rx = C('x') | C('y')
    to_fpga(rx)
