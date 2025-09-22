from collections.abc import Callable, Iterable, Mapping
from datetime import date
from pprint import pprint
from typing import Any, Literal, TypeGuard, cast

from src.task import PriorityEnum, StatusEnum, Task, create_task, has_tag

type TaskList = list[Task]


def create_task_list(tasks: Iterable[Task] | None = None) -> TaskList:
    if tasks is None:
        return []
    ids = [task["id"] for task in tasks]
    if len(ids) != len(set(ids)):
        raise ValueError("Can not be create task list because it contains duplicates.")
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


def sort_by(
    tasks: TaskList,
    *,
    by: Literal["due_date", "created_at", "priority", "description"] = "due_date",
    reverse: bool = False,
) -> TaskList:
    priority_order: dict[PriorityEnum, int] = {
        PriorityEnum.LOW: 0,
        PriorityEnum.MEDIUM: 1,
        PriorityEnum.HIGH: 2,
    }

    key_map: dict[str, Callable[[Task], Any]] = {
        "due_date":    lambda t: (t["due_date"] or date.max),
        "created_at":  lambda t: t["created_at"],
        "priority":    lambda t: priority_order[t["priority"]],
        "description": lambda t: t["description"].lower(),
    }

    if by not in key_map:
        raise ValueError(f"Unsupported sort key: {by}")

    key_fn = key_map[by]
    return cast(TaskList, sorted(tasks, key=key_fn, reverse=reverse))


if __name__ == "__main__":
    tasks_: list[Task] = [
        create_task("python", date(2025, 9, 12), tags=["coding", "learning"]),
        create_task("pytest", date(2025, 10, 12), tags=["coding"], priority=PriorityEnum.HIGH),
        create_task("learning python", tags=["writing", "learning"], status=StatusEnum.COMPLETED),
        create_task("coding python", date(2025, 11, 12), tags=["improving", "learning"]),
    ]

    tl: TaskList = create_task_list(tasks_)
    pprint(tl)
