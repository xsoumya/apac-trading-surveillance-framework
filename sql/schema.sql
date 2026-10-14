CREATE TABLE IF NOT EXISTS trades (
    trade_id INTEGER PRIMARY KEY,
    trade_datetime TEXT NOT NULL,
    desk TEXT NOT NULL,
    product TEXT NOT NULL,
    region TEXT NOT NULL,
    trade_volume REAL NOT NULL,
    alert_flag INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY,
    trade_id INTEGER NOT NULL,
    alert_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    created_at TEXT NOT NULL,
    FOREIGN KEY (trade_id) REFERENCES trades(trade_id)
);

CREATE INDEX IF NOT EXISTS idx_trades_region_product
ON trades(region, product);
