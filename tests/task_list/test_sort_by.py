import pytest

from src.task import Task
from src.task_list import sort_by, TaskList


def test_sort_by_priority(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [base_task, task_priority_low]
    result = sort_by(my_task_list, by="priority")

    assert result == [task_priority_low, base_task]


def test_sort_by_priority_reverse_true(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [base_task, task_priority_low]
    result = sort_by(my_task_list, by="priority", reverse=True)

    assert result == [base_task, task_priority_low]


def test_sort_by_description(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [base_task, task_priority_low]
    result = sort_by(my_task_list, by="description")

    assert result == [task_priority_low, base_task]


def test_sort_by_status(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [task_priority_low, base_task]
    result = sort_by(my_task_list, by='status')

    assert result == [base_task, task_priority_low]


def test_sort_by_due_date(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [base_task, task_priority_low]
    result = sort_by(my_task_list, by="due_date")

    assert result == [base_task, task_priority_low]


def test_sort_by_created_at(base_task: Task, task_priority_low: Task) -> None:
    my_task_list = [base_task, task_priority_low]
    result = sort_by(my_task_list, by="created_at")

    assert result == [task_priority_low, base_task]


def test_sort_by_invalid_by(base_task_list: TaskList) -> None:
    by = 'family'
    with pytest.raises(ValueError, match=f"Unsupported sort key: {by}"):
        sort_by(base_task_list, by=by)  # type: ignore[arg-type]
