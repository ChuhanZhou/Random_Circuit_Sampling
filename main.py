import numpy as np
import gates
import qubits
import circuits

if __name__ == '__main__':
    circuit = circuits.Circuit(4,[
        ["CNOT", [0,1]],
        ["CNOT", [1,2]],
        ["CCNOT", [2,1,0]],
        ["CNOT", [2,1]],
    ])
    out = circuit.forward([1,0,0,0])
    print(out,"\n\n")
    print(qubits.decode_qubits(out))
