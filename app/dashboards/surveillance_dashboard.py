from __future__ import annotations

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

from app.config import get_config


def build_sample_dataframe() -> pd.DataFrame:
    data = {
        "timestamp": pd.date_range("2024-01-01", periods=30, freq="D"),
        "region": ["APAC"] * 10 + ["NORTH_ASIA"] * 10 + ["SE_ASIA"] * 10,
        "product": ["equity", "option", "future"] * 10,
        "trade_volume": [1200, 1500, 1800, 1700, 2100, 2400, 1900, 2200, 2600, 2300,
                         1300, 1600, 1700, 2000, 2300, 2500, 2100, 2600, 2850, 2720,
                         1100, 1400, 1500, 1600, 1750, 2000, 1850, 2100, 2200, 2400],
        "alerts": [3, 4, 2, 6, 5, 7, 5, 8, 6, 9,
                   2, 3, 4, 5, 6, 7, 5, 8, 10, 9,
                   1, 2, 3, 4, 5, 6, 4, 7, 8, 9],
    }
    return pd.DataFrame(data)


def create_dashboard() -> Dash:
    config = get_config()
    df = build_sample_dataframe()

    app = Dash(__name__)
    app.layout = html.Div([
        html.H1(config["dashboard_title"]),
        html.Div([
            dcc.Dropdown(
                id="region-filter",
                options=[{"label": region, "value": region} for region in config["market_regions"]],
                value="APAC",
                clearable=False,
            )
        ], style={"width": "300px", "marginBottom": "20px"}),
        dcc.Graph(id="volume-chart"),
        dcc.Graph(id="alerts-chart"),
    ])

    @app.callback(
        Output("volume-chart", "figure"),
        Input("region-filter", "value"),
    )
    def update_volume_chart(region):
        filtered = df[df["region"] == region]
        fig = px.line(filtered, x="timestamp", y="trade_volume", color="product",
                      title=f"Trade Volume by Product - {region}")
        return fig

    @app.callback(
        Output("alerts-chart", "figure"),
        Input("region-filter", "value"),
    )
    def update_alerts_chart(region):
        filtered = df[df["region"] == region]
        fig = px.bar(filtered, x="timestamp", y="alerts", color="product",
                     title=f"Alert Counts - {region}")
        return fig

    return app


if __name__ == "__main__":
    dashboard = create_dashboard()
    dashboard.run(debug=True, host="0.0.0.0", port=8050)
