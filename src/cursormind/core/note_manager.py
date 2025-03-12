"""
笔记管理模块 - 记录你的学习心得 📝
"""
import os
import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Set
import re
from ..config.settings import settings
from ..utils.helpers import ensure_dir, get_timestamp
from .achievement import achievement_manager

class NoteManager:
    """笔记管理类"""
    
    def __init__(self):
        self._project_root = Path(settings.get('project_root'))
        self._notes_dir = self._project_root / settings.get('notes_dir')
        self._daily_dir = self._notes_dir / 'daily'
        self._topic_dir = self._notes_dir / 'topics'
        self._review_dir = self._notes_dir / 'reviews'
        self._stats_file = self._notes_dir / 'stats.json'
        self._ensure_structure()
        self._load_stats()
        self._update_daily_streak()
    
    def _ensure_structure(self) -> None:
        """确保笔记目录结构存在"""
        for dir_path in [self._daily_dir, self._topic_dir, self._review_dir]:
            ensure_dir(dir_path)
        
        if not self._stats_file.exists():
            self._stats = {
                'total_notes': 0,
                'total_words': 0,
                'topics': {},
                'tags': {},
                'daily_streak': 0,
                'last_note_date': '',
                'last_updated': get_timestamp()
            }
            self._save_stats()
    
    def _load_stats(self) -> None:
        """加载笔记统计数据"""
        if self._stats_file.exists():
            with open(self._stats_file, 'r', encoding='utf-8') as f:
                self._stats = json.load(f)
    
    def _save_stats(self) -> None:
        """保存笔记统计数据"""
        with open(self._stats_file, 'w', encoding='utf-8') as f:
            json.dump(self._stats, f, ensure_ascii=False, indent=2)
    
    def _update_daily_streak(self):
        """更新连续记录天数"""
        with open(self._stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        
        if not stats['last_note_date']:
            return
        
        last_note = datetime.fromisoformat(stats['last_note_date'])
        today = datetime.now()
        
        # 如果最后一条笔记是昨天的
        if (today - last_note).days > 1:
            stats['daily_streak'] = 0
        
        with open(self._stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    
    def _extract_tags(self, content: str) -> Set[str]:
        """从内容中提取标签"""
        return set(tag.strip() for tag in re.findall(r'#(\w+)', content))
    
    def _update_stats(self, content: str, topic: str, tags: Set[str]):
        """更新统计数据"""
        with open(self._stats_file, 'r', encoding='utf-8') as f:
            stats = json.load(f)
        
        # 更新基本统计
        stats['total_notes'] += 1
        stats['total_words'] += len(content.split())
        
        # 更新主题统计
        if topic not in stats['topics']:
            stats['topics'][topic] = 0
        stats['topics'][topic] += 1
        
        # 更新标签统计
        for tag in tags:
            if tag not in stats['tags']:
                stats['tags'][tag] = 0
            stats['tags'][tag] += 1
        
        # 更新连续记录
        today = datetime.now().date()
        if stats['last_note_date']:
            last_note = datetime.fromisoformat(stats['last_note_date']).date()
            if today == last_note:
                pass  # 同一天内不更新连续记录
            elif (today - last_note).days == 1:
                stats['daily_streak'] += 1
            else:
                stats['daily_streak'] = 1
        else:
            stats['daily_streak'] = 1
        
        stats['last_note_date'] = datetime.now().isoformat()
        stats['last_updated'] = get_timestamp()
        
        with open(self._stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        
        # 触发成就检查
        achievement_manager.update_stats('note_created', {
            'topic': topic,
            'tags': list(tags)
        })
    
    def add_note(self, content: str, topic: str = 'general') -> Dict:
        """
        添加新笔记
        :param content: 笔记内容
        :param topic: 主题
        :return: 笔记信息
        """
        timestamp = get_timestamp()
        date = datetime.now().strftime('%Y-%m-%d')
        tags = self._extract_tags(content)
        
        # 创建笔记数据
        note = {
            'id': f"{date}-{self._stats['total_notes'] + 1:04d}",
            'content': content,
            'topic': topic,
            'tags': list(tags),
            'created_at': timestamp,
            'updated_at': timestamp
        }
        
        # 保存到日常笔记
        daily_file = self._daily_dir / f"{date}.json"
        daily_notes = []
        if daily_file.exists():
            with open(daily_file, 'r', encoding='utf-8') as f:
                daily_notes = json.load(f)
        daily_notes.append(note)
        with open(daily_file, 'w', encoding='utf-8') as f:
            json.dump(daily_notes, f, ensure_ascii=False, indent=2)
        
        # 保存到主题目录
        topic_dir = ensure_dir(self._topic_dir / topic)
        topic_file = topic_dir / f"{note['id']}.json"
        with open(topic_file, 'w', encoding='utf-8') as f:
            json.dump(note, f, ensure_ascii=False, indent=2)
        
        # 更新统计数据
        self._update_stats(content, topic, tags)
        
        return note
    
    def get_daily_notes(self, date: Optional[str] = None) -> List[Dict]:
        """
        获取指定日期的笔记
        :param date: 日期字符串（YYYY-MM-DD），默认为今天
        :return: 笔记列表
        """
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        daily_file = self._daily_dir / f"{date}.json"
        if not daily_file.exists():
            return []
        
        with open(daily_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def get_topic_notes(self, topic: str) -> List[Dict]:
        """
        获取指定主题的所有笔记
        :param topic: 主题名称
        :return: 笔记列表
        """
        topic_dir = self._topic_dir / topic
        if not topic_dir.exists():
            return []
        
        notes = []
        for note_file in topic_dir.glob('*.json'):
            with open(note_file, 'r', encoding='utf-8') as f:
                notes.append(json.load(f))
        
        return sorted(notes, key=lambda x: x['created_at'], reverse=True)
    
    def search_notes(self, query: str) -> List[Dict]:
        """
        搜索笔记
        :param query: 搜索关键词
        :return: 匹配的笔记列表
        """
        results = []
        for topic_dir in self._topic_dir.iterdir():
            if topic_dir.is_dir():
                for note_file in topic_dir.glob('*.json'):
                    with open(note_file, 'r', encoding='utf-8') as f:
                        note = json.load(f)
                        if (query.lower() in note['content'].lower() or
                            query.lower() in note['topic'].lower() or
                            any(query.lower() in tag.lower() for tag in note['tags'])):
                            results.append(note)
        
        return sorted(results, key=lambda x: x['created_at'], reverse=True)
    
    def get_stats(self) -> Dict:
        """获取笔记统计数据"""
        return self._stats
    
    def generate_review(self, days: int = 7) -> Dict:
        """
        生成复习报告
        :param days: 要回顾的天数
        :return: 复习报告
        """
        end_date = datetime.now()
        start_date = end_date.replace(day=end_date.day - days + 1)
        
        review = {
            'period': f"{start_date.strftime('%Y-%m-%d')} 至 {end_date.strftime('%Y-%m-%d')}",
            'total_notes': 0,
            'total_words': 0,
            'topics': {},
            'tags': {},
            'daily_notes': [],
            'highlights': []
        }
        
        current = start_date
        while current <= end_date:
            date = current.strftime('%Y-%m-%d')
            daily_notes = self.get_daily_notes(date)
            
            if daily_notes:
                review['total_notes'] += len(daily_notes)
                for note in daily_notes:
                    review['total_words'] += len(note['content'].split())
                    
                    # 更新主题统计
                    if note['topic'] not in review['topics']:
                        review['topics'][note['topic']] = 0
                    review['topics'][note['topic']] += 1
                    
                    # 更新标签统计
                    for tag in note['tags']:
                        if tag not in review['tags']:
                            review['tags'][tag] = 0
                        review['tags'][tag] += 1
                    
                    # 添加到每日笔记列表
                    review['daily_notes'].append({
                        'date': date,
                        'notes': daily_notes
                    })
                    
                    # 如果笔记内容超过100字，添加到亮点列表
                    if len(note['content'].split()) > 100:
                        review['highlights'].append(note)
            
            current = current.replace(day=current.day + 1)
        
        # 保存复习报告
        review_file = self._review_dir / f"review_{end_date.strftime('%Y%m%d')}.json"
        with open(review_file, 'w', encoding='utf-8') as f:
            json.dump(review, f, ensure_ascii=False, indent=2)
        
        # 触发成就检查
        achievement_manager.update_stats('review_generated')
        
        return review

# 创建全局实例
note_manager = NoteManager() 