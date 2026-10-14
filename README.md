# APAC Trading Surveillance Framework

A Python-based framework for developing compliance and trading risk monitoring tools across APAC markets, including equities, options, and futures.

## Overview

This repository is designed for building internal surveillance and oversight solutions that help Compliance and Trading Risk teams monitor trading behaviour, investigate exceptions, and surface patterns across desks, products, and regions.

The project is intentionally structured as a starter framework for:
- Python applications and operational dashboards
- integration with trading surveillance and monitoring APIs
- SQL-backed analytics and reporting workflows
- data pipeline and validation patterns for trade and alert data
- collaboration between technical teams and business stakeholders

## Business Context

The role this project supports sits within Compliance and Trading Risk technology, where teams work across APAC markets to monitor trading activity and identify unusual or potentially risky behaviour.

This repository reflects a typical technical stack for that environment:
- Python for application logic and automation
- pandas for data preparation and analysis
- Plotly and Dash for interactive reporting and monitoring dashboards
- SQL for structured data storage and aggregated reporting
- API integration patterns for surveillance and monitoring data sources

## Use Cases

- monitoring trade activity by desk, product, and region
- identifying unusual alert patterns across equities, options, and futures
- summarising surveillance metrics for compliance and risk teams
- delivering business-facing dashboards for operational oversight
- integrating structured trade, alert, and market data into a single workflow

## Repository Layout

```text
.
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── .env.example
├── app/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── main.py
│   ├── dashboards/
│   │   └── surveillance_dashboard.py
│   ├── data/
│   │   └── sample_data.py
│   ├── models/
│   │   └── trade_models.py
│   ├── services/
│   │   └── alert_service.py
│   └── utils/
│       └── helpers.py
├── sql/
│   ├── schema.sql
│   └── views.sql
├── docs/
│   └── architecture.md
├── notebooks/
│   └── exploratory_analysis.ipynb
├── tests/
│   └── test_sample.py
└── .vscode/
```

## Core Components

### Dashboarding
A Dash application provides a sample surveillance dashboard for monitoring:
- trade volume trends by region and product
- alert count patterns over time
- market activity across different asset classes
- operational KPIs for oversight teams

### Data Layer
The repository includes example trade and alert data structures, with patterns suitable for building onto a SQL-backed warehouse or local database workflow.

### Service Layer
The `AlertService` module provides a simple abstraction for summarising flagged trades and alert-related analytics.

### SQL
The SQL folder contains starter schema definitions and summary views that model a typical trade-and-alert structure.

## Quick Start

1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Configure environment variables

```bash
cp .env.example .env
```

4. Run the dashboard

```bash
python -m app
```

The dashboard will run on:
- http://localhost:8050

## Example Dashboard KPIs

- Total trade volume
- Number of alerts
- Regional trade concentration
- Product-level activity summary
- Time-series trends over recent market periods

## Data Model Pattern

The starter design follows a simple monitoring model:
- trades: trade records with desk, product, region, volume, and flag status
- alerts: alert events linked to underlying trades
- summary views: aggregated results by region/product for business reporting

## Fit for Market Surveillance Roles

This project is suitable as a technical demonstration of Python skills for market surveillance, compliance, and trading risk roles because it reflects common requirements in the domain:
- working with structured market data
- building operational dashboards
- producing KPI-driven reporting
- understanding trade and alert workflows
- translating business rules into repeatable Python-based tooling

## Notes

This repository is intended as a starter framework rather than a full production surveillance platform. It is designed to be extended with production APIs, SQL warehouse integration, alerting logic, and governance controls as required by a specific business environment.
