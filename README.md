
<p align="center">
  <kbd><img src="https://img.shields.io/badge/Ubuntu-E94333?style=for-the-badge&logo=ubuntu&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" /></kbd>
  <kbd><img src="https://img.shields.io/badge/WSL2-0078D6?style=for-the-badge&logo=windows&logoColor=white" /></kbd>
</p>

<div align="center">
  <h1>🛡️ Open Source Audit Framework</h1>
  <p><b>A Professional Linux System Analysis & Automation Suite for Ubuntu (WSL)</b></p>
  <p><i>Developed by Shalini Anand | Engineering Student | Programmer | Problem Solver</i></p>
  
  <p align="center">
    <img src="https://img.shields.io/github/stars/AND-SHAL-0813/open-source-audit-python-wsl?style=social" />
    <img src="https://img.shields.io/github/license/AND-SHAL-0813/open-source-audit-python-wsl?style=flat-square&color=blue" />
    <img src="https://komarev.com/ghpvc/?username=AND-SHAL-0813&label=VIEWS&color=4A90E2&style=flat-square" />

  </p>
</div>

---

## 📖 Project Overview
`open-source-audit-python-wsl` is a high-performance automation suite designed to perform deep-system audits on Linux environments via Windows Subsystem for Linux (WSL). This project bridges the gap between low-level shell scripting and high-level Python system integration.

### 🚀 Key Features
* 📊 **System Identity:** Automated extraction of kernel and hardware metadata.
* 📦 **Package Inspector:** Deep-dive analysis of installed `apt` packages.
* 🔒 **Permission Auditor:** Identification of world-writable security risks.
* 📜 **Log Analyzer:** Intelligent parsing of system error logs.
* 📄 **Manifesto Generator:** Automated documentation of system state.

---

## 📂 Project Architecture
```text
open-source-audit-python-wsl/
├── scripts/
│   ├── script1.sh       # Identity Engine
│   ├── script2.sh       # Pkg Inspector
│   ├── script3.sh       # Security Auditor
│   ├── script4.sh       # Log Parser
│   └── script5.sh       # Report Generator
├── audit_results/       # Generated reports
└── main.py              # Python Control Center
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
```text
chmod +x scripts/*.sh
```
#### 3. Run the audit
```text
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


## 🤝 Connect With Me
##### 👤 Author : SHALINI ANAND
<div align="left">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shalini-anand0813)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AND-SHAL-0813)

</div>


## ⚖️ License
Distributed under the GNU General Public License v3.0. See LICENSE for more information.

## ⭐ Star this Repository
If you find this project helpful for your learning or portfolio, please give it a star! It helps others find the project.
 <div align="center">
   <sub>Developed with ❤️ by Shalini Anand</sub
   <\div>
