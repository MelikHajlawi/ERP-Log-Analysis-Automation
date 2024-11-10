# log_parser.py
# This module defines the log file parsing functions, extracting structured data from raw log entries.

import re
from database import get_last_log_id

# Regular expression pattern for parsing log entries
log_pattern = re.compile(
    r'\[(\d{4}/\d{2}/\d{2}@\d{2}:\d{2}:\d{2}\.\d{3}[+-]\d{4})\] '  # Timestamp
    r'P-(\d+)\s+'      # Process ID
    r'T-(\d+)\s+'      # Thread ID
    r'(\w+)\s+'        # Severity
    r'(\w+)\s+'        # Component
    r'(\d+):\s+'       # Sub-component
    r'\((\d+)\)\s+'    # Event code
    r'(.+)'            # Message
)

def parse_log_file(file_path, serveur, instance, base, engine):
    """
    Parses a log file line-by-line, extracting structured data based on a regular expression pattern.
    Yields dictionaries containing parsed log information for each valid line.
    """
    with open(file_path, 'r', encoding='latin-1') as file:
        log_id = get_last_log_id(engine)
        for line in file:
            match = log_pattern.match(line)
            if match:
                yield {
                    "log_id": log_id,
                    "timestamp": match.group(1),
                    "process_id": match.group(2),
                    "thread_id": match.group(3),
                    "severity": match.group(4),
                    "component": match.group(5),
                    "sub_component": match.group(6),
                    "event_code": match.group(7),
                    "message": match.group(8),
                    "serveur": serveur,
                    "instance": instance,
                    "base": base
                }
                log_id += 1
 
