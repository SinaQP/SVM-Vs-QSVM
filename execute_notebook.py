"""Execute every notebook cell in order and persist execution/failure evidence."""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import json
import os
import sys

import nbformat
from nbclient import NotebookClient

root = Path(__file__).resolve().parent
os.chdir(root)
os.environ["PYTHONIOENCODING"] = "utf-8"
os.environ["MPLBACKEND"] = "module://matplotlib_inline.backend_inline"
os.environ["JUPYTER_RUNTIME_DIR"] = str(root / ".venv" / "jupyter-runtime")
os.environ["IPYTHONDIR"] = str(root / ".venv" / "ipython")
sys.stdout.reconfigure(encoding="utf-8")
notebook_path = root / "svm_vs_qsvm_setup.ipynb"
notebook = nbformat.read(notebook_path, as_version=4)
for cell in notebook.cells:
    if cell.cell_type == "code":
        cell.outputs = []
        cell.execution_count = None
progress = {"status": "RUNNING", "started_utc": datetime.now(timezone.utc).isoformat(), "completed_code_cells": [], "error": None}
started = perf_counter()
progress_path = root / "results" / "phase11_notebook_execution.json"


def record(**kwargs):
    progress.update(kwargs)
    progress["elapsed_seconds"] = perf_counter() - started
    progress_path.write_text(json.dumps(progress, indent=2), encoding="utf-8")


def on_cell_start(cell, cell_index, **kwargs):
    if cell.cell_type == "code":
        record(current_cell=cell_index, current_source=cell.source.splitlines()[0])
        print(f"Executing cell {cell_index}: {cell.source.splitlines()[0]}", flush=True)


def on_cell_executed(cell, cell_index, **kwargs):
    progress["completed_code_cells"].append(cell_index)
    record()


client = NotebookClient(notebook, timeout=7200, kernel_name="python3", allow_errors=False,
                        resources={"metadata": {"path": str(root)}},
                        on_cell_start=on_cell_start, on_cell_executed=on_cell_executed)
try:
    client.execute()
    counts = [cell.execution_count for cell in notebook.cells if cell.cell_type == "code"]
    assert counts == list(range(1, len(counts) + 1)), "Code cells did not execute sequentially."
    record(status="SUCCESS", executed_code_cells=len(counts))
except Exception as error:
    record(status="FAILED", error=repr(error))
    raise
finally:
    nbformat.write(notebook, notebook_path)
print(f"Notebook execution {progress['status']}: {progress['elapsed_seconds']:.1f}s", flush=True)
