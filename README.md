# Log Monitoring Application

This tool processes a log file and tracks job durations, emitting alerts for long-running tasks.

## Features

- Parses CSV-style logs with `START` and `END` events
- Calculates job duration based on PID
- Outputs severity level (`INFO`, `WARNING`, `ERROR`)
- Generates a report in CSV format

## Usage

```bash
python main.py
```

## Output

- `job_report.csv`: report with duration and severity per job

## Tests

```bash
pytest test_job_monitor.py
```
