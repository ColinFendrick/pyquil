from pyquil import Program, get_qc
from pyquil.gates import Z, CNOT
from pyquil.api import local_forest_runtime

prog = Program(Z(0), CNOT(0, 1))

with local_forest_runtime():
    qvm = get_qc('9q-square-qvm')
    results = qvm.run_and_measure(prog, trials=10)