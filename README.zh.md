# ✨ CursorMind

<p align="right">
  <a href="README.md">English Version</a> |
  <a href="README.zh.md">中文版</a>
</p>

<div align="center">
  <h1>CursorMind</h1>
  <h3>提升您的 Cursor 开发效率与项目管理质量</h3>
  <p><strong>当前版本：Beta 0.1</strong></p>
  
  ![许可证](https://img.shields.io/badge/许可证-MIT-blue.svg)
  ![版本](https://img.shields.io/badge/版本-Beta%200.1-brightgreen.svg)
  ![状态](https://img.shields.io/badge/状态-开发中-orange.svg)
  ![语言](https://img.shields.io/badge/语言-Bash%20|%20Python-yellow.svg)
</div>

## 📖 项目简介

**CursorMind** 是一个专为 Cursor 开发者设计的项目管理框架，通过结构化的工作流程、标准化的文档管理和优化的行为规范，帮助开发团队提升项目质量和开发效率。

### 💡 核心功能

- **开发行为规范** - 特定命令优化工作流程，防止分析瘫痪和循环思维
- **标准化文档模板** - 提供日报、周报、任务定义、决策记录等专业模板
- **自动化工具脚本** - 简化项目初始化、报告创建和进度更新等常见任务
- **太平洋时间戳** - 确保全球团队成员使用统一的时间标准
- **项目进度追踪** - 实时监控和记录项目进展，提高项目透明度

### 🛠️ 设计理念

CursorMind 基于以下核心理念设计：

- **专注生产力** - 减少决策疲劳，优化开发思维方式
- **结构化方法** - 提供清晰的项目结构和工作流程
- **自动化优先** - 通过脚本自动化简化重复性任务
- **透明度** - 通过标准化报告提高团队协作与沟通效率

## 🚀 快速入门

### 前提条件

- Git
- Bash 或兼容的 Shell 环境
- Python 3.6+ (用于高级功能，基本功能不依赖)

### 💻 安装步骤

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
   此命令会自动创建初始的日报和周报，并更新项目文件中的名称和时间戳。

## 💼 基本使用

### 📊 项目初始化

项目初始化是使用 CursorMind 的第一步，它会：
- 更新所有文件中的项目名称
- 设置统一的时间戳
- 创建初始日报和周报
- 准备项目进度文档

```bash
./scripts/init_project.sh "我的项目名称"
```

### 📝 报告管理

#### 创建日报和周报

```bash
# 创建今日日报
./scripts/create_report.sh daily

# 创建本周周报
./scripts/create_report.sh weekly
```

#### 日报内容结构

日报包含以下关键信息：
- 今日完成工作
- 工作进度对比
- 遇到的问题与解决方案
- 明日计划
- 风险预警

#### 周报内容结构

周报提供更全面的项目视图，包含：
- 本周工作总结
- 项目进度状态
- 关键指标监控
- 主要问题与解决方案
- 重要决策记录
- 下周工作计划
- 风险预警机制
- 团队成员工作量统计

### 📈 项目进度更新

```bash
# 更新进度为50%并添加说明
./scripts/update_progress.sh 50 "完成了核心功能开发"

# 更新进度为100%并标记项目完成
./scripts/update_progress.sh 100 "项目已完成所有功能开发"
```

进度更新会：
- 更新 PROJECT_PROGRESS.md 中的进度百分比
- 添加详细的进度更新历史记录
- 更新中央控制文档中的进度信息
- 创建决策记录用于追踪重要变更

### ⏰ 时间戳功能

```bash
# 完整格式: YYYY-MM-DD HH:MM:SS PST/PDT
./scripts/timestamp.sh full

# 仅日期: YYYY-MM-DD
./scripts/timestamp.sh date

# 紧凑格式: YYYYMMDD
./scripts/timestamp.sh compact
```

## 📂 项目结构

```
CursorMind/
├── README.md                           # 项目介绍和使用指南
├── PROJECT_PROGRESS.md                 # 项目进度跟踪文档
├── project_management/                 # 项目管理核心目录
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

## ⚡ Cursor 开发行为规范

CursorMind 提供了一套开发行为规范，通过特定命令优化工作流程：

### 核心命令

| 命令 | 用途 | 使用场景 |
|------|------|---------|
| **[CODE NOW]** | 立即停止分析并开始编码 | 当分析超过总时间的20%，无实质性产出时 |
| **[FOCUS]** | 限制上下文到指定范围 | 当被过多信息干扰，导致注意力分散时 |
| **[RESET]** | 抛弃当前方法，重新开始 | 遇到循环思维或无法突破的死胡同时 |
| **[DECISION]** | 确定选择并前进，避免犹豫 | 在多个可行方案中难以抉择时 |

### 代码生成规则

- 始终产出完整可运行的代码，避免占位符
- 保持80%代码对20%解释的比例
- 包含全面的错误处理机制
- 确保代码优化并遵循最佳实践

### 任务格式规范

- 定义清晰、可衡量的交付物和具体的成功标准
- 为每个任务设定明确的时间限制
- 设定明确的上下文边界，防止范围扩大
- 提供顺序、可操作的实施步骤
- 包含验证方法，确认成功完成

## 🚀 最佳实践

为了充分利用 CursorMind，建议遵循以下最佳实践：

1. **每日更新** - 每天结束工作前更新日报，记录进展和问题
2. **周末回顾** - 每周末生成周报，回顾一周工作并规划下周
3. **及时决策** - 重要决策应立即记录，包括原因和影响
4. **进度透明** - 定期更新项目进度，保持项目透明度
5. **风险前置** - 提前识别和记录风险，制定缓解措施
6. **命令意识** - 合理使用 Cursor 命令，优化开发工作流程

## 🔧 高级配置

### 自定义时区

如果需要使用其他时区而非太平洋时间，可以修改 `scripts/generate_timestamp.py` 文件：

```python
# 将 'America/Los_Angeles' 替换为您需要的时区
pacific_tz = pytz.timezone('您的时区')
```

常用时区包括：
- `Asia/Shanghai` - 中国标准时间
- `Asia/Tokyo` - 日本标准时间
- `Europe/London` - 英国标准时间
- `Europe/Paris` - 中欧标准时间
- `America/New_York` - 美国东部时间

### 自定义模板

您可以根据项目需求修改 `project_management/templates/` 目录下的模板文件：

1. 编辑模板文件添加或修改字段
2. 确保替换标记使用 `{{PLACEHOLDER}}` 格式
3. 更新相应的脚本以处理新的占位符

## 🤝 贡献指南

我们欢迎并感谢任何形式的贡献！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 详情请参见 [LICENSE](LICENSE) 文件

## 📝 版本历史

- **Beta 0.1** (2025-03-07)
  - 初始项目结构和核心功能
  - 基础模板文件系统
  - 时间戳功能（太平洋时间）
  - 自动化项目管理脚本

## 📞 联系方式

- **项目维护者**: <a href="https://github.com/yagami1997" target="_blank">Yagami</a>
- **项目仓库**: [https://github.com/yagami1997/CursorMind](https://github.com/yagami1997/CursorMind)

---

<div align="center">
  <p><strong>CursorMind</strong> - 提升开发效率，规范项目管理</p>
  <p><i>最后更新: 2025-03-08 PST</i></p>
  <hr>
</div>
