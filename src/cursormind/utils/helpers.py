"""
辅助函数模块 - 提供常用的工具函数 🛠️
"""
import os
from datetime import datetime
from pathlib import Path
from typing import Optional, Union
import pytz
from ..config.settings import settings

def get_timestamp(timezone: str = 'America/Los_Angeles') -> str:
    """
    获取当前时间戳
    :param timezone: 时区名称
    :return: 格式化的时间戳字符串
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    return now.strftime("%Y-%m-%d %H:%M:%S %Z")

def ensure_dir(path: Union[str, Path]) -> Path:
    """
    确保目录存在，如果不存在则创建
    :param path: 目录路径（字符串或Path对象）
    :return: 目录路径
    """
    path_obj = Path(path) if isinstance(path, str) else path
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj

def format_path(path: str) -> Path:
    """
    格式化路径字符串为Path对象
    :param path: 路径字符串
    :return: Path对象
    """
    return Path(os.path.expanduser(path))

def get_relative_path(path: Path, base: Path) -> str:
    """
    获取相对路径
    :param path: 目标路径
    :param base: 基准路径
    :return: 相对路径字符串
    """
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)

def get_project_root() -> Path:
    """
    获取项目根目录

    Returns:
        项目根目录的Path对象
    """
    return Path(settings.get('project_root'))

def load_template(template_name: str) -> str:
    """
    加载模板文件内容

    Args:
        template_name: 模板文件名

    Returns:
        模板文件内容

    Raises:
        FileNotFoundError: 模板文件不存在时抛出
    """
    template_path = get_project_root() / settings.get('templates_dir') / template_name
    if not template_path.exists():
        raise FileNotFoundError(f"模板文件不存在: {template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def save_file(content: str, file_path: str) -> None:
    """
    保存内容到文件

    Args:
        content: 文件内容
        file_path: 文件路径
    """
    path_obj = Path(file_path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path_obj, 'w', encoding='utf-8') as f:
        f.write(content) 