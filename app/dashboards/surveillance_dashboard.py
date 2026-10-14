from __future__ import annotations

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

from app.config import get_config
from app.data.sample_data import build_sample_trade_dataframe

CONFIG = get_config()


def _metric_card(title: str, value: str, color: str = "#2F6FED") -> html.Div:
    return html.Div(
        style={
            "backgroundColor": "#F5F7FB",
            "padding": "16px 18px",
            "borderRadius": "12px",
            "boxShadow": "0 1px 2px rgba(0,0,0,0.08)",
            "minWidth": "180px",
            "flex": "1",
            "borderLeft": f"4px solid {color}",
        },
        children=[
            html.Div(style={"fontSize": "12px", "color": "#5A6475", "textTransform": "uppercase"}, children=[title]),
            html.Div(style={"fontSize": "28px", "fontWeight": "700", "marginTop": "8px", "color": "#111827"}, children=[value]),
        ],
    )


def create_dashboard() -> Dash:
    df = build_sample_trade_dataframe()
    app = Dash(__name__, title="APAC Trading Surveillance Dashboard")

    product_options = [{"label": product.title(), "value": product} for product in CONFIG["supported_products"]]
    region_options = [{"label": region, "value": region} for region in CONFIG["market_regions"]]

    app.layout = html.Div(
        style={"padding": "24px", "backgroundColor": "#F8FAFC", "minHeight": "100vh"},
        children=[
            html.H1("APAC Trading Surveillance Overview", style={"marginBottom": "18px", "color": "#111827"}),
            html.Div(
                [
                    html.Div(
                        [
                            html.Label("Region", style={"display": "block", "marginBottom": "8px", "fontWeight": "600"}),
                            dcc.Dropdown(
                                id="region-filter",
                                options=region_options,
                                value="APAC",
                                clearable=False,
                            ),
                        ],
                        style={"width": "240px", "marginRight": "16px"},
                    ),
                    html.Div(
                        [
                            html.Label("Product", style={"display": "block", "marginBottom": "8px", "fontWeight": "600"}),
                            dcc.Dropdown(
                                id="product-filter",
                                options=product_options,
                                value="equity",
                                clearable=False,
                            ),
                        ],
                        style={"width": "240px"},
                    ),
                ],
                style={"display": "flex", "marginBottom": "24px"},
            ),
            html.Div(
                id="summary-cards",
                style={"display": "flex", "gap": "16px", "flexWrap": "wrap", "marginBottom": "24px"},
            ),
            html.Div(
                [
                    dcc.Graph(id="trade-volume-chart"),
                    dcc.Graph(id="alert-chart"),
                ],
                style={"display": "grid", "gridTemplateColumns": "1fr 1fr", "gap": "20px"},
            ),
        ],
    )

    @app.callback(
        Output("summary-cards", "children"),
        Input("region-filter", "value"),
        Input("product-filter", "value"),
    )
    def update_summary_cards(region: str, product: str):
        filtered = df[(df["region"] == region) & (df["product"] == product)]
        total_volume = int(filtered["trade_volume"].sum())
        total_alerts = int(filtered["alerts"].sum())
        avg_score = round(filtered["compliance_score"].mean(), 1)
        avg_volume = int(filtered["trade_volume"].mean())

        return [
            _metric_card("Trade Volume", f"{total_volume:,}", "#2F6FED"),
            _metric_card("Alert Count", f"{total_alerts:,}", "#E67E22"),
            _metric_card("Avg Compliance", f"{avg_score:.1f}%", "#16A34A"),
            _metric_card("Avg Volume", f"{avg_volume:,}", "#8B5CF6"),
        ]

    @app.callback(
        Output("trade-volume-chart", "figure"),
        Input("region-filter", "value"),
        Input("product-filter", "value"),
    )
    def update_trade_volume_chart(region: str, product: str):
        filtered = df[(df["region"] == region) & (df["product"] == product)]
        fig = px.line(
            filtered,
            x="timestamp",
            y="trade_volume",
            title=f"Trade Volume Trend - {region} / {product.title()}",
            markers=True,
        )
        fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=50, b=20))
        return fig

    @app.callback(
        Output("alert-chart", "figure"),
        Input("region-filter", "value"),
        Input("product-filter", "value"),
    )
    def update_alert_chart(region: str, product: str):
        filtered = df[(df["region"] == region) & (df["product"] == product)]
        fig = px.bar(
            filtered,
            x="timestamp",
            y="alerts",
            title=f"Alert Counts - {region} / {product.title()}",
            color_discrete_sequence=["#F59E0B"],
        )
        fig.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=50, b=20))
        return fig

    return app
