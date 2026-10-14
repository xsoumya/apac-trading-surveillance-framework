from __future__ import annotations

from app.models.trade_models import AlertRecord, TradeRecord


class AlertService:
    def __init__(self, records: list[TradeRecord] | None = None):
        self.records = records or []

    def flagged_trades(self) -> list[TradeRecord]:
        return [record for record in self.records if record.alert_flag]

    def summary_by_region(self) -> dict[str, int]:
        summary: dict[str, int] = {}
        for record in self.records:
            summary[record.region] = summary.get(record.region, 0) + 1
        return summary

    def summary_by_product(self) -> dict[str, int]:
        summary: dict[str, int] = {}
        for record in self.records:
            summary[record.product] = summary.get(record.product, 0) + 1
        return summary

    def create_alert(self, trade: TradeRecord, alert_type: str, severity: str, created_at: str) -> AlertRecord:
        alert_id = abs(hash((trade.trade_id, alert_type, created_at))) % 1_000_000
        return AlertRecord(
            alert_id=alert_id,
            trade_id=trade.trade_id,
            alert_type=alert_type,
            severity=severity,
            created_at=created_at,
        )
