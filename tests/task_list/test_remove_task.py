import pytest

from src.task import Task
from src.task_list import TaskList, remove_task


def test_remove_task_exist(base_task_list: TaskList, base_task: Task) -> None:
    remove_task(base_task_list, base_task)

    assert base_task not in base_task_list
    assert len(base_task_list) == 1


def test_remove_task_not_exist(base_task_list: TaskList, task_priority_high: Task) -> None:
    with pytest.raises(ValueError, match="Task does not exist in tasks list."):
        remove_task(base_task_list, task_priority_high)


def test_remove_task_incorrect(base_task_list: TaskList) -> None:
    incorrect_task = {"id": 42}
    with pytest.raises(TypeError, match="Task is invalid/missing keys."):
        remove_task(base_task_list, incorrect_task)
