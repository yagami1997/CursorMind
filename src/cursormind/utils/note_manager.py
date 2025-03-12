"""
笔记管理工具 - 记录你的学习历程 📝
"""
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict
import json
from ..config.settings import settings
from .helpers import get_timestamp, ensure_dir

class NoteManager:
    """笔记管理类"""

    def __init__(self):
        self.notes_dir = Path(settings.get('notes_dir', 'learning_notes'))
        self.ensure_notes_structure()

    def ensure_notes_structure(self) -> None:
        """确保笔记目录结构完整"""
        ensure_dir(self.notes_dir)
        ensure_dir(self.notes_dir / 'daily')
        ensure_dir(self.notes_dir / 'projects')
        ensure_dir(self.notes_dir / 'ideas')

    def add_note(self, content: str, note_type: str = 'daily') -> Dict:
        """
        添加新笔记

        Args:
            content: 笔记内容
            note_type: 笔记类型（daily/project/idea）

        Returns:
            笔记信息字典
        """
        timestamp = get_timestamp()
        date_str = datetime.now().strftime('%Y-%m-%d')
        
        # 创建笔记数据
        note_data = {
            'content': content,
            'timestamp': timestamp,
            'type': note_type,
            'tags': self._extract_tags(content),
            'project': settings.get('current_project', '')
        }

        # 保存笔记
        if note_type == 'daily':
            file_path = self.notes_dir / 'daily' / f'{date_str}.md'
        else:
            file_path = self.notes_dir / note_type / f'{date_str}_{self._generate_id()}.md'

        self._save_note(note_data, file_path)
        self._update_stats(note_data)
        
        return note_data

    def get_today_notes(self) -> List[Dict]:
        """获取今天的笔记列表"""
        date_str = datetime.now().strftime('%Y-%m-%d')
        daily_file = self.notes_dir / 'daily' / f'{date_str}.md'
        
        if not daily_file.exists():
            return []
        
        return self._read_notes(daily_file)

    def _save_note(self, note_data: Dict, file_path: Path) -> None:
        """保存笔记到文件"""
        # 确保目录存在
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # 格式化笔记内容
        note_content = f"""
## {note_data['timestamp']}

{note_data['content']}

{'#' + ' #'.join(note_data['tags']) if note_data['tags'] else ''}

---
"""
        # 追加或创建文件
        mode = 'a' if file_path.exists() else 'w'
        with open(file_path, mode, encoding='utf-8') as f:
            f.write(note_content)

    def _extract_tags(self, content: str) -> List[str]:
        """从内容中提取标签"""
        tags = []
        words = content.split()
        for word in words:
            if word.startswith('#') and len(word) > 1:
                tags.append(word[1:])
        return tags

    def _generate_id(self) -> str:
        """生成笔记ID"""
        return datetime.now().strftime('%H%M%S')

    def _update_stats(self, note_data: Dict) -> None:
        """更新笔记统计信息"""
        settings.set('total_notes', settings.get('total_notes', 0) + 1)
        
        # TODO: 实现更多统计功能
        # - 按类型统计
        # - 按标签统计
        # - 生成学习热力图

    def _read_notes(self, file_path: Path) -> List[Dict]:
        """读取笔记文件内容"""
        if not file_path.exists():
            return []
            
        notes = []
        current_note = None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('## '):
                    if current_note:
                        notes.append(current_note)
                    current_note = {
                        'timestamp': line[3:],
                        'content': '',
                        'tags': []
                    }
                elif current_note and line and not line.startswith('---'):
                    if line.startswith('#'):
                        current_note['tags'] = [tag[1:] for tag in line.split()]
                    else:
                        current_note['content'] += line + '\n'
                        
        if current_note:
            notes.append(current_note)
            
        return notes

# 创建全局笔记管理器实例
note_manager = NoteManager() 