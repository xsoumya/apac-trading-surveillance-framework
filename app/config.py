from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AppConfig:
    environment: str = "dev"
    sql_database_url: str = "sqlite:///surveillance.db"
    dashboard_title: str = "APAC Trading Surveillance Overview"
    market_regions: list[str] = field(default_factory=lambda: ["APAC", "NORTH_ASIA", "SE_ASIA"])
    supported_products: list[str] = field(default_factory=lambda: ["equity", "option", "future"])
    api_base_url: str = "https://example.com/surveillance-api"

    @classmethod
    def from_env(cls) -> "AppConfig":
        import os

        return cls(
            environment=os.getenv("APP_ENV", "dev"),
            sql_database_url=os.getenv("DATABASE_URL", "sqlite:///surveillance.db"),
            dashboard_title=os.getenv("DASHBOARD_TITLE", "APAC Trading Surveillance Overview"),
            market_regions=os.getenv("MARKET_REGIONS", "APAC,NORTH_ASIA,SE_ASIA").split(","),
            supported_products=os.getenv("SUPPORTED_PRODUCTS", "equity,option,future").split(","),
            api_base_url=os.getenv("SURVEILLANCE_API_BASE_URL", "https://example.com/surveillance-api"),
        )


CONFIG = AppConfig.from_env()


def get_config() -> dict[str, Any]:
    return {
        "environment": CONFIG.environment,
        "sql_database_url": CONFIG.sql_database_url,
        "dashboard_title": CONFIG.dashboard_title,
        "market_regions": CONFIG.market_regions,
        "supported_products": CONFIG.supported_products,
        "api_base_url": CONFIG.api_base_url,
    }
