# CursorMind - Cursor开发行为规范与文档智能助手

CursorMind是一个专为Cursor开发者设计的项目管理框架，提供开发行为规范指导和文档管理智能支持，帮助开发者提升项目质量和效率。

## 快速入门

1. **克隆项目**
   ```bash
   git clone https://github.com/yourusername/CursorMind.git
   cd CursorMind
   ```

2. **初始化项目**
   ```bash
   ./scripts/init_project.sh "您的项目名称"
   ```

3. **创建日报/周报**
   ```bash
   ./scripts/create_report.sh daily  # 创建今日日报
   ./scripts/create_report.sh weekly # 创建本周周报
   ```

## 目录结构

```
CursorMind/
├── README.md                           # 项目介绍和快速入门指南
├── PROJECT_PROGRESS.md                 # 项目进度跟踪模板
├── project_management/                 # 核心项目管理结构
│   ├── control/                        
│   │   ├── MAIN_CONTROL.md             # 中央控制文档模板
│   │   └── REQUIREMENTS.md             # 需求管理文档模板
│   ├── templates/                      
│   │   ├── daily_report_template.md    # 日报模板
│   │   ├── weekly_report_template.md   # 周报模板
│   │   ├── task_template.md            # 任务定义模板
│   │   ├── decision_template.md        # 决策记录模板
│   │   └── risk_template.md            # 风险评估模板
│   └── actuals/                        
│       ├── reports/
│       │   ├── daily/                  # 日报存放目录
│       │   └── weekly/                 # 周报存放目录
│       └── decisions/                  # 决策记录存放目录
└── scripts/                            # 辅助脚本
    ├── init_project.sh                 # 项目初始化脚本
    ├── create_report.sh                # 报告创建脚本
    ├── update_progress.sh              # 项目进度更新脚本
    ├── timestamp.sh                    # 时间戳生成脚本(太平洋时间)
    ├── simple_timestamp.sh             # 简单时间戳脚本(本地时间)
    └── generate_timestamp.py           # 时间戳生成Python脚本
```

## 使用提示

### 常用命令

- **更新项目进度**：
  ```bash
  ./scripts/update_progress.sh 75 "完成了核心功能开发"
  ```

- **记录决策**：
  ```bash
  # 创建新的决策记录
  cp project_management/templates/decision_template.md project_management/actuals/decisions/decision_$(date +%Y%m%d)_选择技术栈.md
  ```

### 时间戳说明

CursorMind使用美国太平洋时间（PST/PDT）作为标准时间戳，格式为：`YYYY-MM-DD HH:MM:SS PST/PDT`。

- 所有文档和报告自动包含时间戳
- 时间戳会在创建和更新文档时自动生成
- 时间戳格式可以通过以下方式获取：
  ```bash
  ./scripts/timestamp.sh [format_type]
  ```
  支持的格式类型：
  - `full`: 完整格式 (YYYY-MM-DD HH:MM:SS PST/PDT)
  - `date`: 仅日期 (YYYY-MM-DD)
  - `datetime`: 日期和时间 (YYYY-MM-DD HH:MM:SS)
  - `compact`: 紧凑格式 (YYYYMMDD)
  - `week`: 年份和周数 (YYYYWNN)

如果遇到Python依赖问题，可以使用简单时间戳脚本（使用本地时间）：
```bash
./scripts/simple_timestamp.sh [format_type]
```

如需修改时间戳时区，请编辑 `scripts/generate_timestamp.py` 文件中的时区设置。

### Cursor命令

在开发过程中，您可以使用以下命令来优化工作流程：

- `[CODE NOW]` - 立即停止分析并开始编写代码
- `[FOCUS]` - 限制上下文到指定范围，防止分心
- `[RESET]` - 放弃当前方法，以全新视角重新开始
- `[DECISION]` - 确定选择并前进，不再犹豫

### 最佳实践

- 每日更新日报，记录进展和遇到的问题
- 每周生成周报，回顾进度并规划下周工作
- 使用中央控制文档管理项目全局状态
- 重要决策应记录在决策文档中，包括原因和影响

## 依赖项

- Python 3.6+ (用于太平洋时间戳功能)
- pytz 库 (用于时区处理)

如果缺少依赖项，脚本会尝试自动创建虚拟环境并安装依赖。如果仍然失败，会回退到使用系统时间。

## 贡献

欢迎提交问题和改进建议！请先查看现有问题，确保不重复提交。 