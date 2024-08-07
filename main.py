import numpy as np
import gates
import qubits
import circuits

if __name__ == '__main__':
    qubit_0 = qubits.get_basic_qubit_0()  # ∣0⟩
    qubit_1 = qubits.get_basic_qubit_1()  # ∣1⟩
    a = gates.get_gate_by_name("CCNOT",True)
    gate_cnot = gates.get_gate_by_name("CNOT")
    gate_cnot_inverse =  gates.get_gate_by_name("CNOT",[True])
    gate_pauli_y = gates.get_gate_by_name("Y")
    gate_hadamard = gates.get_gate_by_name("H")
    qubits_01 = np.kron(qubit_0, qubit_1)  # ∣01⟩ = ∣0⟩⊗∣1⟩
    qubits_11 = np.kron(qubit_1, qubit_1)  # ∣11⟩ = ∣1⟩⊗∣1⟩
    qubits_10 = np.kron(qubit_1, qubit_0)  # ∣10⟩ = ∣1⟩⊗∣0⟩

    #qubits.decode_qubits(np.array([[1], [0], [0],[1]]))
    #qubits.decode_qubits(qubits_01)

    cnot_qubits_11 = np.dot(gate_cnot, qubits_11)
    cnot_inverse_qubits_11 = np.dot(gate_cnot_inverse, qubits_11)

    hadamard_qubit_1 = np.dot(gate_hadamard,qubit_1)
    hadamard_qubits_10 = np.kron(hadamard_qubit_1, qubit_0)
    a = qubits.decode_qubits(hadamard_qubits_10)
    print(a)


    pauli_y_qubits_01 = np.dot(gate_pauli_y, qubit_1)

    circuit_plan = [
        [1,gates.get_pauli_x_gate()],
        [gates.get_pauli_z_gate(),1],
    ]
    test_circuit = circuits.Circuit(2,2,circuit_plan)
    output = test_circuit.forward([qubit_0,qubit_0])

    # print(qubit_0)
    # print(qubit_1)
    # print(qubits_01)
    print(pauli_y_qubits_01)
