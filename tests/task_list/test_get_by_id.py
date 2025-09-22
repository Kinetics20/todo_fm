import pytest

from src.task_list import TaskList, get_by_id


def test_get_by_id_exist(base_task_list: TaskList) -> None:
    task = get_by_id(base_task_list, "1")

    assert task["id"] == "1"


def test_get_by_id_not_exist(base_task_list: TaskList) -> None:
    idx = "10"
    with pytest.raises(ValueError, match=f"No task with id {idx} found."):
        get_by_id(base_task_list, idx)
