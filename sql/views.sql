CREATE VIEW IF NOT EXISTS trade_alert_summary AS
SELECT
    t.region,
    t.product,
    COUNT(t.trade_id) AS total_trades,
    SUM(CASE WHEN t.alert_flag = 1 THEN 1 ELSE 0 END) AS alert_count,
    ROUND(AVG(t.trade_volume), 2) AS avg_trade_volume
FROM trades t
GROUP BY t.region, t.product;
