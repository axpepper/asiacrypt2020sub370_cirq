import cirq
from cirq import protocols

class Fanout(cirq.ops.CCXPowGate):
    def _circuit_diagram_info_(self, args: 'protocols.CircuitDiagramInfoArgs'
                              ) -> 'protocols.CircuitDiagramInfo':
        return protocols.CircuitDiagramInfo(
            ('@', '@', 'K'),
            exponent=self._diagram_exponent(args))

class UnCompute(cirq.ops.CCXPowGate):
    def _circuit_diagram_info_(self,
                               args: 'protocols.CircuitDiagramInfoArgs'
                               ) -> 'protocols.CircuitDiagramInfo':
        return protocols.CircuitDiagramInfo(
            ('@', '@', 'U'),
            exponent=self._diagram_exponent(args))


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


def append_measurements(circuit, conf):
    for i in range(8):
        circuit.append(cirq.measure(conf.U[i], key='U' + str(i)))
    for i in range(8):
        circuit.append(cirq.measure(conf.S[i], key='S' + str(i)))
    for i in range(4):
        circuit.append(cirq.measure(conf.T[i], key='T' + str(i)))
    for i in range(5):
        circuit.append(cirq.measure(conf.G[i], key='G' + str(i)))


def read_meas_results(register, result):
    quantum_u_values = []
    for qubit in register:
        quantum_u_values += [int(result.measurements[qubit.name])]
    return quantum_u_values


def count_gates(circuit):
    gate_counts = {}

    for moment in circuit:
        for op in moment:

            gate_name = type(op.gate).__name__
            if gate_name not in gate_counts.keys():
                gate_counts[gate_name] = 0

            gate_counts[gate_name] = gate_counts[gate_name] + 1

    print(gate_counts)
    return gate_counts


FANOUT = Fanout()
UNCOMPUTE = UnCompute()
