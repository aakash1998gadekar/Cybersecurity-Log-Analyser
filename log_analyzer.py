import sys
import re
from collections import Counter

def parse_log(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return lines

def detect_suspicious(lines):
    failed_logins = [line for line in lines if 'failed' in line.lower() or 'unauthorized' in line.lower()]
    brute_force_ips = Counter()
    for line in failed_logins:
        match = re.search(r'[\d.]+', line)
        if match:
            brute_force_ips[match.group()] += 1
    return failed_logins, brute_force_ips

def main():
    if len(sys.argv) != 2:
        print('Usage: python log_analyzer.py <logfile>')
        sys.exit(1)
    log_file = sys.argv[1]
    lines = parse_log(log_file)
    failed_logins, brute_force_ips = detect_suspicious(lines)
    print(f"Total failed/unauthorized attempts: {len(failed_logins)}")
    print("Top suspicious IPs:")
    for ip, count in brute_force_ips.most_common(5):
        print(f"{ip}: {count} attempts")

if __name__ == "__main__":
    main()
