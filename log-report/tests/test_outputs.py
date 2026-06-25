import json
from pathlib import Path


REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "report.json was not created"
    with REPORT.open() as f:
        return json.load(f)


def test_report_exists():
    """Success criterion: Create report.json."""
    assert REPORT.exists()


def test_total_requests():
    """Success criterion: report contains the total number of requests."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success criterion: report contains the number of unique client IPs."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion: report contains the most requested path."""
    report = load_report()
    assert report["top_path"] == "/index.html"