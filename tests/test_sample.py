from pathlib import Path


def test_sample_placeholder():
    assert Path("README.md").exists()
    assert Path("app/dashboards/surveillance_dashboard.py").exists()
