<!-- ═══════════════════════════════════════════════════════════════════════════════ -->
<!-- CASE FILE: NGUYEN NGOC ANH TU | CYBERSECURITY STUDENT                        -->
<!-- Classification: PUBLIC | Last Updated: 2026                                  -->
<!-- ═══════════════════════════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=1&section=header" width="100%"/>

<br>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=28&duration=4000&pause=1000&color=C9D1D9&center=true&vCenter=true&multiline=true&repeat=false&width=700&height=80&lines=Nguy%E1%BB%85n+Ng%E1%BB%8Dc+Anh+T%C3%BA" alt="Name"/>

<br>

```
Understanding Systems. Investigating Evidence. Building Better Defenses.
```

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=300&size=14&duration=3000&pause=2000&color=8B949E&center=true&vCenter=true&repeat=true&width=600&height=30&lines=Cybersecurity+Student+%7C+Aspiring+SOC+Analyst+%7C+DFIR+Researcher" alt="Role"/>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=1&section=header" width="100%"/>

</div>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 01: WHOAMI                                                            -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> whoami`

```yaml
analyst@workstation:~$ cat /etc/profile.d/identity.conf

Name            : Nguyen Ngoc Anh Tu
Role            : Cybersecurity Student
Focus           : DFIR | Threat Hunting | Detection Engineering
Objective       : SOC Analyst → Threat Hunter → Detection Engineer
Status          : Building investigation skills through structured research
Operating Mode  : Observe → Investigate → Document → Improve
```

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 02: SECURITY PHILOSOPHY                                               -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> cat /var/log/philosophy.md`

> *The measure of a security operation is not whether incidents occur — they will.*
>
> *It is the speed of detection, the depth of understanding, and the precision of response that define effective defense.*
>
> *Every alert is an opportunity to learn. Every investigation sharpens the analyst. Every detection rule written today prevents tomorrow's blind spot.*

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 03: CURRENT INVESTIGATIONS                                            -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> ls -la /investigations/active/`

| Status | Investigation | Focus Area |
|:------:|:-------------|:-----------|
| `[ACTIVE]` | Windows Event Log Analysis | Correlating security-relevant events across Sysmon, PowerShell, and Security logs |
| `[ACTIVE]` | Malware Behavior Research | Studying execution patterns, persistence mechanisms, and evasion techniques |
| `[ACTIVE]` | Threat Hunting Methodologies | Developing hypothesis-driven hunting workflows using MITRE ATT&CK |
| `[ACTIVE]` | Detection Rule Development | Writing YARA and Sigma rules for known threat behaviors |
| `[ACTIVE]` | Digital Forensics Workflows | Building repeatable evidence collection and analysis procedures |

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 04: SECURITY RESEARCH LABS                                            -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> ls /labs/`

<table>
<tr>
<td width="50%" valign="top">

### 🔬 DFIR Lab
Building repeatable forensic investigation workflows — from evidence acquisition through timeline reconstruction to final reporting.

### 🔍 Threat Hunting Lab
Exploring proactive detection techniques using hypothesis-driven methodologies, behavioral analysis, and threat intelligence correlation.

### 🧪 Malware Analysis Lab
Studying malware execution flows, persistence mechanisms, process injection techniques, and behavioral indicators in controlled environments.

</td>
<td width="50%" valign="top">

### ⚙️ Detection Engineering Lab
Developing and testing YARA signatures and Sigma detection rules mapped to MITRE ATT&CK techniques for measurable coverage improvement.

### 🌐 Network Analysis Lab
Investigating network traffic patterns, C2 communication behaviors, DNS anomalies, and lateral movement indicators through packet-level analysis.

### 📋 Log Analysis Lab
Parsing and correlating Windows Event Logs, Sysmon telemetry, and Linux audit logs to reconstruct attack timelines and identify gaps in visibility.

