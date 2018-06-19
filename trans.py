from rx import *
from nfa import *


def to_fpga(rx):
    nfa = NFA(rx)

    # TODO!


if __name__ == '__main__':
    rx = Star(C('x') | C('y')) & C('z')
    to_fpga(rx)
