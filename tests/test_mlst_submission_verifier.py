"""Regression protection for audited MLST reporting inconsistencies."""

import re
from pathlib import Path

import pandas as pd
import pytest

from scripts.verify_mlst_submission import (
    verify_runtime_ratio_language,
    verify_sample_size_language,
    verify_supplementary_table_references,
)


ROOT = Path(__file__).resolve().parents[1]

SUPPLEMENTARY_TABLES = r"""
\begin{table}
\caption{Per-seed corrected nested QSVC selections.}
\end{table}
\begin{table}
\caption{Complete Sample-Size Scaling Results across 5 Outer Splits.}
\end{table}
\begin{table}
\caption{Execution Time, Computational Complexity, and Storage Footprint.}
\end{table}
"""

CORRECT_REFERENCES = """
Full tabular scaling values are documented in Supplementary Table S2.
Complete runtime profiling is provided in Supplementary Table S3.
"""


def _runtime_artifacts() -> tuple[pd.DataFrame, pd.DataFrame]:
    qsvc = pd.read_csv(ROOT / "results/corrected_nested/qsvc_outer_test_summary.csv")
    linear = pd.read_csv(ROOT / "results/final/final_runtime_summary.csv")
    return qsvc, linear


def _sample_artifact() -> pd.DataFrame:
    return pd.read_csv(ROOT / "results/final/final_sample_size_summary.csv")


def test_corrected_runtime_ratio_prose_passes():
    qsvc, linear = _runtime_artifacts()
    text = (
        "Exact statevector QSVC pipelines took approximately 45 and 71 times "
        "as long for 2Q and 4Q, respectively."
    )
    ratios = verify_runtime_ratio_language(text, qsvc, linear)
    assert ratios == pytest.approx((45.112153281, 70.511848363))


def test_stale_runtime_ratio_prose_fails():
    qsvc, linear = _runtime_artifacts()
    with pytest.raises(AssertionError, match="Obsolete canonical"):
        verify_runtime_ratio_language(
            "Exact statevector QSVC took 47–80 times as long.", qsvc, linear
        )


def test_false_monotonic_sample_size_claim_fails():
    with pytest.raises(AssertionError, match="False monotonic"):
        verify_sample_size_language(
            "QSVC performance steadily improved with sample size.", _sample_artifact()
        )


def test_corrected_non_monotonic_sample_size_prose_passes():
    text = (
        "QSVC performance generally improved. The 2Q sequence peaked at N=300 "
        "and then declined slightly at N=455."
    )
    sequence = verify_sample_size_language(text, _sample_artifact())
    assert sequence[-1] < sequence[-2]


def test_correct_sample_size_to_s2_reference_passes():
    mapping = verify_supplementary_table_references(
        CORRECT_REFERENCES, SUPPLEMENTARY_TABLES
    )
    assert mapping["sample_size"] == "S2"


def test_incorrect_sample_size_to_s1_reference_fails():
    text = CORRECT_REFERENCES.replace(
        "tabular scaling values are documented in Supplementary Table S2",
        "tabular scaling values are documented in Supplementary Table S1",
    )
    with pytest.raises(AssertionError, match="sample_size discussion references"):
        verify_supplementary_table_references(text, SUPPLEMENTARY_TABLES)


def test_correct_runtime_to_s3_reference_passes():
    mapping = verify_supplementary_table_references(
        CORRECT_REFERENCES, SUPPLEMENTARY_TABLES
    )
    assert mapping["runtime"] == "S3"


def test_incorrect_runtime_to_s2_reference_fails():
    text = CORRECT_REFERENCES.replace(
        "runtime profiling is provided in Supplementary Table S3",
        "runtime profiling is provided in Supplementary Table S2",
    )
    with pytest.raises(AssertionError, match="runtime discussion references"):
        verify_supplementary_table_references(text, SUPPLEMENTARY_TABLES)


def test_changed_supplementary_table_order_is_detected():
    tables = re.findall(
        r"\\begin\{table\}.*?\\end\{table\}", SUPPLEMENTARY_TABLES, re.DOTALL
    )
    reordered = "\n".join((tables[1], tables[0], tables[2]))
    with pytest.raises(AssertionError, match="sample_size discussion references"):
        verify_supplementary_table_references(CORRECT_REFERENCES, reordered)
