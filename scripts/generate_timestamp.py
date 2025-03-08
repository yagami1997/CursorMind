#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CursorMind 时间戳生成脚本
生成美国太平洋时间的时间戳
"""

import datetime
import pytz
import sys

def get_pacific_timestamp(format_type='full'):
    """
    获取美国太平洋时间的时间戳
    
    参数:
        format_type (str): 时间戳格式类型
            - 'full': 完整格式 YYYY-MM-DD HH:MM:SS PST/PDT
            - 'date': 仅日期 YYYY-MM-DD
            - 'datetime': 日期和时间 YYYY-MM-DD HH:MM:SS
            - 'compact': 紧凑格式 YYYYMMDD
            - 'week': 年份和周数 YYYYWNN
    
    返回:
        str: 格式化的时间戳
    """
    # 获取太平洋时区的当前时间
    pacific_tz = pytz.timezone('America/Los_Angeles')
    now = datetime.datetime.now(pacific_tz)
    
    # 确定是PST还是PDT
    timezone_name = now.strftime('%Z')
    
    if format_type == 'full':
        # 完整格式: YYYY-MM-DD HH:MM:SS PST/PDT
        return now.strftime('%Y-%m-%d %H:%M:%S') + f" {timezone_name}"
    elif format_type == 'date':
        # 仅日期: YYYY-MM-DD
        return now.strftime('%Y-%m-%d')
    elif format_type == 'datetime':
        # 日期和时间: YYYY-MM-DD HH:MM:SS
        return now.strftime('%Y-%m-%d %H:%M:%S')
    elif format_type == 'compact':
        # 紧凑格式: YYYYMMDD
        return now.strftime('%Y%m%d')
    elif format_type == 'week':
        # 年份和周数: YYYYWNN
        year = now.strftime('%Y')
        week = now.strftime('%U')
        return f"{year}W{week}"
    else:
        raise ValueError(f"不支持的格式类型: {format_type}")

if __name__ == "__main__":
    # 如果有命令行参数，使用它作为格式类型
    format_type = 'full'
    if len(sys.argv) > 1:
        format_type = sys.argv[1]
    
    try:
        timestamp = get_pacific_timestamp(format_type)
        print(timestamp)
    except ValueError as e:
        print(f"错误: {e}", file=sys.stderr)
        print("支持的格式类型: full, date, datetime, compact, week", file=sys.stderr)
        sys.exit(1) 