from re import *

logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]

p = r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>INFO|WARNING|ERROR) User (?P<id>\d+) (?P<message>.+)"
for i in logs:
    if (fullmatch(p, i)):
        print(fullmatch(p, i).groupdict())