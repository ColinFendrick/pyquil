# “What is a QuantumComputer?” Advanced Edition

A QuantumComputer is a wrapper around three constituent parts, each of which has a programatic interface that must be respected by all classes that implement the interface. By having clear interfaces we can write backend-agnostic methods on QuantumComputer and mix-and-match backing objects.

The following diagram shows the three objects that must be provided when constructing a QuantumComputer “by hand”. The abstract classes are backed in grey with example implementing classes listed below. Please consult the api reference for details on each interface.

As an example, let’s construct a 5-qubit QVM with one central node and only even numbered qubits. This is detailed in `five-qubit-vcm.py`.
