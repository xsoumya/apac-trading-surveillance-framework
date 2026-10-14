from __future__ import annotations

import pandas as pd


def build_sample_trade_dataframe() -> pd.DataFrame:
    dates = pd.date_range("2024-01-01", periods=30, freq="D")
    region_cycle = ["APAC"] * 10 + ["NORTH_ASIA"] * 10 + ["SE_ASIA"] * 10
    product_cycle = ["equity", "option", "future"] * 10

    trade_volume = [
        1200, 1500, 1800, 1700, 2100, 2400, 1900, 2200, 2600, 2300,
        1300, 1600, 1700, 2000, 2300, 2500, 2100, 2600, 2850, 2720,
        1100, 1400, 1500, 1600, 1750, 2000, 1850, 2100, 2200, 2400,
    ]

    alerts = [
        3, 4, 2, 6, 5, 7, 5, 8, 6, 9,
        2, 3, 4, 5, 6, 7, 5, 8, 10, 9,
        1, 2, 3, 4, 5, 6, 4, 7, 8, 9,
    ]

    return pd.DataFrame(
        {
            "timestamp": dates,
            "region": region_cycle,
            "product": product_cycle,
            "trade_volume": trade_volume,
            "alerts": alerts,
        }
    )
