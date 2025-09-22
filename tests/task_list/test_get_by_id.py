import pytest

from src.task import Task
from src.task_list import TaskList, get_by_id


def test_get_by_id_exist(base_task_list: TaskList, base_task: Task) -> None:
    get_by_id(base_task_list, "1")
    expected_task = next(task for task in base_task_list if task["id"] == "1")
    assert expected_task == base_task


def test_get_by_id_not_exist(base_task_list: TaskList) -> None:
    idx = "10"
    with pytest.raises(ValueError, match=f"No task with id {idx} found."):
        get_by_id(base_task_list, idx)
