from __future__ import annotations

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from app.config import get_config
from app.data.sample_data import build_sample_trade_dataframe


CONFIG = get_config()


def create_dashboard() -> Dash:
    df = build_sample_trade_dataframe()
    app = Dash(__name__)

    app.layout = html.Div(
        style={"padding": "20px", "fontFamily": "Arial, sans-serif"},
        children=[
            html.H1(CONFIG["dashboard_title"]),
            html.Div(
                [
                    html.Label("Market region"),
                    dcc.Dropdown(
                        id="region-filter",
                        options=[{"label": region, "value": region} for region in CONFIG["market_regions"]],
                        value="APAC",
                        clearable=False,
                    ),
                ],
                style={"width": "300px", "marginBottom": "20px"},
            ),
            html.Div(
                [
                    dcc.Graph(id="volume-chart"),
                    dcc.Graph(id="alerts-chart"),
                ]
            ),
        ],
    )

    @app.callback(Output("volume-chart", "figure"), Input("region-filter", "value"))
    def update_volume_chart(region: str):
        filtered = df[df["region"] == region]
        fig = px.line(
            filtered,
            x="timestamp",
            y="trade_volume",
            color="product",
            title=f"Trade Volume by Product - {region}",
        )
        fig.update_layout(template="plotly_white")
        return fig

    @app.callback(Output("alerts-chart", "figure"), Input("region-filter", "value"))
    def update_alerts_chart(region: str):
        filtered = df[df["region"] == region]
        fig = px.bar(
            filtered,
            x="timestamp",
            y="alerts",
            color="product",
            title=f"Alert Counts - {region}",
        )
        fig.update_layout(template="plotly_white")
        return fig

    return app
