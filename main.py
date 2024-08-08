import numpy as np
import gates
import qubits
import circuits
from matplotlib import pyplot as plt

if __name__ == '__main__':
    input_n = 5
    gate_max_n = 20
    batch_n = 10000

    basic_qubit_list = []
    for i in range(input_n):
        basic_qubit_list.append(0)

    f_list = []
    for f_i in range(batch_n):
        circuit_0 = circuits.get_random_circuit(input_n,np.random.randint(1,gate_max_n+1))
        circuit_1 = circuits.get_random_circuit(input_n, np.random.randint(1, gate_max_n + 1))
        result_0 = circuit_0.run(basic_qubit_list)
        result_1 = circuit_1.run(basic_qubit_list)
        #fidelity
        f = abs(np.dot(result_0.T,result_1))**2
        f_list.append(f[0,0])
        if (f_i+1)%(batch_n/10)==0:
            print("{}|{}".format(batch_n,f_i+1))
    #show P(F)
    plt.xticks(np.arange(0.0, 1.1, 0.1))
    plt.hist(f_list,rwidth=0.5,align="left",bins=np.arange(0.0, 1.1, 0.05))
    plt.title("qubit_num:{}|batch_num:{}|gate_max_num:{}".format(input_n,batch_n,gate_max_n))
    plt.show()


