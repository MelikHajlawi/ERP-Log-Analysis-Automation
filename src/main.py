# main.py
# This main script orchestrates the entire process, from log parsing and filtering to data insertion.

import pandas as pd
from database import engine, test_connection, get_log_paths
from log_parser import parse_log_file
from log_processing import filter_last_24_hours, extract_error_logs
from data_insertion import insert_logs_with_progress
from backup_summary import summarize_backup_logs

def process_log_files():
    """
    Iterates through each log file path, parses the logs, filters recent entries,
    and identifies error-related logs based on predefined keywords.
    Returns two lists: general logs and error logs.
    """
    log_paths = get_log_paths()
    general_log_entries = []
    error_log_entries = []

    for log_path in log_paths:
        serveur, instance, database, file_path = log_path
        print(f"Processing log file: {file_path}")
        log_entries = list(parse_log_file(file_path, serveur, instance, database, engine))
        recent_entries = filter_last_24_hours(log_entries)
        error_entries = extract_error_logs(recent_entries, keywords=[
            "d'erreurs", "erreur", "erreurs", "Arret anormal", "Anormal"
        ])
        general_log_entries.extend(recent_entries)
        error_log_entries.extend(error_entries)

    return general_log_entries, error_log_entries

if __name__ == "__main__":
    # Step 1: Test database connection
    test_connection(engine)

    # Step 2: Process log files and filter data
    general_log_entries, error_log_entries = process_log_files()

    # Step 3: Convert parsed entries to DataFrames
    general_log_df = pd.DataFrame(general_log_entries)
    error_log_df = pd.DataFrame(error_log_entries)

    # Step 4: Enrich general logs with date-related columns
    general_log_df = general_log_df.assign(
        year=lambda df: pd.to_datetime(df['timestamp']).dt.year,
        month=lambda df: pd.to_datetime(df['timestamp']).dt.month,
        day=lambda df: pd.to_datetime(df['timestamp']).dt.day
    )

    # Step 5: Insert error logs into database
    insert_logs_with_progress(error_log_df, 'log_error_2_0', engine)

    # Step 6: Summarize backup logs and insert into database
    backup_summary_df = summarize_backup_logs(general_log_df)
    insert_logs_with_progress(backup_summary_df, 'backup_log_summary', engine)
 
