# backup_summary.py

import pandas as pd
from datetime import datetime, time

def time_to_datetime(t):
    """
    Combines a time object with a base date to create a datetime object.
    """
    base_date = datetime(1900, 1, 1)
    return datetime.combine(base_date, t)

def summarize_backup_logs(df):
    """
    Summarizes backup-related logs, calculating metrics such as backup duration, backup size,
    total data written, and error status.
    Returns a DataFrame containing the summarized backup information.
    """
    backup_summaries = []

    if df.empty:
        print("DataFrame is empty. No backup logs to summarize.")
        return pd.DataFrame(backup_summaries)

    # Ensure 'time_ms' is in a consistent timedelta format
    if isinstance(df['time_ms'].iloc[0], time):
        df['time_ms'] = df['time_ms'].apply(lambda t: str(t))
    df['time_ms'] = pd.to_timedelta(df['time_ms'])

    # Group by 'process_id' for individual backup sessions
    grouped = df.groupby('process_id')
    
    for process_id, group in grouped:
        group = group.sort_values('time_ms')

        # Identify presence of backup start and end messages
        has_backup_start = group['message'].str.contains('Début de la sauvegarde').any()
        has_backup_end = group['message'].str.contains('terminée correctement|pour cause d\'erreurs').any()
        
        # Skip group if no backup start was detected
        if not has_backup_start:
            continue  

        # Retrieve start and end times
        start_time_td = group[group['message'].str.contains('Début de la sauvegarde')]['time_ms'].min()
        end_time_td = group[group['message'].str.contains('terminée correctement|pour cause d\'erreurs')]['time_ms'].max()

        start_time = None
        end_time = None

        if pd.notna(start_time_td):
            base_time = datetime(1900, 1, 1)
            start_time = (base_time + start_time_td).time()

        if pd.notna(end_time_td):
            end_time = (base_time + end_time_td).time()

        # Calculate backup duration if both start and end times are available
        if pd.notna(start_time_td) and pd.notna(end_time_td):
            start_datetime = time_to_datetime(start_time)
            end_datetime = time_to_datetime(end_time)
            backup_duration = (end_datetime - start_datetime).total_seconds() * 1000  # in milliseconds
        else:
            backup_duration = None

        # Calculate backup size and total data written
        backup_size = group[group['message'].str.contains('requiert environ')]['message'] \
                          .str.extract(r'(\d+\.\d+) MBytes').astype(float).sum().iloc[0] \
                      if not group[group['message'].str.contains('requiert environ')].empty else 0
        total_data_written = group[group['message'].str.contains('blocs de sauvegarde écrits')]['message'] \
                                .str.extract(r'(\d+\.\d+) MBytes').astype(float).sum().iloc[0] \
                             if not group[group['message'].str.contains('blocs de sauvegarde écrits')].empty else 0

        # Determine error message, status, and backup type
        error_message = group[group['message'].str.contains('pour cause d\'erreurs')]['message'].values[0] \
                        if not group[group['message'].str.contains('pour cause d\'erreurs')].empty else None
        status = 'failed' if error_message else 'completed'
        backup_type = 'incremental' if 'incrémentale' in group['message'].values[-1] else 'full'

        # Append summarized data to the list
        backup_summaries.append({
            "log_id": group.iloc[0]['log_id'],
            "process_id": group.iloc[0]['process_id'],
            "thread_id": group.iloc[0]['thread_id'],
            "backup_start": start_time,
            "backup_end": end_time,
            "backup_duration": backup_duration,
            "backup_size": backup_size,
            "total_data_written": total_data_written,
            "status": status,
            "backup_type": backup_type,
            "error_message": error_message,
            "serveur": group.iloc[0]['serveur'],
            "instance": group.iloc[0]['instance'],
            "base": group.iloc[0]['base'],
            "day": group.iloc[0]['day'],
            "month": group.iloc[0]['month'],
            "year": group.iloc[0]['year']
        })

    # Return the results as a DataFrame
    return pd.DataFrame(backup_summaries)
 
