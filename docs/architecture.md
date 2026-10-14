# APAC Trading Surveillance Framework

This document outlines the intended architecture for building surveillance and compliance tooling for APAC trading activity.

## Components

1. Data ingestion
   - Connect to surveillance, market data, and internal system APIs
   - Support batch and event-driven ingestion patterns

2. Data processing
   - Normalise trade, position, client, and alert data into a consistent model
   - Enforce quality checks and validation for missing or malformed records

3. Storage
   - Use SQL for structured trade and alert data storage
   - Enable analytics and reporting via warehouse or database views

4. Analytics
   - Aggregate by product, desk, region, and time period
   - Support alert investigation and exception analysis

5. Visualisation
   - Build operational dashboards for compliance and risk teams
   - Use interactive charts for time-series, alert trends, and exception monitoring

6. Delivery
   - Package reusable modules for API integration, dashboarding, and ETL logic
   - Use tests and clear configuration patterns for production-grade development
