"""
代码审查模块，提供代码风格、性能和安全性检查功能。
"""
import os
import ast
import json
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path
import subprocess
from datetime import datetime

class CodeReview:
    """代码审查类，用于检查代码质量和安全性。
    
    提供以下功能：
    1. 代码风格检查：行长度、缩进、文档字符串等
    2. 性能检查：函数复杂度、变量数量等
    3. 安全性检查：SQL注入、命令注入等
    """

    def __init__(self):
        """初始化代码审查类，设置配置目录和加载配置。"""
        self.config_dir = (
            Path.home() / 
            ".cursormind" / 
            "code_review"
        )
        self.config_dir.mkdir(parents=True, exist_ok=True)
        self.reports_dir = self.config_dir / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        self.config_file = self.config_dir / "config.json"
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """加载配置文件，如果不存在则创建默认配置。

        Returns:
            Dict[str, Any]: 配置字典
        """
        default_config = {
            "style": {
                "max_line_length": 88,
                "indent_size": 4,
                "quote_type": "double",
                "docstring_style": "google",
                "import_order": ["stdlib", "third_party", "local"]
            },
            "performance": {
                "max_complexity": 10,
                "max_locals": 15,
                "max_returns": 5,
                "max_statements": 50
            },
            "security": {
                "sql_risk_functions": [
                    "execute", "executemany", "raw_query"
                ],
                "shell_risk_functions": [
                    "system", "popen", "exec", "eval"
                ],
                "file_risk_functions": [
                    "open", "read", "write"
                ]
            }
        }

        if not self.config_file.exists():
            self._save_config(default_config)
            return default_config

        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
                # 验证配置文件结构
                if not all(
                    key in config 
                    for key in ["style", "performance", "security"]
                ):
                    raise ValueError("配置文件缺少必要的键")
                return config
        except Exception as e:
            print(f"加载配置文件时出错：{str(e)}，使用默认配置")
            self._save_config(default_config)
            return default_config

    def _save_config(self, config: Dict[str, Any]) -> None:
        """保存配置到文件。

        Args:
            config: 要保存的配置字典
        """
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存配置文件时出错：{str(e)}")

    def _safe_open(self, file_path: str, mode: str = "r") -> Optional[Path]:
        """安全地打开文件。
        
        Args:
            file_path: 要打开的文件路径
            mode: 打开模式
            
        Returns:
            Optional[Path]: 文件路径对象，如果不安全则返回 None
        """
        try:
            path = Path(file_path).resolve()
            is_safe = True
            
            # 基本检查
            is_safe = is_safe and path.exists() and path.is_file()
                
            # 权限检查
            if mode == "w":
                is_safe = (
                    is_safe and 
                    os.access(path.parent, os.W_OK) and
                    str(path).startswith(str(self.config_dir))
                )
            elif mode == "r":
                is_safe = is_safe and os.access(path, os.R_OK)
                    
            # 符号链接检查
            is_safe = is_safe and not path.is_symlink()
                
            # 文件大小检查
            is_safe = is_safe and path.stat().st_size <= 10 * 1024 * 1024  # 10MB
                
            return path if is_safe else None
            
        except (TypeError, ValueError, OSError):
            return None

    def _check_line_length(self, lines: List[str]) -> List[Dict[str, Any]]:
        """检查行长度。

        Args:
            lines: 代码行列表

        Returns:
            包含行长度问题的列表
        """
        issues = []
        max_length = self.config["style"]["max_line_length"]
        
        for i, line in enumerate(lines, 1):
            if len(line.rstrip()) > max_length:
                issues.append({
                    "type": "style",
                    "rule": "line_length",
                    "message": (
                        f"行长度超过 {max_length} "
                        "个字符"
                    ),
                    "line": i,
                    "severity": "warning"
                })
        
        return issues

    def _check_indentation(self, tree: ast.AST) -> List[Dict[str, Any]]:
        """检查缩进。

        Args:
            tree: AST树

        Returns:
            包含缩进问题的列表
        """
        issues = []
        indent_size = self.config["style"]["indent_size"]
        
        for node in ast.walk(tree):
            if isinstance(
                node, 
                (ast.FunctionDef, ast.ClassDef, ast.If, ast.For, ast.While)
            ):
                if (hasattr(node, "col_offset") and 
                    node.col_offset % indent_size != 0):
                    issues.append({
                        "type": "style",
                        "rule": "indentation",
                        "message": (
                            f"缩进应该是 {indent_size} "
                            "的倍数"
                        ),
                        "line": node.lineno,
                        "severity": "warning"
                    })
        
        return issues

    def _check_docstring(self, tree: ast.AST) -> List[Dict[str, Any]]:
        """检查文档字符串。

        Args:
            tree: AST树

        Returns:
            包含文档字符串问题的列表
        """
        issues = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Module)):
                if not ast.get_docstring(node):
                    issues.append({
                        "type": "style",
                        "rule": "docstring",
                        "message": "缺少文档字符串",
                        "line": node.lineno,
                        "severity": "info"
                    })
        
        return issues

    def _check_quotes(self, lines: List[str]) -> List[Dict[str, Any]]:
        """检查引号使用。

        Args:
            lines: 代码行列表

        Returns:
            包含引号使用问题的列表
        """
        issues = []
        quote_type = self.config["style"]["quote_type"]
        
        for i, line in enumerate(lines, 1):
            if quote_type == "double" and "'" in line and '"' not in line:
                issues.append({
                    "type": "style",
                    "rule": "quotes",
                    "message": "建议使用双引号",
                    "line": i,
                    "severity": "info"
                })
            elif quote_type == "single" and '"' in line and "'" not in line:
                issues.append({
                    "type": "style",
                    "rule": "quotes",
                    "message": "建议使用单引号",
                    "line": i,
                    "severity": "info"
                })
        
        return issues

    def check_style(self, content: str) -> List[Dict[str, Any]]:
        """检查代码风格。

        Args:
            content: 要检查的代码内容

        Returns:
            包含风格问题的列表
        """
        issues = []
        
        try:
            tree = ast.parse(content)
            lines = content.split("\n")
            
            # 检查行长度
            issues.extend(self._check_line_length(lines))
            
            # 检查缩进
            issues.extend(self._check_indentation(tree))
            
            # 检查文档字符串
            issues.extend(self._check_docstring(tree))
            
            # 检查引号使用
            issues.extend(self._check_quotes(lines))
                    
        except SyntaxError as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": e.lineno or 1,
                "severity": "error"
            })
        except Exception as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": 1,
                "severity": "error"
            })
        
        return issues

    def _check_complexity(self, node: ast.FunctionDef) -> Optional[Dict[str, Any]]:
        """检查函数复杂度。

        Args:
            node: 函数节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        complexity = 1
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.For, ast.While, ast.Try)):
                complexity += 1
        
        if complexity > self.config["performance"]["max_complexity"]:
            return {
                "type": "performance",
                "rule": "complexity",
                "message": (
                    f"函数复杂度为 {complexity}，超过最大值 "
                    f"{self.config['performance']['max_complexity']}"
                ),
                "line": node.lineno,
                "severity": "warning"
            }
        
        return None

    def _check_locals(self, node: ast.FunctionDef) -> Optional[Dict[str, Any]]:
        """检查局部变量数量。

        Args:
            node: 函数节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        locals_count = len([
            n for n in ast.walk(node) 
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)
        ])
        
        if locals_count > self.config["performance"]["max_locals"]:
            return {
                "type": "performance",
                "rule": "locals",
                "message": (
                    f"局部变量数量为 {locals_count}，超过最大值 "
                    f"{self.config['performance']['max_locals']}"
                ),
                "line": node.lineno,
                "severity": "warning"
            }
        
        return None

    def _check_returns(self, node: ast.FunctionDef) -> Optional[Dict[str, Any]]:
        """检查return语句数量。

        Args:
            node: 函数节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        returns = len([
            n for n in ast.walk(node) 
            if isinstance(n, ast.Return)
        ])
        
        if returns > self.config["performance"]["max_returns"]:
            return {
                "type": "performance",
                "rule": "returns",
                "message": (
                    f"return语句数量为 {returns}，超过最大值 "
                    f"{self.config['performance']['max_returns']}"
                ),
                "line": node.lineno,
                "severity": "warning"
            }
        
        return None

    def _check_statements(self, node: ast.FunctionDef) -> Optional[Dict[str, Any]]:
        """检查语句数量。

        Args:
            node: 函数节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        statements = len([
            n for n in ast.walk(node) 
            if isinstance(n, ast.stmt)
        ])
        
        if statements > self.config["performance"]["max_statements"]:
            return {
                "type": "performance",
                "rule": "statements",
                "message": (
                    f"语句数量为 {statements}，超过最大值 "
                    f"{self.config['performance']['max_statements']}"
                ),
                "line": node.lineno,
                "severity": "warning"
            }
        
        return None

    def check_performance(self, content: str) -> List[Dict[str, Any]]:
        """检查代码性能相关问题。

        Args:
            content: 要检查的代码内容

        Returns:
            包含性能问题的列表
        """
        issues = []
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # 检查函数复杂度
                    if issue := self._check_complexity(node):
                        issues.append(issue)
                    
                    # 检查局部变量数量
                    if issue := self._check_locals(node):
                        issues.append(issue)
                    
                    # 检查return语句数量
                    if issue := self._check_returns(node):
                        issues.append(issue)
                    
                    # 检查语句数量
                    if issue := self._check_statements(node):
                        issues.append(issue)
                        
        except SyntaxError as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": e.lineno or 1,
                "severity": "error"
            })
        except Exception as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": 1,
                "severity": "error"
            })
        
        return issues

    def _check_sql_injection(self, node: ast.Call) -> Optional[Dict[str, Any]]:
        """检查SQL注入风险。

        Args:
            node: 函数调用节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        if (isinstance(node.func, ast.Name) and 
            node.func.id in self.config["security"]["sql_risk_functions"]):
            return {
                "type": "security",
                "rule": "sql_injection",
                "message": "可能存在SQL注入风险",
                "line": node.lineno,
                "severity": "error"
            }
        
        return None

    def _check_command_injection(self, node: ast.Call) -> Optional[Dict[str, Any]]:
        """检查命令注入风险。

        Args:
            node: 函数调用节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        if (isinstance(node.func, ast.Name) and 
            node.func.id in self.config["security"]["shell_risk_functions"]):
            return {
                "type": "security",
                "rule": "command_injection",
                "message": "可能存在命令注入风险",
                "line": node.lineno,
                "severity": "error"
            }
        
        return None

    def _check_file_access(self, node: ast.Call) -> Optional[Dict[str, Any]]:
        """检查文件访问风险。

        Args:
            node: 函数调用节点

        Returns:
            如果存在问题则返回问题字典，否则返回 None
        """
        if (isinstance(node.func, ast.Name) and 
            node.func.id in self.config["security"]["file_risk_functions"]):
            return {
                "type": "security",
                "rule": "file_access",
                "message": "可能存在不安全的文件访问",
                "line": node.lineno,
                "severity": "warning"
            }
        
        return None

    def check_security(self, content: str) -> List[Dict[str, Any]]:
        """检查代码安全性问题。

        Args:
            content: 要检查的代码内容

        Returns:
            包含安全问题的列表
        """
        issues = []
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    # 检查SQL注入风险
                    if issue := self._check_sql_injection(node):
                        issues.append(issue)
                    
                    # 检查命令注入风险
                    if issue := self._check_command_injection(node):
                        issues.append(issue)
                    
                    # 检查文件访问风险
                    if issue := self._check_file_access(node):
                        issues.append(issue)
                        
        except SyntaxError as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": e.lineno or 1,
                "severity": "error"
            })
        except Exception as e:
            issues.append({
                "type": "error",
                "rule": "parsing",
                "message": f"解析代码时出错：{str(e)}",
                "line": 1,
                "severity": "error"
            })
        
        return issues

    def review_file(self, file_path: str) -> Dict[str, Any]:
        """审查单个文件。

        Args:
            file_path: 要审查的文件路径

        Returns:
            包含审查结果的字典
        """
        result = {
            "file": file_path,
            "time": datetime.now().isoformat(),
            "issues": []
        }

        # 检查文件访问权限
        path = self._safe_open(file_path)
        if not path:
            result["issues"].append({
                "type": "error",
                "rule": "file_access",
                "message": "无法访问文件",
                "line": 1,
                "severity": "error"
            })
            return result
        
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 检查文件是否为空
            if not content.strip():
                result["issues"].append({
                    "type": "error",
                    "rule": "empty_file",
                    "message": "文件为空",
                    "line": 1,
                    "severity": "error"
                })
                return result
            
            # 检查文件编码
            try:
                content.encode("utf-8").decode("utf-8")
            except UnicodeError:
                result["issues"].append({
                    "type": "error",
                    "rule": "encoding",
                    "message": "文件编码不是UTF-8",
                    "line": 1,
                    "severity": "error"
                })
                return result
            
            # 检查语法错误
            try:
                ast.parse(content)
            except SyntaxError as e:
                result["issues"].append({
                    "type": "error",
                    "rule": "syntax",
                    "message": f"语法错误：{str(e)}",
                    "line": e.lineno or 1,
                    "severity": "error"
                })
                return result
            
            # 进行代码审查
            result["issues"].extend(self.check_style(content))
            result["issues"].extend(self.check_performance(content))
            result["issues"].extend(self.check_security(content))
            
        except Exception as e:
            result["issues"].append({
                "type": "error",
                "rule": "file_read",
                "message": f"读取文件时出错：{str(e)}",
                "line": 1,
                "severity": "error"
            })
        
        return result

    def review_directory(self, directory: str) -> Dict[str, Any]:
        """审查目录中的所有Python文件。

        Args:
            directory: 要审查的目录路径

        Returns:
            包含审查结果的字典
        """
        try:
            path = Path(directory).resolve()
            if not path.exists() or not path.is_dir():
                return {
                    "directory": directory,
                    "time": datetime.now().isoformat(),
                    "issues": [{
                        "type": "error",
                        "rule": "directory_access",
                        "message": "无法访问目录",
                        "line": 1,
                        "severity": "error"
                    }]
                }
            
            issues = []
            files_reviewed = 0
            
            for file_path in path.rglob("*.py"):
                result = self.review_file(str(file_path))
                issues.extend(result["issues"])
                files_reviewed += 1
            
            # 统计问题分布
            issue_types = {}
            issue_severities = {}
            
            for issue in issues:
                issue_type = issue["type"]
                issue_severity = issue["severity"]
                
                issue_types[issue_type] = issue_types.get(
                    issue_type, 0
                ) + 1
                issue_severities[issue_severity] = issue_severities.get(
                    issue_severity, 0
                ) + 1
            
            return {
                "directory": directory,
                "time": datetime.now().isoformat(),
                "files_reviewed": files_reviewed,
                "total_issues": len(issues),
                "issue_types": issue_types,
                "issue_severities": issue_severities,
                "issues": issues
            }
            
        except Exception as e:
            return {
                "directory": directory,
                "time": datetime.now().isoformat(),
                "issues": [{
                    "type": "error",
                    "rule": "directory_review",
                    "message": f"审查目录时出错：{str(e)}",
                    "line": 1,
                    "severity": "error"
                }]
            }

    def save_report(self, report: Dict) -> str:
        """保存审查报告。
        
        Args:
            report: 要保存的报告
            
        Returns:
            str: 报告ID
        """
        report_id = datetime.now().strftime("%Y%m%d%H%M%S")
        report_file = self.reports_dir / f"report_{report_id}.json"
        
        path = self._safe_open(str(report_file), "w")
        if not path:
            return None
        
        with path.open("w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        return report_id

    def get_report(self, report_id: str) -> Optional[Dict]:
        """获取审查报告。
        
        Args:
            report_id: 报告ID
            
        Returns:
            Optional[Dict]: 报告内容，如果不存在则返回 None
        """
        report_file = self.reports_dir / f"report_{report_id}.json"
        path = self._safe_open(str(report_file))
        if not path:
            return None
        
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def list_reports(self) -> List[Dict]:
        """列出所有审查报告。
        
        Returns:
            List[Dict]: 报告列表
        """
        reports = []
        for report_file in self.reports_dir.glob("report_*.json"):
            path = self._safe_open(str(report_file))
            if not path:
                continue
            
            with path.open("r", encoding="utf-8") as f:
                report = json.load(f)
                reports.append({
                    "id": report_file.stem.replace("report_", ""),
                    "timestamp": report["timestamp"],
                    "target": report.get("file") or report.get("directory"),
                    "total_issues": (
                        report["summary"]["total_issues"]
                        if "total_issues" in report["summary"]
                        else len(report["issues"])
                    )
                })
        
        return sorted(reports, key=lambda x: x["timestamp"], reverse=True)

    def _calculate_stats(self, issues: List[Dict[str, Any]]) -> Dict[str, Any]:
        """计算问题统计信息。

        Args:
            issues: 问题列表

        Returns:
            包含统计信息的字典
        """
        stats = {
            "total": len(issues),
            "by_type": {},
            "by_severity": {},
            "by_rule": {}
        }
        
        for issue in issues:
            # 按类型统计
            issue_type = issue.get("type", "unknown")
            stats["by_type"][issue_type] = stats["by_type"].get(issue_type, 0) + 1
            
            # 按严重程度统计
            severity = issue.get("severity", "unknown")
            stats["by_severity"][severity] = stats["by_severity"].get(severity, 0) + 1
            
            # 按规则统计
            rule = issue.get("rule", "unknown")
            stats["by_rule"][rule] = stats["by_rule"].get(rule, 0) + 1
        
        return stats

code_review = CodeReview() 