from collections.abc import Iterable, Mapping
from datetime import date
from pprint import pprint
from typing import Any, TypeGuard

from src.task import PriorityEnum, StatusEnum, Task, create_task, has_tag

type TaskList = list[Task]


def create_task_list(tasks: Iterable[Task] | None = None) -> TaskList:
    if tasks is None:
        return []
    return list(tasks)


def validate_task_type(task: Mapping[str, Any]) -> TypeGuard[Task]:
    required_keys = set(Task.__annotations__)

    missing = required_keys - set(task)
    if missing:
        return False
    return True


def add_task(tasks: TaskList, task: Mapping[str, Any]) -> None:
    if not validate_task_type(task):
        raise TypeError("Task is invalid/missing keys.")

    if task in tasks:
        raise ValueError("Task is already registered.")

    tasks.append(task)


def remove_task(tasks: TaskList, task: Mapping[str, Any]) -> None:
    if not validate_task_type(task):
        raise TypeError("Task is invalid/missing keys.")

    if task not in tasks:
        raise ValueError("Task does not exist in tasks list.")

    tasks.remove(task)


def filter_by_tag(tasks: TaskList, tag: str) -> TaskList:
    return [task for task in tasks if has_tag(task, tag)]


def remove_completed(tasks: TaskList) -> None:
    tasks[:] = [task for task in tasks if task["status"] != StatusEnum.COMPLETED]


def remove_overdue(tasks: TaskList) -> None:
    tasks[:] = [task for task in tasks if task["status"] != StatusEnum.OVERDUE]


def get_by_id(tasks: TaskList, idx: str) -> Task:
    for task in tasks:
        if task["id"] == idx:
            return task
    raise ValueError(f"No task with id {idx} found.")


if __name__ == "__main__":
    tasks_: list[Task] = [
        create_task("python", date(2025, 9, 12), tags=["coding", "learning"]),
        create_task("pytest", date(2025, 10, 12), tags=["coding"], priority=PriorityEnum.HIGH),
        create_task("learning python", tags=["writing", "learning"], status=StatusEnum.COMPLETED),
        create_task("coding python", date(2025, 11, 12), tags=["improving", "learning"]),
    ]

    tl: TaskList = create_task_list(tasks_)
    pprint(tl)
