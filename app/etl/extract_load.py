from typing import Any


def load_trade_data() -> list[dict[str, Any]]:
    return [
        {"trade_id": 1001, "product": "equity", "region": "APAC", "qty": 1200, "alert": False},
        {"trade_id": 1002, "product": "option", "region": "NORTH_ASIA", "qty": 980, "alert": True},
        {"trade_id": 1003, "product": "future", "region": "SE_ASIA", "qty": 750, "alert": False},
    ]
