from pyquil import get_qc, Program
from pyquil.gates import Z, CNOT

p = Program(Z(0), CNOT(0, 1))

# run the program on a QVM

qc = get_qc('9q-square-qvm')
result = qc.run_and_measure(p, trials=10)
print(result[0])
print(result[1])