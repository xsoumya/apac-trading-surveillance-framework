from __future__ import annotations

from app.dashboards.surveillance_dashboard import create_dashboard


def main() -> None:
    app = create_dashboard()
    app.run(host="0.0.0.0", port=8050, debug=True)


if __name__ == "__main__":
    main()
