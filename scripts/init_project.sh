#!/bin/bash

# CursorMind 项目初始化脚本
# 用法: ./init_project.sh "项目名称"

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查参数
if [ $# -lt 1 ]; then
    echo -e "${RED}错误: 缺少项目名称参数${NC}"
    echo -e "用法: $0 \"项目名称\""
    exit 1
fi

PROJECT_NAME="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 获取太平洋时间戳
# 尝试使用Python时间戳脚本，如果失败则使用简单时间戳脚本
CURRENT_DATE=$("$SCRIPT_DIR/timestamp.sh" date 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" date)
FULL_TIMESTAMP=$("$SCRIPT_DIR/timestamp.sh" full 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" full)

# 检查是否使用了简单时间戳脚本
if ! "$SCRIPT_DIR/timestamp.sh" full &>/dev/null; then
    echo -e "${YELLOW}警告: 使用本地时间而非太平洋时间${NC}"
    echo -e "${YELLOW}如需使用太平洋时间，请确保已安装Python 3.6+和pytz库${NC}"
fi

echo -e "${BLUE}=== 初始化项目: $PROJECT_NAME ===${NC}"
echo -e "${BLUE}=== 时间戳: $FULL_TIMESTAMP ===${NC}"

# 更新 PROJECT_PROGRESS.md
echo -e "${YELLOW}更新项目进度文件...${NC}"
sed -i '' "s/\[项目名称\]/$PROJECT_NAME/g" "$PROJECT_ROOT/PROJECT_PROGRESS.md"
sed -i '' "s/\[YYYY-MM-DD\]/$CURRENT_DATE/g" "$PROJECT_ROOT/PROJECT_PROGRESS.md"
sed -i '' "s/最后更新: YYYY-MM-DD/最后更新: $FULL_TIMESTAMP/g" "$PROJECT_ROOT/PROJECT_PROGRESS.md"

# 更新 MAIN_CONTROL.md
echo -e "${YELLOW}更新中央控制文档...${NC}"
sed -i '' "s/\[项目名称\]/$PROJECT_NAME/g" "$PROJECT_ROOT/project_management/control/MAIN_CONTROL.md"
sed -i '' "s/\[YYYY-MM-DD\]/$CURRENT_DATE/g" "$PROJECT_ROOT/project_management/control/MAIN_CONTROL.md"
sed -i '' "s/- \*\*最后更新\*\*: \[YYYY-MM-DD\]/- **最后更新**: $FULL_TIMESTAMP/g" "$PROJECT_ROOT/project_management/control/MAIN_CONTROL.md"

# 更新 REQUIREMENTS.md
echo -e "${YELLOW}更新需求文档...${NC}"
sed -i '' "s/\[项目名称\]/$PROJECT_NAME/g" "$PROJECT_ROOT/project_management/control/REQUIREMENTS.md"
sed -i '' "s/\[YYYY-MM-DD\]/$CURRENT_DATE/g" "$PROJECT_ROOT/project_management/control/REQUIREMENTS.md"
sed -i '' "s/- \*\*最后更新\*\*: \[YYYY-MM-DD\]/- **最后更新**: $FULL_TIMESTAMP/g" "$PROJECT_ROOT/project_management/control/REQUIREMENTS.md"

# 创建初始日报
echo -e "${YELLOW}创建今日日报...${NC}"
"$SCRIPT_DIR/create_report.sh" daily

# 创建初始周报
echo -e "${YELLOW}创建本周周报...${NC}"
"$SCRIPT_DIR/create_report.sh" weekly

# 设置脚本权限
echo -e "${YELLOW}设置脚本执行权限...${NC}"
chmod +x "$SCRIPT_DIR"/*.sh
chmod +x "$SCRIPT_DIR"/*.py

echo -e "${GREEN}=== 项目初始化完成! ===${NC}"
echo -e "项目名称: ${BLUE}$PROJECT_NAME${NC}"
echo -e "初始化时间: ${BLUE}$FULL_TIMESTAMP${NC}"
echo -e "\n${YELLOW}接下来您可以:${NC}"
echo -e "1. 查看和编辑 ${BLUE}PROJECT_PROGRESS.md${NC} 文件"
echo -e "2. 查看和编辑 ${BLUE}project_management/control/MAIN_CONTROL.md${NC} 文件"
echo -e "3. 查看今日创建的日报和周报"
echo -e "\n${GREEN}祝您项目顺利!${NC}" 