#!/bin/bash

# CursorMind 报告创建脚本
# 用法: ./create_report.sh [daily|weekly]

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 检查参数
if [ $# -lt 1 ]; then
    echo -e "${RED}错误: 缺少报告类型参数${NC}"
    echo -e "用法: $0 [daily|weekly]"
    exit 1
fi

REPORT_TYPE="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# 获取太平洋时间戳
# 尝试使用Python时间戳脚本，如果失败则使用简单时间戳脚本
CURRENT_DATE=$("$SCRIPT_DIR/timestamp.sh" date 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" date)
FULL_TIMESTAMP=$("$SCRIPT_DIR/timestamp.sh" full 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" full)
COMPACT_DATE=$("$SCRIPT_DIR/timestamp.sh" compact 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" compact)
WEEK_NUMBER=$("$SCRIPT_DIR/timestamp.sh" week 2>/dev/null || "$SCRIPT_DIR/simple_timestamp.sh" week)

# 检查是否使用了简单时间戳脚本
if ! "$SCRIPT_DIR/timestamp.sh" full &>/dev/null; then
    echo -e "${YELLOW}警告: 使用本地时间而非太平洋时间${NC}"
    echo -e "${YELLOW}如需使用太平洋时间，请确保已安装Python 3.6+和pytz库${NC}"
fi

# 获取项目名称
PROJECT_NAME=$(grep "项目名称" "$PROJECT_ROOT/PROJECT_PROGRESS.md" | head -n 1 | cut -d ":" -f 2 | sed 's/^ *//' | sed 's/ *$//')
if [ -z "$PROJECT_NAME" ] || [ "$PROJECT_NAME" = "[项目名称]" ]; then
    PROJECT_NAME="未命名项目"
fi

# 创建日报
create_daily_report() {
    REPORT_FILE="$PROJECT_ROOT/project_management/actuals/reports/daily/daily_report_$COMPACT_DATE.md"
    TEMPLATE_FILE="$PROJECT_ROOT/project_management/templates/daily_report_template.md"
    
    echo -e "${BLUE}=== 创建日报: $COMPACT_DATE ===${NC}"
    echo -e "${BLUE}=== 时间戳: $FULL_TIMESTAMP ===${NC}"
    
    # 检查是否已存在
    if [ -f "$REPORT_FILE" ]; then
        echo -e "${YELLOW}警告: 今日日报已存在${NC}"
        read -p "是否覆盖? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${RED}已取消${NC}"
            return
        fi
    fi
    
    # 复制模板并替换占位符
    cp "$TEMPLATE_FILE" "$REPORT_FILE"
    sed -i '' "s/{{DATE}}/$CURRENT_DATE/g" "$REPORT_FILE"
    sed -i '' "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$REPORT_FILE"
    sed -i '' "s/{{AUTHOR}}/$(whoami)/g" "$REPORT_FILE"
    sed -i '' "s/{{TIMESTAMP}}/$FULL_TIMESTAMP/g" "$REPORT_FILE"
    
    echo -e "${GREEN}日报已创建: $REPORT_FILE${NC}"
}

# 创建周报
create_weekly_report() {
    # 使用太平洋时间的年份和周数
    YEAR_WEEK=$WEEK_NUMBER
    REPORT_FILE="$PROJECT_ROOT/project_management/actuals/reports/weekly/weekly_report_$YEAR_WEEK.md"
    TEMPLATE_FILE="$PROJECT_ROOT/project_management/templates/weekly_report_template.md"
    
    # 计算本周的开始和结束日期
    # 尝试使用Python脚本，如果失败则使用简单方法
    if "$SCRIPT_DIR/timestamp.sh" full &>/dev/null; then
        # 使用Python脚本计算
        WEEK_START=$(python3 -c "
import datetime, pytz
pacific = pytz.timezone('America/Los_Angeles')
now = datetime.datetime.now(pacific)
start = now - datetime.timedelta(days=now.weekday())
print(start.strftime('%Y-%m-%d'))
" 2>/dev/null || date -v-$(date +%u)d +"%Y-%m-%d")
        
        WEEK_END=$(python3 -c "
import datetime, pytz
pacific = pytz.timezone('America/Los_Angeles')
now = datetime.datetime.now(pacific)
start = now - datetime.timedelta(days=now.weekday())
end = start + datetime.timedelta(days=6)
print(end.strftime('%Y-%m-%d'))
" 2>/dev/null || date -v-$(date +%u)d -v+6d +"%Y-%m-%d")
    else
        # 使用简单方法计算
        WEEK_START=$(date -v-$(date +%u)d +"%Y-%m-%d")
        WEEK_END=$(date -v-$(date +%u)d -v+6d +"%Y-%m-%d")
    fi
    
    # 提取周数
    WEEK_NUM=$(echo $YEAR_WEEK | cut -d 'W' -f 2)
    
    echo -e "${BLUE}=== 创建周报: 第$WEEK_NUM周 ($WEEK_START 至 $WEEK_END) ===${NC}"
    echo -e "${BLUE}=== 时间戳: $FULL_TIMESTAMP ===${NC}"
    
    # 检查是否已存在
    if [ -f "$REPORT_FILE" ]; then
        echo -e "${YELLOW}警告: 本周周报已存在${NC}"
        read -p "是否覆盖? (y/n): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${RED}已取消${NC}"
            return
        fi
    fi
    
    # 复制模板并替换占位符
    cp "$TEMPLATE_FILE" "$REPORT_FILE"
    sed -i '' "s/{{WEEK_NUMBER}}/$WEEK_NUM/g" "$REPORT_FILE"
    sed -i '' "s/{{PROJECT_NAME}}/$PROJECT_NAME/g" "$REPORT_FILE"
    sed -i '' "s/{{START_DATE}}/$WEEK_START/g" "$REPORT_FILE"
    sed -i '' "s/{{END_DATE}}/$WEEK_END/g" "$REPORT_FILE"
    sed -i '' "s/{{AUTHOR}}/$(whoami)/g" "$REPORT_FILE"
    sed -i '' "s/{{TIMESTAMP}}/$FULL_TIMESTAMP/g" "$REPORT_FILE"
    
    echo -e "${GREEN}周报已创建: $REPORT_FILE${NC}"
}

# 根据报告类型执行相应的函数
case "$REPORT_TYPE" in
    daily)
        create_daily_report
        ;;
    weekly)
        create_weekly_report
        ;;
    *)
        echo -e "${RED}错误: 无效的报告类型 '$REPORT_TYPE'${NC}"
        echo -e "有效的报告类型: daily, weekly"
        exit 1
        ;;
esac 