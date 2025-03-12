# ✨ CursorMind

<p align="right">
  <a href="README.md">English Version</a> |
  <a href="README.zh.md">中文版</a>
</p>

<div align="center">
  <h1>CursorMind</h1>
  <h3>提升您的 Cursor 开发效率与项目管理质量</h3>
  <p><strong>当前版本：Beta 0.2.1</strong></p>
  
  ![许可证](https://img.shields.io/badge/许可证-MIT-blue.svg)
  ![版本](https://img.shields.io/badge/版本-Beta%200.2.1-brightgreen.svg)
  ![状态](https://img.shields.io/badge/状态-开发中-orange.svg)
  ![语言](https://img.shields.io/badge/语言-Python-yellow.svg)
  ![Python版本](https://img.shields.io/badge/Python-3.9--3.13-blue.svg)
</div>

## 📝 更新日志

### Beta 0.2.1 (2025-03-12 00:25:02 PDT)
- 🔄 重构核心代码结构，提升系统稳定性
- ✨ 新增代码审查功能，支持多种编码规范
- 🛡️ 增强文件操作安全性，防止潜在风险
- ⚡️ 优化性能检查逻辑，提升分析效率
- 📊 改进项目管理功能，支持更多场景
- 📚 添加学习路径功能，助力编程教育

### Beta 0.1 (2025-03-07)
- 🎉 发布初始项目结构
- ✅ 实现基础功能模块

---

## 📖 项目简介

🌟 **CursorMind** 是一个面向开发者 👨‍💻、项目经理 👨‍💼、团队 👥 和学生 👨‍🎓 的综合性开发工具集。它不仅提供了代码质量保证工具 🛠️，还包含了项目管理 📊、学习辅助 📚 和最佳实践指南 📝 等功能模块。对于正在学习编程的中小学生来说，CursorMind 提供了一个理想的学习平台 🎯，帮助他们在编程启蒙阶段就建立正确的软件工程思维 🧠。

### 🎯 核心价值

1. **教育赋能**
   - 为编程初学者提供循序渐进的学习路径
   - 帮助教育工作者建立标准化的教学体系
   - 通过实践项目培养工程思维

2. **开发规范**
   - 提供业界认可的编码标准
   - 实施最佳开发实践
   - 保证代码质量和一致性

3. **项目管理**
   - 标准化项目流程
   - 提高团队协作效率
   - 确保项目交付质量

4. **自动化工具**
   - 代码质量自动检查
   - 性能分析和优化
   - 安全漏洞检测

## 🚀 功能详情

CursorMind 为您提供全方位的开发支持：

### 1. 代码质量保证 ⚡️
- 智能代码审查，确保编码规范
- 性能分析与优化建议
- 安全漏洞自动检测
- 最佳实践指导

<details>
<summary>查看详细功能列表 👉</summary>

- **代码审查**
  - 风格检查：确保代码符合 PEP8、Google Style 等主流编码规范
  - 复杂度分析：计算圈复杂度，识别需要重构的代码块
  - 命名规范：检查变量、函数、类的命名是否符合最佳实践
  - 注释完整性：验证关键功能是否有充分的文档说明
  
- **性能分析**
  - 算法复杂度评估：分析时间和空间复杂度
  - 内存使用监控：识别内存泄漏和过度内存使用
  - 性能瓶颈定位：通过性能分析找出耗时操作
  - 优化建议：提供具体的性能优化方案
  
- **安全检查**
  - SQL 注入检测：识别潜在的数据库安全风险
  - XSS 漏洞扫描：检查跨站脚本攻击隐患
  - 敏感信息检测：发现可能泄露的密钥、令牌等
  - 依赖包安全：检查第三方库的已知漏洞
  
- **最佳实践**
  - 设计模式应用：推荐合适的设计模式
  - 代码重用建议：识别可复用的代码片段
  - 测试覆盖率：检查单元测试的完整性
  - 异常处理规范：确保异常处理的合理性
</details>

## 🎯 使用方式选择

快速上手 CursorMind：

```bash
# 安装完整工具集
pip install cursormind

# 开始使用
cursormind review file your_code.py    # 代码审查
cursormind analyze dir your_project/    # 项目分析
```

#### 📚 学习资源概览
- 循序渐进的学习路径
- 丰富的学习笔记和示例
- 标准化的项目管理模板

<details>
<summary>查看详细使用指南 👉</summary>

CursorMind 提供以下实际功能，您可以根据需求选择：

### 1. 🛠️ 代码质量工具（需要安装）

```bash
# 安装完整工具集
pip install cursormind

# 使用示例
cursormind review file your_code.py
cursormind analyze directory your_project/
```

实际提供的功能：
- 🔍 代码审查
- 📊 目录分析
- 📝 报告生成

### 2. 📚 学习资源

项目实际结构：
```
CursorMind/
├── learning_paths/        # 学习路径定义
├── learning_notes/       # 学习笔记和文档
└── project_management/   # 项目管理相关文件
```

#### 如何使用学习资源

1. **选择合适的学习路径**
   ```bash
   # 第一步：浏览学习路径目录，查看可用的路径
   ls learning_paths/
   
   # 第二步：选择适合自己水平的路径
   # 例如：如果你是Python初学者，打开 python_beginner.md
   cat learning_paths/python_beginner.md
   
   # 第三步：按照路径文件中的指引，逐步学习
   # 路径文件会列出：
   # - 学习目标
   # - 前置知识
   # - 学习步骤
   # - 练习项目
   ```

2. **使用学习笔记**
   ```bash
   # 第一步：查看笔记分类
   ls learning_notes/categories/
   
   # 第二步：选择感兴趣的主题
   # 例如：想学习Python面向对象编程
   cat learning_notes/categories/python/oop_basics.md
   
   # 第三步：动手实践笔记中的示例
   # 每个笔记包含：
   # - 概念解释
   # - 代码示例
   # - 常见问题
   # - 练习题
   ```

3. **使用项目管理模板**
   ```bash
   # 第一步：查看可用的项目模板
   ls project_management/templates/
   
   # 第二步：选择合适的项目模板
   # 例如：创建一个新的Python项目
   cp -r project_management/templates/python_project ./my_project
   
   # 第三步：按照模板中的README进行开发
   cat my_project/README.md
   ```

#### 使用建议

1. **初学者**
   - 👉 从 `learning_paths/beginner/` 开始
   - 👉 结合 `learning_notes/basics/` 深入学习
   - 👉 使用 `project_management/templates/starter/` 创建练习项目

2. **进阶学习者**
   - 👉 选择 `learning_paths/intermediate/` 提升技能
   - 👉 参考 `learning_notes/advanced/` 掌握高级概念
   - 👉 使用 `project_management/templates/advanced/` 开发实际项目

3. **团队使用**
   - 👉 使用 `project_management/guidelines/` 规范团队开发
   - 👉 参考 `learning_notes/best_practices/` 改进开发流程
   - 👉 基于 `project_management/templates/team/` 建立项目结构

> 注：更多学习路径和笔记管理功能正在开发中
</details>

## 💻 安装指南

### 快速开始
1. 确保安装 Python 3.9-3.13
2. 运行安装命令：
```bash
pip install cursormind
export PYTHONPATH=src  # Unix/macOS
set PYTHONPATH=src    # Windows
```

<details>
<summary>查看完整安装说明 👉</summary>

### 系统要求

- Python 3.9-3.13（推荐使用 Python 3.13）
- pip 包管理器
- Git（可选，用于版本控制）

### Windows 安装步骤

1. **安装 Python**
   ```powershell
   # 从 https://www.python.org/downloads/ 下载并安装 Python 3.13
   # 安装时必须勾选 "Add Python to PATH"
   ```

2. **打开 PowerShell 并创建虚拟环境**
   ```powershell
   # 创建项目目录
   mkdir CursorMind
   cd CursorMind
   
   # 创建并激活虚拟环境
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # 如果出现权限错误，请以管理员身份运行：
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. **安装 CursorMind**
   ```powershell
   # 升级 pip
   python -m pip install --upgrade pip
   
   # 安装 cursormind
   pip install cursormind
   
   # 设置 PYTHONPATH（PowerShell）
   $env:PYTHONPATH = "src"
   ```

4. **验证安装**
   ```powershell
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### macOS 安装步骤

1. **使用 Homebrew 安装 Python**
   ```bash
   # 安装 Homebrew（如果未安装）
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # 安装 Python 3.13
   brew install python@3.13
   ```

2. **创建虚拟环境**
   ```bash
   # 创建项目目录
   mkdir CursorMind && cd CursorMind
   
   # 创建并激活虚拟环境
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

3. **安装 CursorMind**
   ```bash
   # 升级 pip
   pip install --upgrade pip
   
   # 安装 cursormind
   pip install cursormind
   
   # 设置 PYTHONPATH
   export PYTHONPATH=src
   ```

4. **验证安装**
   ```bash
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### Ubuntu/Debian 安装步骤

1. **安装 Python 和依赖**
   ```bash
   # 更新包列表
   sudo apt update
   
   # 添加 deadsnakes PPA 以获取最新的 Python 版本
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   
   # 安装 Python 3.13 和开发工具
   sudo apt install python3.13 python3.13-venv python3.13-dev python3-pip git
   ```

2. **创建虚拟环境**
   ```bash
   # 创建项目目录
   mkdir CursorMind && cd CursorMind
   
   # 创建并激活虚拟环境
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

3. **安装 CursorMind**
   ```bash
   # 升级 pip
   pip install --upgrade pip
   
   # 安装 cursormind
   pip install cursormind
   
   # 设置 PYTHONPATH
   export PYTHONPATH=src
   ```

4. **验证安装**
   ```bash
   cursormind --version
   cursormind review file src/cursormind/core/code_review.py
   ```

### 安装验证清单

请确保以下所有命令都能正常运行：

1. **版本检查**
   ```bash
   cursormind --version
   # 应输出：cursormind, version 0.2.1
   ```

2. **代码审查**
   ```bash
   cursormind review file src/cursormind/core/code_review.py
   # 应显示代码审查报告
   ```

3. **目录审查**
   ```bash
   cursormind review dir src/cursormind/core
   # 应显示目录审查报告
   ```

如果任何命令失败，请参考下方的故障排除指南。
</details>

## ❗ 常见问题

遇到问题？以下是一些快速解决方案：

1. 确保 Python 版本兼容（3.9-3.13）
2. 检查 PYTHONPATH 环境变量设置
3. 验证虚拟环境是否正确激活

<details>
<summary>查看完整故障排除指南 👉</summary>

### Windows 常见问题

1. **Python 未添加到 PATH**
   ```powershell
   # 检查 Python 是否在 PATH 中
   python --version
   
   # 如果未找到，手动添加到 PATH
   # 打开系统属性 -> 环境变量 -> Path -> 添加 Python 安装路径
   # 通常在：C:\Users\用户名\AppData\Local\Programs\Python\Python313
   ```

2. **虚拟环境激活失败**
   ```powershell
   # 如果出现权限错误
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # 重新激活虚拟环境
   .\.venv\Scripts\Activate.ps1
   ```

3. **模块未找到**
   ```powershell
   # 确保 PYTHONPATH 正确设置
   echo $env:PYTHONPATH
   
   # 如果需要，重新设置
   $env:PYTHONPATH = "src"
   ```

### macOS 常见问题

1. **Python 版本冲突**
   ```bash
   # 检查 Python 版本
   python3 --version
   
   # 使用特定版本
   python3.13 -m pip install cursormind
   ```

2. **权限问题**
   ```bash
   # 修复权限
   sudo chown -R $USER ~/.local
   chmod +x ~/.local/bin/cursormind
   ```

3. **环境变量持久化**
   ```bash
   # 添加到 .zshrc 或 .bash_profile
   echo 'export PYTHONPATH=src' >> ~/.zshrc
   source ~/.zshrc
   ```

### Ubuntu/Debian 常见问题

1. **PPA 添加失败**
   ```bash
   # 安装必要工具
   sudo apt install software-properties-common
   
   # 重试添加 PPA
   sudo add-apt-repository ppa:deadsnakes/ppa
   ```

2. **依赖问题**
   ```bash
   # 安装编译依赖
   sudo apt install build-essential libssl-dev libffi-dev python3.13-dev
   ```

3. **权限问题**
   ```bash
   # 修复权限
   sudo chown -R $USER ~/.local
   sudo chmod +x ~/.local/bin/cursormind
   ```
</details>

<details>
<summary>🕒 时间戳规范</summary>

为确保项目文档中的时间戳保持一致性和准确性，我们提供了专门的时间戳生成工具。

### 时间戳工具使用

```bash
# 生成完整格式的时间戳（默认）
python3 scripts/generate_timestamp.py full
# 输出示例：2025-03-11 23:37:45 PDT

# 仅生成日期
python3 scripts/generate_timestamp.py date
# 输出示例：2025-03-11

# 生成日期和时间（不含时区）
python3 scripts/generate_timestamp.py datetime
# 输出示例：2025-03-11 23:37:45

# 生成紧凑格式
python3 scripts/generate_timestamp.py compact
# 输出示例：20250311

# 生成年份和周数
python3 scripts/generate_timestamp.py week
# 输出示例：2025W11
```

### 时间戳规范说明

1. **强制要求**
   - 所有文档中的时间戳必须使用 `scripts/generate_timestamp.py` 生成
   - 禁止手动编写或修改时间戳
   - 时区必须保持一致（默认使用美国太平洋时区 PST/PDT）
   - 如需使用其他时区，请在项目根目录的 `.env` 文件中设置 `TZ` 环境变量，并确保所有团队成员使用相同配置

2. **Git Hook 配置**
   ```bash
   # 复制 pre-commit hook 到 Git hooks 目录
   cp scripts/hooks/pre-commit .git/hooks/
   
   # 设置执行权限
   chmod +x .git/hooks/pre-commit
   ```
</details>

## 📢 宣言

我们坚信：
- 技术应该是平等的，每个人都应该有机会学习和使用AI编程
- Cursor不仅是一个IDE，更是一个让编程变得更简单、更智能的工具
- 通过CursorMind，我们致力于让每个开发者都能享受到AI辅助编程的便利
- 开源精神是技术进步的基石，欢迎大家fork项目，共同建设AI编程生态

## 🤝 参与贡献

我们热烈欢迎社区的每一位成员参与到CursorMind的开发中来：
- 🌟 如果您觉得这个项目有帮助，请给我们一个star
- 🐛 发现bug？请提交 [Issues](https://github.com/yourusername/cursormind/issues)
- 💡 有新想法？欢迎提交 [Pull Requests](https://github.com/yourusername/cursormind/pulls)
- 📝 帮助改进文档？这对初学者来说非常重要
- 💬 分享您的使用经验和建议

让我们一起打造更好的AI编程工具！

---
*最后更新：2025-03-12 00:53:07 PDT*
