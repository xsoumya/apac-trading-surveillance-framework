from dataclasses import dataclass


@dataclass
class TradeRecord:
    trade_id: int
    desk: str
    product: str
    region: str
    trade_volume: float
    alert_flag: bool = False
