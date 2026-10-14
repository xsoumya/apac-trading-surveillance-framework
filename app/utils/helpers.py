from __future__ import annotations

from pathlib import Path


def format_metric(value: float | int) -> str:
    if isinstance(value, float):
        return f"{value:,.2f}"
    return f"{value:,}"


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent
