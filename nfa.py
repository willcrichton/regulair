from rx import *
from collections import defaultdict

class State(object):
    def __init__(self):
        self._transitions = defaultdict(list)

    def add_transition(self, inp, state):
        self._transitions[inp].append(state)

class NFA(object):
    def __init__(self, rx):
        (q, f) = self._rx_to_nfa(rx)
        self._input = q
        self._output = f

    def _rx_to_nfa(self, rx):
        q = State()
        f = State()

        if isinstance(rx, C):
            q.add_transition(rx._c, f)

        elif isinstance(rx, Or):
            (q1, f1) = self._rx_to_nfa(rx._l)
            (q2, f2) = self._rx_to_nfa(rx._r)
            q.add_transition(EPSILON, q1)
            f1.add_transition(EPSILON, f)
            q.add_transition(EPSILON, q2)
            f2.add_transition(EPSILON, f)

        elif isinstance(rx, And):
            (q1, f1) = self._rx_to_nfa(rx._l)
            (q2, f2) = self._rx_to_nfa(rx._r)
            q.add_transition(EPSILON, q1)
            f1.add_transition(EPSILON, q2)
            f2.add_transition(EPSILON, f)

        elif isinstance(rx, Star):
            (q1, f1) = self._rx_to_nfa(rx._rx)
            q.add_transition(EPSILON, q1)
            q.add_transition(EPSILON, f)
            f1.add_transition(EPSILON, f)
            f1.add_transition(EPSILON, q1)

        return (q, f)
            
            

if __name__ == '__main__':
    nfa = NFA(Star(C('x') | C('y')) & C('z'))

