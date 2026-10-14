# APAC Trading Surveillance Framework

This repository provides a framework for building technical solutions in compliance and trading risk, focused on APAC markets including equities, options, and futures.

## Context

The role sits within Compliance and Trading Risk technology and supports oversight of trading activity across APAC markets. The work combines:
- Python application development
- Dashboard and reporting tooling
- API integrations with surveillance and monitoring platforms
- Data pipeline and SQL workflows
- Collaboration with Compliance and Trading Risk teams to translate business requirements into technical solutions

## Goal of this repository

This project is a starter framework for building internal tools that help teams monitor trading activity, investigate alerts, and deliver operational oversight across market products and regions.

## Core capabilities

- Trade monitoring dashboards for product and region views
- Alert investigation workflows and summary metrics
- SQL schema patterns for storing trade and surveillance data
- ETL and API integration scaffolding
- Configurable environment and deployment settings

## Repository layout

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
│   │   ├── __init__.py
│   │   └── surveillance_dashboard.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── sample_data.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── trade_models.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── alert_service.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── sql/
│   ├── schema.sql
│   └── views.sql
├── tests/
│   └── test_sample.py
├── docs/
│   └── architecture.md
└── notebooks/
    └── exploratory_analysis.ipynb
```

## Recommended technology stack

- Python
- pandas
- Plotly
- Dash
- SQLAlchemy
- PostgreSQL / SQLite for local development
- Requests for API integration
- Jupyter for exploratory analysis

## Quick start

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy environment variables:

```bash
cp .env.example .env
```

4. Run the dashboard:

```bash
python -m app
```

This starts the sample Dash surveillance dashboard locally.

## Example dashboard views

- trade volume by region and product
- alert counts and exception trends
- time-based series monitoring
- desk and market segment segmentation

## Example production use cases

- Monitoring unusual trading activity in equities, options, and futures
- Building operational or regulatory dashboards for APAC surveillance teams
- Aggregating trade and alert metrics for investigation workflows
- Integrating with surveillance or monitoring platform APIs
- Driving business-facing reporting with SQL and Python analytics

## Notes

This repository is intentionally structured as a starter framework to support building production-ready monitoring and compliance tools while maintaining strong separation between data, models, services, and UI layers.
