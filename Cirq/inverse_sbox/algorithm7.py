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
        self.Z = cirq.NamedQubit("Z")
        self.i = cirq.NamedQubit("i")
        self.j = cirq.NamedQubit("j")

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
    algorithm_6(circuit, conf.U, conf.T, conf.i)
    algorithm_7(circuit, conf.U, conf.T, conf.S, conf.Z, conf.i, conf.j)
    print(f"First count: {count_gates(circuit)}")

    print("*** Formulas ***")
    print("---> New")
    count_gates(circuit)
    print(circuit)
'''*****

 * The input of Algorithm 6 can be explained as follows:

 * U[0]=x_0, U[1]=x_1, U[2]=x_2, U[3]=x_3, U[4]=x_4, U[5]=x_5, U[6]=x_6, U[7]=x_7

 * T[0]=0, T[1]=0, T[2]=0, T[3]=0, T[4]=0, T[5]=0.

 * The output of Algorithm 6 can be explained as follows:

 * U[0]=y_7, U[1]=y_5, U[2]=y_4, U[3]=y_6, U[4]=y_1, U[5]=y_2, U[6]=y_0, U[7]=y_3

 * T[0]=t_29, T[1]=t_40, T[2]=t_33, T[3]=t_34, T[4]=t_37, T[5]=t_35.

*****'''

