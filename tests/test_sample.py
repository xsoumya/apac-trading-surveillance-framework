from pathlib import Path


def test_sample_placeholder():
    assert Path("README.md").exists()
