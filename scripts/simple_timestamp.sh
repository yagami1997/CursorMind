#!/bin/bash

# CursorMind 简单时间戳生成脚本
# 用法: ./simple_timestamp.sh [format_type]
# format_type 可以是: full, date, datetime, compact, week

# 注意: 此脚本使用系统时间，不是太平洋时间
# 如果需要太平洋时间，请使用timestamp.sh脚本

format_type="${1:-full}"

case "$format_type" in
    full)
        # 完整格式: YYYY-MM-DD HH:MM:SS TZ
        date "+%Y-%m-%d %H:%M:%S %Z"
        ;;
    date)
        # 仅日期: YYYY-MM-DD
        date "+%Y-%m-%d"
        ;;
    datetime)
        # 日期和时间: YYYY-MM-DD HH:MM:SS
        date "+%Y-%m-%d %H:%M:%S"
        ;;
    compact)
        # 紧凑格式: YYYYMMDD
        date "+%Y%m%d"
        ;;
    week)
        # 年份和周数: YYYYWNN
        date "+%YW%U"
        ;;
    *)
        echo "错误: 不支持的格式类型: $format_type" >&2
        echo "支持的格式类型: full, date, datetime, compact, week" >&2
        exit 1
        ;;
esac 