from __future__ import annotations

import pandas as pd


def build_sample_trade_dataframe() -> pd.DataFrame:
    dates = pd.date_range("2024-01-01", periods=90, freq="D")
    regions = ["APAC", "NORTH_ASIA", "SE_ASIA"]
    products = ["equity", "option", "future"]
    desks = ["Flow Desk", "Options Desk", "Futures Desk", "Macro Desk", "Index Desk"]

    rows = []
    for idx, date in enumerate(dates):
        region = regions[idx % len(regions)]
        product = products[idx % len(products)]
        desk = desks[idx % len(desks)]
        trade_volume = 1200 + ((idx * 97) % 2200)
        alerts = (idx % 8) + (1 if product == "option" else 0) + (2 if region == "APAC" else 0)
        compliance_score = max(60, 98 - alerts * 3 + (idx % 4))

        rows.append(
            {
                "timestamp": date,
                "region": region,
                "product": product,
                "desk": desk,
                "trade_volume": trade_volume,
                "alerts": alerts,
                "compliance_score": compliance_score,
            }
        )

    return pd.DataFrame(rows)
