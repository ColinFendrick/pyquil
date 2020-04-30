from pyquil import Program
from pyquil.gates import CNOT, H
from pyquil.paulis import sZ
from pyquil.api import WavefunctionSimulator

p = Program(H(0), CNOT(0, 1))

z0 = (1-sZ(0))*0.5
z1 = (1-sZ(1))*0.5
xor = (1-sZ(0)*sZ(1))*0.5
print (xor)

for observable in [z0, z1, xor]:
    expectation = WavefunctionSimulator().expectation(prep_prog=p, pauli_terms=observable)
    print(observable, '\t', expectation)