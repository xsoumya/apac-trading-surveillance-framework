CREATE TABLE IF NOT EXISTS trades (
    trade_id INTEGER PRIMARY KEY,
    timestamp TEXT,
    desk TEXT,
    product TEXT,
    region TEXT,
    trade_volume REAL,
    alert_flag INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS alerts (
    alert_id INTEGER PRIMARY KEY,
    trade_id INTEGER,
    alert_type TEXT,
    severity TEXT,
    created_at TEXT,
    FOREIGN KEY (trade_id) REFERENCES trades(trade_id)
);
