import numpy as np
import gates

class  Circuit():
    #gate_plan(each gate):[gate_name,[gate_indexs...]]
    #ex: [cnot,[contral_qubit_i,target_qubit_i]
    def __init__(self,input_n=0,gate_step=0,gate_plan = []):
        #super().__init__()
        self.gate_matrix = np.zeros((input_n, gate_step))
        step = 0
        for g_name,g_indexs in gate_plan:
            if len(g_indexs)>1:

                g = gates.get_gate_by_name(g_name,)

        self.gate_matrix = np.array(gate_plan)

    def forward(self,input_list=[]):
        input_list = np.array(input_list.copy()).T
        step_num = self.gate_matrix.shape[1]
        for step_n in range(step_num):
            input_list*self.gate_matrix[:,step_n]
        return input_list