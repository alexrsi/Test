import csv

def generate_report(report_data, output_path="report.csv"):
    fieldnames = ["pid", "description", "start", "end", "duration_sec", "status"]
    with open(output_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_data)
    print(f"Report written to {output_path}")