def algorithm_6(circuit, U, T, i):

    circuit.append(cirq.CNOT(U[3],U[7]))
    # U[7]=y_15

    circuit.append(cirq.X(U[7])) 
    # U[6]=y_14

    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    # T[0]=t_5

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[7],T[0])))
    # T[2]=t_5

    circuit.append(cirq.CNOT(T[0],T[2]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    # U[5]=y_17

    circuit.append(cirq.X(U[5])) 
    # U[7]=y_16

    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # T[0]=t_5 ^ t_3

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    # T[1]=t_5 ^ t_3

    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    # U[7]=y_9

    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    # U[6]=y_8

    circuit.append(cirq.X(U[6])) 
    # T[2]=t_5 ^ t_9

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[7],T[2])))
    # T[3]=t_5 ^ t_9

    circuit.append(cirq.CNOT(T[2],T[3]))
    # U[5]=y_13

    circuit.append(cirq.CNOT(U[6],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    # U[7]=y_12

    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # T[0]=t_5 ^ t_3 ^ t_6  ** first computation of t_6= U[5]& U[7]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    # T[2]=t_5 ^ t_9 ^ t_6  ** second computation of t_6= U[5]& U[7]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[2])))
    # As shown in the above (with **), we need to compute t_6 two times.

    # If we introduce a new qubit (i.e. T[6]) to store t_6, we can save one Toffoli gate and one Toffoli depth.

    # U[7]=y_11

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    # U[5]=y_10

    circuit.append(cirq.X(U[5])) 
    # T[1]=t_5 ^ t_3 ^ t_7  ** first computation of t_7= U[5]& U[7]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[1])))
    # T[3]=t_5 ^ t_9 ^ t_7  ** second computation of t_7= U[5]& U[7]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[3])))
    # As shown in the above (with **), we need to compute t_7 two times.

    # If we introduce a new qubit (i.e. T[7]) to store t_7, we can save one Toffoli gate and one Toffoli depth.

    # U[5]=y_7

    circuit.append(cirq.CNOT(U[6],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    # U[7]=y_3

    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    # T[0]=t_5 ^ t_3 ^ t_6 ^ t_2 =t_18 ^ y_21

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    # U[7]=y_6

    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.CNOT(U[7],U[1]))
    # U[1]=y_2

    circuit.append(cirq.X(U[1])) 
    # T[1]=t_5 ^ t_3 ^ t_7 ^ t_4 =t_20 ^ y_20

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[7],U[1],T[1])))
    # U[1]=y_5

    circuit.append(cirq.CNOT(U[7],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[3],U[4]))
    circuit.append(cirq.CNOT(U[2],U[4]))
    circuit.append(cirq.CNOT(U[1],U[4]))
    # U[4]=y_1

    circuit.append(cirq.X(U[4])) 
    # T[2]=t_5 ^ t_9 ^ t_6 ^ t_8 =t_22 ^ y_19

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[4],T[2])))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    # U[5]=y_4

    circuit.append(cirq.X(U[5])) 
    # U[6]=y_0

    circuit.append(cirq.CNOT(U[4],U[6]))
    # T[3]=t_5 ^ t_9 ^ t_7 ^ t_10 =t_24 ^ y_18

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[5],T[3])))
    # U[7]=y_21

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    # T[0]=t_18

    circuit.append(cirq.CNOT(U[7],T[0]))
    # U[5]=y_20

    circuit.append(cirq.CNOT(U[3],U[5]))
    # T[1]=t_20

    circuit.append(cirq.CNOT(U[5],T[1]))
    # U[7]=y_19

    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # T[2]=t_22

    circuit.append(cirq.CNOT(U[7],T[2]))
    # U[6]=y_18

    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    # T[3]=t_24

    circuit.append(cirq.CNOT(U[6],T[3]))
    # T[4]=t_26   ** first computation of t_26= T[1]& T[3]

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[4])))
    # T[3]=t_30

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[4]=t_31

    circuit.append(cirq.CNOT(T[0],T[4]))
    # T[5]=t_22

    circuit.append(cirq.CNOT(T[2],T[5]))
    # T[5]=t_33

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],T[4],T[5])))
    # T[4]=t_26,  we do not count this t_26, because we do not need Toffoli gate here.

    circuit.append(cirq.CNOT(T[0],T[4]))
    # T[4]=t_27

    circuit.append(cirq.CNOT(T[2],T[4]))
    # T[3]=t_24

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[5]=t_35

    circuit.append(cirq.CNOT(T[4],T[5]))
    # T[4]=t_38

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],T[2],T[4])))
    # T[2]=t_27   ** second computation of t_26= T[1]& T[3]

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[2])))
    # As shown in the above (with **), we need to compute t_26 two times.

    # If we introduce a new qubit (i.e. T[8]) to store t_26, we can save one Toffoli gate and one Toffoli depth.

    # T[1]=t_25

    circuit.append(cirq.CNOT(T[1],T[0]))
    # T[0]=t_29

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[2],T[0])))
    # T[1]=t_40

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[4],T[1])))
    # T[4]=t_36

    circuit.append(cirq.CNOT(T[2],T[4]))
    # T[2]=t_33

    circuit.append(cirq.CNOT(T[5],T[2]))
    # T[3]=t_34

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[3],T[4]))
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # U[7]=y_3

    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    # U[5]=y_2

    circuit.append(cirq.X(U[5])) 
    #  U[6]=y_0

    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    #  U[0]=y_7

    circuit.append(cirq.CNOT(U[5],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    #  U[3]=y_6

    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    # U[2]=y_4

    circuit.append(cirq.X(U[2])) 
'''*****

 * The input of Algorithm 7 can be explained as follows:

 * U[0]=y_7, U[1]=y_5, U[2]=y_4, U[3]=y_6, U[4]=y_1, U[5]=y_2, U[6]=y_0, U[7]=y_3

 * T[0]=t_29, T[1]=t_40, T[2]=t_33, T[3]=t_34, T[4]=t_37, T[5]=t_35

 * S[0]=0, S[1]=0, S[2]=0, S[3]=0, S[4]=0, S[5]=0, S[6]=0, S[7]=0.

 * The output of Algorithm 4 can be explained as follows:

 * U[0]=x_0, U[1]=x_1, U[2]=x_2, U[3]=x_3, U[4]=x_4, U[5]=x_5, U[6]=x_6, U[7]=x_7

 * T[0]=0, T[1]=0, T[2]=0, T[3]=0, T[4]=0, T[5]=0

 * S[0]=s_0, S[1]=s_1, S[2]=s_2, S[3]=s_3, S[4]=s_4, S[5]=s_5, S[6]=s_6, S[7]=s_7.

*****'''

def algorithm_7(circuit, U, T, S, Z, i, j):

    '''** This part is used to generate the output of S-box, the result is stored in S[] **'''

    # Z=z_0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[2],Z)))
    # S[0]=z_0

    circuit.append(cirq.CNOT(Z,S[0]))
    # S[6]=z_0

    circuit.append(cirq.CNOT(Z,S[6]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[2],Z)))
    # S[0]=z_0,  S[1]=0,  S[2]=0,     S[3]=0,

    # S[4]=0,    S[5]=0,  S[6]=z_0,   S[7]=0,

    # T[0]=t_45

    circuit.append(cirq.CNOT(T[1],T[0]))
    # U[2]=y_9

    circuit.append(cirq.CNOT(U[1],U[2]))
    # Z= z_1

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[2],Z)))
    # S[1]=z_1

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[3]=z_1

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[6]=z_0^z_1

    circuit.append(cirq.CNOT(Z,S[6]))
    # Z= 0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[2],Z)))
    # T[0]=t_29

    circuit.append(cirq.CNOT(T[1],T[0]))
    # U[2]=y_4

    circuit.append(cirq.CNOT(U[1],U[2]))
    # S[0]=z_0,  S[1]=z_1,  S[2]=0,        S[3]=z_1,

    # S[4]=0,    S[5]=0,    S[6]=z_0^z_1,  S[7]=0,

    # Z=z_2

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[1],Z)))
    # S[0]=z_0^z_2

    circuit.append(cirq.CNOT(Z,S[0]))
    # S[1]=z_1^z_2

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[3]=z_1^z_2

    circuit.append(cirq.CNOT(Z,S[3]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[1],Z)))
    # S[0]=z_0^z_2,  S[1]=z_1^z_2,  S[2]=0,        S[3]=z_1^z_2,

    # S[4]=0,        S[5]=0,        S[6]=z_0^z_1,  S[7]=0,

    # T[4]=t_44

    circuit.append(cirq.CNOT(T[1],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[2]=y_11

    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[1],U[2]))
    circuit.append(cirq.CNOT(U[0],U[2]))
    # Z=z_3

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[2],Z)))
    # S[0]=z_0^z_2^z_3

    circuit.append(cirq.CNOT(Z,S[0]))
    # S[2]=z_3

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[5]=z_3

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[6]=z_0^z_1^z_3

    circuit.append(cirq.CNOT(Z,S[6]))
    # S[7]=z_3

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[2],Z)))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[1],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[2]=y_4

    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[1],U[2]))
    circuit.append(cirq.CNOT(U[0],U[2]))
    # S[0]=z_0^z_2^z_3,  S[1]=z_1^z_2,    S[2]=z_3,          S[3]=z_1^z_2^z_3,

    # S[4]=0,            S[5]=z_3,        S[6]=z_0^z_1^z_3,  S[7]=z_3,

    # T[0]=t_42

    circuit.append(cirq.CNOT(T[2],T[0]))
    # U[1]=y_15

    circuit.append(cirq.CNOT(U[0],U[1]))
    # Z=z_4

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[1],Z)))
    # S[1]=z_1^z_2^z_4

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[6]=z_0^z_1^z_3^z_4

    circuit.append(cirq.CNOT(Z,S[6]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[1],Z)))
    # T[0]=t_29

    circuit.append(cirq.CNOT(T[2],T[0]))
    # U[1]=y_5

    circuit.append(cirq.CNOT(U[0],U[1]))
    # S[0]=z_0^z_2^z_3,  S[1]=z_1^z_2^z_4,  S[2]=z_3,              S[3]=z_1^z_2^z_3,

    # S[4]=0,            S[5]=z_3,          S[6]=z_0^z_1^z_3^z_4,  S[7]=z_3,

    # T[4]=t_43

    circuit.append(cirq.CNOT(T[1],T[4]))
    # U[3]=y_13

    circuit.append(cirq.CNOT(U[2],U[3]))
    # Z=z_5

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[3],Z)))
    # S[0]=z_0^z_2^z_3^z_5

    circuit.append(cirq.CNOT(Z,S[0]))
    # S[1]=z_1^z_2^z_4^z_5

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[2]=z_3^z_5

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[5]=z_3^z_5

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[7]=z_3^z_5

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[3],Z)))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[1],T[4]))
    # U[3]=y_6

    circuit.append(cirq.CNOT(U[2],U[3]))
    # S[0]=z_0^z_2^z_3^z_5,  S[1]=z_1^z_2^z_4^z_5,  S[2]=z_3^z_5,          S[3]=z_1^z_2^z_3^z_5,

    # S[4]=0,                S[5]=z_3^z_5,          S[6]=z_0^z_1^z_3^z_4,  S[7]=z_3^z_5,

    # Z=z_6

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[3],Z)))
    # S[2]=z_3^z_5^z_6

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5^z_6

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[5]=z_3^z_5^z_6

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[7]=z_3^z_5^z_6

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[3],Z)))
    # S[0]=z_0^z_2^z_3^z_5,  S[1]=z_1^z_2^z_4^z_5,  S[2]=z_3^z_5^z_6,      S[3]=z_1^z_2^z_3^z_5^z_6 ,

    # S[4]=0,                S[5]=z_3^z_5^z_6,      S[6]=z_0^z_1^z_3^z_4,  S[7]=z_3^z_5^z_6,

    # Z=z_8

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[0],Z)))
    # S[2]=z_3^z_5^z_6^z_8

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[5]=z_3^z_5^z_6^z_8

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[7]=z_3^z_5^z_6^z_8

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[0],Z)))
    # S[0]=z_0^z_2^z_3^z_5,  S[1]=z_1^z_2^z_4^z_5,  S[2]=z_3^z_5^z_6^z_8,  S[3]=z_1^z_2^z_3^z_5^z_6 ,

    # S[4]=0,                S[5]=z_3^z_5^z_6^z_8,  S[6]=z_0^z_1^z_3^z_4,  S[7]=z_3^z_5^z_6^z_8,

    # Z=z_9

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # S[2]=z_3^z_5^z_6^z_8^z_9

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5^z_6^z_9

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[6]=z_0^z_1^z_3^z_4^z_9

    circuit.append(cirq.CNOT(Z,S[6]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # S[0]=z_0^z_2^z_3^z_5,  S[1]=z_1^z_2^z_4^z_5,  S[2]=z_3^z_5^z_6^z_8^z_9,  S[3]=z_1^z_2^z_3^z_5^z_6^z_9 ,

    # S[4]=0,                S[5]=z_3^z_5^z_6^z_8,  S[6]=z_0^z_1^z_3^z_4^z_9,  S[7]=z_3^z_5^z_6^z_8,

    # T[1]=t_45

    circuit.append(cirq.CNOT(T[0],T[1]))
    # U[6]=y_8

    circuit.append(cirq.CNOT(U[4],U[6]))
    # Z=z_10

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # S[4]=z_10

    circuit.append(cirq.CNOT(Z,S[4]))
    # S[5]=z_3^z_5^z_6^z_8^z_10

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[6]=z_0^z_1^z_3^z_4^z_9^z_10

    circuit.append(cirq.CNOT(Z,S[6]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # T[1]=t_40

    circuit.append(cirq.CNOT(T[0],T[1]))
    # U[6]=y_0

    circuit.append(cirq.CNOT(U[4],U[6]))
    # S[0]=z_0^z_2^z_3^z_5,  S[1]=z_1^z_2^z_4^z_5,       S[2]=z_3^z_5^z_6^z_8^z_9,       S[3]=z_1^z_2^z_3^z_5^z_6^z_9 ,

    # S[4]=z_10,             S[5]=z_3^z_5^z_6^z_8^z_10,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10,  S[7]=z_3^z_5^z_6^z_8,

    # Z=z_11

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[4],Z)))
    # S[2]=z_3^z_5^z_6^z_8^z_9^z_11

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[4]=z_10^z_11

    circuit.append(cirq.CNOT(Z,S[4]))
    # S[5]=z_3^z_5^z_6^z_8^z_10^z_11

    circuit.append(cirq.CNOT(Z,S[5]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[4],Z)))
    # S[0]=z_0^z_2^z_3^z_5,    S[1]=z_1^z_2^z_4^z_5,            S[2]=z_3^z_5^z_6^z_8^z_9^z_11,  S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11,

    # S[4]=z_10^z_11,          S[5]=z_3^z_5^z_6^z_8^z_10^z_11,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10,  S[7]=z_3^z_5^z_6^z_8,

    # T[4]=t_44

    circuit.append(cirq.CNOT(T[1],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[7]=y_10

    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    # Z=z_12

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[7],Z)))
    # S[4]=z_10^z_11^z_12

    circuit.append(cirq.CNOT(Z,S[4]))
    # S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12

    circuit.append(cirq.CNOT(Z,S[6]))
    # S[7]=z_3^z_5^z_6^z_8^z_12

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[7],Z)))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[1],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[7]=y_3

    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    # S[0]=z_0^z_2^z_3^z_5,    S[1]=z_1^z_2^z_4^z_5,            S[2]=z_3^z_5^z_6^z_8^z_9^z_11,        S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11,

    # S[4]=z_10^z_11^z_12,     S[5]=z_3^z_5^z_6^z_8^z_10^z_11,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12 ,  S[7]=z_3^z_5^z_6^z_8^z_12 ,

    # T[0]=t_42

    circuit.append(cirq.CNOT(T[2],T[0]))
    # U[7]=y_14

    circuit.append(cirq.CNOT(U[4],U[7]))
    # Z=z_13

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[7],Z)))
    # S[1]=z_1^z_2^z_4^z_5^z_13

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13

    circuit.append(cirq.CNOT(Z,S[6]))
    # S[7]=z_3^z_5^z_6^z_8^z_12^z_13

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],U[7],Z)))
    # T[0]=t_29

    circuit.append(cirq.CNOT(T[2],T[0]))
    # U[7]=y_3

    circuit.append(cirq.CNOT(U[4],U[7]))
    # S[0]=z_0^z_2^z_3^z_5,    S[1]=z_1^z_2^z_4^z_5^z_13,       S[2]=z_3^z_5^z_6^z_8^z_9^z_11,            S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11,

    # S[4]=z_10^z_11^z_12,     S[5]=z_3^z_5^z_6^z_8^z_10^z_11,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13,  S[7]=z_3^z_5^z_6^z_8^z_12^z_13,

    # T[1]=t_43

    circuit.append(cirq.CNOT(T[4],T[1]))
    # U[6]=y_12

    circuit.append(cirq.CNOT(U[5],U[6]))
    # Z=z_14

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # S[1]=z_1^z_2^z_4^z_5^z_13^z_14

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[4]=z_10^z_11^z_14

    circuit.append(cirq.CNOT(Z,S[4]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[6],Z)))
    # T[1]=t_40

    circuit.append(cirq.CNOT(T[4],T[1]))
    # U[6]=y_0

    circuit.append(cirq.CNOT(U[5],U[6]))
    # S[0]=z_0^z_2^z_3^z_5,      S[1]=z_1^z_2^z_4^z_5^z_13^z_14,  S[2]=z_3^z_5^z_6^z_8^z_9^z_11,            S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11,

    # S[4]=z_10^z_11^z_12^z_14,  S[5]=z_3^z_5^z_6^z_8^z_10^z_11,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13,  S[7]=z_3^z_5^z_6^z_8^z_12^z_13,

    # Z=z_15

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[5],Z)))
    # S[2]=z_3^z_5^z_6^z_8^z_9^z_11^z_15

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[4]=z_10^z_11^z_14^z_15

    circuit.append(cirq.CNOT(Z,S[4]))
    # S[7]=z_3^z_5^z_6^z_8^z_12^z_13^z_15

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[5],Z)))
    # S[0]=z_0^z_2^z_3^z_5,           S[1]=z_1^z_2^z_4^z_5^z_13^z_14,  S[2]=z_3^z_5^z_6^z_8^z_9^z_11^z_15,       S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15,

    # S[4]=z_10^z_11^z_12^z_14^z_15,  S[5]=z_3^z_5^z_6^z_8^z_10^z_11,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13,  S[7]=z_3^z_5^z_6^z_8^z_12^z_13^z_15,

    # T[4]=t_41

    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[7]=y_16

    circuit.append(cirq.CNOT(U[5],U[7]))
    # Z=z_16

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[7],Z)))
    # S[1]=z_1^z_2^z_4^z_5^z_13^z_14^z_16

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[4]=z_10^z_11^z_14^z_15^z_16

    circuit.append(cirq.CNOT(Z,S[4]))
    # S[5]=z_3^z_5^z_6^z_8^z_10^z_11^z_16

    circuit.append(cirq.CNOT(Z,S[5]))
    # S[7]=z_3^z_5^z_6^z_8^z_12^z_13^z_15^z_16

    circuit.append(cirq.CNOT(Z,S[7]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[7],Z)))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[7]=y_3

    circuit.append(cirq.CNOT(U[5],U[7]))
    # S[0]=z_0^z_2^z_3,                   S[1]=z_1^z_2^z_4^z_5^z_13^z_14^z_16,  S[2]=z_3^z_5^z_6^z_8^z_9^z_11^z_15,       S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15,

    # S[4]=z_10^z_11^z_12^z_14^z_15^z_16, S[5]=z_3^z_5^z_6^z_8^z_10^z_11^z_16,  S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13,  S[7]=z_3^z_5^z_6^z_8^z_12^z_13^z_15^z_16,

    # Z=z_17

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[7],Z)))
    # S[1]=z_1^z_2^z_4^z_5^z_13^z_14^z_16^z_17

    circuit.append(cirq.CNOT(Z,S[1]))
    # S[2]=z_3^z_5^z_6^z_8^z_9^z_11^z_15^z_17

    circuit.append(cirq.CNOT(Z,S[2]))
    # S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15^z_17

    circuit.append(cirq.CNOT(Z,S[3]))
    # S[5]=z_3^z_5^z_6^z_8^z_10^z_11^z_16^z_17

    circuit.append(cirq.CNOT(Z,S[5]))
    # Z=0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[7],Z)))
    # S[0]=z_0^z_2^z_3^z_5,                         S[1]=z_1^z_2^z_4^z_5^z_13^z_14^z_16^z_17 ,  S[2]=z_3^z_5^z_6^z_8^z_9^z_11^z_15^z_17,

    # S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15^z_17,  S[4]=z_10^z_11^z_12^z_14^z_15^z_16,         S[5]=z_3^z_5^z_6^z_8^z_10^z_11^z_16^z_17,

    # S[6]=z_0^z_1^z_3^z_4^z_9^z_10^z_12^z_13,      S[7]=z_3^z_5^z_6^z_8^z_12^z_13^z_15^z_16,

    # T[4]=t_41

    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[0]=y_17

    circuit.append(cirq.CNOT(U[3],U[0]))
    # T[4]& U[0]=z_7 and S[3]=z_1^z_2^z_3^z_5^z_6^z_9^z_11^z_15^z_17 ^z_7

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[4],U[0],S[3])))
    # T[4]=t_37

    circuit.append(cirq.CNOT(T[2],T[4]))
    # U[0]=y_7

    circuit.append(cirq.CNOT(U[3],U[0]))
    '''** This part is used to generate the input of S-box, the result is stored in U[] **'''

    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    circuit.append(cirq.X(U[2])) 
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[5],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    circuit.append(cirq.X(U[5])) 
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.CNOT(T[3],T[4]))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.CNOT(T[5],T[2]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[4],T[1])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[2],T[0])))
    circuit.append(cirq.CNOT(T[1],T[0]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[2])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],T[2],T[4])))
    circuit.append(cirq.CNOT(T[4],T[5]))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],T[4],T[5])))
    circuit.append(cirq.CNOT(T[2],T[5]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[4])))
    circuit.append(cirq.CNOT(U[6],T[3]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[7],T[2]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[5],T[1]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[7],T[0]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[5],T[3])))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.X(U[5])) 
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[4],T[2])))
    circuit.append(cirq.CNOT(U[3],U[4]))
    circuit.append(cirq.CNOT(U[2],U[4]))
    circuit.append(cirq.CNOT(U[1],U[4]))
    circuit.append(cirq.X(U[4])) 
    circuit.append(cirq.CNOT(U[7],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[7],U[1],T[1])))
    circuit.append(cirq.CNOT(U[7],U[1]))
    circuit.append(cirq.X(U[1])) 
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.CNOT(U[6],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[3])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[1])))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.CNOT(U[0],U[5]))
    circuit.append(cirq.X(U[5])) 
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[2])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[6],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.CNOT(U[1],U[5]))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[7],T[2])))
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    circuit.append(cirq.X(U[6])) 
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.X(U[7])) 
    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[7],T[0])))
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[2],U[5]))
    circuit.append(cirq.X(U[5])) 
    circuit.append(cirq.CNOT(T[0],T[2]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[6],U[7],T[0])))
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[0],U[6]))
    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.X(U[7])) 
    #algorithm 6

    # algorithm 7


if __name__ == "__main__":
    main()
