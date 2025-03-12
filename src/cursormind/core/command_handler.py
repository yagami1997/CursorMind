"""
命令处理核心模块
"""
from typing import Dict, Callable, Any, Optional
import logging

class CommandHandler:
    """命令处理器类"""
    
    def __init__(self):
        self._commands: Dict[str, Callable] = {}
        self._logger = logging.getLogger(__name__)

    def register(self, name: str) -> Callable:
        """
        命令注册装饰器

        Args:
            name: 命令名称

        Returns:
            装饰器函数
        """
        def decorator(func: Callable) -> Callable:
            self._commands[name] = func
            self._logger.debug(f"注册命令: {name}")
            return func
        return decorator

    def execute(self, name: str, *args: Any, **kwargs: Any) -> Optional[Any]:
        """
        执行命令

        Args:
            name: 命令名称
            args: 位置参数
            kwargs: 关键字参数

        Returns:
            命令执行结果

        Raises:
            KeyError: 命令不存在时抛出
        """
        if name not in self._commands:
            raise KeyError(f"未知命令: {name}")
        
        try:
            self._logger.info(f"执行命令: {name}")
            return self._commands[name](*args, **kwargs)
        except Exception as e:
            self._logger.error(f"命令执行失败: {name}, 错误: {str(e)}")
            raise

# 创建全局命令处理器实例
handler = CommandHandler() 