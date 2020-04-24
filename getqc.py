from pyquil import get_qc, Program
from pyquil.gates import CNOT, H
import numpy as np

qc = get_qc('3q-qvm')
qc
print(qc.qubits())

p = Program(H(0), CNOT(0, 1))

bitstrings = qc.run_and_measure(p, trials=10)
print(bitstrings)

bitstring_array = np.vstack([bitstrings[q] for q in qc.qubits()]).T
sums = np.sum(bitstring_array, axis=1)
print(sums)

sample_is_ghz = np.logical_or(sums == 0, sums == 3)
print(sample_is_ghz)
print(np.all(sample_is_ghz))
