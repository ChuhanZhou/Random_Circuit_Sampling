import numpy as np
import gates
import qubits
import circuits
from matplotlib import pyplot as plt
import datetime
import ipywidgets as widgets
from ipywidgets import interact

if __name__ == '__main__':
    input_qubit_number = 1
    gate_number = 100
    batch_calculation_number = 100

    f_list = circuits.rcs(input_qubit_number, gate_number, batch_calculation_number)
    # show P(F) and P_Haar(F)
    circuits.show_p_f(f_list, input_qubit_number, gate_number, batch_calculation_number)
    # show P_Haar(F)
    #circuits.show_p_haar_f(input_qubit_number)
