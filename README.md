<p align="center">
  <img src="https://capsule-render.vercel.app/render?type=waving&color=0:667eea,100:764ba2&height=250&section=header&text=Open%20Source%20Audit&fontSize=75&animation=fadeIn&fontAlignY=35" width="100%" />
</p>

<p align="center">
  <kbd><img src="https://img.shields.io/badge/Ubuntu-E94333?style=for-the-badge&logo=ubuntu&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/WSL2-0078D6?style=for-the-badge&logo=windows&logoColor=white" /></kbd>
</p>

<div align="center">
  <h1>🛡️ Open Source Audit Framework</h1>
  <p><i>A Sophisticated Linux System Analysis & Automation Suite optimized for Ubuntu (WSL)</i></p>
  
  <p align="center">
    <img src="https://img.shields.io/github/stars/AND-SHAL-0813/open-source-audit-python-wsl?style=social" />
    <img src="https://img.shields.io/github/forks/AND-SHAL-0813/open-source-audit-python-wsl?style=social" />
    <img src="https://img.shields.io/github/license/AND-SHAL-0813/open-source-audit-python-wsl?style=flat-square&color=blue" />
  </p>
</div>

---

## 📽️ Project Demonstration
<div align="center">
  <p><b>Watch the Audit Suite in Action</b></p>
  <a href="INSERT_YOUR_VIDEO_LINK_HERE">
    <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="4px" />
    <br>
    <img src="https://play-lh.googleusercontent.com/vA9tNx966Gj9D_uJk6Xz7M_9V_P-H150aX2K_A9vA0j_k9Z_G8fW_8P8=w512-h512" width="50px" /><br>
    <b>[ ▶ PLAY PROJECT WALKTHROUGH ]</b>
    <br><br>
    <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%" height="4px" />
  </a>
</div>

---

## 📖 Project Overview
The `open-source-audit-python-wsl` framework is engineered for high-visibility system monitoring. By combining the raw speed of **Bash** with the structured data handling of **Python**, this tool provides a 360-degree security and performance health check of any Ubuntu-based environment.

### ✨ Key Features
| Feature | Description | Icon |
| :--- | :--- | :---: |
| **System Identity** | Full metadata extraction (Kernel, Host, User) | 📊 |
| **Package Audit** | Analyzes `apt` binaries and storage footprint | 📦 |
| **Security Scan** | Detects world-writable files & permission leaks | 🔒 |
| **Log Analytics** | Automated error hunting within system logs | 📜 |
| **Manifesto** | Generates a clean, portable audit report | 📄 |

---

## 📂 Architecture
```text
open-source-audit-python-wsl/
├── 📂 scripts/
│   ├── 📑 script1.sh       # Identity Engine
│   ├── 📑 script2.sh       # Pkg Inspector
│   ├── 📑 script3.sh       # Security Auditor
│   ├── 📑 script4.sh       # Log Parser
│   └── 📑 script5.sh       # Report Generator
├── 📂 audit_results/       # Report Storage
└── 🐍 main.py              # Python Controller
```
## 📜 Shell Scripts (Core Audit Engine)
# 🔹 Script1.sh
```
#!/bin/bash
# Description: Generates a snapshot of the system identity
echo "------------------------------------------"
echo "🔍 SYSTEM IDENTITY REPORT"
echo "------------------------------------------"
echo "Timestamp: $(date)"
echo "User:      $USER"
echo "Hostname:  $(hostname)"
echo "Kernel:    $(uname -r)"
echo "------------------------------------------"
```
# 🔹 Script2.sh
```
#!/bin/bash
# Description: Audits installed software packages
echo "📦 AUDITING INSTALLED PACKAGES..."
dpkg-query -Wf '${Installed-Size}\t${Package}\n' | sort -n -r | head -n 5
```
# 🔹 Script3.sh
```
#!/bin/bash
# Description: Scans for world-writable files and disk usage
echo "💾 DISK USAGE SUMMARY:"
df -h --total | grep 'total'
echo -e "\n🔒 SECURITY SCAN: World-Writable Files"
find . -maxdepth 2 -perm -o+w -type f 2>/dev/null
```
# 🔹 Script4.sh
```
#!/bin/bash
# Description: Analyzes system logs for errors
LOG_FILE="/var/log/bootstrap.log"
echo "📜 ANALYZING SYSTEM LOGS..."
grep -iE "error|fail" "$LOG_FILE" | tail -n 5
```
# 🔹 Script5.sh
```
#!/bin/bash
# Description: Compiles audit data into a report
OUTPUT="system_manifesto.txt"
echo "Audit Generated: $(date)" > "$OUTPUT"
echo "✅ Manifesto successfully generated at: $OUTPUT"
```
## ⚙️ How to Run

#### 1. Clone the repo
git clone [https://github.com/AND-SHAL-0813/open-source-audit-python-wsl.git](https://github.com/AND-SHAL-0813/open-source-audit-python-wsl.git)

#### 2. Set permissions
chmod +x scripts/*.sh

#### 3. Run the audit
```
./scripts/script1.sh && ./scripts/script5.sh
```


## 🎓 Learning Outcomes
##### Linux Systems: Gained deep knowledge of the /etc and /var file structures.

##### Automation: Mastered the chain-execution of shell scripts for complex reporting.

##### WSL Integration: Optimized scripts for the Windows-Linux interoperability layer.

##### Security Auditing: Learned to identify permission vulnerabilities and log patterns.

## 📝 Important Notes
WSL Performance: These scripts are optimized for WSL2.

Permissions: Running script4.sh may require sudo depending on your log visibility settings.

## 👤 Author
SHALINI ANAND

GitHub: https://github.com/AND-SHAL-0813

Role: OSS Security & Automation Enthusiast

## ⚖️ License
Distributed under the GNU General Public License v3.0. See LICENSE for more information.

## ⭐ Star this Repository
If you find this project helpful for your learning or portfolio, please give it a star! It helps others find the project.
