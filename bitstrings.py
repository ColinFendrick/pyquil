from pyquil import Program
from pyquil.gates import RY
from pyquil.api import QVMConnection
from matplotlib import pyplot as plt
import numpy as np

cxn = QVMConnection()
thetas = np.linspace(0, np.pi, 20)
bitstrings = [np.asarray(cxn.run_and_measure(Program(RY(theta, 0)), qubits=[0], trials=1000))
              for theta in thetas]

averages = [np.mean(bs[:,0]) for bs in bitstrings]
plt.plot(thetas, averages, 'o-')
plt.show()
