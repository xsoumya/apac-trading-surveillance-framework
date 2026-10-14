CREATE VIEW IF NOT EXISTS trade_alert_summary AS
SELECT
    t.region,
    t.product,
    COUNT(t.trade_id) AS total_trades,
    SUM(CASE WHEN t.alert_flag = 1 THEN 1 ELSE 0 END) AS total_alerts,
    ROUND(AVG(t.trade_volume), 2) AS avg_trade_volume,
    ROUND(AVG(CASE WHEN t.alert_flag = 1 THEN t.trade_volume ELSE 0 END), 2) AS avg_alert_trade_volume
FROM trades t
GROUP BY t.region, t.product;

SELECT
    region,
    product,
    SUM(trade_volume) AS yy_total_volume,
    SUM(CASE WHEN alert_flag = 1 THEN 1 ELSE 0 END) AS alert_counts
FROM trades
GROUP BY region, product
ORDER BY region, product;
