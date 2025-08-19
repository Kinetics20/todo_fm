from datetime import date
from typing import cast
from src.task import Task, time_left


def test_time_left_done_returns_completed(base_task: Task, fixed_today: date) -> None:
    task = cast(Task, ({**base_task, 'done': True}))
    assert time_left(task, today=fixed_today) == "Task already completed."


def test_time_left_infinite_when_no_due_date(base_task: Task, fixed_today: date) -> None:
    task = cast(Task, ({**base_task, 'due_date': None}))
    assert time_left(task, today=fixed_today) == "Infinite time left."


# test_time_left_overdue_plural @one day overdue
# test_time_left_overdue_singular @more than one day overdue
# test_time_left_due_today
# test_time_left_future_plural
# test_time_left_future_singular