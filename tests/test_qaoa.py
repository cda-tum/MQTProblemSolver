from mqt.problemsolver.partialcompiler.qaoa import QAOA
from qiskit import QuantumCircuit


def test_qaoa_init() -> None:
    q = QAOA(num_qubits=4, repetitions=3, remove_probability=0.5)
    assert isinstance(q.qc, QuantumCircuit)
    assert isinstance(q.qc_baseline, QuantumCircuit)
    assert isinstance(q.qc_compiled, QuantumCircuit)
    assert isinstance(q.to_be_removed_gates_indices, list)


def test_compile_qc() -> None:
    q = QAOA(num_qubits=4, repetitions=3, remove_probability=0.5)
    qc_baseline_compiled = q.compile_qc(baseline=True, opt_level=2)
    assert isinstance(qc_baseline_compiled, QuantumCircuit)
    qc_baseline_compiled = q.compile_qc(baseline=False, opt_level=2)
    assert isinstance(qc_baseline_compiled, QuantumCircuit)


def test_get_to_be_checked_gates() -> None:
    q = QAOA(num_qubits=4, repetitions=3, remove_probability=0.5)
    indices = q.get_to_be_removed_gate_indices()
    assert isinstance(indices, list)


def test_check_gates() -> None:
    q = QAOA(num_qubits=2, repetitions=1, remove_probability=1.0)
    compiled_qc = q.remove_unnecessary_gates(
        qc=q.qc_compiled.copy(),
        optimize_swaps=False,
    )
    assert isinstance(compiled_qc, QuantumCircuit)
    assert len(compiled_qc._data) == len(q.qc_compiled._data) - 1
