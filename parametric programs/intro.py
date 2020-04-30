'''
A hybrid algorithm involves using the quantum computer to create a quantum state that would be
difficult to prepare classically; measure it in a way particular to your problem;
and then update your procedure for creating the state so that the measurements are closer to the correct answer.
A real hybrid algorithm involves structured ansatze like QAOA for optimization or a UCC ansatz for chemistry.
Here, we’ll do a much simpler parameterized program
'''

from pyquil import Program, get_qc
from pyquil.gates import RY

def ansatz(theta):
    program = Program()
    program += RY(theta, 0)
    return program

print(ansatz(theta=0.2))
