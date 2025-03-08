#!/bin/bash

# CursorMind 时间戳生成脚本包装器
# 用法: ./timestamp.sh [format_type]
# format_type 可以是: full, date, datetime, compact, week

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/generate_timestamp.py"
VENV_DIR="$SCRIPT_DIR/.venv"

# 检查Python脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "错误: 找不到Python时间戳脚本: $PYTHON_SCRIPT" >&2
    exit 1
fi

# 如果虚拟环境不存在，创建一个
if [ ! -d "$VENV_DIR" ]; then
    echo "创建Python虚拟环境..." >&2
    python3 -m venv "$VENV_DIR" || {
        echo "错误: 无法创建虚拟环境，请确保已安装Python 3.6+" >&2
        
        # 回退方案：直接使用系统Python，但可能会失败
        echo "尝试使用系统Python..." >&2
        if ! python3 -c "import pytz" &>/dev/null; then
            echo "错误: 未安装pytz模块，请手动安装: pip3 install pytz" >&2
            
            # 生成一个基本的时间戳作为回退
            date "+%Y-%m-%d %H:%M:%S"
            exit 1
        fi
        
        python3 "$PYTHON_SCRIPT" "$@"
        exit $?
    }
    
    # 安装依赖
    "$VENV_DIR/bin/pip" install pytz || {
        echo "错误: 无法安装pytz模块" >&2
        exit 1
    }
fi

# 使用虚拟环境中的Python运行脚本
"$VENV_DIR/bin/python" "$PYTHON_SCRIPT" "$@" || {
    # 如果失败，尝试使用系统Python
    echo "警告: 虚拟环境执行失败，尝试使用系统Python..." >&2
    python3 "$PYTHON_SCRIPT" "$@" || {
        # 如果仍然失败，使用系统日期命令作为回退
        echo "错误: 无法执行Python脚本，使用系统日期命令作为回退" >&2
        if [ "$1" = "full" ]; then
            date "+%Y-%m-%d %H:%M:%S"
        elif [ "$1" = "date" ]; then
            date "+%Y-%m-%d"
        elif [ "$1" = "compact" ]; then
            date "+%Y%m%d"
        elif [ "$1" = "week" ]; then
            date "+%YW%U"
        else
            date "+%Y-%m-%d %H:%M:%S"
        fi
    }
} 