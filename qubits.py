import math

import numpy as np

def get_basic(type=0):
    if type==0:
        return get_basic_qubit_0()
    return get_basic_qubit_1()

def get_basic_qubit_0():# ∣0⟩
    return np.array([[1], [0]])

def get_basic_qubit_1():# ∣1⟩
    return np.array([[0], [1]])

def decode_qubits(qubits = np.array([])):
    qubit_num = int(math.log2(qubits.shape[0]))
    qubit_list = []
    one_i_list = np.nonzero(qubits)[0]
    for i in one_i_list:
        product_group = []
        for qubit_i in range(qubit_num):
            q = np.zeros((2, 1))

            qubit_matrix_i = int(i%2**(qubit_num-qubit_i)>=2**(qubit_num-qubit_i)/2)
            q[qubit_matrix_i,0]=1
            product_group.append(q)
        qubit_list.append(product_group)
    return qubit_list