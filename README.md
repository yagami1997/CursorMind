# ✨ CursorMind

<p align="right">
  <a href="README.md">English Version</a> |
  <a href="README.zh.md">中文版</a>
</p>

<div align="center">
  <h1>CursorMind</h1>
  <h3>Enhance Your Cursor Development Efficiency and Project Management Quality</h3>
  <p><strong>Current Version: Beta 0.1</strong></p>
  
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version](https://img.shields.io/badge/Version-Beta%200.1-brightgreen.svg)
  ![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)
  ![Languages](https://img.shields.io/badge/Languages-Bash%20|%20Python-yellow.svg)
</div>

## 📖 Project Introduction

**CursorMind** is a project management framework designed specifically for Cursor developers, helping development teams improve project quality and development efficiency through structured workflows, standardized document management, and optimized behavior guidelines.

### 💡 Core Features

- **Development Behavior Guidelines** - Specific commands optimize workflow, prevent analysis paralysis and circular thinking
- **Standardized Document Templates** - Professional templates for daily reports, weekly reports, task definitions, decision records, etc.
- **Automated Tool Scripts** - Simplify common tasks like project initialization, report creation, and progress updates
- **Pacific Time Timestamps** - Ensure global team members use a unified time standard
- **Project Progress Tracking** - Monitor and record project progress in real-time, increasing project transparency

### 🛠️ Design Philosophy

CursorMind is designed based on the following core principles:

- **Focus on Productivity** - Reduce decision fatigue, optimize development thinking patterns
- **Structured Approach** - Provide clear project structure and workflows
- **Automation First** - Simplify repetitive tasks through scripting
- **Transparency** - Improve team collaboration and communication efficiency through standardized reporting

## 🚀 Quick Start

### Prerequisites

- Git
- Bash or compatible Shell environment
- Python 3.6+ (for advanced features, basic functionality does not depend on it)

### 💻 Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CursorMind.git
   cd CursorMind
   ```

2. **Set script permissions**
   ```bash
   chmod +x scripts/*.sh
   chmod +x scripts/*.py
   ```

3. **Initialize project**
   ```bash
   ./scripts/init_project.sh "Your Project Name"
   ```
   This command will automatically create initial daily and weekly reports, and update project names and timestamps in all files.

## 💼 Basic Usage

### 📊 Project Initialization

Project initialization is the first step in using CursorMind, it will:
- Update project names in all files
- Set unified timestamps
- Create initial daily and weekly reports
- Prepare project progress documents

```bash
./scripts/init_project.sh "My Project Name"
```

### 📝 Report Management

#### Creating Daily and Weekly Reports

```bash
# Create today's daily report
./scripts/create_report.sh daily

# Create this week's weekly report
./scripts/create_report.sh weekly
```

#### Daily Report Structure

Daily reports contain the following key information:
- Work completed today
- Work progress comparison
- Problems encountered and solutions
- Next day's plans
- Risk warnings

#### Weekly Report Structure

Weekly reports provide a more comprehensive project view, containing:
- Weekly work summary
- Project progress status
- Key metrics monitoring
- Major issues and solutions
- Important decision records
- Next week's work plan
- Risk warning mechanism
- Team member workload statistics

### 📈 Project Progress Updates

```bash
# Update progress to 50% with description
./scripts/update_progress.sh 50 "Completed core functionality development"

# Update progress to 100% and mark project completion
./scripts/update_progress.sh 100 "Project has completed all feature development"
```

Progress updates will:
- Update the progress percentage in PROJECT_PROGRESS.md
- Add detailed progress update history
- Update progress information in the central control document
- Create decision records for tracking important changes

### ⏰ Timestamp Functionality

```bash
# Full format: YYYY-MM-DD HH:MM:SS PST/PDT
./scripts/timestamp.sh full

# Date only: YYYY-MM-DD
./scripts/timestamp.sh date

# Compact format: YYYYMMDD
./scripts/timestamp.sh compact
```

## 📂 Project Structure

```
CursorMind/
├── README.md                           # Project introduction and usage guide
├── PROJECT_PROGRESS.md                 # Project progress tracking document
├── project_management/                 # Project management core directory
│   ├── control/                        # Control documents directory
│   │   ├── MAIN_CONTROL.md             # Central control document
│   │   └── REQUIREMENTS.md             # Requirements management document
│   ├── templates/                      # Template files directory
│   │   ├── daily_report_template.md    # Daily report template
│   │   ├── weekly_report_template.md   # Weekly report template
│   │   ├── task_template.md            # Task definition template
│   │   ├── decision_template.md        # Decision record template
│   │   └── risk_template.md            # Risk assessment template
│   └── actuals/                        # Actual documents directory
│       ├── reports/                    # Report documents directory
│       │   ├── daily/                  # Daily reports storage
│       │   └── weekly/                 # Weekly reports storage
│       └── decisions/                  # Decision records storage
└── scripts/                            # Helper scripts directory
    ├── init_project.sh                 # Project initialization script
    ├── create_report.sh                # Report creation script
    ├── update_progress.sh              # Project progress update script
    ├── timestamp.sh                    # Timestamp generation script (Pacific time)
    ├── simple_timestamp.sh             # Simple timestamp script (local time)
    └── generate_timestamp.py           # Timestamp generation Python script
```

## ⚡ Cursor Development Behavior Guidelines

CursorMind provides a set of development behavior guidelines that optimize workflow through specific commands:

### Core Commands

| Command | Purpose | Usage Scenario |
|---------|---------|----------------|
| **[CODE NOW]** | Immediately stop analysis and start coding | When analysis exceeds 20% of total time without substantial output |
| **[FOCUS]** | Limit context to specified scope | When distracted by too much information |
| **[RESET]** | Abandon current method and restart | When encountering circular thinking or dead ends |
| **[DECISION]** | Make a choice and move forward, avoid hesitation | When difficult to decide between multiple viable options |

### Code Generation Rules

- Always produce complete, runnable code, avoid placeholders
- Maintain an 80% code to 20% explanation ratio
- Include comprehensive error handling
- Ensure code is optimized and follows best practices

### Task Format Guidelines

- Define clear, measurable deliverables and concrete success criteria
- Establish specific time limits for completion of each task
- Set explicit context boundaries to prevent scope expansion
- Provide sequential, actionable implementation steps
- Include verification methods to confirm successful completion

## 🚀 Best Practices

To fully leverage CursorMind, we recommend following these best practices:

1. **Daily Updates** - Update daily reports at the end of each workday, recording progress and issues
2. **Weekend Reviews** - Generate weekly reports at the end of the week, reviewing the week's work and planning for the next
3. **Timely Decisions** - Record important decisions immediately, including reasons and impacts
4. **Progress Transparency** - Regularly update project progress, maintaining transparency
5. **Risk Prioritization** - Identify and record risks early, develop mitigation measures
6. **Command Awareness** - Use Cursor commands appropriately to optimize development workflow

## 🔧 Advanced Configuration

### Custom Timezone

If you need to use a timezone other than Pacific time, you can modify the `scripts/generate_timestamp.py` file:

```python
# Replace 'America/Los_Angeles' with your desired timezone
pacific_tz = pytz.timezone('your_timezone')
```

Common timezones include:
- `Asia/Shanghai` - China Standard Time
- `Asia/Tokyo` - Japan Standard Time
- `Europe/London` - British Standard Time
- `Europe/Paris` - Central European Time
- `America/New_York` - US Eastern Time

### Custom Templates

You can modify the template files in the `project_management/templates/` directory according to project requirements:

1. Edit template files to add or modify fields
2. Ensure replacement markers use the `{{PLACEHOLDER}}` format
3. Update corresponding scripts to handle new placeholders

## 🤝 Contribution Guidelines

We welcome and appreciate contributions of any form!

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## 📝 Version History

- **Beta 0.1** (2025-03-07)
  - Initial project structure and core functionality
  - Basic template file system
  - Timestamp functionality (Pacific Time)
  - Automated project management scripts

## 📞 Contact Information

- **Project Maintainer**: <a href="https://github.com/yagami1997" target="_blank">Yagami</a>
- **Project Repository**: [https://github.com/yagami1997/CursorMind](https://github.com/yagami1997/CursorMind)


---

<div align="center">
  <p><strong>CursorMind</strong> - Enhance Development Efficiency, Standardize Project Management</p>
  <p><i>Last Updated: 2025-03-08 PST</i></p>
  <hr>
</div>
