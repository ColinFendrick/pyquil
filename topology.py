from pyquil import get_qc
import networkx as nx
from matplotlib import pyplot as plt

qc = get_qc('9q-square-qvm')
nx.draw(qc.qubit_topology())
plt.title('9q-square-qvm', fontsize=18)
plt.show()

"""
WavefunctionSimulator still has no notion of qubit connectivity,
so feel free to use that for simulating quantum algorithms that you aren’t concerned about running on an actual QPU.

Can do any "{n}q-qvm"
(subject to computational resource constraints).
These QVM’s are constructed with a topology!
It just happens to be fully connected.
"""

nx.draw(get_qc('5q-qvm').qubit_topology())
plt.title('5q-qvm is fully connected', fontsize=16)
plt.show()

nx.draw(get_qc('22q-qvm').qubit_topology())
plt.title('5q-qvm is fully connected', fontsize=16)
plt.show()

nx.draw(get_qc('222q-qvm').qubit_topology())
plt.title('5q-qvm is fully connected', fontsize=16)
plt.show()