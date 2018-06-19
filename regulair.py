import magma as m
m.set_mantle_target("ice40")

import mantle
from loam.boards.icestick import IceStick

from rx import *
from nfa import *


def to_fpga(rx):

    icestick = IceStick()
    icestick.Clock.on()

    main = icestick.DefineMain()

    charin = ()
    (i, o) = rx.to_circuit(charin)

    # m.wire(Constant(1).O, i)
    # m.wire(o, ???)

    m.EndDefine()

    m.compile('regulair', main)


if __name__ == '__main__':
    #rx = Star(C('x') | C('y')) & C('z')
    rx = C('x') | C('y')
    to_fpga(rx)
