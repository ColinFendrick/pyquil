
# Heirarchy of realism

- `WavefunctionSimulator` to debug algorithm
- `get_qc("5q-qvm")` to debug sampling
- `get_qc("9q-square-qvm")` to debug mapping to a lattice
- `get_qc("9q-square-noisy-qvm")` to debug generic noise characteristics
- `get_qc("Aspen-0-16Q-A-qvm")` to debug mapping to a real lattice
- `get_qc("Aspen-0-16Q-A-noisy-qvm")` to debug noise characteristics of a real device
- `get_qc("Aspen-0-16Q-A")` to run on a real device
