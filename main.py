import numpy as np
import gates
import qubits
import circuits
from matplotlib import pyplot as plt

if __name__ == '__main__':
    input_qubit_number = 3
    max_gate_number = 20
    batch_calculation_number = 10000

    f_list = circuits.rcs(input_qubit_number,max_gate_number,batch_calculation_number)
    # show P(F)
    circuits.show_p_f(f_list,input_qubit_number,max_gate_number,batch_calculation_number)


