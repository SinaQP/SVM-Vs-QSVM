"""Reusable plotting routines for final research figures."""

from pathlib import Path
from typing import Union
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def set_research_plot_style():
    """Apply standard clean styling for research figures."""
    plt.rcParams.update({
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.8,
        "grid.color": "#e0e0e0",
        "grid.linestyle": "--",
        "grid.linewidth": 0.5,
    })


def plot_f1_comparison(
    models_df: pd.DataFrame, output_path: Union[str, Path]
) -> Path:
    """Generate final outer-test F1 comparison bar chart."""
    set_research_plot_style()
    df = models_df[~models_df["Model"].str.contains("Supplementary")].copy()
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    colors = ["#1f77b4", "#aec7e8", "#ff7f0e", "#2ca02c"]
    bars = ax.bar(
        df["Model"],
        df["F1 Mean"],
        yerr=df["F1 SD"],
        capsize=5,
        color=colors[:len(df)],
        edgecolor="#333333",
        linewidth=1.0,
    )
    ax.set_ylabel("Malignant F1 Score (Mean ± SD)", fontsize=12)
    ax.set_title("Outer-Test Malignant F1 Score across 5 Stratified Splits", fontsize=13, pad=12)
    ax.set_ylim(0.70, 1.0)
    ax.grid(axis="y", alpha=0.6)
    plt.xticks(rotation=15, ha="right", fontsize=10)
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(p, dpi=300)
    plt.close(fig)
    return p
