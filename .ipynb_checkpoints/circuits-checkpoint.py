import numpy as np
import gates
import qubits
from matplotlib import pyplot as plt
import datetime

class  Circuit():
    # gate_plan(each gate):[gate_name,[gate_indexs...]]
    # ex: [cnot,[contral_qubit_i,target_qubit_i]
    def __init__(self,input_n=0,gate_plan = []):
        #super().__init__()
        self.gate_plan = gate_plan
        self.blue_print, self.gate_list = self.create_blue_print(input_n,gate_plan)
        self.circuit_matrix = self.create_circuit_matrix(self.blue_print, self.gate_list)

    # input_list=[q0,q1,q2,...,qn]
    # ex: [0,1,1,0,1]
    def run(self,input_list=[]):
        """
        """
        qubit_matrix = qubits.get_qubit_matrix(input_list)
        out = np.dot(self.circuit_matrix,qubit_matrix)
        #normalization => <ψ|ψ>=1
        s = (np.abs(out)**2).sum()
        out = out/np.sqrt(s)
        return out

    def create_blue_print(self,input_n=0,gate_plan=[]):
        blue_print = np.ones((input_n, len(gate_plan))).astype(int) * -1
        gate_list = []
        step = 0
        for g_name, g_indexs in gate_plan:
            # single_qubit_gate
            if len(g_indexs) == 1:
                gate_list.append(gates.get_gate_by_name(g_name))
                if blue_print[g_indexs[0], step] != -1:
                    step += 1
                blue_print[g_indexs[0], step] = len(gate_list) - 1
            # muti_qubit_gate
            elif len(g_indexs) > 1:
                if g_indexs[0] != g_indexs[-1]:
                    is_inverse = g_indexs[0] > g_indexs[-1]
                    g_indexs.sort(reverse=is_inverse)
                    inner_gates = []
                    for g_i in range(len(g_indexs) - 1):
                        i_gate_num = abs(g_indexs[g_i] - g_indexs[g_i + 1]) - 1
                        inner_gate = 1
                        if i_gate_num > 0:
                            for i in range(i_gate_num):
                                inner_gate = np.kron(inner_gate, gates.get_identity_gate())
                            inner_gates.append(inner_gate)
                        else:
                            inner_gates.append(inner_gate)
                    gate_list.append(gates.get_gate_by_name(g_name, is_inverse, inner_gates))
                    if blue_print[min(g_indexs):max(g_indexs) + 1, step].max() != -1:
                        step += 1
                    blue_print[min(g_indexs):max(g_indexs) + 1, step] = len(gate_list) - 1
        blue_print = blue_print[:,0:step+1]
        return blue_print,gate_list

    def create_circuit_matrix(self,blue_print=np.zeros((0, 0)), gate_list=[]):
        circuit_matrix = 1

        for step_i in range(blue_print.shape[1]):
            step_matrix = 1
            gate_i_old = -1
            for gate_i in blue_print[:,step_i:step_i+1].T[0]:
                gate = 1
                if gate_i >= 0:
                    if gate_i != gate_i_old:
                        gate = gate_list[gate_i]
                        gate_i_old = gate_i
                elif gate_i == -1:
                    gate = gates.get_identity_gate()
                step_matrix = np.kron(step_matrix,gate)
            circuit_matrix = np.dot(step_matrix,circuit_matrix)
        return circuit_matrix

def get_random_circuit(input_n=3,gate_n=10):
    gate_plan = []
    g_list = gates.gate_list
    g_weighted_list = []
    for t_i in range(len(g_list)):
        if t_i>=input_n:
            break
        t_len = (t_i+1)*len(g_list[t_i])
        for t_len_i in range(t_len):
            g_weighted_list.append(t_i)
    g_list_weighting = np.array(g_weighted_list)
    for g_i in range(gate_n):
        g_type = np.random.choice(g_list_weighting)
        g_name = g_list[g_type][np.random.randint(0,len(g_list[g_type]))]
        g_indexs = []
        g_index_old = -1
        for index_i in range(g_type+1):
            g_index_old = np.random.randint(g_index_old+1,input_n-g_type+index_i)
            g_indexs.append(g_index_old)#(input_n-(g_type+1)+1)
        if bool(np.random.randint(0,2)):
            g_indexs.reverse()
        gate_plan.append([g_name,g_indexs])
    return Circuit(input_n,gate_plan)

#random_circuit_sampling
def rcs(input_n = 3,gate_max_n = 15,batch_n = 1000):
    basic_qubit_list = []
    for i in range(input_n):
        basic_qubit_list.append(0)

    f_list = []
    start_time = datetime.datetime.now()
    for f_i in range(batch_n):
        circuit_0 = get_random_circuit(input_n, np.random.randint(1, gate_max_n + 1))
        circuit_1 = get_random_circuit(input_n, np.random.randint(1, gate_max_n + 1))
        result_0 = circuit_0.run(basic_qubit_list)
        result_1 = circuit_1.run(basic_qubit_list)
        # fidelity
        f = abs(np.dot(result_0.T, result_1)) ** 2
        f_list.append(f[0, 0])
        if (f_i + 1) % (batch_n / 10) == 0:
            print("[{}] {}|{}".format(datetime.datetime.now(),batch_n, f_i + 1))
    end_time = datetime.datetime.now()
    print("(2 circuits per batch) avg_batch_running_time[hh:mm:ss]: {}".format((end_time-start_time)/batch_n))
    return f_list

def show_p_f(f_list=[],input_n = "N/A",gate_max_n = "N/A",batch_n = "N/A"):
    plt.xticks(np.arange(-0.1, 1.1, 0.1))
    plt.hist(f_list, rwidth=0.75, align="left", bins=np.arange(-0.1, 1.1, 0.01))
    plt.title("qubit_num:{}|batch_num:{}|gate_max_num:{}".format(input_n, batch_n, gate_max_n))
    plt.show()

def show_p_haar_f(input_n = 1):
    f = np.linspace(0, 1, 1000)
    N = 2 ** input_n
    a = plt.plot(f, (N - 1) * (1 - f) ** (N - 2))
    plt.title("qubit_num:{}|Hilbert_space_dim:{}".format(input_n, N))
    plt.show()