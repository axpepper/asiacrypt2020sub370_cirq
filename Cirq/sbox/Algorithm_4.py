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
    algorithm_3(circuit, conf.U, conf.T)
    algorithm_4(circuit, conf.U, conf.T, conf.S)
    print(f"First count: {count_gates(circuit)}")
    print(circuit)
'''*****

 * The input of Algorithm 3 can be explained as follows:

 * U[0]=x_0, U[1]=x_1, U[2]=x_2, U[3]=x_3, U[4]=x_4, U[5]=x_5, U[6]=x_6, U[7]=x_7

 * T[0]=0, T[1]=0, T[2]=0, T[3]=0, T[4]=0, T[5]=0.

 * The output of Algorithm 3 can be explained as follows:

 * U[0]=y_19, U[1]=y_4, U[2]=y_2, U[3]=y_5, U[4]=y_14, U[5]=y_6, U[6]=y_21, U[7]=x_7

 * T[0]=t_24, T[1]=t_37, T[2]=t_29, T[3]=t_40, T[4]=t_27, T[5]=t_33.

*****'''

def algorithm_3(circuit, U, T):

    #U[0]=y_13

    circuit.append(cirq.CNOT(U[6],U[0]))
    #U[6]=y_16

    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[5],U[6]))
    #T[0]=t_7

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[0])))
    #T[1]=t_7

    circuit.append(cirq.CNOT(T[0],T[1]))
    #U[1]=y_1

    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[7],U[1]))
    #U[2]=y_5

    circuit.append(cirq.CNOT(U[1],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    circuit.append(cirq.CNOT(U[5],U[2]))
    circuit.append(cirq.CNOT(U[6],U[2]))
    #T[1]=t_9

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[2],T[1])))
    # In fact, we can compute U[0]=y_13, U[6]=y_16, U[1]=y_1, U[2]=y_5 in the first place.

    # Then we can compute T[0]=(U[0] & U[6]) ^ T[0] and T[1]=(U[1] & U[2]) ^ T[1] in parallel.

    # We maintain the above order of operation just for convenience of the reader

    #U[0]=y_9

    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    #U[6]=y_11

    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[7],U[6]))
    #T[2]=t_12

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[2])))
    #T[3]=t_12

    circuit.append(cirq.CNOT(T[2],T[3]))
    #U[5]=y_14

    circuit.append(cirq.CNOT(U[3],U[5]))
    #U[0]=y_17

    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    # T[3]=t_14

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[0],T[3])))
    #  T[1]=t_19

    circuit.append(cirq.CNOT(T[3],T[1]))
    #  U[0]=y_21

    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    #  T[1]=t_23

    circuit.append(cirq.CNOT(U[0],T[1]))
    #U[0]=y_2

    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    #U[6]=y_7

    circuit.append(cirq.CNOT(U[7],U[6]))
    #T[0]=t_11

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[0])))
    # U[0]=y_12

    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[5],U[0]))
    # U[5]=y_15

    circuit.append(cirq.CNOT(U[0],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[4],U[5]))
    # T[4]=t_2, ** first computation of t_2=U[0]& U[5]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[4])))
    # T[3]=t_19^t_2

    circuit.append(cirq.CNOT(T[4],T[3]))
    # U[0]=y_3

    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    # U[5]=y_6

    circuit.append(cirq.CNOT(U[7],U[5]))
    # T[3]=t_19^t_4

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[3])))
    # U[1]=y_20

    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    #  T[3]=t_21

    circuit.append(cirq.CNOT(U[1],T[3]))
    # U[1]=y_10

    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    # U[0]=y_8

    circuit.append(cirq.CNOT(U[2],U[0]))
    # T[2]=t_16

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[0],T[2])))
    # T[0]=t_20

    circuit.append(cirq.CNOT(T[2],T[0]))
    # T[0]=t_16^t_2

    circuit.append(cirq.CNOT(T[4],T[2]))
    # U[0]=y_12

    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[5],U[0]))
    # U[5]=y_15

    circuit.append(cirq.CNOT(U[7],U[5]))
    # T[4]=0, ** second computation of t_2=U[0]& U[5]

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[4])))
    # As shown in the above (with **), we need to compute t_2 two times.

    # If we introduce a new qubit (i.e. T[6]) to store t_2, we can save one Toffoli gate and one Toffoli depth.

    # U[2]=y_18

    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    circuit.append(cirq.CNOT(U[5],U[2]))
    circuit.append(cirq.CNOT(U[6],U[2]))
    # T[0]=t_24

    circuit.append(cirq.CNOT(U[2],T[0]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[7],U[1]))
    # T[2]=t_18

    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[7],T[2])))
    # U[0]=y_19

    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    # T[2]=t_22

    circuit.append(cirq.CNOT(U[0],T[2]))
    # T[4]=t_26

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[4])))
    # T[1]=t_30

    circuit.append(cirq.CNOT(T[0],T[1]))
    # T[4]=t_31

    circuit.append(cirq.CNOT(T[2],T[4]))
    # T[5]=t_32

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[4],T[5])))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[0],T[5]))
    # T[1]=t_34

    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.CNOT(T[5],T[1]))
    # T[4]=t_27

    circuit.append(cirq.CNOT(T[2],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    # T[5]=t_35

    circuit.append(cirq.CNOT(T[4],T[5]))
    # T[1]=t_37  *** first computation of t_36=T[0]& T[5]

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[1])))
    # T[3]=t_25

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[2]=t_29

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],T[4],T[2])))
    # T[4]=t_38  *** second computation of t_36=T[0]& T[5]

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[4])))
    # T[3]=t_40

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],T[4],T[3])))
    # T[4]=t_27  *** third computation of t_36=T[0]& T[5]

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[4])))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[4],T[5]))
    # As shown in the above (with ***), we need to compute t_36 three times.

    # If we introduce a new qubit (i.e. T[7]) to store t_36, we can save two Toffoli gate and two Toffoli depth.

    # U[3]=y_5

    circuit.append(cirq.CNOT(U[2],U[3]))
    circuit.append(cirq.CNOT(U[4],U[3]))
    circuit.append(cirq.CNOT(U[5],U[3]))
    circuit.append(cirq.CNOT(U[6],U[3]))
    # U[4]=y_14

    circuit.append(cirq.CNOT(U[0],U[4]))
    circuit.append(cirq.CNOT(U[3],U[4]))
    circuit.append(cirq.CNOT(U[7],U[4]))
    # U[2]=y_2

    circuit.append(cirq.CNOT(U[6],U[2]))
    # U[5]=y_6

    circuit.append(cirq.CNOT(U[7],U[5]))
    # U[6]=y_21

    circuit.append(cirq.CNOT(U[0],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[5],U[6]))
