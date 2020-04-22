from pyquil import Program
from pyquil.gates import CNOT, H
from pyquil.api import WavefunctionSimulator

# construct a Bell State program
p = Program(H(0), CNOT(0, 1))

wfn = WavefunctionSimulator().wavefunction(p)
print(wfn)