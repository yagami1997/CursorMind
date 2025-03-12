# ✨ CursorMind

<p align="right">
  <a href="README.md">English Version</a> |
  <a href="README.zh.md">中文版</a>
</p>

<div align="center">
  <h1>CursorMind</h1>
  <h3>Enhance Your Cursor Development Efficiency and Project Management Quality</h3>
  <p><strong>Current Version: Beta 0.2.1</strong></p>
  
  ![License](https://img.shields.io/badge/License-MIT-blue.svg)
  ![Version](https://img.shields.io/badge/Version-Beta%200.2.1-brightgreen.svg)
  ![Status](https://img.shields.io/badge/Status-In%20Development-orange.svg)
  ![Language](https://img.shields.io/badge/Language-Python-yellow.svg)
  ![Python Version](https://img.shields.io/badge/Python-3.9--3.13-blue.svg)
</div>

## 📝 Update Log

### Beta 0.2.1 (2025-03-12 00:25:02 PDT)
- 🔄 Refactored core code structure, improved system stability
- ✨ Added code review functionality, supporting multiple coding standards
- 🛡️ Enhanced file operation security, preventing potential risks
- ⚡️ Optimized performance check logic, improved analysis efficiency
- 📊 Improved project management features, supporting more scenarios
- 📚 Added learning path functionality, supporting programming education

### Beta 0.1 (2025-03-07)
- 🎉 Released initial project structure
- ✅ Implemented basic functional modules

## 📖 Project Introduction

🌟 **CursorMind** is a comprehensive development toolkit for developers 👨‍💻, project managers 👨‍💼, teams 👥, and students 👨‍🎓. It provides not only code quality assurance tools 🛠️ but also includes project management 📊, learning assistance 📚, and best practice guidelines 📝. For middle and high school students learning programming, CursorMind offers an ideal learning platform 🎯, helping them establish correct software engineering mindset 🧠 from the beginning of their programming journey.

### 🎯 Core Values

1. **Educational Empowerment**
   - Provide progressive learning paths for programming beginners
   - Help educators establish standardized teaching systems
   - Cultivate engineering thinking through practical projects

2. **Development Standards**
   - Provide industry-recognized coding standards
   - Implement best development practices
   - Ensure code quality and consistency

3. **Project Management**
   - Standardize project processes
   - Improve team collaboration efficiency
   - Ensure project delivery quality

4. **Automation Tools**
   - Automatic code quality checks
   - Performance analysis and optimization
   - Security vulnerability detection

## 🚀 Feature Details

### 1. Code Quality Assurance
- **Code Review**
  - Style Check: Ensure code complies with PEP8, Google Style, and other mainstream coding standards
  - Complexity Analysis: Calculate cyclomatic complexity, identify code blocks needing refactoring
  - Naming Conventions: Check if variables, functions, and classes follow best practices
  - Comment Completeness: Verify if key functionality has sufficient documentation
  
- **Performance Analysis**
  - Algorithm Complexity Assessment: Analyze time and space complexity
  - Memory Usage Monitoring: Identify memory leaks and excessive memory usage
  - Performance Bottleneck Location: Find time-consuming operations through performance analysis
  - Optimization Suggestions: Provide specific performance optimization solutions
  
- **Security Check**
  - SQL Injection Detection: Identify potential database security risks
  - XSS Vulnerability Scanning: Check for cross-site scripting attack vulnerabilities
  - Sensitive Information Detection: Discover potentially leaked keys, tokens, etc.
  - Dependency Package Security: Check known vulnerabilities in third-party libraries
  
- **Best Practices**
  - Design Pattern Application: Recommend suitable design patterns
  - Code Reuse Suggestions: Identify reusable code segments
  - Test Coverage: Check unit test completeness
  - Exception Handling Standards: Ensure exception handling reasonability

### 2. Project Management Tools
- **Progress Tracking**
  - Milestone Management: Set and monitor key project nodes
  - Burndown Chart Analysis: Visualize project progress and workload
  - Delay Warning: Intelligently identify tasks that may cause delays
  - Resource Allocation: Optimize team member work distribution
  
- **Task Management**
  - Task Breakdown: Break large tasks into manageable subtasks
  - Priority Sorting: Sort tasks based on importance and urgency
  - Dependency Relationships: Manage task prerequisites and post-conditions
  - Time Estimation: Assist in evaluating task time requirements
  
- **Report Generation**
  - Daily/Weekly Reports: Automatically generate standardized work reports
  - Code Quality Reports: Summarize code review and test results
  - Project Health: Assess overall project status
  - Trend Analysis: Predict project development direction
  
- **Team Collaboration**
  - Code Review: Standardized code review process
  - Knowledge Sharing: Team best practices and experience sharing
  - Team Kanban: Visual task collaboration management
  - Instant Feedback: Quick response to team member issues

### 3. Learning and Development
- **Learning Paths**
  - Skill Map: Personalized skill improvement routes
  - Advanced Guides: Graded learning resource recommendations
  - Practical Projects: Supporting practice projects
  - Learning Tracking: Record learning progress and achievements
  
- **Best Practices**
  - Coding Standards: Detailed code writing guidelines
  - Architecture Design: Common architecture patterns and application scenarios
  - Performance Optimization: System performance tuning methodology
  - Secure Development: Security coding guidelines and practices
  
- **Example Code**
  - Design Patterns: Implementation examples of common design patterns
  - Algorithm Implementation: Best practices for classic algorithms
  - Function Modules: Reference implementations of common features
  - Test Cases: Unit test writing examples
  
- **Technical Documentation**
  - API Documentation: Detailed interface usage instructions
  - Architecture Documentation: System design and module descriptions
  - Deployment Guide: Environment configuration and deployment process
  - Troubleshooting: Common problem solutions

## 🎯 Usage Method Selection

CursorMind provides the following actual features that you can choose based on your needs:

### 1. 🛠️ Code Quality Tools (Installation Required)

```bash
# Install complete toolkit
pip install cursormind

# Usage examples
cursormind review file your_code.py
cursormind analyze directory your_project/
```

Actually provided features:
- 🔍 Code review
- 📊 Directory analysis
- 📝 Report generation

### 2. 📚 Learning Resources

Project actual structure:
```
CursorMind/
├── learning_paths/        # Learning path definitions
├── learning_notes/       # Learning notes and documentation
└── project_management/   # Project management related files
```

#### How to Use Learning Resources

1. **Choose Suitable Learning Path**
   ```bash
   # Step 1: Browse learning path directory, check available paths
   ls learning_paths/
   
   # Step 2: Choose path suitable for your level
   # For example: If you're a Python beginner, open python_beginner.md
   cat learning_paths/python_beginner.md
   
   # Step 3: Follow the guidance in the path file, learn step by step
   # Path file will list:
   # - Learning objectives
   # - Prerequisites
   # - Learning steps
   # - Practice projects
   ```

2. **Use Learning Notes**
   ```bash
   # Step 1: Check note categories
   ls learning_notes/categories/
   
   # Step 2: Choose interesting topic
   # For example: Want to learn Python OOP
   cat learning_notes/categories/python/oop_basics.md
   
   # Step 3: Practice examples in notes
   # Each note contains:
   # - Concept explanation
   # - Code examples
   # - Common problems
   # - Exercises
   ```

3. **Use Project Management Templates**
   ```bash
   # Step 1: Check available project templates
   ls project_management/templates/
   
   # Step 2: Choose suitable project template
   # For example: Create a new Python project
   cp -r project_management/templates/python_project ./my_project
   
   # Step 3: Develop according to template README
   cat my_project/README.md
   ```

#### Usage Suggestions

1. **Beginners**
   - 👉 Start from `learning_paths/beginner/`
   - 👉 Combine with `learning_notes/basics/` for deep learning
   - 👉 Use `project_management/templates/starter/` to create practice projects

2. **Advanced Learners**
   - 👉 Choose `learning_paths/intermediate/` to improve skills
   - 👉 Reference `learning_notes/advanced/` to master advanced concepts
   - 👉 Use `project_management/templates/advanced/` to develop actual projects

3. **Team Usage**
   - 👉 Use `project_management/guidelines/` to standardize team development
   - 👉 Reference `learning_notes/best_practices/` to improve development process
   - 👉 Based on `project_management/templates/team/` to establish project structure

> Note: More learning path and note management features are under development

### 3. 🔧 Development Tools

Actually included tools:
```
CursorMind/
├── src/                 # Source code directory
├── scripts/             # Utility scripts
└── tests/              # Test cases
```

## 💡 Usage Suggestions

Based on actual project situations:

### Individual Developers
- ✅ Use code review tools
- ✅ Reference learning paths
- ✅ Use project management templates

### Team Usage
- ✅ Install complete toolkit
- ✅ Use project management features
- ✅ Configure team development standards

## 💻 Installation Guide

### System Requirements

- Python 3.9-3.13 (Python 3.13 recommended)
- pip package manager
- Git (optional, for version control)

### Windows Installation Steps

1. **Install Python**
   ```powershell
   # Download and install Python 3.13 from https://www.python.org/downloads/
   # Must check "Add Python to PATH" during installation
   ```

2. **Open PowerShell and Create Virtual Environment**
   ```powershell
   # Create project directory
   mkdir CursorMind
   cd CursorMind
   
   # Create and activate virtual environment
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # If permission error occurs, run as administrator:
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **Install CursorMind**
   ```powershell
   # Upgrade pip
   python -m pip install --upgrade pip
   
   # Install cursormind
   pip install cursormind
   
   # Set PYTHONPATH (PowerShell)
   $env:PYTHONPATH = "src"
   ```

4. **Verify Installation**
   ```powershell
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### macOS Installation Steps

1. **Install Python Using Homebrew**
   ```bash
   # Install Homebrew (if not installed)
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install Python 3.13
   brew install python@3.13
   ```

2. **Create Virtual Environment**
   ```bash
   # Create project directory
   mkdir CursorMind && cd CursorMind
   
   # Create and activate virtual environment
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install CursorMind**
   ```bash
   # Upgrade pip
   pip install --upgrade pip
   
   # Install cursormind
   pip install cursormind
   
   # Set PYTHONPATH
   export PYTHONPATH=src
   ```

4. **Verify Installation**
   ```bash
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### Ubuntu/Debian Installation Steps

1. **Install Python and Dependencies**
   ```bash
   # Update package list
   sudo apt update
   
   # Add deadsnakes PPA to get latest Python version
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   
   # Install Python 3.13 and development tools
   sudo apt install python3.13 python3.13-venv python3.13-dev python3-pip git
   ```

2. **Create Virtual Environment**
   ```bash
   # Create project directory
   mkdir CursorMind && cd CursorMind
   
   # Create and activate virtual environment
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install CursorMind**
   ```bash
   # Upgrade pip
   pip install --upgrade pip
   
   # Install cursormind
   pip install cursormind
   
   # Set PYTHONPATH
   export PYTHONPATH=src
   ```

4. **Verify Installation**
   ```bash
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### Troubleshooting

#### Windows Common Issues

1. **Python Not Added to PATH**
   ```powershell
   # Check if Python is in PATH
   python --version
   
   # If not found, manually add to PATH
   # Open System Properties -> Environment Variables -> Path -> Add Python installation path
   # Usually at: C:\Users\username\AppData\Local\Programs\Python\Python313
   ```

2. **Virtual Environment Activation Failed**
   ```powershell
   # If permission error occurs
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # Reactivate virtual environment
   .\.venv\Scripts\Activate.ps1
   ```

3. **Module Not Found**
   ```powershell
   # Ensure PYTHONPATH is correctly set
   echo $env:PYTHONPATH
   
   # If needed, reset
   $env:PYTHONPATH = "src"
   ```

#### macOS Common Issues

1. **Python Version Conflict**
   ```bash
   # Check Python version
   python3 --version
   
   # Use specific version
   python3.13 -m pip install cursormind
   ```

2. **Permission Issues**
   ```bash
   # Fix permissions
   sudo chown -R $USER ~/.local
   chmod +x ~/.local/bin/cursormind
   ```

3. **Environment Variable Persistence**
   ```bash
   # Add to .zshrc or .bash_profile
   echo 'export PYTHONPATH=src' >> ~/.zshrc
   source ~/.zshrc
   ```

#### Ubuntu/Debian Common Issues

1. **PPA Addition Failed**
   ```bash
   # Install necessary tools
   sudo apt install software-properties-common
   
   # Retry adding PPA
   sudo add-apt-repository ppa:deadsnakes/ppa
   ```

2. **Dependency Issues**
   ```bash
   # Install build dependencies
   sudo apt install build-essential libssl-dev libffi-dev python3.13-dev
   ```

3. **Permission Issues**
   ```bash
   # Fix permissions
   sudo chown -R $USER ~/.local
   sudo chmod +x ~/.local/bin/cursormind
   ```

### Installation Verification Checklist

Please ensure all following commands run normally:

1. **Version Check**
   ```bash
   cursormind --version
   # Should output: cursormind, version 0.2.1
   ```

2. **Code Review**
   ```bash
   cursormind review file src/cursormind/core/code_review.py
   # Should display code review report
   ```

3. **Directory Review**
   ```bash
   cursormind review dir src/cursormind/core
   # Should display directory review report
   ```

If any command fails, please refer to the troubleshooting guide above. If problems persist, please report in GitHub Issues.

---
*Last updated: 2025-03-12 00:52:15 PDT*
