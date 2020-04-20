from pyquil import get_qc, Program
from pyquil.gates import Z, CNOT, H
from pyquil.api import local_forest_runtime, WavefunctionSimulator
from pyquil.paulis import sZ

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
