WARNING_THRESHOLD = 5 * 60
ERROR_THRESHOLD = 10 * 60

def process_jobs(entries):
    jobs = {}
    report = []

    for entry in entries:
        pid = entry["pid"]
        if entry["event"] == "START":
            jobs[pid] = entry
        elif entry["event"] == "END" and pid in jobs:
            start_entry = jobs.pop(pid)
            duration = (entry["timestamp"] - start_entry["timestamp"]).total_seconds()

            if duration > ERROR_THRESHOLD:
                level = "ERROR"
            elif duration > WARNING_THRESHOLD:
                level = "WARNING"
            else:
                level = "INFO"

            report.append({
                "pid": pid,
                "description": start_entry["description"],
                "start": start_entry["timestamp"].time(),
                "end": entry["timestamp"].time(),
                "duration_sec": int(duration),
                "status": level
            })
    return report
