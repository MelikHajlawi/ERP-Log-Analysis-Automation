# log_processing.py
# This module provides functions to filter log entries and identify error logs.

from datetime import datetime, timedelta

def filter_last_24_hours(log_entries):
    """
    Filters log entries to include only those from the last 24 hours.
    """
    last_24_hours = datetime.now().astimezone() - timedelta(days=1)
    return [
        entry for entry in log_entries 
        if datetime.strptime(entry['timestamp'], '%Y/%m/%d@%H:%M:%S.%f%z') >= last_24_hours
    ]

def extract_error_logs(log_entries, keywords):
    """
    Extracts log entries containing error-related keywords.
    """
    error_logs = []
    for entry in log_entries:
        if any(keyword.lower() in entry['message'].lower() for keyword in keywords):
            error_logs.append(entry)
    return error_logs
 
