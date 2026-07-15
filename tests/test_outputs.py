import json
from pathlib import Path


def test_report_exists():
    """Criterion: produce /app/report.json (file existence)."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_schema_and_types():
    """Criterion: report.json must contain keys total_requests, unique_ips, top_path with correct types."""
    data = json.loads(Path("/app/report.json").read_text())
    assert {"total_requests", "unique_ips", "top_path"} <= set(data.keys()), "report.json is missing required keys"
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert isinstance(data["top_path"], str), "top_path must be a string"


def test_report_values():
    """Criterion: values must match the access log exactly: total_requests==6, unique_ips==3, top_path==/index.html."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6, "total_requests is not 6"
    assert data["unique_ips"] == 3, "unique_ips is not 3"
    assert data["top_path"] == "/index.html", "top_path is not /index.html"

