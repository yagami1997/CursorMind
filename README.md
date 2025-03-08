# CursorMind - Cursor开发行为规范与文档智能助手 (Beta 0.1)

<div align="center">
  <img src="https://via.placeholder.com/150?text=CursorMind" alt="CursorMind Logo" width="150" height="150">
  <p><em>提升您的Cursor开发效率与项目管理质量</em></p>
  <p><strong>当前版本：Beta 0.1</strong></p>
</div>

## 📖 项目简介

CursorMind (Beta 0.1) 是一个专为Cursor开发者设计的项目管理框架，提供开发行为规范指导和文档管理智能支持，帮助开发者提升项目质量和效率。通过标准化的模板、自动化的工具和结构化的工作流程，CursorMind使项目管理变得简单而高效。

### 核心功能

- **标准化文档模板** - 提供日报、周报、任务、决策和风险评估等标准模板
- **自动化工具脚本** - 简化项目初始化、报告创建和进度更新等常见任务
- **太平洋时间戳** - 确保所有文档使用统一的时间标准
- **开发行为规范** - 通过特定命令优化开发工作流程
- **项目进度追踪** - 实时监控和记录项目进展情况

## 🚀 快速入门

### 前提条件

- Git
- Bash或兼容的Shell环境
- Python 3.6+（用于高级功能，但基本功能不依赖）

### 安装步骤

1. **克隆项目仓库**
   ```bash
   git clone https://github.com/yourusername/CursorMind.git
   cd CursorMind
   ```

2. **设置脚本权限**
   ```bash
   chmod +x scripts/*.sh
   chmod +x scripts/*.py
   ```

3. **初始化项目**
   ```bash
   ./scripts/init_project.sh "您的项目名称"
   ```
   这将自动创建初始的日报和周报，并更新项目文件中的名称和时间戳。

### 基本使用

#### 创建日报和周报

```bash
# 创建今日日报
./scripts/create_report.sh daily

# 创建本周周报
./scripts/create_report.sh weekly
```

#### 更新项目进度

```bash
# 更新项目进度为75%，并添加说明
./scripts/update_progress.sh 75 "完成了核心功能开发"
```

#### 获取时间戳

```bash
# 获取完整格式的太平洋时间戳
./scripts/timestamp.sh full

# 获取仅日期格式的时间戳
./scripts/timestamp.sh date
```

## 📂 目录结构详解

```
CursorMind/
├── README.md                           # 项目介绍和使用指南
├── PROJECT_PROGRESS.md                 # 项目进度跟踪文档
├── project_management/                 # 核心项目管理结构
│   ├── control/                        # 控制文档目录
│   │   ├── MAIN_CONTROL.md             # 中央控制文档
│   │   └── REQUIREMENTS.md             # 需求管理文档
│   ├── templates/                      # 模板文件目录
│   │   ├── daily_report_template.md    # 日报模板
│   │   ├── weekly_report_template.md   # 周报模板
│   │   ├── task_template.md            # 任务定义模板
│   │   ├── decision_template.md        # 决策记录模板
│   │   └── risk_template.md            # 风险评估模板
│   └── actuals/                        # 实际文档目录
│       ├── reports/                    # 报告文档目录
│       │   ├── daily/                  # 日报存放目录
│       │   └── weekly/                 # 周报存放目录
│       └── decisions/                  # 决策记录存放目录
└── scripts/                            # 辅助脚本目录
    ├── init_project.sh                 # 项目初始化脚本
    ├── create_report.sh                # 报告创建脚本
    ├── update_progress.sh              # 项目进度更新脚本
    ├── timestamp.sh                    # 时间戳生成脚本(太平洋时间)
    ├── simple_timestamp.sh             # 简单时间戳脚本(本地时间)
    └── generate_timestamp.py           # 时间戳生成Python脚本
```

## 📝 详细使用指南

### 项目初始化

项目初始化是使用CursorMind的第一步。初始化过程会：
- 更新项目名称
- 设置时间戳
- 创建初始日报和周报
- 准备项目进度文档

```bash
./scripts/init_project.sh "我的项目名称"
```

### 日报和周报管理

日报和周报是项目管理的重要组成部分，帮助团队成员了解项目进展和问题。

#### 日报内容

