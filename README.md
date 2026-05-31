# 🔍 Log Analyzer

A Python-based Command Line Interface (CLI) tool designed to analyze log files and identify suspicious activities. This tool helps cybersecurity professionals, SOC analysts, system administrators, and security enthusiasts quickly detect common attack patterns such as brute-force attempts, repeated failed logins, and other potentially malicious behavior.

---

## 📌 Overview

Log files contain valuable security information that can help identify unauthorized access attempts, system issues, and ongoing attacks. Manually reviewing large log files can be time-consuming and error-prone.

The Log Analyzer automates this process by parsing log files, extracting relevant information, and generating security-focused reports that highlight suspicious events.

---

## ✨ Features

### 📂 Log File Parsing
- Supports analysis of:
  - Apache Access Logs
  - Nginx Access Logs
  - Linux Syslog Files
  - Custom Text-Based Logs

### 🚨 Suspicious Activity Detection
Detects common security threats including:

- Multiple failed login attempts
- Potential brute-force attacks
- Excessive requests from a single IP address
- Unauthorized access attempts
- Suspicious HTTP response codes
- Repeated authentication failures

### 📊 Reporting
- Summary of analyzed logs
- Total events processed
- Top offending IP addresses
- Number of failed login attempts
- Detected security alerts

### 🔧 Extensible Architecture
- Easily add custom detection rules
- Modify thresholds for alert generation
- Extend support for additional log formats

### ⚡ Lightweight
- Uses only Python Standard Library
- No external dependencies required
- Fast and easy deployment

---

## 🏗 Project Structure

```text
log-analyzer/
│
├── log_analyzer.py      # Main application
├── sample.log           # Sample log file
├── README.md            # Project documentation
└── reports/             # Optional report storage
```

---

## 🛠 Requirements

### Software Requirements

- Python 3.8 or higher

### Dependencies

No external packages are required.

The tool relies entirely on Python's built-in libraries such as:

- `re`
- `collections`
- `datetime`
- `argparse`
- `os`
- `sys`

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/log-analyzer.git
```

### Navigate to the Project Directory

```bash
cd log-analyzer
```

---

## ▶️ Usage

### Basic Usage

Analyze a log file:

```bash
python log_analyzer.py sample.log
```

### Example

```bash
python log_analyzer.py apache_access.log
```

---

## 📋 Sample Input

Example log entries:

```text
192.168.1.10 - - [01/Jun/2026:10:15:23] "GET /login HTTP/1.1" 401
192.168.1.10 - - [01/Jun/2026:10:15:30] "GET /login HTTP/1.1" 401
192.168.1.10 - - [01/Jun/2026:10:15:40] "GET /login HTTP/1.1" 401
```

---

## 📊 Sample Output

```text
====================================
LOG ANALYSIS REPORT
====================================

Total Log Entries: 500

Failed Login Attempts:
  192.168.1.10 -> 15 attempts

Potential Brute Force Detected:
  192.168.1.10

Top Active IP Addresses:
  192.168.1.10 -> 120 requests
  192.168.1.20 -> 87 requests

Analysis Complete.
```

---

## 🔍 Detection Logic

The analyzer currently uses rule-based detection methods:

### Failed Login Detection

Flags repeated login failures from the same source.

Example indicators:

- HTTP 401 responses
- Authentication failure messages
- Invalid credential attempts

### Brute Force Detection

Generates alerts when failed login attempts exceed a predefined threshold.

Example:

```python
BRUTE_FORCE_THRESHOLD = 10
```

### High Request Volume Detection

Identifies IP addresses generating unusually high traffic.

---

## 🔧 Customization

You can easily add new detection rules.

Example:

```python
def detect_custom_rule(log_entry):
    if "suspicious_keyword" in log_entry:
        return True
    return False
```

Possible additions:

- SQL Injection Detection
- XSS Detection
- Directory Traversal Detection
- Malware Indicators
- Threat Intelligence Integration

---

## 🧪 Testing

Run the analyzer against the included sample log:

```bash
python log_analyzer.py sample.log
```

Verify that:

- Log entries are parsed correctly
- Alerts are generated
- Reports are displayed as expected

---

## 📈 Future Enhancements

Planned improvements include:

- Export reports to CSV
- Export reports to JSON
- Email alert notifications
- Real-time log monitoring
- Dashboard integration
- Threat intelligence feeds
- Geo-IP enrichment
- SIEM integration
- Machine Learning-based anomaly detection

---

## 🔐 Security Use Cases

This tool can be useful for:

- Security Operations Centers (SOC)
- Threat Hunting
- Incident Response
- Log Auditing
- Security Monitoring
- Security Awareness Training
- Cybersecurity Learning Labs

---

## 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---


## 👨‍💻 Author

**Aakash Gadekar**

Cybersecurity Professional | Security Analyst | Python Enthusiast
