from typing import Any


def format_metric(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)
