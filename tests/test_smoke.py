"""Smoke test -- verifies the package is importable and pytest runs."""

from prediction_market_qts import hello


def test_import():
    assert hello() == "Hello from prediction-market-qts!"
