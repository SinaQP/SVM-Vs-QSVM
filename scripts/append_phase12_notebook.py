"""Append Phase 12 section to svm_vs_qsvm_setup.ipynb and execute newly added cells."""

from pathlib import Path
import json
import nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output

ROOT = Path(__file__).resolve().parent.parent
NOTEBOOK_PATH = ROOT / "notebooks" / "svm_vs_qsvm_setup.ipynb"

MD_PHASE12_INTRO = """## 22. Phase 12 — Final Research Synthesis

This section provides the canonical final experimental analysis and synthesis of the project:
* Audits all persisted sources from Phases 1–11.
* Reports the canonical final performance table across outer test splits.
* Synthesizes quantum feature-map ablation and sample-size scaling dynamics.
* Compares quantum kernel geometry with the classical RBF kernel reference (including Centered Kernel Alignment).
* Displays publication-quality final figures and statistical inferential summaries.
* Documents supported vs unsupported conclusions and research limitations."""

CODE_PHASE12_MODELS = """import importlib
import json
import pandas as pd
from IPython.display import display, Markdown, Image
import phase12
phase12 = importlib.reload(phase12)

phase12_val = phase12.validate_phase12()
print(f"Phase 12 validation status: {phase12_val['status']}")
print(f"Audited source files: {phase12_val['total_source_files_audited']}; Generated tables: {phase12_val['tables_generated']}; Generated figures: {phase12_val['figures_generated']}")

final_models_df = pd.read_csv("results/final/final_model_comparison.csv")
print("\\n--- Canonical Final Model Performance (Mean ± SD across 5 outer splits) ---")
display(final_models_df[~final_models_df["Model"].str.contains("Supplementary")][[
    "Model", "PCA Components", "Qubits", "Accuracy Mean", "Accuracy SD",
    "F1 Mean", "F1 SD", "ROC-AUC Mean", "ROC-AUC SD", "Runtime Mean"
]])"""

MD_PHASE12_FIGS = """### Canonical Final Visualizations

The key experimental dimensions: outer test F1, paired F1 differences, sample-size scaling, and classical RBF vs quantum kernel geometry."""

CODE_PHASE12_FIGS = """display(Image(filename="results/final/final_f1_comparison.png", width=650))
display(Image(filename="results/final/final_paired_f1_differences.png", width=650))
display(Image(filename="results/final/final_sample_size_scaling.png", width=800))
display(Image(filename="results/final/final_kernel_heatmaps.png", width=700))"""

MD_PHASE12_STATS = """### Statistical Comparison and Kernel Alignment"""

CODE_PHASE12_STATS = """stat_df = pd.read_csv("results/final/final_statistical_comparison.csv")
display(stat_df[["Comparison", "Metric", "Mean Paired Diff", "Classical/Left Wins", "Quantum/Right Wins", "Raw p-value", "Holm-Adjusted p-value", "Bootstrap 95% CI Low", "Bootstrap 95% CI High"]])

kernel_df = pd.read_csv("results/final/final_kernel_comparison.csv")
print("\\n--- Kernel Alignment & Geometry (Averaged across 5 seeds) ---")
print("PCA 2 (2Q): Mean CKA =", f"{kernel_df[kernel_df['pca_components']==2]['cka_alignment'].mean():.4f}", 
      "| Mean Frobenius Alignment =", f"{kernel_df[kernel_df['pca_components']==2]['frobenius_alignment'].mean():.4f}",
      "| Quantum Eff Rank =", f"{kernel_df[kernel_df['pca_components']==2]['quantum_effective_rank'].mean():.2f}",
      "| RBF Eff Rank =", f"{kernel_df[kernel_df['pca_components']==2]['rbf_effective_rank'].mean():.2f}")
print("PCA 4 (4Q): Mean CKA =", f"{kernel_df[kernel_df['pca_components']==4]['cka_alignment'].mean():.4f}", 
      "| Mean Frobenius Alignment =", f"{kernel_df[kernel_df['pca_components']==4]['frobenius_alignment'].mean():.4f}",
      "| Quantum Eff Rank =", f"{kernel_df[kernel_df['pca_components']==4]['quantum_effective_rank'].mean():.2f}",
      "| RBF Eff Rank =", f"{kernel_df[kernel_df['pca_components']==4]['rbf_effective_rank'].mean():.2f}")"""

MD_PHASE12_STOP = """### Phase 12 Stop Point — Final Research Synthesis Complete

The canonical final experimental analysis is complete. All research questions (RQ1–RQ8) have been answered with empirical measurements, the full research report is saved at `results/final/final_research_report.md`, and all canonical tables and figures are persisted in `results/final/`."""


def main():
    nb = nbformat.read(NOTEBOOK_PATH, as_version=4)
    
    # Check if Phase 12 already exists
    has_phase12 = any("Phase 12" in "".join(c.get("source", [])) for c in nb.cells)
    if has_phase12:
        print("Phase 12 already exists in notebook. Removing old Phase 12 cells to re-append cleanly...")
        # Find index of first Phase 12 cell
        idx = next(i for i, c in enumerate(nb.cells) if "Phase 12" in "".join(c.get("source", [])))
        nb.cells = nb.cells[:idx]
    
    # Calculate starting execution count
    code_counts = [c.execution_count for c in nb.cells if c.cell_type == "code" and c.execution_count is not None]
    start_count = (max(code_counts) + 1) if code_counts else 1
    
    shell = InteractiveShell.instance()
    
    new_cells = [
        nbformat.v4.new_markdown_cell(source=MD_PHASE12_INTRO),
        nbformat.v4.new_code_cell(source=CODE_PHASE12_MODELS),
        nbformat.v4.new_markdown_cell(source=MD_PHASE12_FIGS),
        nbformat.v4.new_code_cell(source=CODE_PHASE12_FIGS),
        nbformat.v4.new_markdown_cell(source=MD_PHASE12_STATS),
        nbformat.v4.new_code_cell(source=CODE_PHASE12_STATS),
        nbformat.v4.new_markdown_cell(source=MD_PHASE12_STOP),
    ]
    
    current_exec_count = start_count
    for cell in new_cells:
        if cell.cell_type == "code":
            print(f"Executing Phase 12 code cell (execution_count={current_exec_count})...")
            with capture_output() as cap:
                res = shell.run_cell(cell.source)
            if not res.success:
                print("Execution error in cell:")
                print(res.error_in_exec)
                raise RuntimeError(f"Cell execution failed: {res.error_in_exec}")
            
            # Format captured outputs into nbformat outputs
            cell.execution_count = current_exec_count
            outputs = []
            if cap.stdout:
                outputs.append(nbformat.v4.new_output(output_type="stream", name="stdout", text=cap.stdout))
            if cap.stderr:
                outputs.append(nbformat.v4.new_output(output_type="stream", name="stderr", text=cap.stderr))
            for out in cap.outputs:
                outputs.append(nbformat.v4.new_output(
                    output_type="display_data",
                    data=dict(out.data),
                    metadata=dict(out.metadata) if hasattr(out, "metadata") else {}
                ))
            cell.outputs = outputs
            current_exec_count += 1
        
        nb.cells.append(cell)
    
    nbformat.write(nb, NOTEBOOK_PATH)
    print(f"Successfully appended and executed Phase 12 cells in {NOTEBOOK_PATH}")
    print(f"Total cells in notebook now: {len(nb.cells)}")


if __name__ == "__main__":
    main()
