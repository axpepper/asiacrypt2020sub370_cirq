import cirq

from sage.all import *
from itertools import combinations, permutations
from sbox_gates import *

class SboxVariables():
    def __init__(self):
        self.U = [
            cirq.NamedQubit("U" + str(i)) for i in range(8)
        ]
        self.T = [
            cirq.NamedQubit("T" + str(i)) for i in range(6)
        ]
        # self.g, self.d, self.h, self.i = self.T
        # S = eng.allocate_qureg(8)
        self.S = [
            cirq.NamedQubit("S" + str(i)) for i in range(8)
        ]


def configure_circuit_input(configuration, orig_circuit=None, input_bit_list = []):
    moment_ops = []
    for k in range(len(input_bit_list)):  # initialize Ubox to given ival
        if input_bit_list[k]:
            # X | U[k]
            # circuit.append()
            moment_ops.append(cirq.ops.X.on(configuration.U[k]))

    # TODO: Doubts
    circuit = cirq.Moment(moment_ops) + orig_circuit

    return circuit

def main():

    conf = SboxVariables()
    print("created vars...")

    circuit = cirq.Circuit()
    circuit.append(algorithm_3(conf.U, conf.T))
    circuit.append(algorithm_4(conf.U, conf.T, conf.S))
    print(f"First count: {count_gates(circuit)}")


    print("*** Formulas ***")
    print("---> New")
    count_gates(circuit)