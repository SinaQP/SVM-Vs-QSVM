"""Utility module for configuration loading, naming, and data persistence."""

from pathlib import Path
from typing import Any, Dict, List, Optional, Union
import json
import pandas as pd

DEFAULT_SEEDS: List[int] = [42, 123, 456, 789, 2026]
DEFAULT_C_VALUES: List[float] = [0.01, 0.1, 1.0, 10.0, 100.0]
DEFAULT_GAMMA_VALUES: List[Union[str, float]] = ["scale", "auto", 0.01, 0.1, 1.0]
TIE_ATOL: float = 1e-12
BOOTSTRAP_SEED: int = 42
N_BOOTSTRAP: int = 10000
METRICS: List[str] = ["accuracy", "precision", "recall", "f1", "roc_auc"]
PRIMARY_COMPARISONS: List[str] = [
    "Classical PCA2 vs QSVC PCA2",
    "Classical PCA4 vs QSVC PCA4",
    "QSVC PCA2 vs QSVC PCA4",
]

SEEDS = DEFAULT_SEEDS
C_VALUES = DEFAULT_C_VALUES
GAMMA_VALUES = DEFAULT_GAMMA_VALUES


def model_name(kernel: str, dim: int) -> str:
    """Return standardized model display name."""
    if kernel == "quantum":
        return f"QSVC — PCA {dim} / {dim}Q (reps=1, full)"
    prefix = "Linear" if kernel == "linear" else "RBF"
    return f"{prefix} SVM — PCA {dim}"


def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
    """Load configuration from YAML, JSON, or TOML file."""
    path = Path(config_path)
    if not path.exists():
        raise FileNotFoundError(f"Configuration file not found: {path}")

    suffix = path.suffix.lower()
    if suffix in (".yaml", ".yml"):
        import yaml
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    elif suffix == ".json":
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    elif suffix == ".toml":
        try:
            import tomllib
            with open(path, "rb") as f:
                return tomllib.load(f)
        except ImportError:
            import tomli
            with open(path, "rb") as f:
                return tomli.load(f)
    else:
        raise ValueError(f"Unsupported configuration file extension: {suffix}")


def save_json(data: Any, path: Union[str, Path], indent: int = 2) -> Path:
    """Save serializable data to JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
    return p


def save_csv(frame: pd.DataFrame, directory: Union[str, Path], name: str) -> Path:
    """Save DataFrame to CSV in specified directory."""
    d = Path(directory)
    d.mkdir(parents=True, exist_ok=True)
    p = d / name
    frame.to_csv(p, index=False)
    return p
