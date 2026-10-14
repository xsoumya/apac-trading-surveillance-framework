# APAC Trading Surveillance Framework

This repository provides a starter framework for building compliance and trading risk tooling focused on APAC markets, including equities, options, and futures.

## Purpose

This project is designed to support:
- Python-based applications for surveillance and oversight
- Interactive dashboards for compliance and trading risk teams
- Integration with trading surveillance, monitoring, and market data APIs
- Data pipeline and SQL workflows for analytics and investigation use cases
- Collaboration with business stakeholders to translate requirements into technical solutions

## Typical Use Cases

- Monitoring unusual execution patterns
- Investigating trading alerts and exceptions
- Surveilling client or desk activity across multiple instruments
- Building operational dashboards for APAC market oversight
- Combining trade, reference, and surveillance system data in a unified workflow

## Repository Layout

```text
.
├── README.md
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── dashboards/
│   │   ├── __init__.py
│   │   └── surveillance_dashboard.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── sample_data.py
│   ├── etl/
│   │   ├── __init__.py
│   │   └── extract_load.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── trade_models.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── sql/
│   ├── schema.sql
│   └── views.sql
├── tests/
│   └── test_sample.py
├── notebooks/
│   └── exploratory_analysis.ipynb
└── docs/
    └── architecture.md
```

## Technology Stack

- Python
- pandas
- Plotly
- Dash
- SQL / PostgreSQL-compatible patterns
- API client integration
- Jupyter notebooks for exploration and prototyping

## Getting Started

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the sample dashboard:
   ```bash
   python -m app.main
   ```

## Example Dashboard Features

- Trade volume and activity overview
- Alert and surveillance event summaries
- Instrument- and desk-level breakdowns
- Time-series visualisation of activity trends
- Filters for product type, region, and date range

## Notes

This is a starter framework intended for internal technical enablement and prototype development in the compliance and trading risk domain.
