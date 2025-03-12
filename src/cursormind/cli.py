"""
命令行接口模块 - 你的学习助手入口 🚀
"""
import click
from typing import Dict, List, Optional
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
from cursormind.core.learning_path import learning_path_manager
from cursormind.core.note_manager import note_manager
from cursormind.core.achievement import achievement_manager
from cursormind.core.cursor_framework import cursor_framework
from cursormind.core.project_manager import project_manager
from cursormind.core.code_review import CodeReview
from cursormind.config.settings import settings
from cursormind import __version__

console = Console()

@click.group()
@click.version_option(version=__version__)
def main():
    """CursorMind - 你的智能学习助手 📚"""
    pass

@main.group(name='cursor')
def cursor():
    """Cursor 规范框架 🎯"""
    pass

@cursor.command(name='init')
@click.argument('project_path', type=click.Path(exists=True), default='.')
@click.option('--template', '-t', default='default', help='项目模板名称')
def cursor_init(project_path: str, template: str):
    """初始化项目结构"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console
    ) as progress:
        progress.add_task("正在生成项目结构...", total=None)
        if cursor_framework.generate_project_template(project_path, template):
            console.print("[green]✨ 项目结构初始化成功！[/green]")
        else:
            console.print("[red]❌ 项目结构初始化失败[/red]")

@cursor.command(name='check')
@click.argument('project_path', type=click.Path(exists=True), default='.')
def cursor_check(project_path: str):
    """检查项目结构是否符合规范"""
    issues = cursor_framework.check_project_structure(project_path)
    
    if not issues["missing_dirs"] and not issues["missing_files"]:
        console.print("[green]✨ 项目结构符合规范！[/green]")
        return
    
    console.print("[yellow]⚠️ 发现以下问题：[/yellow]")
    
    if issues["missing_dirs"]:
        console.print("\n[red]缺少必要的目录：[/red]")
        for dir_name in issues["missing_dirs"]:
            console.print(f"- {dir_name}")
    
    if issues["missing_files"]:
        console.print("\n[red]缺少必要的文件：[/red]")
        for file_name in issues["missing_files"]:
            console.print(f"- {file_name}")

@cursor.command(name='commit')
@click.argument('message')
def cursor_commit(message: str):
    """验证提交信息是否符合规范"""
    result = cursor_framework.validate_commit_message(message)
    
    if result["valid"]:
        console.print("[green]✨ 提交信息符合规范！[/green]")
    else:
        console.print("[red]❌ 提交信息不符合规范[/red]")
        if not result["type_valid"]:
            console.print("\n提交类型必须是以下之一：")
            for type_ in cursor_framework.rules["git"]["commit_types"]:
                console.print(f"- {type_}")
        if not result["format_valid"]:
            console.print(f"\n提交格式必须符合：[yellow]{cursor_framework.rules['git']['commit_format']}[/yellow]")
            console.print("示例：feat(user): add login function")

@cursor.command(name='branch')
@click.argument('branch_name')
def cursor_branch(branch_name: str):
    """验证分支名称是否符合规范"""
    result = cursor_framework.validate_branch_name(branch_name)
    
    if result["valid"]:
        console.print("[green]✨ 分支名称符合规范！[/green]")
    else:
        console.print("[red]❌ 分支名称不符合规范[/red]")
        console.print("\n分支名称格式必须符合：")
        for type_, format_ in cursor_framework.rules["git"]["branch_format"].items():
            console.print(f"- {type_}: {format_}")
            console.print(f"  示例：{format_.replace('<name>', 'login')}")

@main.group(name='path')
def path():
    """学习路径管理 🗺️"""
    pass

@path.command(name='list')
def path_list():
    """列出所有可用的学习路径"""
    paths = learning_path_manager.get_all_paths()
    
    table = Table(title="可用的学习路径")
    table.add_column("ID", style="cyan")
    table.add_column("名称", style="green")
    table.add_column("描述", style="blue")
    table.add_column("难度", style="yellow")
    table.add_column("预计时间", style="magenta")
    
    for path in paths:
        table.add_row(
            path['id'],
            path['name'],
            path['description'],
            path['difficulty'],
            path['estimated_time']
        )
    
    console.print(table)

@path.command(name='start')
@click.argument('path_id')
def path_start(path_id: str):
    """开始一个学习路径"""
    if learning_path_manager.set_current_path(path_id):
        progress = learning_path_manager.get_current_progress()
        console.print(f"[green]✨ 成功开始学习路径：{progress['path_name']}[/green]")
        console.print(f"\n当前阶段：[yellow]{progress['current_stage_name']}[/yellow]")
        console.print(f"当前任务：[blue]{progress['current_step_name']}[/blue]")
        
        # 显示学习资源
        resources = learning_path_manager.get_current_resources()
        if resources:
            console.print("\n📚 推荐学习资源：")
            for resource in resources:
                console.print(f"- {resource['name']}: {resource['url']}")
        
        # 显示练习项目
        projects = learning_path_manager.get_current_projects()
        if projects:
            console.print("\n🎯 练习项目：")
            for project in projects:
                console.print(f"- {project['name']}: {project['description']}")
    else:
        console.print(f"[red]❌ 未找到ID为 {path_id} 的学习路径[/red]")

@path.command(name='status')
def path_status():
    """查看当前学习进度"""
    progress = learning_path_manager.get_current_progress()
    if progress:
        console.print(f"\n📊 当前学习进度：[green]{progress['path_name']}[/green]")
        console.print(f"阶段：[yellow]{progress['current_stage_name']}[/yellow]")
        console.print(f"任务：[blue]{progress['current_step_name']}[/blue]")
        console.print(f"完成度：[magenta]{progress['progress']} ({progress['percentage']}%)[/magenta]")
        
        # 显示当前阶段的资源和项目
        resources = learning_path_manager.get_current_resources()
        if resources:
            console.print("\n📚 当前阶段学习资源：")
            for resource in resources:
                console.print(f"- {resource['name']}: {resource['url']}")
        
        projects = learning_path_manager.get_current_projects()
        if projects:
            console.print("\n🎯 当前阶段练习项目：")
            for project in projects:
                console.print(f"- {project['name']}: {project['description']}")
    else:
        console.print("[yellow]⚠️ 你还没有开始任何学习路径[/yellow]")
        console.print("使用 [green]cursormind path list[/green] 查看可用的学习路径")
        console.print("使用 [green]cursormind path start <路径ID>[/green] 开始学习")

@path.command(name='next')
def path_next():
    """完成当前任务，进入下一个任务"""
    progress_before = learning_path_manager.get_current_progress()
    if not progress_before:
        console.print("[yellow]⚠️ 你还没有开始任何学习路径[/yellow]")
        return
    
    if learning_path_manager.advance_progress():
        progress = learning_path_manager.get_current_progress()
        console.print(f"[green]✨ 恭喜完成任务：{progress_before['current_step_name']}[/green]")
        if progress:
            console.print(f"\n下一个任务：[blue]{progress['current_step_name']}[/blue]")
            
            # 显示新任务的资源和项目
            resources = learning_path_manager.get_current_resources()
            if resources:
                console.print("\n📚 推荐学习资源：")
                for resource in resources:
                    console.print(f"- {resource['name']}: {resource['url']}")
            
            projects = learning_path_manager.get_current_projects()
            if projects:
                console.print("\n🎯 练习项目：")
                for project in projects:
                    console.print(f"- {project['name']}: {project['description']}")
        else:
            console.print("[yellow]🎉 恭喜！你已经完成了当前学习路径的所有任务！[/yellow]")

@main.group(name='note')
def note():
    """笔记管理 📝"""
    pass

@note.command(name='add')
@click.argument('content')
@click.option('--topic', '-t', default='general', help='笔记主题')
def note_add(content: str, topic: str):
    """添加新笔记"""
    note = note_manager.add_note(content, topic)
    console.print(f"[green]✨ 笔记已保存！[/green]")
    console.print(f"ID: [blue]{note['id']}[/blue]")
    console.print(f"主题: [yellow]{note['topic']}[/yellow]")
    if note['tags']:
        console.print(f"标签: [magenta]{', '.join(note['tags'])}[/magenta]")

@note.command(name='today')
def note_today():
    """查看今天的笔记"""
    notes = note_manager.get_daily_notes()
    if notes:
        console.print("\n📝 今日笔记：")
        for note in notes:
            console.print(f"\n[blue]{note['created_at']}[/blue]")
            console.print(f"[yellow]主题：{note['topic']}[/yellow]")
            if note['tags']:
                console.print(f"[magenta]标签：{', '.join(note['tags'])}[/magenta]")
            console.print(Markdown(note['content']))
    else:
        console.print("[yellow]今天还没有记录笔记哦～[/yellow]")

@note.command(name='topic')
@click.argument('topic')
def note_topic(topic: str):
    """查看指定主题的笔记"""
    notes = note_manager.get_topic_notes(topic)
    if notes:
        console.print(f"\n📚 主题 [green]{topic}[/green] 的笔记：")
        for note in notes:
            console.print(f"\n[blue]{note['created_at']}[/blue]")
            if note['tags']:
                console.print(f"[magenta]标签：{', '.join(note['tags'])}[/magenta]")
            console.print(Markdown(note['content']))
    else:
        console.print(f"[yellow]还没有 {topic} 主题的笔记～[/yellow]")

@note.command(name='search')
@click.argument('query')
def note_search(query: str):
    """搜索笔记"""
    notes = note_manager.search_notes(query)
    if notes:
        console.print(f"\n🔍 搜索结果：")
        for note in notes:
            console.print(f"\n[blue]{note['created_at']}[/blue]")
            console.print(f"[yellow]主题：{note['topic']}[/yellow]")
            if note['tags']:
                console.print(f"[magenta]标签：{', '.join(note['tags'])}[/magenta]")
            console.print(Markdown(note['content']))
    else:
        console.print(f"[yellow]没有找到匹配的笔记～[/yellow]")

@note.command(name='stats')
def note_stats():
    """查看笔记统计信息"""
    stats = note_manager.get_stats()
    
    console.print("\n📊 笔记统计：")
    console.print(f"总笔记数：[blue]{stats['total_notes']}[/blue] 条")
    console.print(f"总字数：[blue]{stats['total_words']}[/blue] 字")
    console.print(f"连续记录：[green]{stats['daily_streak']}[/green] 天")
    
    if stats['topics']:
        console.print("\n📚 主题分布：")
        topics_table = Table(show_header=False)
        topics_table.add_column("主题", style="yellow")
        topics_table.add_column("数量", style="cyan", justify="right")
        for topic, count in sorted(stats['topics'].items(), key=lambda x: x[1], reverse=True):
            topics_table.add_row(topic, str(count))
        console.print(topics_table)
    
    if stats['tags']:
        console.print("\n🏷️ 常用标签：")
        tags_table = Table(show_header=False)
        tags_table.add_column("标签", style="magenta")
        tags_table.add_column("使用次数", style="cyan", justify="right")
        for tag, count in sorted(stats['tags'].items(), key=lambda x: x[1], reverse=True)[:10]:
            tags_table.add_row(tag, str(count))
        console.print(tags_table)

@note.command(name='review')
@click.option('--days', '-d', default=7, help='要回顾的天数')
def note_review(days: int):
    """生成学习回顾报告"""
    review = note_manager.generate_review(days)
    
    console.print(f"\n📅 学习回顾：{review['period']}")
    console.print(f"记录笔记：[blue]{review['total_notes']}[/blue] 条")
    console.print(f"总字数：[blue]{review['total_words']}[/blue] 字")
    
    if review['topics']:
        console.print("\n📚 主题分布：")
        topics_table = Table(show_header=False)
        topics_table.add_column("主题", style="yellow")
        topics_table.add_column("数量", style="cyan", justify="right")
        for topic, count in sorted(review['topics'].items(), key=lambda x: x[1], reverse=True):
            topics_table.add_row(topic, str(count))
        console.print(topics_table)
    
    if review['tags']:
        console.print("\n🏷️ 常用标签：")
        tags_table = Table(show_header=False)
        tags_table.add_column("标签", style="magenta")
        tags_table.add_column("使用次数", style="cyan", justify="right")
        for tag, count in sorted(review['tags'].items(), key=lambda x: x[1], reverse=True)[:10]:
            tags_table.add_row(tag, str(count))
        console.print(tags_table)
    
    if review['highlights']:
        console.print("\n✨ 学习亮点：")
        for note in review['highlights']:
            console.print(f"\n[blue]{note['created_at']}[/blue]")
            console.print(f"[yellow]主题：{note['topic']}[/yellow]")
            if note['tags']:
                console.print(f"[magenta]标签：{', '.join(note['tags'])}[/magenta]")
            console.print(Markdown(note['content']))

@main.group(name='achievement')
def achievement():
    """成就系统 🏆"""
    pass

@achievement.command(name='list')
@click.option('--all', '-a', is_flag=True, help='显示所有成就，包括未解锁的')
def achievement_list(all: bool):
    """查看成就列表"""
    achievements = achievement_manager.get_achievements(include_locked=all)
    
    console.print("\n🏆 成就系统")
    stats = achievement_manager.get_stats()
    console.print(f"总积分：[green]{stats['points']}[/green] 分")
    console.print(f"已解锁：[blue]{len(stats['unlocked_achievements'])}[/blue] 个成就\n")
    
    for category, category_achievements in achievements.items():
        if category_achievements:
            console.print(f"\n[yellow]== {category.upper()} ==[/yellow]")
            for achievement_id, achievement in category_achievements.items():
                status = "[green]✓[/green]" if achievement['unlocked'] else "[grey]✗[/grey]"
                console.print(
                    f"{status} {achievement['icon']} [{'green' if achievement['unlocked'] else 'grey'}"
                    f"]{achievement['name']}[/{'green' if achievement['unlocked'] else 'grey'}]"
                )
                console.print(f"   {achievement['description']}")
                console.print(f"   奖励：[yellow]{achievement['reward']}[/yellow] 分")

@achievement.command(name='stats')
def achievement_stats():
    """查看成就统计"""
    stats = achievement_manager.get_stats()
    
    console.print("\n📊 学习统计")
    console.print(f"总积分：[green]{stats['points']}[/green] 分")
    console.print(f"解锁成就：[blue]{len(stats['unlocked_achievements'])}[/blue] 个")
    
    stats_data = stats['stats']
    console.print("\n[yellow]== 学习路径 ==[/yellow]")
    console.print(f"开始的路径：[blue]{stats_data['paths_started']}[/blue] 个")
    console.print(f"完成的路径：[green]{stats_data['paths_completed']}[/green] 个")
    
    console.print("\n[yellow]== 笔记记录 ==[/yellow]")
    console.print(f"笔记总数：[blue]{stats_data['notes_created']}[/blue] 条")
    console.print(f"连续记录：[green]{stats_data['daily_streak']}[/green] 天")
    console.print(f"使用的标签：[magenta]{len(stats_data['unique_tags'])}[/magenta] 个")
    console.print(f"涉及的主题：[cyan]{len(stats_data['unique_topics'])}[/cyan] 个")
    
    console.print("\n[yellow]== 学习回顾 ==[/yellow]")
    console.print(f"生成的回顾报告：[blue]{stats_data['reviews_generated']}[/blue] 次")
    
    console.print(f"\n最后更新：[grey]{stats['last_updated']}[/grey]")

@main.group(name='project')
def project():
    """项目管理 📋"""
    pass

@project.command(name='create')
@click.argument('title')
@click.option('--type', '-t', 'type_', help='任务类型')
@click.option('--priority', '-p', help='优先级')
@click.option('--assignee', '-a', help='负责人')
@click.option('--description', '-d', help='任务描述')
@click.option('--deadline', help='截止日期 (YYYY-MM-DD)')
@click.option('--tags', help='标签（逗号分隔）')
def project_create(title: str, type_: str, priority: str, assignee: str,
                  description: str, deadline: str, tags: str):
    """创建新任务"""
    kwargs = {}
    if type_:
        kwargs['type'] = type_
    if priority:
        kwargs['priority'] = priority
    if assignee:
        kwargs['assignee'] = assignee
    if description:
        kwargs['description'] = description
    if deadline:
        kwargs['deadline'] = deadline
    if tags:
        kwargs['tags'] = [tag.strip() for tag in tags.split(',')]
    
    task = project_manager.create_task(title, **kwargs)
    console.print(f"[green]✨ 任务创建成功！[/green]")
    _print_task_details(task)

@project.command(name='list')
@click.option('--status', '-s', help='任务状态')
@click.option('--priority', '-p', help='优先级')
@click.option('--type', '-t', 'type_', help='任务类型')
@click.option('--assignee', '-a', help='负责人')
@click.option('--tags', help='标签（逗号分隔）')
def project_list(status: str, priority: str, type_: str, assignee: str, tags: str):
    """列出任务"""
    tags_list = [tag.strip() for tag in tags.split(',')] if tags else None
    tasks = project_manager.list_tasks(
        status=status,
        priority=priority,
        type_=type_,
        assignee=assignee,
        tags=tags_list
    )
    
    if not tasks:
        console.print("[yellow]没有找到匹配的任务[/yellow]")
        return
    
    table = Table(title="任务列表")
    table.add_column("ID", style="cyan")
    table.add_column("标题", style="green")
    table.add_column("状态", style="yellow")
    table.add_column("优先级", style="red")
    table.add_column("类型", style="blue")
    table.add_column("负责人", style="magenta")
    table.add_column("截止日期", style="cyan")
    
    for task in tasks:
        table.add_row(
            task['id'],
            task['title'],
            task['status'],
            task['priority'],
            task['type'],
            task['assignee'] or '-',
            task['deadline'] or '-'
        )
    
    console.print(table)

@project.command(name='show')
@click.argument('task_id')
def project_show(task_id: str):
    """查看任务详情"""
    task = project_manager.get_task(task_id)
    if not task:
        console.print(f"[red]未找到任务：{task_id}[/red]")
        return
    
    _print_task_details(task)

@project.command(name='update')
@click.argument('task_id')
@click.option('--title', '-t', help='任务标题')
@click.option('--status', '-s', help='任务状态')
@click.option('--priority', '-p', help='优先级')
@click.option('--type', 'type_', help='任务类型')
@click.option('--assignee', '-a', help='负责人')
@click.option('--description', '-d', help='任务描述')
@click.option('--deadline', help='截止日期 (YYYY-MM-DD)')
@click.option('--tags', help='标签（逗号分隔）')
def project_update(task_id: str, **kwargs):
    """更新任务"""
    if kwargs.get('tags'):
        kwargs['tags'] = [tag.strip() for tag in kwargs['tags'].split(',')]
    
    task = project_manager.update_task(task_id, **{k: v for k, v in kwargs.items() if v is not None})
    if not task:
        console.print(f"[red]未找到任务：{task_id}[/red]")
        return
    
    console.print(f"[green]✨ 任务更新成功！[/green]")
    _print_task_details(task)

@project.command(name='subtask')
@click.argument('task_id')
@click.argument('title')
@click.option('--status', '-s', help='任务状态')
def project_subtask(task_id: str, title: str, status: str):
    """添加子任务"""
    kwargs = {}
    if status:
        kwargs['status'] = status
    
    subtask = project_manager.add_subtask(task_id, title, **kwargs)
    if not subtask:
        console.print(f"[red]未找到任务：{task_id}[/red]")
        return
    
    console.print(f"[green]✨ 子任务添加成功！[/green]")
    console.print(f"ID: [blue]{subtask['id']}[/blue]")
    console.print(f"标题: [green]{subtask['title']}[/green]")
    console.print(f"状态: [yellow]{subtask['status']}[/yellow]")

@project.command(name='note')
@click.argument('task_id')
@click.argument('content')
def project_note(task_id: str, content: str):
    """添加任务笔记"""
    note = project_manager.add_note(task_id, content)
    if not note:
        console.print(f"[red]未找到任务：{task_id}[/red]")
        return
    
    console.print(f"[green]✨ 笔记添加成功！[/green]")
    console.print(f"ID: [blue]{note['id']}[/blue]")
    console.print(f"内容: [green]{note['content']}[/green]")
    console.print(f"时间: [yellow]{note['created_at']}[/yellow]")

@project.command(name='link')
@click.argument('task_id')
@click.argument('related_task_id')
def project_link(task_id: str, related_task_id: str):
    """关联任务"""
    if project_manager.link_tasks(task_id, related_task_id):
        console.print(f"[green]✨ 任务关联成功！[/green]")
    else:
        console.print(f"[red]任务关联失败，请检查任务ID是否正确[/red]")

@project.command(name='stats')
def project_stats():
    """查看任务统计"""
    stats = project_manager.get_task_stats()
    
    console.print("\n📊 任务统计")
    console.print(f"总任务数：[blue]{stats['total_tasks']}[/blue]")
    console.print(f"完成率：[green]{stats['completion_rate']:.1f}%[/green]")
    console.print(f"平均完成时间：[yellow]{stats['average_completion_time']:.1f} 天[/yellow]")
    
    if stats['status_counts']:
        console.print("\n[cyan]== 状态分布 ==[/cyan]")
        for status, count in stats['status_counts'].items():
            console.print(f"{status}: [blue]{count}[/blue]")
    
    if stats['priority_counts']:
        console.print("\n[cyan]== 优先级分布 ==[/cyan]")
        for priority, count in stats['priority_counts'].items():
            console.print(f"{priority}: [blue]{count}[/blue]")
    
    if stats['type_counts']:
        console.print("\n[cyan]== 类型分布 ==[/cyan]")
        for type_, count in stats['type_counts'].items():
            console.print(f"{type_}: [blue]{count}[/blue]")
    
    if stats['assignee_counts']:
        console.print("\n[cyan]== 负责人分布 ==[/cyan]")
        for assignee, count in stats['assignee_counts'].items():
            console.print(f"{assignee}: [blue]{count}[/blue]")
    
    if stats['tag_counts']:
        console.print("\n[cyan]== 标签统计 ==[/cyan]")
        for tag, count in sorted(stats['tag_counts'].items(), key=lambda x: x[1], reverse=True)[:10]:
            console.print(f"{tag}: [blue]{count}[/blue]")

def _print_task_details(task: Dict):
    """打印任务详情"""
    console.print(f"\n[cyan]== 任务详情 ==[/cyan]")
    console.print(f"ID: [blue]{task['id']}[/blue]")
    console.print(f"标题: [green]{task['title']}[/green]")
    console.print(f"状态: [yellow]{task['status']}[/yellow]")
    console.print(f"优先级: [red]{task['priority']}[/red]")
    console.print(f"类型: [magenta]{task['type']}[/magenta]")
    
    if task['description']:
        console.print("\n[cyan]描述:[/cyan]")
        console.print(Markdown(task['description']))
    
    if task['assignee']:
        console.print(f"负责人: [blue]{task['assignee']}[/blue]")
    
    if task['deadline']:
        console.print(f"截止日期: [yellow]{task['deadline']}[/yellow]")
    
    if task['tags']:
        console.print(f"标签: [magenta]{', '.join(task['tags'])}[/magenta]")
    
    if task['subtasks']:
        console.print("\n[cyan]子任务:[/cyan]")
        for subtask in task['subtasks']:
            status_color = "green" if subtask['status'] == "已完成" else "yellow"
            console.print(
                f"- [{status_color}]{subtask['status']}[/{status_color}] "
                f"{subtask['title']} [blue]({subtask['id']})[/blue]"
            )
    
    if task['notes']:
        console.print("\n[cyan]笔记:[/cyan]")
        for note in task['notes']:
            console.print(f"\n[blue]{note['created_at']}[/blue]")
            console.print(Markdown(note['content']))
    
    if task['related_tasks']:
        console.print("\n[cyan]关联任务:[/cyan]")
        for related_id in task['related_tasks']:
            related_task = project_manager.get_task(related_id)
            if related_task:
                console.print(
                    f"- [blue]{related_id}[/blue]: "
                    f"[green]{related_task['title']}[/green] "
                    f"([yellow]{related_task['status']}[/yellow])"
                )

@main.group(name='review')
def review():
    """代码审查 🔍"""
    pass

@review.command(name='file')
@click.argument('file_path', type=click.Path(exists=True))
def review_file(file_path):
    """审查单个文件。

    Args:
        file_path: 要审查的文件路径
    """
    try:
        reviewer = CodeReview()
        with console.status("正在审查文件..."):
            report = reviewer.review_file(file_path)
        
        console.print("\n== 文件审查报告 ==")
        console.print(f"文件：{report['file']}")
        console.print(f"时间：{report['time']}")
        
        issues = report["issues"]
        
        # 统计问题
        total_issues = len(issues)
        issue_types = {}
        issue_severities = {}
        
        for issue in issues:
            issue_type = issue["type"]
            issue_severity = issue["severity"]
            
            issue_types[issue_type] = issue_types.get(issue_type, 0) + 1
            issue_severities[issue_severity] = issue_severities.get(issue_severity, 0) + 1
        
        # 打印统计信息
        console.print("\n统计信息:")
        console.print(f"总问题数：{total_issues}")
        
        if issue_types:
            console.print("\n问题类型分布：")
            for type_name, count in issue_types.items():
                console.print(f"- {type_name}: {count}")
        
        if issue_severities:
            console.print("\n严重程度分布：")
            for severity, count in issue_severities.items():
                console.print(f"- {severity}: {count}")
        
        # 打印具体问题
        if issues:
            console.print("\n具体问题：\n")
            for issue in issues:
                severity = issue["severity"].upper()
                line = issue["line"]
                type_name = issue["type"]
                rule = issue["rule"]
                message = issue["message"]
                
                console.print(f"{severity} 第 {line} 行")
                console.print(f"类型：{type_name}")
                console.print(f"规则：{rule}")
                console.print(f"说明：{message}\n")
        
    except Exception as e:
        console.print(f"[red]错误：{str(e)}[/red]")
        raise click.Abort()

@review.command(name='dir')
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
def review_directory(directory):
    """审查目录中的所有Python文件。

    Args:
        directory: 要审查的目录路径
    """
    try:
        reviewer = CodeReview()
        with console.status("正在审查目录..."):
            report = reviewer.review_directory(directory)
        
        console.print("\n== 目录审查报告 ==")
        console.print(f"目录：{report['directory']}")
        console.print(f"时间：{report['time']}")
        console.print(f"审查文件数：{report['files_reviewed']}")
        
        total_issues = report["total_issues"]
        issue_types = report["issue_types"]
        issue_severities = report["issue_severities"]
        issues = report["issues"]
        
        # 打印统计信息
        console.print(f"\n总问题数：{total_issues}")
        
        if issue_types:
            console.print("\n问题类型分布：")
            for type_name, count in issue_types.items():
                console.print(f"- {type_name}: {count}")
        
        if issue_severities:
            console.print("\n严重程度分布：")
            for severity, count in issue_severities.items():
                console.print(f"- {severity}: {count}")
        
        # 打印具体问题
        if issues:
            console.print("\n具体问题：\n")
            for issue in issues:
                severity = issue["severity"].upper()
                line = issue["line"]
                type_name = issue["type"]
                rule = issue["rule"]
                message = issue["message"]
                
                console.print(f"{severity} 第 {line} 行")
                console.print(f"类型：{type_name}")
                console.print(f"规则：{rule}")
                console.print(f"说明：{message}\n")
        
    except Exception as e:
        console.print(f"[red]错误：{str(e)}[/red]")
        raise click.Abort()

@review.command(name='list')
def review_list():
    """列出审查报告"""
    reports = CodeReview.list_reports()
    
    if not reports:
        console.print("[yellow]还没有审查报告[/yellow]")
        return
    
    table = Table(title="审查报告列表")
    table.add_column("ID", style="cyan")
    table.add_column("时间", style="blue")
    table.add_column("目标", style="green")
    table.add_column("问题数", style="red", justify="right")
    
    for report in reports:
        table.add_row(
            report["id"],
            report["timestamp"],
            report["target"],
            str(report["total_issues"])
        )
    
    console.print(table)

@review.command(name='show')
@click.argument('report_id')
def review_show(report_id: str):
    """查看审查报告"""
    report = CodeReview.get_report(report_id)
    
    if not report:
        console.print(f"[red]未找到报告：{report_id}[/red]")
        return
    
    _print_review_report(report)

def _print_review_report(report: Dict):
    """打印审查报告"""
    if "file" in report:
        console.print(f"\n[cyan]== 文件审查报告 ==[/cyan]")
        console.print(f"文件：[blue]{report['file']}[/blue]")
    else:
        console.print(f"\n[cyan]== 目录审查报告 ==[/cyan]")
        console.print(f"目录：[blue]{report['directory']}[/blue]")
        console.print(f"文件数：[green]{report['summary']['total_files']}[/green]")
    
    console.print(f"时间：[yellow]{report['timestamp']}[/yellow]")
    
    # 打印统计信息
    console.print("\n[cyan]统计信息:[/cyan]")
    console.print(f"总问题数：[red]{report['summary']['total']}[/red]")
    
    if report["summary"]["by_type"]:
        console.print("\n[yellow]问题类型分布：[/yellow]")
        for type_, count in report["summary"]["by_type"].items():
            console.print(f"- {type_}: [blue]{count}[/blue]")
    
    if report["summary"]["by_severity"]:
        console.print("\n[yellow]严重程度分布：[/yellow]")
        for severity, count in report["summary"]["by_severity"].items():
            color = {
                "error": "red",
                "warning": "yellow",
                "info": "blue"
            }.get(severity, "white")
            console.print(f"- {severity}: [{color}]{count}[/{color}]")
    
    # 打印具体问题
    if report["issues"]:
        console.print("\n[cyan]具体问题：[/cyan]")
        for issue in sorted(report["issues"], key=lambda x: (x["severity"], x["line"])):
            severity_color = {
                "error": "red",
                "warning": "yellow",
                "info": "blue"
            }.get(issue["severity"], "white")
            
            console.print(
                f"\n[{severity_color}]{issue['severity'].upper()}[/{severity_color}] "
                f"第 {issue['line']} 行"
            )
            console.print(f"类型：[blue]{issue['type']}[/blue]")
            console.print(f"规则：[yellow]{issue['rule']}[/yellow]")
            console.print(f"说明：{issue['message']}")
    
    # 如果是目录报告，打印每个文件的问题数
    if "files" in report:
        console.print("\n[cyan]文件问题分布：[/cyan]")
        files_table = Table()
        files_table.add_column("文件", style="blue")
        files_table.add_column("问题数", style="red", justify="right")
        
        for file_report in sorted(report["files"], key=lambda x: len(x["issues"]), reverse=True):
            if file_report["issues"]:
                files_table.add_row(
                    file_report["file"],
                    str(len(file_report["issues"]))
                )
        
        console.print(files_table)

if __name__ == '__main__':
    main() 