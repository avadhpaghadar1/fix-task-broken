An Apache access log is available at:

/app/access.log

Read the log and create a JSON file at:

/app/report.json

The JSON object must contain exactly these fields:

- "total_requests": the total number of non-empty log entries.
- "unique_ips": the number of distinct client IP addresses.
- "top_path": the request path that appears most frequently in the log.

The output must be valid JSON.

No additional files are required.