# DefensrC2 Framework 🛡️

**DefensrC2** is a defensive Command and Control (C2) framework built for blue teams, SOC analysts, and cybersecurity defenders. Inspired by the architecture of offensive C2 platforms like Metasploit, DefensrC2 focuses entirely on **detection, response, and containment** within a secure environment.

---

## 🧠 Purpose

In a world dominated by offensive C2 frameworks, **DefensrC2** provides a defensive alternative. It helps security teams monitor endpoints, detect anomalies, and coordinate proactive responses in real-time across multiple systems.

---

## 🚀 Features

- 🔐 **Secure Client-Server Communication**  
  Encrypted communication channels between endpoints and central controller.

- 📡 **Agent-based Monitoring**  
  Lightweight agents collect system telemetry and report to the central server.

- 🛠️ **Incident Response Actions**  
  Isolate host, terminate process, notify user, collect evidence — all from one place.

- 📈 **Real-time Dashboard (Optional)**  
  Visual interface for monitoring connected nodes and triggering defense actions.

- 🔌 **Modular Plugin Support**  
  Add custom scripts or defense modules to expand capabilities.

- 📝 **Logging & Alerting**  
  Detailed logs of all activity and customizable alert rules.

---

## 🛠️ Components

### 1. **Controller (Server)**
- Receives data from agents
- Displays system statuses
- Sends back defense instructions

### 2. **Agent (Client)**
- Installed on target systems
- Monitors logs, processes, open ports, etc.
- Executes defense tasks when triggered

### 3. **Plugin Modules (Optional)**
- Memory scanner
- Suspicious login detector
- File integrity checker

---

## 📦 Tech Stack

- Python (Backend & Agents)
- Flask/FastAPI (API & Controller)
- SQLite/PostgreSQL (Database)
- WebSockets/HTTPS (Communication)
- Optional: React/TailwindCSS (for frontend dashboard)

---

## 💡 Use Cases
 - Defending lab setups and honeypots
 - Training and simulation for SOC teams
 - Endpoint behavior analysis

## 🧩 Future Enhancements
 - AI/ML-based anomaly detection
 - Integration with MITRE ATT&CK mapping
 - Cross-platform agents (Linux, Windows, Mac)

## 🧑‍💻 Author

**Shiva Kumar Radharapu**  
Cybersecurity Enthusiast | SOC & C2 Framework Develope 
[LinkedIn](https://www.linkedin.com/in/shiva-kumar-radharapu-2b79b9240/)


---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/DefensrC2.git
cd DefensrC2
pip install -r requirements.txt
python controller/main.py
