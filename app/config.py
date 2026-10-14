from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
APP_DIR = BASE_DIR / "app"

DEFAULT_CONFIG = {
    "environment": "dev",
    "sql_database_url": "sqlite:///surveillance.db",
    "market_regions": ["APAC", "NORTH_ASIA", "SE_ASIA"],
    "supported_products": ["equity", "option", "future"],
    "dashboard_title": "APAC Trading Surveillance Overview",
}


def get_config() -> dict:
    return DEFAULT_CONFIG.copy()
