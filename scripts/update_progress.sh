#!/bin/bash

# CursorMind 项目进度更新脚本
# 用法: ./update_progress.sh <进度百分比> ["更新内容"]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查参数
if [ $# -lt 1 ]; then
    echo -e "${RED}错误: 缺少进度百分比参数${NC}"
    echo -e "用法: $0 <进度百分比> [\"更新内容\"]"
    exit 1
fi

PROGRESS="$1"
UPDATE_CONTENT="${2:-项目进度更新}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PROGRESS_FILE="$PROJECT_ROOT/PROJECT_PROGRESS.md"
MAIN_CONTROL_FILE="$PROJECT_ROOT/project_management/control/MAIN_CONTROL.md"

# 获取太平洋时间戳
# 尝试使用Python时间戳脚本，如果失败则使用简单时间戳脚本
CURRENT_DATE=$("$SCRIPT_DIR/timestamp.sh" date 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" date)
FULL_TIMESTAMP=$("$SCRIPT_DIR/timestamp.sh" full 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" full)

# 检查是否使用了简单时间戳脚本
if ! "$SCRIPT_DIR/timestamp.sh" full &>/dev/null; then
    echo -e "${YELLOW}警告: 使用本地时间而非太平洋时间${NC}"
    echo -e "${YELLOW}如需使用太平洋时间，请确保已安装Python 3.6+和pytz库${NC}"
fi

# 验证进度百分比
if ! [[ "$PROGRESS" =~ ^[0-9]+$ ]] || [ "$PROGRESS" -lt 0 ] || [ "$PROGRESS" -gt 100 ]; then
    echo -e "${RED}错误: 进度百分比必须是0-100之间的整数${NC}"
    exit 1
fi

echo -e "${BLUE}=== 更新项目进度: $PROGRESS% ===${NC}"
echo -e "${BLUE}=== 时间戳: $FULL_TIMESTAMP ===${NC}"

# 获取当前用户
CURRENT_USER=$(whoami)

# 更新 PROJECT_PROGRESS.md
echo -e "${YELLOW}更新项目进度文件...${NC}"

# 更新当前进度
sed -i '' "s/- \*\*当前进度\*\*: \[[0-9]*-[0-9]*\]%/- **当前进度**: $PROGRESS%/g" "$PROGRESS_FILE"
sed -i '' "s/- \*\*当前进度\*\*: [0-9]*%/- **当前进度**: $PROGRESS%/g" "$PROGRESS_FILE"

# 更新最后更新时间
sed -i '' "s/最后更新: .*$/最后更新: $FULL_TIMESTAMP/g" "$PROGRESS_FILE"

# 添加进度更新历史
# 查找进度更新历史表格的结束位置
TABLE_END=$(grep -n "## 风险与问题" "$PROGRESS_FILE" | cut -d ":" -f 1)
TABLE_START=$(grep -n "## 进度更新历史" "$PROGRESS_FILE" | cut -d ":" -f 1)
TABLE_START=$((TABLE_START + 2)) # 跳过表头和分隔行

# 在表格开头插入新行
NEW_LINE="| $CURRENT_DATE | $PROGRESS% | $UPDATE_CONTENT | $CURRENT_USER |"
sed -i '' "${TABLE_START}a\\
$NEW_LINE" "$PROGRESS_FILE"

# 更新 MAIN_CONTROL.md
echo -e "${YELLOW}更新中央控制文档...${NC}"
sed -i '' "s/- \*\*进度\*\*: \[[0-9]*-[0-9]*\]%/- **进度**: $PROGRESS%/g" "$MAIN_CONTROL_FILE"
sed -i '' "s/- \*\*进度\*\*: [0-9]*%/- **进度**: $PROGRESS%/g" "$MAIN_CONTROL_FILE"
sed -i '' "s/- \*\*最后更新\*\*: .*$/- **最后更新**: $FULL_TIMESTAMP/g" "$MAIN_CONTROL_FILE"

# 添加变更记录
# 查找关键决策记录表格的开始位置
DECISION_TABLE_START=$(grep -n "## 关键决策记录" "$MAIN_CONTROL_FILE" | cut -d ":" -f 1)
DECISION_TABLE_START=$((DECISION_TABLE_START + 2)) # 跳过表头和分隔行

# 生成新的决策ID
LAST_DECISION_ID=$(grep -A 1 "## 关键决策记录" "$MAIN_CONTROL_FILE" | grep "D[0-9]\{3\}" | sort | tail -n 1 | awk '{print $1}' | sed 's/|//g')
if [ -z "$LAST_DECISION_ID" ]; then
    NEW_DECISION_ID="D001"
else
    LAST_NUM=${LAST_DECISION_ID:1}
    NEW_NUM=$((10#$LAST_NUM + 1))
    NEW_DECISION_ID="D$(printf "%03d" $NEW_NUM)"
fi

# 在表格开头插入新行
DECISION_LINE="| $NEW_DECISION_ID | $CURRENT_DATE | 进度更新至 $PROGRESS% | 项目进度变更 | $CURRENT_USER |"
sed -i '' "${DECISION_TABLE_START}a\\
$DECISION_LINE" "$MAIN_CONTROL_FILE"

echo -e "${GREEN}=== 项目进度已更新! ===${NC}"
echo -e "当前进度: ${BLUE}$PROGRESS%${NC}"
echo -e "更新内容: ${BLUE}$UPDATE_CONTENT${NC}"
echo -e "更新时间: ${BLUE}$FULL_TIMESTAMP${NC}"
echo -e "更新人: ${BLUE}$CURRENT_USER${NC}" 