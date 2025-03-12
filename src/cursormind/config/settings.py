"""
配置管理模块 - 保存你的个人设置 ⚙️
"""
import os
import json
from datetime import datetime
import pytz
from pathlib import Path
from typing import Dict, Any, Optional

class Settings:
    """配置管理类"""

    def __init__(self):
        self._config: Dict[str, Any] = {}
        self._config_dir = Path.home() / '.cursormind'
        self._config_file = self._config_dir / 'config.json'
        self._first_time = not self._config_file.exists()
        self.load()

    def load(self) -> None:
        """
        加载配置文件
        如果是第一次使用，会创建默认配置并显示欢迎信息
        """
        if self._first_time:
            self._create_default_config()
            self._show_welcome()
        else:
            with open(self._config_file, 'r', encoding='utf-8') as f:
                self._config = json.load(f)

    def save(self) -> None:
        """保存配置到文件"""
        self._config_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self._config_file, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, ensure_ascii=False, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        return self._config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """设置配置项"""
        self._config[key] = value
        self.save()

    def _get_timestamp(self) -> str:
        """获取当前时间戳"""
        tz = pytz.timezone(self.get('timezone', 'America/Los_Angeles'))
        now = datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")

    def _create_default_config(self) -> None:
        """创建默认配置"""
        # 获取当前工作目录作为项目根目录
        project_root = str(Path.cwd())
        
        default_config = {
            # 基本信息
            'user_name': '',              # 用户名
            'current_project': '',        # 当前项目
            'learning_goal': '',          # 学习目标
            
            # 个性化设置
            'timezone': 'America/Los_Angeles',  # 时区
            'language': 'zh',             # 语言
            'theme': 'light',             # 主题
            'emoji_enabled': True,        # 是否启用表情
            
            # 项目设置
            'project_root': project_root,  # 项目根目录
            'learning_paths_dir': 'learning_paths',  # 学习路径目录
            'notes_dir': 'learning_notes',     # 笔记目录
            'backups_dir': 'backups',          # 备份目录
            
            # 学习记录
            'start_date': self._get_timestamp(),  # 开始使用日期
            'study_days': 0,              # 学习天数
            'total_notes': 0,             # 笔记总数
            'achievements': [],           # 已获得的成就
            
            # 提醒设置
            'daily_reminder': True,       # 每日提醒
            'reminder_time': '20:00',     # 提醒时间
            
            # 版本信息
            'version': 'Beta 0.1.1'       # 当前版本
        }
        self._config = default_config
        self.save()

    def _show_welcome(self) -> None:
        """显示首次使用的欢迎信息"""
        welcome_message = """
🎉 欢迎使用 CursorMind！

这是你第一次使用这个学习助手，我已经为你创建了默认配置文件：
~/.cursormind/config.json

你可以随时修改这些设置，让它更适合你的使用习惯。
现在，让我们开始你的学习之旅吧！

💡 快速开始：
1. cursormind path          # 查看学习路径
2. cursormind start         # 开始今天的学习
3. cursormind note "内容"   # 记录学习笔记
4. cursormind help         # 查看更多帮助

记住：每一个小进步都很重要，坚持记录，你会看到自己的成长！ 💪
"""
        print(welcome_message)

# 创建全局配置实例
settings = Settings() 