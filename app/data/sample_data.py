import pandas as pd


def build_sample_trade_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "trade_id": [101, 102, 103, 104, 105],
            "desk": ["Equity Flow", "Options Desk", "Futures Desk", "Macro Desk", "Equity Flow"],
            "product": ["equity", "option", "future", "equity", "option"],
            "region": ["APAC", "APAC", "NORTH_ASIA", "SE_ASIA", "APAC"],
            "trade_volume": [15000, 22000, 18000, 25000, 31000],
            "alert_flag": [False, True, False, True, False],
        }
    )
