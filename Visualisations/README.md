# Backup and Error Monitoring Visualizations

This repository provides a set of visualizations to monitor backup and error trends for a database system. The following charts and plots are designed to offer insights into backup success rates, database size evolution, backup durations, error types, and error frequency patterns over different time periods. The data is sourced from the "Backup Entries" and "Error Entries" tables.

## Visualizations

### 1. **Daily, Monthly, and Yearly Count of Successful Full Backups**
   - **Type:** Grouped Histogram
   - **Description:** This visualization shows the number of successful full backups over time, with a hierarchical time axis extending from days to months and years. Filters exclude failed backups and isolate only full backups, offering insights into backup frequency trends and success rates over specific periods.

### 2. **Database Size Evolution Over Time**
   - **Type:** Area Chart
   - **Description:** This area chart visualizes the growth of the database over time by displaying the total saved data volume at each date. Only full backups are included, providing a clear view of storage capacity changes across time.

### 3. **Duration of Successful Full Backups by Day, Month, and Year**
   - **Type:** Line Chart
   - **Description:** This line chart visualizes the average duration of successful full backups over time. The X-axis represents the temporal hierarchy (day, month, year), and the Y-axis shows the average duration in minutes and seconds. This chart highlights performance issues, flagging unusually lengthy backups, such as one on June 2, 2024, which spiked to 162 minutes against an average of 2 seconds. Only successful backups are included for accuracy in performance tracking.

### 4. **Count of Full Backups by Status and Date**
   - **Type:** Scatter Plot
   - **Description:** This scatter plot displays the number of full backups conducted each day, with the X-axis representing a temporal hierarchy (year, quarter, month, day) and the Y-axis showing the count of backups. Blue dots indicate successful backups, while red dots mark failures. Interactive filters allow users to refine the view by server, instance, and database, enabling quick identification of backup frequency and failure patterns. This visualization is based on data from the "Backup Entries" table and exclusively shows full backups for precise monitoring.

### 5. **Percentage of Successful and Failed Backups**
   - **Type:** Pie Chart
   - **Description:** This pie chart provides an overall view of the success rate for backup operations by highlighting the proportion of successfully completed backups compared to failures. Based on data from the "Backup Entries" table and filtered to include only full backups, this visualization offers a clear breakdown of backup reliability, enabling a quick assessment of the backup process's overall performance over a specified period.

### 6. **Number of Errors by Type and Date**
   - **Type:** Bar Chart
   - **Description:** This bar chart illustrates the distribution of various error types recorded over a specific time period. Built from the "Error Entries" table, it enables analysis of system errors based on event code (`event_code`) and occurrence date. The X-axis represents the temporal hierarchy, while the Y-axis shows the count of errors. Each event code is color-coded, allowing a clear view of the frequency of each error type. This visualization is essential for identifying recurring errors and planning corrective actions.

### 7. **Error Frequency by Hour and Day of the Week**
   - **Type:** Heatmap
   - **Description:** This heatmap visualizes the distribution of system errors across different hours and days. Sourced from the "Error Entries" table, it highlights peak error periods to aid in identifying systematic issues. The X-axis represents the days of the week (Sunday to Saturday), while the Y-axis shows each hour of the day (0 to 23). Each cell is shaded in purple tones, with darker shades indicating higher error frequencies. Notably, Saturdays between 2 a.m. and 4 a.m. show a peak, with 198 errors logged at 3 a.m., providing valuable insights for scheduling audits or interventions during critical periods.

## Data Sources
- **Backup Entries Table:** Contains information about full and incremental backups, including success or failure status.
- **Error Entries Table:** Contains recorded errors with event codes, occurrence dates, and error types.

## Installation


