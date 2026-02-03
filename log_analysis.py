# Simple SOC-style log analysis

log_data = [
    "2026-02-01 10:12:01 LOGIN SUCCESS user=admin",
    "2026-02-01 10:15:22 LOGIN FAILED user=admin",
    "2026-02-01 10:16:10 LOGIN FAILED user=admin",
    "2026-02-01 10:20:45 LOGIN SUCCESS user=john",
    "2026-02-01 10:25:30 LOGIN FAILED user=admin"
]

failed_attempts = 0

for log in log_data:
    if "FAILED" in log:
        failed_attempts += 1
        print("ALERT:", log)

print("\nTotal failed login attempts:", failed_attempts)

if failed_attempts >= 3:
    print("⚠️  Potential brute-force attack detected!")
