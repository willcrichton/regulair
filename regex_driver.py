import magma as m
from loam.boards.icestick import IceStick

icestick = IceStick()
icestick.Clock.on()

main = icestick.main()

m.EndCircuit()