</td>
</tr>
</table>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 05: ANALYST THINKING FRAMEWORK                                        -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> cat /procedures/investigation-framework.md`

*How I approach every security investigation:*

```
    ╔═══════════════════════════════════════════════════════════════╗
    ║                  INVESTIGATION FRAMEWORK                     ║
    ╠═══════════════════════════════════════════════════════════════╣
    ║                                                               ║
    ║       ┌─────────────────────┐                                ║
    ║       │   01  OBSERVE       │  Monitor telemetry and alerts  ║
    ║       └────────┬────────────┘                                ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 02  COLLECT EVIDENCE│  Acquire logs, artifacts,      ║
    ║       └────────┬────────────┘  and forensic images           ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 03  CORRELATE       │  Map events across multiple    ║
    ║       └────────┬────────────┘  data sources and timelines    ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 04  HYPOTHESIZE     │  Develop investigative         ║
    ║       └────────┬────────────┘  theories based on evidence    ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 05  VALIDATE        │  Test hypotheses against       ║
    ║       └────────┬────────────┘  additional data points        ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 06  RESPOND         │  Execute containment and       ║
    ║       └────────┬────────────┘  remediation procedures        ║
    ║                │                                              ║
    ║                ▼                                              ║
    ║       ┌─────────────────────┐                                ║
    ║       │ 07  IMPROVE         │  Write new detections and      ║
    ║       │     DETECTION       │  update playbooks              ║
    ║       └─────────────────────┘                                ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
```

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 06: TECHNICAL CAPABILITY MAP                                          -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> cat /etc/capabilities.conf`

<table>
<tr>
<td valign="top" width="33%">

#### Operating Systems
```
├── Windows
│   ├── Event Logs
│   ├── Registry Analysis
│   └── Internals
├── Linux
│   ├── System Administration
│   ├── Security Hardening
│   └── Audit Framework
└── Kali Linux
    └── Security Tooling
```

#### Programming
```
├── Python
│   ├── Automation Scripts
│   └── Log Parsers
└── Bash
    ├── System Scripts
    └── Pipeline Tools
```

</td>
<td valign="top" width="33%">

#### Investigation
```
├── DFIR
│   ├── Disk Forensics
│   └── Timeline Analysis
├── Memory Analysis
│   └── Process Examination
├── Log Analysis
│   ├── Windows Event Logs
│   ├── Sysmon Telemetry
│   └── Linux Audit Logs
└── Network Forensics
    ├── Packet Analysis
    └── Traffic Patterns
```

#### Detection
```
├── YARA
│   └── Signature Development
├── Sigma
│   └── Detection Rules
└── Threat Hunting
    ├── Hypothesis-Driven
    └── MITRE ATT&CK Mapping
```

</td>
<td valign="top" width="34%">

#### Security Operations
```
├── SIEM
│   ├── Log Ingestion
│   └── Alert Triage
├── Incident Response
│   ├── Containment
│   └── Remediation
└── Monitoring
    ├── Endpoint Telemetry
    └── Network Visibility
```

#### Infrastructure
```
├── Git
│   └── Version Control
├── Docker
│   └── Lab Environments
├── VirtualBox
│   └── Analysis VMs
└── VMware
    └── Isolated Labs
```

</td>
</tr>
</table>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 07: LEARNING JOURNEY                                                  -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> git log --oneline /journey/`

```
Timeline                Progress
─────────────────────────────────────────────────────────────────────

2025 ──────────── ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ █████
│
│   ▸ Built foundational Linux and networking knowledge
│   ▸ Learned system administration and security fundamentals
│   ▸ Set up first home lab environments
│   ▸ Began studying security monitoring and log analysis
│
2026 ──────────── ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ░░░░░
│
│   ▸ Focused on Digital Forensics and Incident Response
│   ▸ Developing threat hunting methodologies
│   ▸ Studying malware behavior and analysis techniques
│   ▸ Writing YARA and Sigma detection rules
│   ▸ Building structured investigation workflows
│
NEXT ──────────── ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ▪ ░░░░░
│
│   ▸ Transition into SOC operations
│   ▸ Advance detection engineering capabilities
│   ▸ Contribute to open-source security tooling
│   ▸ Pursue professional certifications (BTL1, CCD)
│
─────────────────────────────────────────────────────────────────────
```

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 08: FEATURED REPOSITORIES                                             -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> find /cases/ -name "*.case" -type f`

<table>
<tr>
<td width="50%">

