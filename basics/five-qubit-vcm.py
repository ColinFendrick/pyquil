import networkx as nx
from pyquil import Program
from pyquil.gates import X
from pyquil.device import NxDevice
from pyquil.api._qac import AbstractCompiler
from pyquil.api import QuantumComputer, QVM, ForestConnection
from matplotlib import pyplot as plt

topology = nx.from_edgelist([
    (10, 2),
    (10, 4),
    (10, 6),
    (10, 8),
])

device = NxDevice(topology)

class MyLazyCompiler(AbstractCompiler):
    def quil_to_native_quil(self, program, *, protoquil=None):
        return program

    def native_quil_to_executable(self, nq_program):
        return nq_program

my_qc = QuantumComputer(
    name='my-qvm',
    qam=QVM(connection=ForestConnection()),
    device=device,
    compiler=MyLazyCompiler(),
)

nx.draw(my_qc.qubit_topology())
plt.title('5qcm', fontsize=18)
plt.show()

my_qc.run_and_measure(Program(X(10)), trials=5)