日报包含以下关键信息：
- 今日完成工作
- 工作进度
- 遇到的问题
- 明日计划
- 风险预警

```bash
# 创建今日日报
./scripts/create_report.sh daily
```

#### 周报内容

周报提供更全面的项目视图，包含：
- 本周工作总结
- 项目进度
- 关键指标
- 主要问题与解决方案
- 重要决策
- 下周计划
- 风险预警
- 团队成员工作量

```bash
# 创建本周周报
./scripts/create_report.sh weekly
```

### 项目进度更新

定期更新项目进度是保持项目透明度的关键。进度更新会：
- 更新PROJECT_PROGRESS.md中的进度百分比
- 添加进度更新历史记录
- 更新中央控制文档中的进度信息
- 添加决策记录

```bash
# 更新进度为50%
./scripts/update_progress.sh 50 "完成了一半的功能开发"

# 更新进度为100%
./scripts/update_progress.sh 100 "项目已完成"
```

### 时间戳功能

CursorMind使用美国太平洋时间（PST/PDT）作为标准时间戳，确保团队成员在不同时区也能保持时间一致性。

#### 时间戳格式

支持多种格式的时间戳：

```bash
# 完整格式: YYYY-MM-DD HH:MM:SS PST/PDT
./scripts/timestamp.sh full

# 仅日期: YYYY-MM-DD
./scripts/timestamp.sh date

# 日期和时间: YYYY-MM-DD HH:MM:SS
./scripts/timestamp.sh datetime

# 紧凑格式: YYYYMMDD
./scripts/timestamp.sh compact

# 年份和周数: YYYYWNN
./scripts/timestamp.sh week
```

#### 本地时间回退

如果遇到Python依赖问题，可以使用本地时间作为回退：

```bash
./scripts/simple_timestamp.sh full
```

### Cursor开发行为规范

CursorMind提供了一套开发行为规范，通过特定命令优化工作流程：

- **[CODE NOW]** - 当分析过多时，使用此命令立即开始编码
- **[FOCUS]** - 限制上下文到指定范围，防止分心
- **[RESET]** - 遇到循环思维时，使用此命令重新开始
- **[DECISION]** - 做出决策并前进，避免犹豫不决

在文档和代码注释中使用这些命令，可以提醒自己和团队成员保持高效的工作状态。

## 🔧 高级配置

### 自定义时区

如果需要使用其他时区而非太平洋时间，可以修改`scripts/generate_timestamp.py`文件：

```python
# 将 'America/Los_Angeles' 替换为您需要的时区
pacific_tz = pytz.timezone('您的时区')
```

常用时区包括：
- 'Asia/Shanghai' - 中国标准时间
- 'Asia/Tokyo' - 日本标准时间
- 'Europe/London' - 英国标准时间
- 'Europe/Paris' - 中欧标准时间
- 'America/New_York' - 美国东部时间

### 自定义模板

您可以根据需要修改`project_management/templates/`目录下的模板文件，添加或删除内容。

## 📊 最佳实践

为了充分利用CursorMind，建议遵循以下最佳实践：

1. **每日更新** - 每天结束工作前更新日报，记录进展和问题
2. **周末回顾** - 每周末生成周报，回顾一周工作并规划下周
3. **及时决策** - 重要决策应立即记录，包括原因和影响
4. **进度透明** - 定期更新项目进度，保持透明度
5. **风险前置** - 提前识别和记录风险，制定缓解措施
6. **命令意识** - 合理使用Cursor命令，优化工作流程

## 🤝 贡献指南

我们欢迎并感谢任何形式的贡献！以下是参与项目的方式：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 开启一个Pull Request

## 📄 许可证

本项目采用MIT许可证 - 详情请参见[LICENSE](LICENSE)文件

## 📝 版本历史

- **Beta 0.1** (2025-03-07) - 初始版本
  - 基础项目结构
  - 核心模板文件
  - 时间戳功能
  - 自动化脚本

## 📞 联系方式

如有问题或建议，请通过以下方式联系我们：

- 项目维护者: [您的名字](mailto:your.email@example.com)
- 项目仓库: [https://github.com/yourusername/CursorMind](https://github.com/yourusername/CursorMind)

---

*最后更新: 2025-03-07 20:02:41 PST* 