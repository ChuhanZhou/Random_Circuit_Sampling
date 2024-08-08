import numpy as np
import gates
import qubits
import circuits
from matplotlib import pyplot as plt

if __name__ == '__main__':
    f_n = 1000
    input_n = 3
    gate_max_n = 25

    basic_qubit_list = []
    for i in range(input_n):
        basic_qubit_list.append(0)

    f_list = []
    for f_i in range(1000):
        circuit_0 = circuits.get_random_circuit(input_n,np.random.randint(1,gate_max_n+1))
        circuit_1 = circuits.get_random_circuit(input_n, np.random.randint(1, gate_max_n + 1))
        result_0 = circuit_0.run(basic_qubit_list)
        result_1 = circuit_1.run(basic_qubit_list)
        f = abs(np.dot(result_0.T,result_1))**2
        f_list.append(f[0,0])

    plt.hist(f_list,linewidth=0,rwidth=0.5,align="left")
    plt.show()


