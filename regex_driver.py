import magma
from loam.boards.icestick import IceStick
import matcher

icestick = IceStick()
icestick.Clock.on()
icestick.D1.on()
icestick.D2.on()

main = icestick.main()

matcher_circuit = matcher.generate_matcher()()
magma.wire(matcher_circuit.done, main.D1)
magma.wire(matcher_circuit.match, main.D2)

magma.EndCircuit()
