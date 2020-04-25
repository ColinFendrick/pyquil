from pyquil import get_qc
import networkx as nx
from matplotlib import pyplot as plt

qc = get_qc('9q-square-qvm')
nx.draw(qc.qubit_topology())
plt.title('9q-square-qvm', fontsize=18)
plt.show()