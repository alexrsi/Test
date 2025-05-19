import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from job_monitor import process_jobs
from datetime import datetime

def test_process_jobs_simple_case():
    entries = [
        {"timestamp": datetime.strptime("12:00:00", "%H:%M:%S"), "description": "task 001", "event": "START", "pid": "123"},
        {"timestamp": datetime.strptime("12:05:01", "%H:%M:%S"), "description": "task 001", "event": "END", "pid": "123"},
    ]
    result = process_jobs(entries)
    assert len(result) == 1
    assert result[0]["duration_sec"] == 301
    assert result[0]["status"] == "WARNING"
