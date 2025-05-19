from log_parser import parse_log_file
from job_monitor import process_jobs
from report_generator import generate_report

def main():
    log_path = "logs.log"
    entries = parse_log_file(log_path)
    job_reports = process_jobs(entries)
    generate_report(job_reports, output_path="job_report.csv")

if __name__ == "__main__":
    main()
