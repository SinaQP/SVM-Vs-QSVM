# Reproducibility Guide

## 1. System Requirements and Environment
* **Python:** 3.10, 3.11, or 3.12 (tested on Python 3.12.14, Windows 64-bit).
* **Package Management:** Standard pip or virtual environment (`venv`).

### Installation
```bash
# Clone the repository
git clone https://github.com/SinaQP/SVM-Vs-QSVM.git
cd SVM-Vs-QSVM

# Create and activate virtual environment
python -m venv .venv
# On Windows:
.\.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

# Install dependencies and package in editable mode
pip install -e .
```

---

## 2. Experimental Random Seeds
All experiments rely on deterministic, pre-frozen pseudo-random seeds:
* **Outer Cross-Validation Seeds:** `[42, 123, 456, 789, 2026]`
* **Inner Cross-Validation Seeds:** Same seed per outer split for stratified inner shuffling.
* **Statistical Bootstrap Seed:** `42` (10,000 resamples).

---

## 3. One-Command Full Project Validation
To verify package installation, configuration integrity, test suite pass, and canonical artifact checksums:
```bash
python scripts/validate_project.py
```
This executes all 23 unit and regression tests, validates canonical files in `results/final/`, and updates `results/final/repository_validation.json`.

---

## 4. Reproducing Experiments
All reproduction scripts write to `results/reproduced/` by default to preserve the frozen canonical artifacts in `results/final/`.

### Classical Baselines
```bash
python scripts/run_baselines.py --config configs/base.yaml --output-dir results/reproduced
```

### Feature-Map Ablation (Phase 9)
```bash
python scripts/run_ablation.py --config configs/phase9_ablation.yaml --output-dir results/reproduced
```

### Sample-Size Scaling (Phase 10)
```bash
python scripts/run_scaling.py --config configs/phase10_scaling.yaml --output-dir results/reproduced
```

### Nested Tuning and Paired Statistics (Phase 11)
```bash
python scripts/run_tuning.py --output-dir results/reproduced
```

### Final Synthesis and Report (Phase 12)
```bash
python scripts/build_final_report.py
```

### Fast One-Command End-to-End Pipeline
```bash
python scripts/reproduce_final.py --output-dir results/reproduced
```

---

## 5. Approximate Runtimes and Computational Cost
Benchmark timings measured on modern consumer hardware (Intel Core i7 / AMD Ryzen):

| Script / Phase | Evaluation Engine | Typical Runtime | Notes |
| :--- | :--- | :---: | :--- |
| `scripts/run_baselines.py` | Classical LibSVM | ~0.1 s | 5 seeds, PCA 2 and 4 |
| `scripts/reproduce_final.py` | Exact Statevector Gram | ~2.5 s | Modern fast evaluation |
| `tests/` (full test suite) | Pytest (23 tests) | ~5.2 s | Unit, property, regression |
| `scripts/run_ablation.py` | Exact Statevector Gram | ~25 s | 60 quantum runs |
| `scripts/run_scaling.py` | Exact Statevector Gram | ~35 s | 150 scaling evaluations |
| `scripts/run_tuning.py` | Nested 5-fold CV | ~90 s | 1,750 candidate evaluations |

### Exclusion of Historical `ComputeUncompute` from Default Path
In exploratory Phase 7, naive pairwise circuit execution using Qiskit's `ComputeUncompute` required 120s (2Q) and 455s (4Q) per split (~25,000x to 55,000x slower than classical SVM). Because `exact_statevector_gram` computes mathematically identical fidelity inner products ($|\langle \psi_i | \psi_j \rangle|^2$) in fractions of a second, the slow pairwise sampler is preserved for historical record but excluded from the standard reproduction pipeline.
