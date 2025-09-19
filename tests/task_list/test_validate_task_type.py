from src.task import Task
from src.task_list import validate_task_type


def test_validate_task_type_correct_task(base_task: Task) -> None:
    assert validate_task_type(base_task) is True


def test_validate_task_type_incorrect_task() -> None:
    incorrect_task = {"index": "42"}
    assert validate_task_type(incorrect_task) is False
