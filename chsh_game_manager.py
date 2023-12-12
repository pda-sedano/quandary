import numpy as np
from qiskit import QuantumCircuit


class CHSHGameManager:
    """
    This class manages the CHSH game, providing classical bits and qubits to the players and determining
    wins and losses.
    """

    def __init__(self, player1, player2):
        self.bits = None
        self.response_bits = None
        self.quantum_circuit = None
        self.player1 = player1
        self.player2 = player2

    def generate_classical_bits(self):
        self.bits = np.random.randint(2, size=2)

    def generate_qubits(self):
        self.quantum_circuit = QuantumCircuit(2, 2)
        self.quantum_circuit.h(0)
        self.quantum_circuit.cx(0, 1)

    def get_result(self):
        return (self.response_bits[0] ^ self.response_bits[1]) == (self.bits[0] and self.bits[1])
