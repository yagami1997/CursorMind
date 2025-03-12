# CursorMind 快速入门指南

## 简介
CursorMind (Beta 0.1.1) 是一个专为Cursor开发者设计的轻量级项目管理框架，帮助您在使用AI辅助编程的同时，培养良好的软件工程实践。

## 快速开始（5分钟上手）

### 1. 初始化项目
```bash
# 克隆项目
git clone [your-repo-url]
cd your-project

# 初始化项目结构
./project_management/scripts/init_project.sh "我的新项目"
```

### 2. 日常工作流程

#### 创建并更新日报
```bash
# 创建今日工作报告
./project_management/scripts/create_daily_report.sh

# 示例：更新今日工作内容
vim project_management/actuals/reports/daily/daily_report_20250311.md

# 更新项目进度（例：完成35%并添加说明）
./project_management/scripts/update_progress.sh 35 "完成用户认证模块开发"
```

#### 生成周报
```bash
# 在每周结束时生成周报
./project_management/scripts/create_weekly_report.sh

# 系统会自动汇总本周的日报内容
```

#### 创建新任务
```bash
# 创建新任务
./project_management/scripts/create_task.sh "实现用户登录功能"

# 更新任务状态
./project_management/scripts/update_task.sh TASK-001 "进行中"
```

### 3. 项目管理最佳实践
- 每日更新工作日报，记录具体进展
  ```markdown
  ## 今日工作内容
  1. 完成用户认证模块
     - 实现JWT认证
     - 添加密码加密
  ```
- 及时更新项目进度文件
  ```markdown
  ## 项目进度
  - 版本: Beta 0.1.1
  - 进度: 35%
  - 说明: 完成核心功能开发
  ```
- 使用标准命令管理工作流
  ```bash
  # 当遇到问题需要重新规划时
  [RESET] ./project_management/scripts/reset_task.sh TASK-001
  
  # 当需要快速开始执行时
  [CODE NOW] ./project_management/scripts/start_task.sh TASK-001
  ```

## 项目结构
```
project_management/
├── control/          # 项目控制文档
│   └── MAIN_CONTROL.md  # 项目主控制文件
├── templates/        # 文档模板
│   ├── daily_report_template.md
│   ├── weekly_report_template.md
│   └── task_template.md
├── actuals/         # 实际文档
│   └── reports/     # 报告目录
│       ├── daily/   # 日报
│       └── weekly/  # 周报
└── scripts/         # 工具脚本
    ├── init_project.sh
    ├── create_daily_report.sh
    └── update_progress.sh
```

## 常见命令
- `create_daily_report.sh`: 创建今日工作报告
  ```bash
  # 示例：创建带有特定说明的日报
  ./project_management/scripts/create_daily_report.sh "重要版本发布"
  ```
- `create_weekly_report.sh`: 生成本周工作报告
  ```bash
  # 示例：生成指定周的报告
  ./project_management/scripts/create_weekly_report.sh 2025W11
  ```
- `update_progress.sh`: 更新项目进度
  ```bash
  # 示例：更新进度并添加里程碑
  ./project_management/scripts/update_progress.sh 50 "完成MVP版本"
  ```

## 注意事项
1. 所有时间戳使用PST时区
   ```markdown
   ## 时间
   2025-03-11 20:02:41 PST
   ```
2. 文档命名遵循规范
   ```
   daily_report_20250311.md
   weekly_report_2025W11.md
   TASK-001_user_auth.md
   ```
3. 确保Git忽略了正确的文件
   ```gitignore
   # .gitignore示例
   .DS_Store
   node_modules/
   .env
   ```

## 常见问题

Q: 如何修改默认时区？
A: 编辑project_management/scripts/config.sh：
```bash
# 修改时区设置
TIMEZONE="America/Los_Angeles"  # PST时区
```

Q: 报告格式是否可以自定义？
A: 可以修改templates/目录下的对应模板：
```markdown
# 自定义日报模板示例
## 时间
[TIMESTAMP]

## 自定义字段
[YOUR_CONTENT]
```

Q: 如何处理任务依赖关系？
A: 在任务模板中明确标注：
```markdown
## 依赖关系
- 前置任务: TASK-001, TASK-002
- 后续任务: TASK-004
```

## 获取帮助
如有问题，请参考：
1. 项目文档（docs/）
2. 示例项目（examples/）
3. 提交Issue获取支持

## 命令速查表
| 命令 | 说明 | 示例 |
|-----|------|-----|
| init_project.sh | 初始化项目 | ./scripts/init_project.sh "项目名" |
| create_daily_report.sh | 创建日报 | ./scripts/create_daily_report.sh |
| update_progress.sh | 更新进度 | ./scripts/update_progress.sh 35 "说明" |
| create_task.sh | 创建任务 | ./scripts/create_task.sh "任务名" |

---
*最后更新: 2025-03-11 20:02:41 PST* 