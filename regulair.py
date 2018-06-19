import magma as m
m.set_mantle_target("ice40")

from mantle import Counter
from loam.boards.icestick import IceStick

from rx import *
from nfa import *


def to_fpga(rx):
    nfa = NFA(rx)

    icestick = IceStick()
    icestick.Clock.on()

    main = icestick.DefineMain()

    # TODO

    m.EndDefine()

    m.compile('regulair', main)


if __name__ == '__main__':
    rx = Star(C('x') | C('y')) & C('z')
    to_fpga(rx)
