"""
学习路径管理模块 - 指导你的学习之旅 🗺️
"""
import os
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from ..config.settings import settings
from ..utils.helpers import get_timestamp, ensure_dir
from .achievement import achievement_manager

class LearningPath:
    """学习路径管理类"""
    
    def __init__(self):
        # 获取项目根目录和学习路径目录
        self._project_root = Path(settings.get('project_root'))
        self._paths_dir = self._project_root / settings.get('learning_paths_dir')
        self._paths_file = self._paths_dir / 'paths.json'
        self._current_path_file = self._paths_dir / 'current_path.json'
        self._current_path: Optional[Dict[str, Any]] = None
        self._ensure_paths_file()
        self._ensure_current_path_file()
    
    def _ensure_paths_file(self) -> None:
        """确保学习路径文件存在"""
        # 确保目录存在
        ensure_dir(self._paths_dir)
        
        if not self._paths_file.exists():
            default_paths = {
                "python-beginner": {
                    "id": "python-beginner",
                    "name": "Python入门之路",
                    "description": "从零开始学习Python编程",
                    "difficulty": "初级",
                    "estimated_time": "4周",
                    "stages": [
                        {
                            "name": "基础语法",
                            "steps": [
                                "变量和数据类型",
                                "控制流程",
                                "函数和模块"
                            ],
                            "resources": [
                                {
                                    "name": "Python官方文档",
                                    "url": "https://docs.python.org/zh-cn/3/"
                                },
                                {
                                    "name": "Python入门教程",
                                    "url": "https://www.runoob.com/python3/python3-tutorial.html"
                                }
                            ],
                            "projects": [
                                {
                                    "name": "数字游戏",
                                    "description": "创建一个简单的猜数字游戏"
                                },
                                {
                                    "name": "计算器",
                                    "description": "实现一个基础的命令行计算器"
                                }
                            ]
                        }
                    ]
                },
                "web-beginner": {
                    "id": "web-beginner",
                    "name": "网页设计入门",
                    "description": "学习HTML、CSS和JavaScript基础",
                    "difficulty": "初级",
                    "estimated_time": "6周",
                    "stages": [
                        {
                            "name": "HTML基础",
                            "steps": [
                                "HTML文档结构",
                                "常用标签",
                                "表单和表格"
                            ],
                            "resources": [
                                {
                                    "name": "MDN Web文档",
                                    "url": "https://developer.mozilla.org/zh-CN/"
                                }
                            ],
                            "projects": [
                                {
                                    "name": "个人主页",
                                    "description": "创建一个简单的个人介绍页面"
                                }
                            ]
                        }
                    ]
                },
                "project-beginner": {
                    "id": "project-beginner",
                    "name": "项目管理入门",
                    "description": "学习基本的项目管理知识和工具",
                    "difficulty": "初级",
                    "estimated_time": "3周",
                    "stages": [
                        {
                            "name": "版本控制",
                            "steps": [
                                "Git基础概念",
                                "常用Git命令",
                                "分支管理"
                            ],
                            "resources": [
                                {
                                    "name": "Git教程",
                                    "url": "https://www.liaoxuefeng.com/wiki/896043488029600"
                                }
                            ],
                            "projects": [
                                {
                                    "name": "项目实践",
                                    "description": "创建一个Git仓库并进行基本操作"
                                }
                            ]
                        }
                    ]
                }
            }
            
            with open(self._paths_file, 'w', encoding='utf-8') as f:
                json.dump(default_paths, f, ensure_ascii=False, indent=2)
    
    def _ensure_current_path_file(self):
        """确保当前路径文件存在"""
        if not self._current_path_file.exists():
            current_path = {
                "path_id": None,
                "current_stage": 0,
                "current_step": 0,
                "started_at": None,
                "last_updated": None
            }
            
            with open(self._current_path_file, 'w', encoding='utf-8') as f:
                json.dump(current_path, f, ensure_ascii=False, indent=2)
    
    def get_all_paths(self) -> List[Dict[str, Any]]:
        """获取所有学习路径"""
        if not self._paths_file.exists():
            self._ensure_paths_file()
        with open(self._paths_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [
            {
                'id': path['id'],
                'name': path['name'],
                'description': path['description'],
                'difficulty': path['difficulty'],
                'estimated_time': path['estimated_time']
            }
            for path in data['paths']
        ]
    
    def get_path_info(self, path_id: str) -> Optional[Dict[str, Any]]:
        """获取指定学习路径的信息"""
        with open(self._paths_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for path in data['paths']:
                if path['id'] == path_id:
                    return path
            return None
    
    def set_current_path(self, path_id: str) -> bool:
        """设置当前学习路径"""
        path = self.get_path_info(path_id)
        if not path:
            return False
        
        current_path = {
            "path_id": path_id,
            "current_stage": 0,
            "current_step": 0,
            "started_at": get_timestamp(),
            "last_updated": get_timestamp()
        }
        
        with open(self._current_path_file, 'w', encoding='utf-8') as f:
            json.dump(current_path, f, ensure_ascii=False, indent=2)
        
        # 触发成就检查
        achievement_manager.update_stats('path_started')
        
        return True
    
    def get_current_progress(self) -> Optional[Dict[str, Any]]:
        """获取当前学习进度"""
        if not self._current_path_file.exists():
            return None
        
        with open(self._current_path_file, 'r', encoding='utf-8') as f:
            current = json.load(f)
            
        if not current['path_id']:
            return None
        
        path = self.get_path_info(current['path_id'])
        if not path:
            return None
        
        total_steps = sum(len(stage['steps']) for stage in path['stages'])
        completed_steps = 0
        for i in range(current['current_stage']):
            completed_steps += len(path['stages'][i]['steps'])
        completed_steps += current['current_step']
        
        return {
            'path_id': current['path_id'],
            'path_name': path['name'],
            'current_stage': current['current_stage'],
            'current_stage_name': path['stages'][current['current_stage']]['name'],
            'current_step': current['current_step'],
            'current_step_name': path['stages'][current['current_stage']]['steps'][current['current_step']],
            'progress': f"{completed_steps}/{total_steps}",
            'percentage': round(completed_steps / total_steps * 100, 1)
        }
    
    def advance_progress(self) -> bool:
        """推进当前进度"""
        if not self._current_path_file.exists():
            return False
        
        with open(self._current_path_file, 'r', encoding='utf-8') as f:
            current = json.load(f)
        
        if not current['path_id']:
            return False
        
        path = self.get_path_info(current['path_id'])
        if not path:
            return False
        
        # 获取当前阶段
        stage = path['stages'][current['current_stage']]
        
        # 检查是否需要进入下一步或下一阶段
        if current['current_step'] + 1 < len(stage['steps']):
            # 进入下一步
            current['current_step'] += 1
        elif current['current_stage'] + 1 < len(path['stages']):
            # 进入下一阶段
            current['current_stage'] += 1
            current['current_step'] = 0
        else:
            # 学习路径已完成
            current['path_id'] = None
            # 触发成就检查
            achievement_manager.update_stats('path_completed')
        
        current['last_updated'] = get_timestamp()
        
        with open(self._current_path_file, 'w', encoding='utf-8') as f:
            json.dump(current, f, ensure_ascii=False, indent=2)
        
        return True
    
    def get_current_resources(self) -> List[Dict[str, str]]:
        """获取当前阶段的学习资源"""
        progress = self.get_current_progress()
        if not progress:
            return []
        
        path = self.get_path_info(progress['path_id'])
        if not path or not path['stages']:
            return []
        
        current_stage = int(progress['current_stage'])
        if current_stage >= len(path['stages']):
            return []
            
        stage = path['stages'][current_stage]
        return stage.get('resources', [])
    
    def get_current_projects(self) -> List[Dict[str, str]]:
        """获取当前阶段的练习项目"""
        progress = self.get_current_progress()
        if not progress:
            return []
        
        path = self.get_path_info(progress['path_id'])
        if not path or not path['stages']:
            return []
        
        current_stage = int(progress['current_stage'])
        if current_stage >= len(path['stages']):
            return []
            
        stage = path['stages'][current_stage]
        return stage.get('projects', [])

# 创建全局实例
learning_path_manager = LearningPath() 