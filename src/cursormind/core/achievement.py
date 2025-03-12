"""
成就系统模块 - 跟踪和奖励学习进度
"""
import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from ..utils.helpers import get_timestamp, ensure_dir

class AchievementManager:
    """成就系统管理器"""
    
    def __init__(self):
        """初始化成就系统"""
        self.base_dir = os.path.expanduser('~/.cursormind')
        self.achievements_dir = os.path.join(self.base_dir, 'achievements')
        self.achievements_file = os.path.join(self.achievements_dir, 'achievements.json')
        self.stats_file = os.path.join(self.achievements_dir, 'stats.json')
        
        # 确保目录存在
        ensure_dir(self.achievements_dir)
        
        # 初始化成就数据
        self._ensure_achievements_file()
        self._ensure_stats_file()
        
        # 加载成就定义和用户统计
        self.achievements = self._load_achievements()
        self.stats = self._load_stats()
    
    def _ensure_achievements_file(self):
        """确保成就定义文件存在，不存在则创建默认成就"""
        if not os.path.exists(self.achievements_file):
            default_achievements = {
                "learning_path": {
                    "first_path": {
                        "name": "学习启航",
                        "description": "开始第一个学习路径",
                        "icon": "🚀",
                        "condition": {"type": "path_started", "count": 1},
                        "reward": 100
                    },
                    "path_master": {
                        "name": "学习大师",
                        "description": "完成一个完整的学习路径",
                        "icon": "🎓",
                        "condition": {"type": "path_completed", "count": 1},
                        "reward": 500
                    }
                },
                "notes": {
                    "first_note": {
                        "name": "记录者",
                        "description": "写下第一篇学习笔记",
                        "icon": "📝",
                        "condition": {"type": "note_created", "count": 1},
                        "reward": 50
                    },
                    "note_streak": {
                        "name": "坚持不懈",
                        "description": "连续7天记录学习笔记",
                        "icon": "🔥",
                        "condition": {"type": "daily_streak", "count": 7},
                        "reward": 300
                    },
                    "note_master": {
                        "name": "笔记达人",
                        "description": "累计记录100篇笔记",
                        "icon": "✍️",
                        "condition": {"type": "note_created", "count": 100},
                        "reward": 1000
                    }
                },
                "tags": {
                    "tag_organizer": {
                        "name": "标签达人",
                        "description": "使用20个不同的标签",
                        "icon": "🏷️",
                        "condition": {"type": "unique_tags", "count": 20},
                        "reward": 200
                    }
                },
                "topics": {
                    "topic_explorer": {
                        "name": "主题探索者",
                        "description": "在5个不同主题下记录笔记",
                        "icon": "🗺️",
                        "condition": {"type": "unique_topics", "count": 5},
                        "reward": 300
                    }
                },
                "review": {
                    "weekly_reviewer": {
                        "name": "复习达人",
                        "description": "生成4次周回顾报告",
                        "icon": "📊",
                        "condition": {"type": "review_generated", "count": 4},
                        "reward": 200
                    }
                }
            }
            
            with open(self.achievements_file, 'w', encoding='utf-8') as f:
                json.dump(default_achievements, f, ensure_ascii=False, indent=2)
    
    def _ensure_stats_file(self):
        """确保用户统计文件存在"""
        if not os.path.exists(self.stats_file):
            default_stats = {
                "points": 0,
                "unlocked_achievements": [],
                "stats": {
                    "paths_started": 0,
                    "paths_completed": 0,
                    "notes_created": 0,
                    "daily_streak": 0,
                    "unique_tags": set(),
                    "unique_topics": set(),
                    "reviews_generated": 0
                },
                "last_updated": get_timestamp()
            }
            
            with open(self.stats_file, 'w', encoding='utf-8') as f:
                json.dump(default_stats, f, ensure_ascii=False, indent=2, 
                         default=lambda x: list(x) if isinstance(x, set) else x)
    
    def _load_achievements(self) -> Dict:
        """加载成就定义"""
        with open(self.achievements_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _load_stats(self) -> Dict:
        """加载用户统计数据"""
        with open(self.stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
            # 将列表转换回集合
            stats['stats']['unique_tags'] = set(stats['stats']['unique_tags'])
            stats['stats']['unique_topics'] = set(stats['stats']['unique_topics'])
            return stats
    
    def _save_stats(self):
        """保存用户统计数据"""
        with open(self.stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, ensure_ascii=False, indent=2,
                     default=lambda x: list(x) if isinstance(x, set) else x)
    
    def _check_achievements(self) -> List[Dict]:
        """检查是否有新的成就达成"""
        new_achievements = []
        stats = self.stats['stats']
        
        for category, achievements in self.achievements.items():
            for achievement_id, achievement in achievements.items():
                # 跳过已解锁的成就
                if achievement_id in self.stats['unlocked_achievements']:
                    continue
                
                condition = achievement['condition']
                achieved = False
                
                # 检查不同类型的成就条件
                if condition['type'] == 'path_started':
                    achieved = stats['paths_started'] >= condition['count']
                elif condition['type'] == 'path_completed':
                    achieved = stats['paths_completed'] >= condition['count']
                elif condition['type'] == 'note_created':
                    achieved = stats['notes_created'] >= condition['count']
                elif condition['type'] == 'daily_streak':
                    achieved = stats['daily_streak'] >= condition['count']
                elif condition['type'] == 'unique_tags':
                    achieved = len(stats['unique_tags']) >= condition['count']
                elif condition['type'] == 'unique_topics':
                    achieved = len(stats['unique_topics']) >= condition['count']
                elif condition['type'] == 'review_generated':
                    achieved = stats['reviews_generated'] >= condition['count']
                
                if achieved:
                    self.stats['unlocked_achievements'].append(achievement_id)
                    self.stats['points'] += achievement['reward']
                    new_achievements.append({
                        'id': achievement_id,
                        'name': achievement['name'],
                        'description': achievement['description'],
                        'icon': achievement['icon'],
                        'reward': achievement['reward']
                    })
        
        if new_achievements:
            self._save_stats()
        
        return new_achievements
    
    def update_stats(self, event_type: str, data: Optional[Dict] = None) -> List[Dict]:
        """
        更新用户统计并检查成就
        
        Args:
            event_type: 事件类型，如 'path_started', 'note_created' 等
            data: 事件相关的数据
            
        Returns:
            新解锁的成就列表
        """
        stats = self.stats['stats']
        
        if event_type == 'path_started':
            stats['paths_started'] += 1
        elif event_type == 'path_completed':
            stats['paths_completed'] += 1
        elif event_type == 'note_created':
            stats['notes_created'] += 1
            if data:
                if 'tags' in data:
                    stats['unique_tags'].update(data['tags'])
                if 'topic' in data:
                    stats['unique_topics'].add(data['topic'])
        elif event_type == 'review_generated':
            stats['reviews_generated'] += 1
        
        self.stats['last_updated'] = get_timestamp()
        self._save_stats()
        
        return self._check_achievements()
    
    def get_stats(self) -> Dict:
        """获取用户统计信息"""
        stats = self.stats.copy()
        # 转换集合为列表以便序列化
        stats['stats']['unique_tags'] = list(stats['stats']['unique_tags'])
        stats['stats']['unique_topics'] = list(stats['stats']['unique_topics'])
        return stats
    
    def get_achievements(self, include_locked: bool = False) -> Dict:
        """
        获取成就列表
        
        Args:
            include_locked: 是否包含未解锁的成就
            
        Returns:
            成就列表，包含解锁状态
        """
        result = {}
        for category, achievements in self.achievements.items():
            result[category] = {}
            for achievement_id, achievement in achievements.items():
                if achievement_id in self.stats['unlocked_achievements'] or include_locked:
                    achievement_data = achievement.copy()
                    achievement_data['unlocked'] = achievement_id in self.stats['unlocked_achievements']
                    result[category][achievement_id] = achievement_data
        return result

# 创建全局实例
achievement_manager = AchievementManager() 