'''*****

 * The input of Algorithm 4 can be explained as follows:

 * U[0]=y_19, U[1]=y_4, U[2]=y_2, U[3]=y_5, U[4]=y_14, U[5]=y_6, U[6]=y_21, U[7]=x_7

 * T[0]=t_24, T[1]=t_37, T[2]=t_29, T[3]=t_40, T[4]=t_27, T[5]=t_33

 * S[0]=0, S[1]=0, S[2]=0, S[3]=0, S[4]=0, S[5]=0, S[6]=0, S[7]=0.

 * The output of Algorithm 4 can be explained as follows:

 * U[0]=x_0, U[1]=x_1, U[2]=x_2, U[3]=x_3, U[4]=x_4, U[5]=x_5, U[6]=x_6, U[7]=x_7

 * T[0]=0, T[1]=0, T[2]=0, T[3]=0, T[4]=0, T[5]=0

 * S[0]=s_0, S[1]=s_1, S[2]=s_2, S[3]=s_3, S[4]=s_4, S[5]=s_5, S[6]=s_6, S[7]=s_7.

*****'''

def algorithm_4(circuit, U, T, S):

    '''** This part is used to generate the output of S-box, the result is stored in S[] **'''

    # U[1]=y_10

    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[3]=t_41

    circuit.append(cirq.CNOT(T[1],T[3]))
    #  T[3]& U[1]=z_8 and S[5]=z_8

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],U[1],S[5])))
    #  S[6]=z_8

    circuit.append(cirq.CNOT(S[5],S[6]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[3]=t_33

    circuit.append(cirq.CNOT(T[1],T[3]))
    # S[0]=0,  S[1]=0 ,   S[2]=0,   S[3]=0,

    # S[4]=0,  S[5]=z_8,  S[6]=z_8, S[7]=0,

    # T[2]& U[2]=z_14 and S[2]=z_14

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[2],S[2])))
    # S[5]=z_8^z_14

    circuit.append(cirq.CNOT(S[5],S[2]))
    # S[2]=z_8^z_14

    circuit.append(cirq.CNOT(S[6],S[2]))
    # S[0]=0,  S[1]=0 ,        S[2]=z_8^z_14,   S[3]=0,

    # S[4]=0,  S[5]=z_8^z_14,  S[6]=z_8,        S[7]=0,

    #  T[1]& U[5]=z_1

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[5],S[4])))
    #  S[1]=z_1

    circuit.append(cirq.CNOT(S[4],S[1]))
    #  S[3]=z_1

    circuit.append(cirq.CNOT(S[4],S[3]))
    # S[0]=0,   S[1]=z_1,       S[2]=z_8^z_14,   S[3]=z_1,

    # S[4]=z_1, S[5]=z_8^z_14,  S[6]=z_8,        S[7]=0,

    # U[5]=y_15

    circuit.append(cirq.CNOT(U[7],U[5]))
    # T[1]=t_44

    circuit.append(cirq.CNOT(T[5],T[1]))
    # T[1]& U[5]=z_0 and S[7]=z_0

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[5],S[7])))
    # S[1]=z_1^z_0

    circuit.append(cirq.CNOT(S[7],S[1]))
    # S[3]=z_1^z_0

    circuit.append(cirq.CNOT(S[7],S[3]))
    # S[4]=z_1^z_0

    circuit.append(cirq.CNOT(S[7],S[4]))
    # U[5]=y_6

    circuit.append(cirq.CNOT(U[7],U[5]))
    # T[1]=t_37

    circuit.append(cirq.CNOT(T[5],T[1]))
    # S[0]=0,       S[1]=z_1^z_0,   S[2]=z_8^z_14,   S[3]=z_1^z_0,

    # S[4]=z_1^z_0, S[5]=z_8^z_14,  S[6]=z_8,        S[7]=z_0,

    # T[5]& U[7]=z_2 and S[7]=z_0^z_2

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[7],S[7])))
    # S[2]=z_8^z_14^z_0^z_2

    circuit.append(cirq.CNOT(S[7],S[2]))
    # S[5]=z_8^z_14^z_0^z_2

    circuit.append(cirq.CNOT(S[7],S[5]))
    # S[6]=z_8^z_0^z_2

    circuit.append(cirq.CNOT(S[7],S[6]))
    # S[0]=0,       S[1]=z_1^z_0,           S[2]=z_8^z_14^z_0^z_2,   S[3]=z_1^z_0,

    # S[4]=z_1^z_0, S[5]=z_8^z_14^z_0^z_2,  S[6]=z_8^z_0^z_2,        S[7]=z_0^z_2,

    # Done

    # U[1]=y_7

    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    # T[2]& U[1]=z_5 and S[7]=z_0^z_2^z_5

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[1],S[7])))
    # S[2]=z_8^z_14^z_5

    circuit.append(cirq.CNOT(S[7],S[2]))
    # S[4]=z_1^z_2^z_5

    circuit.append(cirq.CNOT(S[7],S[4]))
    # S[5]=z_8^z_14^z_5

    circuit.append(cirq.CNOT(S[7],S[5]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    # S[0]=0,           S[1]=z_1^z_0,       S[2]=z_8^z_14^z_5,   S[3]=z_1^z_0,

    # S[4]=z_1^z_2^z_5, S[5]=z_8^z_14^z_5,  S[6]=z_8^z_0^z_2,    S[7]=z_0^z_2^z_5,

    # U[2]=y_13

    circuit.append(cirq.CNOT(U[3],U[2]))
    # T[3]=t_43

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[3]& U[2]=z_12 and S[7]=z_0^z_2^z_5^z_12

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],U[2],S[7])))
    # S[2]=z_8^z_14^z_0^z_2^z_12

    circuit.append(cirq.CNOT(S[7],S[2]))
    # S[5]=z_8^z_14^z_0^z_2^z_12

    circuit.append(cirq.CNOT(S[7],S[5]))
    # U[2]=y_2

    circuit.append(cirq.CNOT(U[3],U[2]))
    # T[3]=t_40

    circuit.append(cirq.CNOT(T[2],T[3]))
    # S[0]=0,           S[1]=z_1^z_0,                S[2]=z_8^z_14^z_0^z_2^z_12,  S[3]=z_1^z_0,

    # S[4]=z_1^z_2^z_5, S[5]=z_8^z_14^z_0^z_2^z_12,  S[6]=z_8^z_0^z_2,            S[7]=z_0^z_2^z_5^z_12,

    #T[3]& U[3]=z_13 and S[7]=z_0^z_2^z_5^z_12^z_13

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],U[3],S[7])))
    #S[6]= z_8^z_5^z_12^z_13

    circuit.append(cirq.CNOT(S[7],S[6]))
    # S[0]=0,           S[1]=z_1^z_0,                S[2]=z_8^z_14^z_0^z_2^z_12,  S[3]=z_1^z_0,

    # S[4]=z_1^z_2^z_5, S[5]=z_8^z_14^z_0^z_2^z_12,  S[6]=z_8^z_5^z_12^z_13,      S[7]=z_0^z_2^z_5^z_12^z_13,

    # U[6]=y_16

    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    # T[2]=t_43

    circuit.append(cirq.CNOT(T[2],T[3]))
    # T[2]& U[6]=z_3 and S[0]=z_3

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],U[6],S[0])))
    # S[4]=z_1^z_2^z_5^z_3

    circuit.append(cirq.CNOT(S[0],S[4]))
    # S[6]=z_8^z_5^z_12^z_13^z_3

    circuit.append(cirq.CNOT(S[0],S[6]))
    # S[7]=z_0^z_2^z_5^z_12^z_13^z_3

    circuit.append(cirq.CNOT(S[0],S[7]))
    # U[6]=y_21

    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[2],U[6]))
    # T[2]=t_29

    circuit.append(cirq.CNOT(T[2],T[3]))
    # S[0]=z_3,              S[1]=z_1^z_0,                S[2]=z_8^z_14^z_0^z_2^z_12,  S[3]=z_1^z_0,

    # S[4]=z_1^z_2^z_5^z_3,  S[5]=z_8^z_14^z_0^z_2^z_12,  S[6]=z_8^z_5^z_12^z_13^z_3,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3,

    # U[1]=y_1

    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    # T[3]& U[1]=z_4 and S[0]=z_3^z_4

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],U[1],S[0])))
    # S[1]=z_1^z_0^z_3^z_4

    circuit.append(cirq.CNOT(S[0],S[1]))
    # S[2]=z_8^z_14^z_0^z_2^z_12^z_3^z_4

    circuit.append(cirq.CNOT(S[0],S[2]))
    # S[3]=z_1^z_0^z_3^z_4

    circuit.append(cirq.CNOT(S[0],S[3]))
    # S[4]=z_1^z_2^z_5^z_4

    circuit.append(cirq.CNOT(S[0],S[4]))
    # S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4

    circuit.append(cirq.CNOT(S[0],S[5]))
    # S[6]=z_8^z_5^z_12^z_13^z_4

    circuit.append(cirq.CNOT(S[0],S[6]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[0],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    # S[0]=z_3^z_4,          S[1]=z_1^z_0^z_3^z_4,                S[2]=z_8^z_14^z_0^z_2^z_12^z_3^z_4,  S[3]=z_1^z_0^z_3^z_4,

    # S[4]=z_1^z_2^z_5^z_4,  S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4,  S[6]=z_8^z_5^z_12^z_13^z_4,          S[7]=z_0^z_2^z_5^z_12^z_13^z_3,

    # U[3]=y_11

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # T[5]=t_42

    circuit.append(cirq.CNOT(T[2],T[5]))
    # T[5]& U[3]=z_6 and S[0]=z_3^z_4^z_6

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[3],S[0])))
    # S[2]=z_8^z_14^z_0^z_2^z_12^z_6

    circuit.append(cirq.CNOT(S[0],S[2]))
    # S[5]=z_8^z_14^z_0^z_2^z_12^z_6

    circuit.append(cirq.CNOT(S[0],S[5]))
    # S[6]=z_8^z_5^z_12^z_13^z_3^z_6

    circuit.append(cirq.CNOT(S[0],S[6]))
    # U[3]=y_5

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[0],U[7]))
    circuit.append(cirq.CNOT(U[4],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[6],U[7]))
    circuit.append(cirq.CNOT(U[1],U[7]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[2],T[5]))
    # S[0]=z_3^z_4^z_6,      S[1]=z_1^z_0^z_3^z_4,            S[2]=z_8^z_14^z_0^z_2^z_12^z_6,  S[3]=z_1^z_0^z_3^z_4,

    # S[4]=z_1^z_2^z_5^z_4,  S[5]=z_8^z_14^z_0^z_2^z_12^z_6,  S[6]=z_8^z_5^z_12^z_13^z_3^z_6,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3,

    # U[3]=y_17

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[6],U[7]))
    # T[5]=t_45

    circuit.append(cirq.CNOT(T[2],T[5]))
    circuit.append(cirq.CNOT(T[1],T[5]))
    circuit.append(cirq.CNOT(T[3],T[5]))
    # T[5]& U[3]=z_7 and S[0]=z_3^z_4^z_6^z_7

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[3],S[0])))
    # S[3]=z_1^z_0^z_6^z_7

    circuit.append(cirq.CNOT(S[0],S[3]))
    # S[4]= z_1^z_2^z_5^z_3^z_6^z_7

    circuit.append(cirq.CNOT(S[0],S[4]))
    # S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7

    circuit.append(cirq.CNOT(S[0],S[5]))
    # S[6]=z_8^z_5^z_12^z_13^z_4^z_7

    circuit.append(cirq.CNOT(S[0],S[6]))
    # U[3]=y_5

    circuit.append(cirq.CNOT(U[3],U[7]))
    circuit.append(cirq.CNOT(U[2],U[7]))
    circuit.append(cirq.CNOT(U[5],U[7]))
    circuit.append(cirq.CNOT(U[6],U[7]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[2],T[5]))
    circuit.append(cirq.CNOT(T[1],T[5]))
    circuit.append(cirq.CNOT(T[3],T[5]))
    # S[0]=z_3^z_4^z_6^z_7,          S[1]=z_1^z_0^z_3^z_4,                    S[2]=z_8^z_14^z_0^z_2^z_12^z_6,  S[3]=z_1^z_0^z_6^z_7,

    # S[4]=z_1^z_2^z_5^z_3^z_6^z_7,  S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7,  S[6]=z_8^z_5^z_12^z_13^z_4^z_7,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3,

    # U[2]=y_12

    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[1],T[5]))
    # T[5]& U[2]=z_9 and S[0]=z_3^z_4^z_6^z_7^z_9

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[2],S[0])))
    # S[5]=z_8^z_14^z_0^z_2^z_12^z_6^z_9

    circuit.append(cirq.CNOT(S[0],S[5]))
    # U[2]=y_2

    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[1],T[5]))
    # S[0]=z_3^z_4^z_6^z_7^z_9,      S[1]=z_1^z_0^z_3^z_4,                S[2]=z_8^z_14^z_0^z_2^z_12^z_6,  S[3]=z_1^z_0^z_6^z_7,

    # S[4]=z_1^z_2^z_5^z_3^z_6^z_7,  S[5]=z_8^z_14^z_0^z_2^z_12^z_6^z_9,  S[6]=z_8^z_5^z_12^z_13^z_4^z_7,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3,

    # U[1]=y_3

    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[1]& U[1]=z_10 and S[0]=z_3^z_4^z_6^z_7^z_9^z_10

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],U[1],S[0])))
    # S[2]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_9^z_10

    circuit.append(cirq.CNOT(S[0],S[2]))
    # S[6]=z_8^z_5^z_12^z_13^z_3^z_6^z_9^z_10

    circuit.append(cirq.CNOT(S[0],S[6]))
    # S[7]=z_0^z_2^z_5^z_12^z_13^z_4^z_6^z_7^z_9^z_10

    circuit.append(cirq.CNOT(S[0],S[7]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # S[0]=z_3^z_4^z_6^z_7^z_9^z_10,  S[1]=z_1^z_0^z_3^z_4,          S[2]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_9^z_10,

    # S[3]=z_1^z_0^z_6^z_7,           S[4]=z_1^z_2^z_5^z_3^z_6^z_7,  S[5]=z_8^z_14^z_0^z_2^z_12^z_6^z_9,

    # S[6]=z_8^z_5^z_12^z_13^z_3^z_6^z_9^z_10,                       S[7]=z_0^z_2^z_5^z_12^z_13^z_4^z_6^z_7^z_9^z_10,

    # U[1]=y_9

    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[5]=t_42

    circuit.append(cirq.CNOT(T[2],T[5]))
    # T[5]& U[1]=z_15 and S[0]= z_3^z_4^z_6^z_7^z_9^z_10^z_15

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[1],S[0])))
    # S[2]= z_8^z_14^z_0^z_2^z_12^z_6^z_15

    circuit.append(cirq.CNOT(S[0],S[2]))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[2],T[5]))
    # S[0]=z_3^z_4^z_6^z_7^z_9^z_10^z_15,  S[1]=z_1^z_0^z_3^z_4,          S[2]=z_8^z_14^z_0^z_2^z_12^z_6^z_15,

    # S[3]=z_1^z_0^z_6^z_7,                S[4]=z_1^z_2^z_5^z_3^z_6^z_7,  S[5]=z_8^z_14^z_0^z_2^z_12^z_6^z_9,

    # S[6]=z_8^z_5^z_12^z_13^z_3^z_6^z_9^z_10,                            S[7]=z_0^z_2^z_5^z_12^z_13^z_4^z_6^z_7^z_9^z_10,

    # T[5]=t_45

    circuit.append(cirq.CNOT(T[2],T[5]))
    circuit.append(cirq.CNOT(T[1],T[5]))
    circuit.append(cirq.CNOT(T[3],T[5]))
    # T[5]& U[4]=z_16 and S[0]=z_3^z_4^z_6^z_7^z_9^z_10^z_15^z_16

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[4],S[0])))
    # S[1]=z_1^z_0^z_6^z_7^z_9^z_10^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[1]))
    # S[3]=z_1^z_0^z_3^z_4^z_9^z_10^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[3]))
    # S[4]=z_1^z_2^z_5^z_4^z_9^z_10^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[4]))
    # S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_10^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[5]))
    # S[6]=z_8^z_5^z_12^z_13^z_4^z_7^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[6]))
    # S[7]=z_0^z_2^z_5^z_12^z_13^z_3^z_15^z_16

    circuit.append(cirq.CNOT(S[0],S[7]))
    # T[5]=t_33

    circuit.append(cirq.CNOT(T[2],T[5]))
    circuit.append(cirq.CNOT(T[1],T[5]))
    circuit.append(cirq.CNOT(T[3],T[5]))
    # S[0]=z_3^z_4^z_6^z_7^z_9^z_10^z_15^z_16,   S[1]=z_1^z_0^z_6^z_7^z_9^z_10^z_15^z_16,  S[2]=z_8^z_14^z_0^z_2^z_12^z_6^z_15,

    # S[3]=z_1^z_0^z_3^z_4^z_9^z_10^z_15^z_16,   S[4]=z_1^z_2^z_5^z_4^z_9^z_10^z_15^z_16,      S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_10^z_15^z_16,

    # S[6]=z_8^z_5^z_12^z_13^z_4^z_7^z_15^z_16,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3^z_15^z_16,

    # U[1]=y_8

    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[3]=t_41

    circuit.append(cirq.CNOT(T[1],T[3]))
    # T[3]& U[1]=z_17 and S[2]=z_8^z_14^z_0^z_2^z_12^z_6^z_15^z_17

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],U[1],S[2])))
    # U[1]=y_4

    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    # T[3]=t_40

    circuit.append(cirq.CNOT(T[1],T[3]))
    # S[0]=z_3^z_4^z_6^z_7^z_9^z_10^z_15^z_16,   S[1]=z_1^z_0^z_6^z_7^z_9^z_10^z_15^z_16,  S[2]=z_8^z_14^z_0^z_2^z_12^z_6^z_15^z_17,

    # S[3]=z_1^z_0^z_3^z_4^z_9^z_10^z_15^z_16,   S[4]=z_1^z_2^z_5^z_4^z_9^z_10^z_15^z_16,      S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_10^z_15^z_16,

    # S[6]=z_8^z_5^z_12^z_13^z_4^z_7^z_15^z_16,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3^z_15^z_16,

    #  T[5]& U[1]=z_11 and S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_10^z_15^z_16^z_11

    circuit.append(cirq.decompose(cirq.TOFFOLI(T[5],U[1],S[5])))
    # S[0]=z_3^z_4^z_6^z_7^z_9^z_10^z_15^z_16,   S[1]=z_1^z_0^z_6^z_7^z_9^z_10^z_15^z_16,  S[2]=z_8^z_14^z_0^z_2^z_12^z_6^z_15^z_17,

    # S[3]=z_1^z_0^z_3^z_4^z_9^z_10^z_15^z_16,   S[4]=z_1^z_2^z_5^z_4^z_9^z_10^z_15^z_16,  S[5]=z_8^z_14^z_0^z_2^z_12^z_3^z_4^z_7^z_10^z_15^z_16^z_11,

    # S[6]=z_8^z_5^z_12^z_13^z_4^z_7^z_15^z_16,  S[7]=z_0^z_2^z_5^z_12^z_13^z_3^z_15^z_16,

    circuit.append(cirq.X(S[1])) 
    circuit.append(cirq.X(S[2])) 
    circuit.append(cirq.X(S[6])) 
    circuit.append(cirq.X(S[7])) 
    '''** This part is used to generate the input of S-box, the result is stored in U[] **'''

    circuit.append(cirq.CNOT(U[0],U[6]))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[3],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[6],U[2]))
    circuit.append(cirq.CNOT(U[0],U[4]))
    circuit.append(cirq.CNOT(U[3],U[4]))
    circuit.append(cirq.CNOT(U[7],U[4]))
    circuit.append(cirq.CNOT(U[2],U[3]))
    circuit.append(cirq.CNOT(U[4],U[3]))
    circuit.append(cirq.CNOT(U[5],U[3]))
    circuit.append(cirq.CNOT(U[6],U[3]))
    circuit.append(cirq.CNOT(T[4],T[5]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[4])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[2],T[4],T[3])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[4])))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[3],T[4],T[2])))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[0],T[5],T[1])))
    circuit.append(cirq.CNOT(T[4],T[5]))
    circuit.append(cirq.CNOT(T[2],T[4]))
    circuit.append(cirq.CNOT(T[0],T[4]))
    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.CNOT(T[5],T[1]))
    circuit.append(cirq.CNOT(T[0],T[5]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[4],T[5])))
    circuit.append(cirq.CNOT(T[2],T[4]))
    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(T[1],T[3],T[4])))
    circuit.append(cirq.CNOT(U[0],T[2]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[7],T[2])))
    circuit.append(cirq.CNOT(U[3],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[7],U[1]))
    circuit.append(cirq.CNOT(U[2],T[0]))
    circuit.append(cirq.CNOT(U[3],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    circuit.append(cirq.CNOT(U[5],U[2]))
    circuit.append(cirq.CNOT(U[6],U[2]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[4])))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[5],U[0]))
    circuit.append(cirq.CNOT(T[4],T[2]))
    circuit.append(cirq.CNOT(T[2],T[0]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[0],T[2])))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    circuit.append(cirq.CNOT(U[1],T[3]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[4],U[1]))
    circuit.append(cirq.CNOT(U[5],U[1]))
    circuit.append(cirq.CNOT(U[6],U[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[3])))
    circuit.append(cirq.CNOT(U[7],U[5]))
    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(T[4],T[3]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[5],T[4])))
    circuit.append(cirq.CNOT(U[0],U[5]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(U[4],U[5]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[5],U[0]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[0])))
    circuit.append(cirq.CNOT(U[7],U[6]))
    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    circuit.append(cirq.CNOT(U[0],T[1]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    circuit.append(cirq.CNOT(T[3],T[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[5],U[0],T[3])))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[4],U[0]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    circuit.append(cirq.CNOT(U[7],U[0]))
    circuit.append(cirq.CNOT(U[3],U[5]))
    circuit.append(cirq.CNOT(T[2],T[3]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[2])))
    circuit.append(cirq.CNOT(U[1],U[6]))
    circuit.append(cirq.CNOT(U[7],U[6]))
    circuit.append(cirq.CNOT(U[1],U[0]))
    circuit.append(cirq.CNOT(U[2],U[0]))
    circuit.append(cirq.CNOT(U[3],U[0]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[1],U[2],T[1])))
    circuit.append(cirq.CNOT(U[1],U[2]))
    circuit.append(cirq.CNOT(U[4],U[2]))
    circuit.append(cirq.CNOT(U[5],U[2]))
    circuit.append(cirq.CNOT(U[6],U[2]))
    circuit.append(cirq.CNOT(U[2],U[1]))
    circuit.append(cirq.CNOT(U[7],U[1]))
    circuit.append(cirq.CNOT(T[0],T[1]))
    circuit.append(cirq.decompose(cirq.TOFFOLI(U[0],U[6],T[0])))
    circuit.append(cirq.CNOT(U[2],U[6]))
    circuit.append(cirq.CNOT(U[4],U[6]))
    circuit.append(cirq.CNOT(U[5],U[6]))
    circuit.append(cirq.CNOT(U[6],U[0]))
    #algorithm 3

    #algorithm 4


if __name__ == "__main__":
    main()
