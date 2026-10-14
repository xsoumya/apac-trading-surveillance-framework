from dataclasses import dataclass


@dataclass
class TradeRecord:
    trade_id: int
    desk: str
    product: str
    region: str
    trade_volume: float
    alert_flag: bool = False


@dataclass
class AlertRecord:
    alert_id: int
    trade_id: int
    alert_type: str
    severity: str
    created_at: str
