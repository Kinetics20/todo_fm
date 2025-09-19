import pytest

from src.task import Task
from src.task_list import TaskList, add_task, create_task_list


def test_add_task_correct(base_task: Task) -> None:
    task_list = create_task_list()
    add_task(task_list, base_task)
    assert len(task_list) == 1
    assert task_list[0] == base_task


def test_add_task_incorrect(base_task_list: TaskList) -> None:
    incorrect_task = {"index": "42"}
    with pytest.raises(TypeError, match="Task is invalid/missing keys."):
        add_task(base_task_list, incorrect_task)


def test_add_task_duplicate_task(base_task_list: TaskList, base_task: Task) -> None:
    with pytest.raises(ValueError, match="Task is already registered."):
        add_task(base_task_list, base_task)
