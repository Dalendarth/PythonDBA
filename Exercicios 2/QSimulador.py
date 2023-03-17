from qiskit import QuantumCircuit, Aer, execute

# cria um circuito quântico com 1 qubit
qc = QuantumCircuit(1, 1)

# aplica a porta Hadamard no qubit
qc.h(0)

# mede o qubit
qc.measure(0, 0)

# obtém o backend do simulador
backend = Aer.get_backend('qasm_simulator')

# executa o circuito no simulador
job = execute(qc, backend, shots=1024)

# obtém o resultado da execução
result = job.result()

# exibe o resultado
print(result.get_counts())