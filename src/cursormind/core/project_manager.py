"""
项目管理工具模块
"""
import os
import json
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path

class ProjectManager:
    def __init__(self):
        self.config_dir = Path.home() / '.cursormind' / 'project_manager'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.tasks_dir = self.config_dir / 'tasks'
        self.tasks_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / 'config.json'
        self._load_config()

    def _load_config(self):
        """加载配置"""
        if not self.config_file.exists():
            self.config = {
                "task_status_options": [
                    "待处理", "进行中", "已完成", "已取消", "已延期"
                ],
                "task_priority_options": [
                    "低", "中", "高", "紧急"
                ],
                "task_type_options": [
                    "功能开发", "bug修复", "文档编写", "代码重构",
                    "性能优化", "测试编写", "其他"
                ],
                "default_task_fields": {
                    "status": "待处理",
                    "priority": "中",
                    "type": "功能开发",
                    "deadline": None,
                    "assignee": None,
                    "description": "",
                    "notes": [],
                    "subtasks": [],
                    "related_tasks": [],
                    "tags": []
                }
            }
            self._save_config()
        else:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = json.load(f)

    def _save_config(self):
        """保存配置"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def create_task(self, title: str, **kwargs) -> Dict:
        """创建新任务"""
        task_id = datetime.now().strftime("%Y%m%d%H%M%S")
        task = {
            "id": task_id,
            "title": title,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            **self.config["default_task_fields"],
            **kwargs
        }
        
        task_file = self.tasks_dir / f"{task_id}.json"
        with open(task_file, 'w', encoding='utf-8') as f:
            json.dump(task, f, ensure_ascii=False, indent=2)
        
        return task

    def update_task(self, task_id: str, **kwargs) -> Optional[Dict]:
        """更新任务"""
        task_file = self.tasks_dir / f"{task_id}.json"
        if not task_file.exists():
            return None
        
        with open(task_file, 'r', encoding='utf-8') as f:
            task = json.load(f)
        
        task.update(kwargs)
        task["updated_at"] = datetime.now().isoformat()
        
        with open(task_file, 'w', encoding='utf-8') as f:
            json.dump(task, f, ensure_ascii=False, indent=2)
        
        return task

    def get_task(self, task_id: str) -> Optional[Dict]:
        """获取任务详情"""
        task_file = self.tasks_dir / f"{task_id}.json"
        if not task_file.exists():
            return None
        
        with open(task_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_tasks(self, status: Optional[str] = None, priority: Optional[str] = None,
                  type_: Optional[str] = None, assignee: Optional[str] = None,
                  tags: Optional[List[str]] = None) -> List[Dict]:
        """列出任务"""
        tasks = []
        for task_file in self.tasks_dir.glob("*.json"):
            with open(task_file, 'r', encoding='utf-8') as f:
                task = json.load(f)
                
                # 应用过滤条件
                if status and task["status"] != status:
                    continue
                if priority and task["priority"] != priority:
                    continue
                if type_ and task["type"] != type_:
                    continue
                if assignee and task["assignee"] != assignee:
                    continue
                if tags and not all(tag in task["tags"] for tag in tags):
                    continue
                
                tasks.append(task)
        
        # 按优先级和创建时间排序
        priority_order = {p: i for i, p in enumerate(self.config["task_priority_options"])}
        tasks.sort(key=lambda x: (priority_order[x["priority"]], x["created_at"]), reverse=True)
        
        return tasks

    def add_subtask(self, parent_id: str, title: str, **kwargs) -> Optional[Dict]:
        """添加子任务"""
        parent_task = self.get_task(parent_id)
        if not parent_task:
            return None
        
        subtask = {
            "id": f"{parent_id}-{len(parent_task['subtasks'])+1}",
            "title": title,
            "created_at": datetime.now().isoformat(),
            "status": "待处理",
            **kwargs
        }
        
        parent_task["subtasks"].append(subtask)
        self.update_task(parent_id, subtasks=parent_task["subtasks"])
        
        return subtask

    def add_note(self, task_id: str, content: str) -> Optional[Dict]:
        """添加任务笔记"""
        task = self.get_task(task_id)
        if not task:
            return None
        
        note = {
            "id": len(task["notes"]) + 1,
            "content": content,
            "created_at": datetime.now().isoformat()
        }
        
        task["notes"].append(note)
        self.update_task(task_id, notes=task["notes"])
        
        return note

    def link_tasks(self, task_id: str, related_task_id: str) -> bool:
        """关联任务"""
        task = self.get_task(task_id)
        related_task = self.get_task(related_task_id)
        
        if not task or not related_task:
            return False
        
        if related_task_id not in task["related_tasks"]:
            task["related_tasks"].append(related_task_id)
            self.update_task(task_id, related_tasks=task["related_tasks"])
        
        if task_id not in related_task["related_tasks"]:
            related_task["related_tasks"].append(task_id)
            self.update_task(related_task_id, related_tasks=related_task["related_tasks"])
        
        return True

    def get_task_stats(self) -> Dict:
        """获取任务统计信息"""
        stats = {
            "total_tasks": 0,
            "status_counts": {},
            "priority_counts": {},
            "type_counts": {},
            "assignee_counts": {},
            "tag_counts": {},
            "completion_rate": 0,
            "average_completion_time": 0
        }
        
        completed_tasks = []
        for task_file in self.tasks_dir.glob("*.json"):
            with open(task_file, 'r', encoding='utf-8') as f:
                task = json.load(f)
                
                stats["total_tasks"] += 1
                
                # 统计状态
                stats["status_counts"][task["status"]] = \
                    stats["status_counts"].get(task["status"], 0) + 1
                
                # 统计优先级
                stats["priority_counts"][task["priority"]] = \
                    stats["priority_counts"].get(task["priority"], 0) + 1
                
                # 统计类型
                stats["type_counts"][task["type"]] = \
                    stats["type_counts"].get(task["type"], 0) + 1
                
                # 统计负责人
                if task["assignee"]:
                    stats["assignee_counts"][task["assignee"]] = \
                        stats["assignee_counts"].get(task["assignee"], 0) + 1
                
                # 统计标签
                for tag in task["tags"]:
                    stats["tag_counts"][tag] = stats["tag_counts"].get(tag, 0) + 1
                
                # 收集已完成的任务
                if task["status"] == "已完成":
                    completed_tasks.append(task)
        
        # 计算完成率
        if stats["total_tasks"] > 0:
            stats["completion_rate"] = \
                len(completed_tasks) / stats["total_tasks"] * 100
        
        # 计算平均完成时间（天）
        if completed_tasks:
            total_days = 0
            for task in completed_tasks:
                created = datetime.fromisoformat(task["created_at"])
                updated = datetime.fromisoformat(task["updated_at"])
                total_days += (updated - created).days
            stats["average_completion_time"] = total_days / len(completed_tasks)
        
        return stats

project_manager = ProjectManager() 