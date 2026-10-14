from app.dashboards.surveillance_dashboard import create_dashboard

if __name__ == "__main__":
    dashboard = create_dashboard()
    dashboard.run(debug=True, host="0.0.0.0", port=8050)
