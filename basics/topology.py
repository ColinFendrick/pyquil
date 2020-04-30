from pyquil import get_qc
import networkx as nx
from matplotlib import pyplot as plt

"""
WavefunctionSimulator still has no notion of qubit connectivity,
so feel free to use that for simulating quantum algorithms that you aren’t concerned about running on an actual QPU.

Can do any "{n}q-qvm"
(subject to computational resource constraints).
These QVM’s are constructed with a topology!
It just happens to be fully connected.
"""

def nqqvm(n):
    nx.draw(get_qc('{}q-qvm'.format(n)).qubit_topology())
    plt.title('{}q-qvm is fully connected'.format(n), fontsize=16)
    plt.show()

nqqvm(5)
nqqvm(9)
nqqvm(22)
nqqvm(234)
