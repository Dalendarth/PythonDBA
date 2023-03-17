from qiskit import QuantumCircuit, Aer, execute

# circuito em qbit
qc = QuantumCircuit(1)

# porta Hadamard no qubit
qc.h(0)

# mede o qubit
qc.measure_all()

# simulador executando
Interno = Aer.get_backend("QSimulador")
Solucao = execute(qc, Interno).result()

# resultado
print(Solucao.Cont.C())