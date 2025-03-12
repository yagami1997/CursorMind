"""
Cursor 规范框架核心模块
"""
import os
import json
from typing import Dict, List, Optional
from datetime import datetime
from pathlib import Path

class CursorFramework:
    def __init__(self):
        self.config_dir = Path.home() / '.cursormind' / 'cursor_framework'
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.templates_dir = self.config_dir / 'templates'
        self.templates_dir.mkdir(exist_ok=True)
        self.rules_file = self.config_dir / 'rules.json'
        self._load_rules()

    def _load_rules(self):
        """加载规范规则"""
        if not self.rules_file.exists():
            self.rules = {
                "project_structure": {
                    "required_dirs": ["src", "tests", "docs", "scripts"],
                    "required_files": ["README.md", "LICENSE", "setup.py", "requirements.txt"]
                },
                "code_style": {
                    "python": {
                        "line_length": 88,
                        "indent": 4,
                        "quotes": "double",
                        "docstring": "google"
                    }
                },
                "git": {
                    "commit_types": [
                        "feat", "fix", "docs", "style", "refactor",
                        "perf", "test", "build", "ci", "chore"
                    ],
                    "commit_format": "<type>(<scope>): <subject>",
                    "branch_format": {
                        "feature": "feature/<name>",
                        "bugfix": "bugfix/<name>",
                        "hotfix": "hotfix/<name>",
                        "release": "release/<version>"
                    }
                },
                "documentation": {
                    "required_sections": [
                        "项目简介",
                        "快速开始",
                        "安装指南",
                        "使用说明",
                        "API文档",
                        "贡献指南"
                    ]
                }
            }
            self._save_rules()
        else:
            with open(self.rules_file, 'r', encoding='utf-8') as f:
                self.rules = json.load(f)

    def _save_rules(self):
        """保存规范规则"""
        with open(self.rules_file, 'w', encoding='utf-8') as f:
            json.dump(self.rules, f, ensure_ascii=False, indent=2)

    def check_project_structure(self, project_path: str) -> Dict[str, List[str]]:
        """检查项目结构是否符合规范"""
        issues = {
            "missing_dirs": [],
            "missing_files": []
        }
        
        for required_dir in self.rules["project_structure"]["required_dirs"]:
            if not os.path.exists(os.path.join(project_path, required_dir)):
                issues["missing_dirs"].append(required_dir)
        
        for required_file in self.rules["project_structure"]["required_files"]:
            if not os.path.exists(os.path.join(project_path, required_file)):
                issues["missing_files"].append(required_file)
        
        return issues

    def validate_commit_message(self, message: str) -> Dict[str, bool]:
        """验证提交信息是否符合规范"""
        result = {
            "valid": False,
            "type_valid": False,
            "format_valid": False
        }
        
        # 检查是否为空
        if not message:
            return result
        
        # 检查格式
        parts = message.split(":")
        if len(parts) != 2:
            return result
        
        commit_type = parts[0].strip().lower()
        if "(" in commit_type:
            commit_type = commit_type.split("(")[0]
        
        # 检查类型
        result["type_valid"] = commit_type in self.rules["git"]["commit_types"]
        
        # 检查格式是否符合规范
        result["format_valid"] = (
            len(parts[1].strip()) > 0 and  # 描述不能为空
            len(parts[1].strip()) <= 72    # 描述不能太长
        )
        
        result["valid"] = result["type_valid"] and result["format_valid"]
        return result

    def validate_branch_name(self, branch_name: str) -> Dict[str, bool]:
        """验证分支名称是否符合规范"""
        result = {
            "valid": False,
            "type_valid": False,
            "format_valid": False
        }
        
        if not branch_name or "/" not in branch_name:
            return result
        
        branch_type = branch_name.split("/")[0]
        
        # 检查分支类型
        result["type_valid"] = branch_type in self.rules["git"]["branch_format"]
        
        # 检查分支格式
        if result["type_valid"]:
            expected_format = self.rules["git"]["branch_format"][branch_type]
            format_parts = expected_format.split("/")
            branch_parts = branch_name.split("/")
            
            result["format_valid"] = (
                len(branch_parts) == len(format_parts) and
                branch_parts[0] == format_parts[0] and
                len(branch_parts[1]) > 0
            )
        
        result["valid"] = result["type_valid"] and result["format_valid"]
        return result

    def generate_project_template(self, project_path: str, template_name: str = "default") -> bool:
        """生成项目模板"""
        try:
            # 创建必要的目录
            for dir_name in self.rules["project_structure"]["required_dirs"]:
                os.makedirs(os.path.join(project_path, dir_name), exist_ok=True)
            
            # 创建必要的文件
            for file_name in self.rules["project_structure"]["required_files"]:
                file_path = os.path.join(project_path, file_name)
                if not os.path.exists(file_path):
                    with open(file_path, 'w', encoding='utf-8') as f:
                        if file_name == "README.md":
                            f.write(self._generate_readme_template())
                        elif file_name == "setup.py":
                            f.write(self._generate_setup_template())
                        elif file_name == "requirements.txt":
                            f.write("# Project dependencies\n")
            
            return True
        except Exception as e:
            print(f"Error generating project template: {e}")
            return False

    def _generate_readme_template(self) -> str:
        """生成 README 模板"""
        sections = self.rules["documentation"]["required_sections"]
        template = "# 项目名称\n\n"
        
        for section in sections:
            template += f"## {section}\n\n"
        
        return template

    def _generate_setup_template(self) -> str:
        """生成 setup.py 模板"""
        return '''from setuptools import setup, find_packages

setup(
    name="your-project-name",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 在这里列出你的项目依赖
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
'''

cursor_framework = CursorFramework() 