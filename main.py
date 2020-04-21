from pyquil import get_qc, Program
from pyquil.gates import Z, CNOT, H, RY
from pyquil.api import local_forest_runtime, WavefunctionSimulator, QVMConnection
from pyquil.paulis import sZ
import numpy as np
from matplotlib import pyplot as plt

z0 = (1-sZ(0))*0.5
z1 = (1-sZ(1))*0.5
xor = (1-sZ(0)*sZ(1))*0.5
print (xor)

prog = Program(Z(0), CNOT(0, 1))

with local_forest_runtime():
    qvm = get_qc('9q-square-qvm')
    results = qvm.run_and_measure(prog, trials=10)

# construct a Bell State program
p = Program(H(0), CNOT(0, 1))

# run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run_and_measure(p, trials=10)
print(result[0])
print(result[1])

wfn = WavefunctionSimulator().wavefunction(p)
print(wfn)

for observable in [z0, z1, xor]:
    expectation = WavefunctionSimulator().expectation(prep_prog=p, pauli_terms=observable)
    print(observable, '\t', expectation)

cxn = QVMConnection()
thetas = np.linspace(0, np.pi, 20)
bitstrings = [np.asarray(cxn.run_and_measure(Program(RY(theta, 0)), qubits=[0], trials=1000))
              for theta in thetas]


averages = [np.mean(bs[:,0]) for bs in bitstrings]
plt.plot(thetas, averages, 'o-')
plt.show()
