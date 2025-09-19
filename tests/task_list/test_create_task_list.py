from src.task_list import TaskList, create_task_list


def test_create_task_list_empty() -> None:
    assert create_task_list() == []


def test_create_task_list_from_iterable(base_task_list: TaskList) -> None:
    assert create_task_list(base_task_list) == base_task_list
