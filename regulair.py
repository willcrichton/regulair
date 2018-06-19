import magma as m
m.set_mantle_target("ice40")

import mantle
from mantle import Counter, Memory
from loam.boards.icestick import IceStick

import math

from rx import *
from nfa import *
from matcher import Matcher


def string_to_rom(string):
    ADDR_BITS = 9
    assert(len(string) <= (1 << ADDR_BITS))
    counter = Counter(ADDR_BITS)
    tab = [ord(string[i]) for i in range(len(string))]
    tab += [0 for _ in range((1 << ADDR_BITS) - len(string))]
    assert(len(tab) == 1 << ADDR_BITS)
    rom = Memory(height=(1 << ADDR_BITS), width=8, rom=tab, readonly=True)
    m.wire(1, rom.RE)
    return rom(counter.O)


def to_fpga(rx):
    icestick = IceStick()
    icestick.Clock.on()
    icestick.D1.on()
    #icestick.D2.on()

    main = icestick.DefineMain()

    rom = string_to_rom('x' * 16)
    matcher = Matcher(rx)

    m.wire(rom, matcher.char)
    m.wire(matcher.match, main.D1)
    #m.wire(matcher.done, main.D2)

    m.EndDefine()

    m.compile('regulair', main)


if __name__ == '__main__':
    #rx = Star(C('x') | C('y')) & C('z')
    rx = C('x') #| C('y')
    to_fpga(rx)
