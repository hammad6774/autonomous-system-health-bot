# 🤖 Autonomous System Health Bot

A proactive DevOps automation tool built with **Python** and **Linux** to monitor server disk storage and automate data management.

## 🚀 Features
- **Real-time Monitoring:** Tracks disk usage percentages using Python's `shutil`.
- **Automated Backup:** Automatically triggers a ZIP archive of critical directories when storage hits **80%**.
- **Self-Scheduling:** Runs autonomously in the background using **Linux Cron Jobs**.
- **Persistent Logging:** Captures all activity and errors in a timestamped `bot_log.txt` using I/O redirection (`2>&1`).

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **OS:** Linux (Ubuntu)
- **Tools:** Cron, Bash, Git

## 📂 Installation & Usage
1. Clone the repo:
   `git clone https://github.com/hammad6774/autonomous-system-health-bot.git`
2. Run the script manually:
   `python3 health_bot.py`
3. Automate with Cron:
   `* * * * * /usr/bin/python3 /path/to/health_bot.py >> bot_log.txt 2>&1`

---
*Created by Hammad - Aspiring DevOps Engineer*
