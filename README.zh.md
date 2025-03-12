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

### 2. 项目管理工具 📊
- 项目进度追踪与管理
- 团队协作流程规范
- 自动化报告生成
- 质量指标监控

### 3. 学习与发展 📚
- 个性化学习路径规划
- 丰富的学习资源库
- 实战项目练习
- 技术能力评估

### 4. 开发工具集成 🛠️
- 自动化工作流配置
- 代码版本控制集成
- 持续集成/部署支持
- 开发环境标准化

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
  
- **项目管理**
  - 进度追踪：里程碑管理和燃尽图分析
  - 任务分配：智能任务分解和工作量评估
  - 团队协作：代码评审流程和知识共享
  - 质量监控：自动化测试和性能监测
  
- **学习资源**
  - 技能图谱：个性化的技能提升路线
  - 实战项目：配套的练习项目集
  - 最佳实践：详细的编码规范和架构指南
  - 示例代码：常用功能的参考实现

- **工具集成**
  - CI/CD：持续集成和部署流程配置
  - Git集成：版本控制和分支管理
  - 环境配置：开发环境自动化设置
  - 扩展支持：主流IDE和工具链集成
</details>

## 🎯 使用方式选择

CursorMind 提供三种主要使用场景，选择最适合您的方式开始：

### 1. 个人开发者 👨‍💻

快速开始使用代码质量工具：
```bash
# 安装工具
pip install cursormind
export PYTHONPATH=src  # Unix/macOS
set PYTHONPATH=src    # Windows

# 开始使用
cursormind review file your_code.py    # 代码审查
cursormind analyze dir your_project/    # 项目分析
```

### 2. 学习者 📚

开始您的学习之旅：
```bash
# 查看可用的学习路径
cursormind path list

# 选择并开始一个学习路径（如：Python入门）
cursormind path start python-beginner

# 查看当前进度和推荐资源
cursormind path status

# 完成当前任务并获取下一步建议
cursormind path next
```

### 3. 项目团队 👥

规范化的项目管理流程：
```bash
# 第1步：初始化新项目
./project_management/scripts/init_project.sh "项目名称"

# 第2步：日常工作管理
./project_management/scripts/create_daily_report.sh    # 创建日报
./project_management/scripts/update_progress.sh 35 "完成用户认证模块"  # 更新进度
./project_management/scripts/create_task.sh "实现登录功能"   # 创建新任务
./project_management/scripts/update_task.sh TASK-001 "进行中"  # 更新任务状态

# 第3步：生成工作报告
./project_management/scripts/create_weekly_report.sh    # 生成周报
```

<details>
<summary>查看详细使用指南 👉</summary>

### 开发者工作流

1. **代码质量管理**
   - 使用 `cursormind review` 进行代码审查
   - 运行 `cursormind analyze` 进行项目分析
   - 应用推荐的最佳实践和优化建议
   - 检查并修复潜在的安全漏洞

2. **项目文档管理**
   - 使用标准化的文档模板（位于 `project_management/templates/`）
   - 遵循时间戳规范记录更新（使用 `scripts/generate_timestamp.py`）
   - 维护项目进度文件（`PROJECT_PROGRESS.md`）
   - 记录技术决策和设计方案

3. **工程实践规范**
   - 遵循语言特定的编码标准（如 Python 的 PEP8）
   - 保持代码文档比例（80:20）
   - 确保单元测试覆盖率（最低 85%）
   - 定期进行安全漏洞检查

### 学习路径指南

1. **选择学习路径**
   - 浏览可用的学习路径（`learning_paths/`）
   - 根据个人水平选择合适的路径
   - 设置学习目标和计划
   - 跟踪学习进度

2. **使用学习资源**
   - 查看推荐的学习资源和文档
   - 完成阶段性练习项目
   - 参考示例代码和最佳实践
   - 记录学习心得和问题

3. **实践项目开发**
   - 使用项目模板快速启动
   - 应用所学知识解决实际问题
   - 获取导师反馈和建议
   - 持续改进和优化

### 团队协作流程

1. **项目初始化**
   ```bash
   # 创建标准项目结构
   ./project_management/scripts/init_project.sh "项目名称"
   
   # 配置工作流程
   cp project_management/templates/* ./
   ```

2. **日常工作管理**
   ```bash
   # 创建今日工作报告
   ./project_management/scripts/create_daily_report.sh "重要版本发布"
   
   # 更新项目进度
   ./project_management/scripts/update_progress.sh 50 "完成MVP版本"
   
   # 创建和更新任务
   ./project_management/scripts/create_task.sh "新功能开发"
   ./project_management/scripts/update_task.sh TASK-001 "进行中"
   ```

3. **质量控制**
   ```bash
   # 代码审查
   cursormind review file src/main.py
   
   # 项目分析
   cursormind analyze dir ./src
   
   # 生成质量报告
   ./project_management/scripts/generate_quality_report.sh
   ```

### 最佳实践建议

1. **个人开发**
   - 每次提交前进行代码审查
   - 保持文档的实时更新
   - 遵循项目编码规范
   - 定期进行性能优化

2. **学习提升**
   - 制定合理的学习计划
   - 保持练习的连续性
   - 及时记录和总结
   - 参与社区讨论和分享

3. **团队协作**
   - 严格遵循项目规范
   - 保持良好的沟通习惯
   - 注重知识的沉淀和共享
   - 定期进行团队代码评审

</details>

## 💻 安装指南

快速开始：
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
   # 创建并激活虚拟环境
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **安装 CursorMind**
   ```powershell
   pip install --upgrade pip
   pip install cursormind
   $env:PYTHONPATH = "src"
   ```

### macOS/Linux 安装步骤

1. **创建虚拟环境**
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```

2. **安装 CursorMind**
   ```bash
   pip install --upgrade pip
   pip install cursormind
   export PYTHONPATH=src
   ```

### 验证安装

运行以下命令确认安装成功：
```bash
cursormind --version
cursormind review file your_code.py
```

如果遇到问题，请参考下方的故障排除指南。
</details>

### ❗ 常见问题

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

### 📢 宣言

我们坚信：
- 技术应该是平等的，每个人都应该有机会学习和使用AI编程
- Cursor不仅是一个IDE，更是一个让编程变得更简单、更智能的工具
- 通过CursorMind，我们致力于让每个开发者都能享受到AI辅助编程的便利
- 开源精神是技术进步的基石，欢迎大家fork项目，共同建设AI编程生态

### 🤝 参与贡献

我们热烈欢迎社区的每一位成员参与到CursorMind的开发中来：
- 🌟 如果您觉得这个项目有帮助，请给我们一个star
- 🐛 发现bug？请提交 [Issues](https://github.com/yourusername/cursormind/issues)
- 💡 有新想法？欢迎提交 [Pull Requests](https://github.com/yourusername/cursormind/pulls)
- 📝 帮助改进文档？这对初学者来说非常重要
- 💬 分享您的使用经验和建议

让我们一起打造更好的AI编程工具！

### 📜 MIT 开源许可

CursorMind 采用 MIT 许可证开源，这意味着：
- ✅ 您可以自由使用、修改和分发本软件
- ✅ 您可以将其用于商业项目
- ✅ 您可以创建和分发闭源版本
- ℹ️ 唯一的要求是包含原始版权声明和许可证

我们鼓励个人和组织：
- 🔄 根据特定需求分支（Fork）和修改项目
- 🌱 将改进分享回社区
- 🤝 共同推进 AI 辅助开发的普及

完整许可证详情，请查看 [LICENSE](LICENSE) 文件。

---
*最后更新：2025-03-12 02:37:42 PDT*
