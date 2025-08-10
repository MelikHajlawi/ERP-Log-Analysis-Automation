# ERP Log Monitoring and Analysis

## Overview
This project was developed during an internship at Poulina Group Holding with the objective of automating the Monotoring ERP Databases through processing and storage of Error and Backup logs entries. The system extracts error and backup logs, stores them in a SQL Server database, and prepares the data for real-time monitoring and analysis with Power BI.

## Project Structure
- `config.py`: Database connection configuration.
- `database.py`: Database utility functions for connection and data retrieval.
- `log_parser.py`: Functions for parsing raw log files into structured entries.
- `log_processing.py`: Functions to filter recent log entries and extract error logs.
- `backup_summary.py`: Summarizes backup-related logs with calculated metrics.
- `data_insertion.py`: Inserts logs into SQL Server with chunked processing.
- `main.py`: Main script coordinating the end-to-end process, from parsing to database insertion.


