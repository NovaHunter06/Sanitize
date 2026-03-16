# 🛡️ Sentinel-Linux (v1.2.0)

**Sentinel-Linux** is a lightweight, heuristic-based security analyzer and process neutralizer. It is designed to detect and terminate unauthorized background processes, malicious systemd services, and resource-exhaustion attacks (DoS) in real-time.

## 🚀 Key Capabilities

* **Heuristic Process Scanning:** Identifies scripts using suspicious modules (e.g., `pynput`, `os.urandom`) or hidden self-destruct logic.
* **Active Neutralization:** Automatically issues `SIGKILL` signals to processes flagged as high-threat to prevent system crashes.
* **Persistence Auditing:** Scans `/etc/systemd/system/` for unauthorized or suspicious service entries.
* **Forensic Reporting:** Generates a detailed breakdown of identified threats, including Process ID (PID), command-line arguments, and timestamps.
* **Load Analysis:** Monitors CPU and Memory usage to detect "Logic Bomb" triggers before they achieve total system lockout.

## 🛠️ Installation

Sentinel requires `psutil` for process table inspection.

```bash
# Clone the analyzer
git clone [https://github.com/NovaHunter06/sentinel-linux.git](https://github.com/NovaHunter06/sentinel-linux.git)
cd sentinel-linux

# Install dependencies
pip install psutil

# Execute the scanner with elevated privileges
sudo python3 sanitize.py
