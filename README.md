# ✨ CursorMind

<p align="right">
  <a href="README.md">English Version</a> |
  <a href="README.zh.md">中文版</a>
</p>

<div align="center">
  <h1>CursorMind</h1>
  <h3>Elevate Your Development Experience with AI-Powered Tools</h3>
  <p><strong>Current Version: Beta 0.2.1</strong></p>
  
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version](https://img.shields.io/badge/Version-Beta%200.2.1-brightgreen.svg)
  ![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)
  ![Language](https://img.shields.io/badge/Language-Python-yellow.svg)
  ![Python Version](https://img.shields.io/badge/Python-3.9--3.13-blue.svg)
</div>

## 📝 Update Log

### Beta 0.2.1 (2025-03-12 00:25:02 PDT)
- 🔄 Enhanced core architecture for improved stability and performance
- ✨ Introduced comprehensive code review system with multi-standard support
- 🛡️ Strengthened file operation security mechanisms
- ⚡️ Optimized performance analysis algorithms
- 📊 Expanded project management capabilities
- 📚 Launched interactive learning paths feature

### Beta 0.1 (2025-03-07)
- 🎉 Initial release with foundational framework
- ✅ Core functionality implementation

---

## 📖 Project Introduction

🌟 **CursorMind** is your intelligent companion for AI-assisted development, designed to serve developers 👨‍💻, project managers 👨‍💼, teams 👥, and students 👨‍🎓. Beyond traditional development tools, it integrates code quality assurance 🛠️, project management 📊, learning assistance 📚, and best practice guidelines 📝. For students beginning their programming journey, CursorMind provides an ideal platform 🎯 to develop proper software engineering mindset 🧠 from day one.

### 🎯 Core Values

1. **Educational Excellence**
   - Structured learning paths for programming beginners
   - Standardized teaching frameworks for educators
   - Hands-on projects for practical skill development

2. **Development Standards**
   - Industry-aligned coding guidelines
   - Best practice implementations
   - Quality-focused development approach

3. **Project Management**
   - Streamlined project workflows
   - Enhanced team collaboration
   - Quality-driven delivery process

4. **Automation Tools**
   - Intelligent code quality assessment
   - Performance optimization tools
   - Security vulnerability detection

## 🚀 Feature Details

CursorMind offers comprehensive development support:

### 1. Code Quality Assurance ⚡️
- Smart code review with standard compliance
- Performance analysis and optimization
- Automated security vulnerability detection
- Best practice guidance

### 2. Project Management Tools 📊
- Project progress tracking
- Team collaboration workflows
- Automated reporting system
- Quality metrics monitoring

### 3. Learning & Development 📚
- Personalized learning paths
- Rich resource library
- Practical project exercises
- Skill assessment tools

### 4. Development Tools Integration 🛠️
- Automated workflow configuration
- Version control integration
- CI/CD pipeline support
- Development environment standardization

<details>
<summary>View Detailed Feature List 👉</summary>

- **Code Review**
  - Style Compliance: PEP8, Google Style, and other standard checks
  - Complexity Analysis: Cyclomatic complexity calculation and refactoring suggestions
  - Naming Conventions: Best practice validation for variables, functions, and classes
  - Documentation Coverage: Critical functionality documentation verification
  
- **Performance Analysis**
  - Algorithm Complexity: Time and space complexity assessment
  - Memory Management: Leak detection and usage optimization
  - Performance Profiling: Bottleneck identification
  - Optimization Guide: Targeted improvement recommendations
  
- **Project Management**
  - Progress Tracking: Milestone management and burndown analysis
  - Task Management: Smart task breakdown and workload assessment
  - Team Collaboration: Code review workflow and knowledge sharing
  - Quality Monitoring: Automated testing and performance tracking
  
- **Learning Resources**
  - Skill Map: Personalized improvement pathways
  - Practice Projects: Curated exercise collection
  - Best Practices: Detailed coding standards and architecture guidelines
  - Reference Code: Common functionality implementations
  
- **Tool Integration**
  - CI/CD: Pipeline configuration and automation
  - Git Integration: Version control and branch management
  - Environment Setup: Development environment automation
  - IDE Support: Popular development tool integration
</details>

## 🎯 Getting Started

Choose your path with CursorMind:

### 1. Individual Developer 👨‍💻

Quick start with code quality tools:
```bash
# Install the toolkit
pip install cursormind
export PYTHONPATH=src  # Unix/macOS
set PYTHONPATH=src    # Windows

# Begin using
cursormind review file your_code.py    # Code review
cursormind analyze dir your_project/    # Project analysis
```

### 2. Learner 📚

Start your learning journey:
```bash
# Browse available learning paths
cursormind path list

# Begin a learning path (e.g., Python basics)
cursormind path start python-beginner

# Check progress and resources
cursormind path status

# Complete current task and get next steps
cursormind path next
```

### 3. Project Team 👥

Structured project management workflow:
```bash
# Step 1: Initialize new project
./project_management/scripts/init_project.sh "Project Name"

# Step 2: Daily workflow management
./project_management/scripts/create_daily_report.sh    # Daily report
./project_management/scripts/update_progress.sh 35 "Auth module complete"  # Update progress
./project_management/scripts/create_task.sh "Implement login"   # Create task
./project_management/scripts/update_task.sh TASK-001 "In Progress"  # Update status

# Step 3: Generate reports
./project_management/scripts/create_weekly_report.sh    # Weekly summary
```

<details>
<summary>View Detailed Usage Guide 👉</summary>

### Developer Workflow

1. **Quality Management**
   - Use `cursormind review` for code analysis
   - Run `cursormind analyze` for project assessment
   - Apply recommended best practices
   - Address security vulnerabilities

2. **Documentation Management**
   - Use standardized templates (`project_management/templates/`)
   - Follow timestamp conventions (`scripts/generate_timestamp.py`)
   - Maintain progress tracking (`PROJECT_PROGRESS.md`)
   - Document technical decisions

3. **Engineering Standards**
   - Follow language-specific guidelines (e.g., PEP8 for Python)
   - Maintain code-to-documentation ratio (80:20)
   - Ensure test coverage (minimum 85%)
   - Regular security audits

### Learning Guide

1. **Path Selection**
   - Browse available paths (`learning_paths/`)
   - Choose appropriate skill level
   - Set learning objectives
   - Track progress

2. **Resource Utilization**
   - Access recommended materials
   - Complete milestone projects
   - Study example implementations
   - Document learning insights

3. **Practical Development**
   - Use project templates
   - Apply learned concepts
   - Get mentor feedback
   - Continuous improvement

### Team Collaboration

1. **Project Setup**
   ```bash
   # Create project structure
   ./project_management/scripts/init_project.sh "Project Name"
   
   # Configure workflow
   cp project_management/templates/* ./
   ```

2. **Daily Operations**
   ```bash
   # Create daily report
   ./project_management/scripts/create_daily_report.sh "Version Release"
   
   # Update progress
   ./project_management/scripts/update_progress.sh 50 "MVP Complete"
   
   # Task management
   ./project_management/scripts/create_task.sh "New Feature"
   ./project_management/scripts/update_task.sh TASK-001 "In Progress"
   ```

3. **Quality Control**
   ```bash
   # Code review
   cursormind review file src/main.py
   
   # Project analysis
   cursormind analyze dir ./src
   
   # Quality report
   ./project_management/scripts/generate_quality_report.sh
   ```

### Best Practices

1. **Individual Development**
   - Pre-commit code review
   - Real-time documentation updates
   - Coding standard compliance
   - Regular performance optimization

2. **Learning Enhancement**
   - Structured learning plan
   - Consistent practice
   - Regular reflection
   - Community engagement

3. **Team Collaboration**
   - Standard adherence
   - Effective communication
   - Knowledge sharing
   - Regular code reviews

</details>

## 💻 Installation Guide

Quick Start:
1. Ensure Python 3.9-3.13 is installed
2. Run installation commands:
```bash
pip install cursormind
export PYTHONPATH=src  # Unix/macOS
set PYTHONPATH=src    # Windows
```

<details>
<summary>View Complete Installation Guide 👉</summary>

### System Requirements

- Python 3.9-3.13 (3.13 recommended)
- pip package manager
- Git (optional, for version control)

### Windows Installation

1. **Install Python**
   ```powershell
   # Download Python 3.13 from https://www.python.org/downloads/
   # Enable "Add Python to PATH" during installation
   ```

2. **Setup Environment**
   ```powershell
   # Create and activate virtual environment
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install CursorMind**
   ```powershell
   pip install --upgrade pip
   pip install cursormind
   $env:PYTHONPATH = "src"
   ```

### macOS/Linux Installation

1. **Create Environment**
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install CursorMind**
   ```bash
   pip install --upgrade pip
   pip install cursormind
   export PYTHONPATH=src
   ```

### Verify Installation

Run these commands:
```bash
cursormind --version
cursormind review file your_code.py
```

For issues, refer to the troubleshooting guide below.
</details>

### ❗ Common Issues

Quick solutions for common problems:

1. Verify Python version compatibility (3.9-3.13)
2. Check PYTHONPATH environment variable
3. Confirm virtual environment activation

<details>
<summary>View Complete Troubleshooting Guide 👉</summary>

### Windows Troubleshooting

1. **Python PATH Issues**
   ```powershell
   # Check Python installation
   python --version
   
   # Manual PATH addition if needed
   # System Properties -> Environment Variables -> Path
   # Add: C:\Users\username\AppData\Local\Programs\Python\Python313
   ```

2. **Virtual Environment Problems**
   ```powershell
   # Fix permission issues
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # Reactivate environment
   .\.venv\Scripts\Activate.ps1
   ```

3. **Module Import Errors**
   ```powershell
   # Verify PYTHONPATH
   echo $env:PYTHONPATH
   
   # Reset if needed
   $env:PYTHONPATH = "src"
   ```

### macOS Troubleshooting

1. **Python Version Issues**
   ```bash
   # Version check
   python3 --version
   
   # Use specific version
   python3.13 -m pip install cursormind
   ```

2. **Permission Problems**
   ```bash
   # Fix permissions
   sudo chown -R $USER ~/.local
   chmod +x ~/.local/bin/cursormind
   ```

3. **Environment Variables**
   ```bash
   # Add to shell profile
   echo 'export PYTHONPATH=src' >> ~/.zshrc
   source ~/.zshrc
   ```

### Ubuntu/Debian Troubleshooting

1. **PPA Issues**
   ```bash
   # Install prerequisites
   sudo apt install software-properties-common
   
   # Add PPA
   sudo add-apt-repository ppa:deadsnakes/ppa
   ```

2. **Dependency Problems**
   ```bash
   # Install build requirements
   sudo apt install build-essential libssl-dev libffi-dev python3.13-dev
   ```

3. **Permission Issues**
   ```bash
   # Fix permissions
   sudo chown -R $USER ~/.local
   sudo chmod +x ~/.local/bin/cursormind
   ```
</details>

<details>
<summary>🕒 Timestamp Standards</summary>

Ensure consistency in project documentation with our timestamp tools.

### Using Timestamp Tools

```bash
# Generate full timestamp (default)
python3 scripts/generate_timestamp.py full
# Output: 2025-03-11 23:37:45 PDT

# Date only
python3 scripts/generate_timestamp.py date
# Output: 2025-03-11

# Date and time (no timezone)
python3 scripts/generate_timestamp.py datetime
# Output: 2025-03-11 23:37:45

# Compact format
python3 scripts/generate_timestamp.py compact
# Output: 20250311

# Year and week
python3 scripts/generate_timestamp.py week
# Output: 2025W11
```

### Timestamp Guidelines

1. **Requirements**
   - Use `scripts/generate_timestamp.py` for all timestamps
   - No manual timestamp modifications
   - Maintain consistent timezone (default: US Pacific Time PST/PDT)
   - Configure timezone in `.env` file if needed

2. **Git Hook Setup**
   ```bash
   # Copy pre-commit hook
   cp scripts/hooks/pre-commit .git/hooks/
   
   # Set permissions
   chmod +x .git/hooks/pre-commit
   ```
</details>

### 📢 Manifesto

We believe:
- Technology should be accessible to everyone
- Cursor is more than an IDE; it's a gateway to smarter programming
- CursorMind empowers developers with AI-assisted programming
- Open source drives technological progress - fork and contribute!

### 🤝 Community Participation

Join our vibrant community:
- 🌟 Star us if you find CursorMind helpful
- 🐛 Report bugs via [Issues](https://github.com/yourusername/cursormind/issues)
- 💡 Submit [Pull Requests](https://github.com/yourusername/cursormind/pulls)
- 📝 Help improve documentation
- 💬 Share your experience and suggestions

Let's build better AI programming tools together!

#### 📜 MIT License

CursorMind is released under the MIT License, which means:
- ✅ You can freely use, modify, and distribute this software
- ✅ You can use it for commercial projects
- ✅ You can make and distribute closed source versions
- ℹ️ The only requirement is to include the original copyright notice and license

We encourage individuals and organizations to:
- 🔄 Fork and modify the project for your specific needs
- 🌱 Share your improvements back with the community
- 🤝 Collaborate on making AI-assisted development more accessible

For full license details, see the [LICENSE](LICENSE) file.

<div align="center" style="color: #666;">

*Cursor empowers efficiency, while your vision creates the future.*

</div>

---
*Last updated: 2025-03-12 02:37:42 PDT*
