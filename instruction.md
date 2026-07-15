Analyze the traffic in `/app/access.log` and write a summary JSON file at `/app/report.json` containing exactly the following keys:

- `total_requests`: integer — the total number of HTTP request lines in `/app/access.log`.
- `unique_ips`: integer — the number of unique client IP addresses present in the log.
- `top_path`: string — the single request path with the highest request count (use the verbatim path as it appears in the log).

Success criteria (one test per criterion):

1. Produce the file `/app/report.json` (existence).
2. The file contains the three keys `total_requests`, `unique_ips`, and `top_path` and their types are integer, integer, and string respectively (schema and types).
3. The values must exactly match the content of `/app/access.log`: `total_requests == 6`, `unique_ips == 3`, `top_path == "/index.html"` (correct values).

Do not modify `/app/access.log`. The environment disallows network access.

You have 120 seconds to complete this task.