#### 📁 Case File: DFIR Investigation Toolkit
```yaml
Classification : Research
Objective      : Build a structured toolkit for conducting
                 digital forensic investigations with
                 repeatable, documented workflows
Skills         : Evidence Acquisition, Timeline Analysis,
                 Artifact Parsing, Report Generation
Tools          : Autopsy, Volatility, Python, Linux CLI
Status         : In Progress
```

</td>
<td width="50%">

#### 📁 Case File: Detection Rule Library
```yaml
Classification : Engineering
Objective      : Develop and maintain a collection of
                 detection rules covering common attack
                 techniques mapped to MITRE ATT&CK
Skills         : Sigma Rule Authoring, YARA Signatures,
                 Threat Modeling, Log Source Mapping
Tools          : Sigma, YARA, MITRE ATT&CK Navigator
Status         : In Progress
```

</td>
</tr>
<tr>
<td width="50%">

#### 📁 Case File: Threat Hunting Playbooks
```yaml
Classification : Operations
Objective      : Document hypothesis-driven threat hunting
                 procedures for proactive detection of
                 adversary behaviors in enterprise telemetry
Skills         : Hypothesis Development, Data Analysis,
                 ATT&CK Mapping, Statistical Baselines
Tools          : Python, Jupyter, ELK Stack, Sysmon
Status         : In Progress
```

</td>
<td width="50%">

#### 📁 Case File: Malware Analysis Notes
```yaml
Classification : Research
Objective      : Analyze malware samples in isolated
                 environments to understand execution flows,
                 persistence, and evasion techniques
Skills         : Static Analysis, Dynamic Analysis,
                 Behavioral Indicators, YARA Signatures
Tools          : REMnux, Ghidra, Process Monitor, Wireshark
Status         : In Progress
```

</td>
</tr>
</table>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 09: ANALYTICS                                                         -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> cat /var/log/metrics.log`

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=ekaznya&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=c9d1d9&text_color=8b949e&icon_color=58a6ff&ring_color=58a6ff" alt="GitHub Stats" height="170"/>
&nbsp;&nbsp;
<img src="https://streak-stats.demolab.com?user=ekaznya&theme=github-dark-blue&hide_border=true&background=0D1117&ring=58A6FF&fire=58A6FF&currStreakLabel=C9D1D9&sideLabels=8B949E&dates=8B949E&currStreakNum=C9D1D9&sideNums=C9D1D9" alt="GitHub Streak" height="170"/>

<br><br>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=ekaznya&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=c9d1d9&text_color=8b949e" alt="Top Languages" height="150"/>

</div>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- SECTION 10: CONTACT                                                           -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

## `> cat /etc/contact.conf`

<div align="center">

[![Email](https://img.shields.io/badge/Email-anhtunguyen.sec@proton.me-0d1117?style=flat&logo=protonmail&logoColor=8b949e&labelColor=0d1117&color=161b22)](mailto:anhtunguyen.sec@proton.me)
&nbsp;&nbsp;
[![Telegram](https://img.shields.io/badge/Telegram-@ekaznya-0d1117?style=flat&logo=telegram&logoColor=8b949e&labelColor=0d1117&color=161b22)](https://t.me/ekaznya)
&nbsp;&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-ekaznya-0d1117?style=flat&logo=github&logoColor=8b949e&labelColor=0d1117&color=161b22)](https://github.com/ekaznya)
&nbsp;&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0d1117?style=flat&logo=linkedin&logoColor=8b949e&labelColor=0d1117&color=161b22)](https://linkedin.com/in/)

</div>

<br>

<!-- ─────────────────────────────────────────────────────────────────────────────── -->
<!-- FOOTER                                                                        -->
<!-- ─────────────────────────────────────────────────────────────────────────────── -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=rect&color=0d1117&height=1&section=footer" width="100%"/>

<br>

```
Every investigation teaches something. Every detection rule is a lesson documented.
I am not chasing titles — I am building the discipline to understand what happened,
why it happened, and how to ensure it is detected next time.
```

<sub>Profile last updated: 2026 · This README is a living document, updated as skills and investigations evolve.</sub>

</div>