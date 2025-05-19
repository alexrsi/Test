import csv
from datetime import datetime

TIME_FORMAT = "%H:%M:%S"

def parse_log_file(file_path):
    entries = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 4:
                continue
            time_str, description, event_type, pid = map(str.strip, row)
            timestamp = datetime.strptime(time_str, TIME_FORMAT)
            entries.append({
                "timestamp": timestamp,
                "description": description,
                "event": event_type.upper(),
                "pid": pid
            })
    return entries
