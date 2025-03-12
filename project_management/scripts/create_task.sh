#!/bin/bash

# 设置时区为PST
export TZ="America/Los_Angeles"

# 检查参数
if [ $# -lt 1 ]; then
    echo "用法: $0 <任务名称> [优先级(高/中/低)]"
    exit 1
fi

# 获取参数
TASK_NAME="$1"
PRIORITY="${2:-中}"  # 默认优先级为"中"

# 生成任务ID（格式：TASK-XXX）
TASK_COUNT_FILE="project_management/.task_count"
if [ ! -f "$TASK_COUNT_FILE" ]; then
    echo "1" > "$TASK_COUNT_FILE"
fi
TASK_NUM=$(cat "$TASK_COUNT_FILE")
TASK_ID="TASK-$(printf "%03d" $TASK_NUM)"

# 更新任务计数
echo $((TASK_NUM + 1)) > "$TASK_COUNT_FILE"

# 获取当前时间戳
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S %Z")

# 创建任务文件
TASK_FILE="project_management/actuals/tasks/${TASK_ID}_$(echo "$TASK_NAME" | tr ' ' '_').md"
mkdir -p "project_management/actuals/tasks"

# 从模板创建任务文件
sed -e "s/\[TASK-ID\]/$TASK_ID/g" \
    -e "s/\[任务名称\]/$TASK_NAME/g" \
    -e "s/\[TIMESTAMP\]/$TIMESTAMP/g" \
    -e "s/\[高\/中\/低\]/$PRIORITY/g" \
    -e "s/\[未开始\/进行中\/已完成\/已暂停\]/未开始/g" \
    "project_management/templates/task_template.md" > "$TASK_FILE"

echo "已创建任务：$TASK_ID"
echo "任务文件：$TASK_FILE" 