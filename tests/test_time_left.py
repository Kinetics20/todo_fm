from datetime import date, timedelta
from typing import cast
from src.task import Task, time_left


def test_time_left_done_returns_completed(base_task: Task, fixed_today: date) -> None:
    task = cast(Task, ({**base_task, 'done': True}))
    assert time_left(task, today=fixed_today) == "Task already completed."


def test_time_left_infinite_when_no_due_date(base_task: Task, fixed_today: date) -> None:
    task = cast(Task, ({**base_task, 'due_date': None}))
    assert time_left(task, today=fixed_today) == "Infinite time left."


def test_time_left_overdue_plural(base_task: Task, fixed_today: date) -> None:

    task = cast(Task, ({**base_task, 'due_date': fixed_today - timedelta(days=1), "done": False}))
    assert time_left(task, today=fixed_today) == f"Overdue by 1 day."


def test_time_left_overdue_singular(base_task: Task, fixed_today: date) -> None:

    task = cast(Task, ({**base_task, 'due_date': fixed_today - timedelta(days=3), "done": False}))
    assert time_left(task, today=fixed_today) == f"Overdue by {(timedelta(days=3)).days} days."


def test_time_left_due_today(base_task: Task, fixed_today: date) -> None:

    task = cast(Task, ({**base_task, 'due_date': fixed_today, "done": False}))
    assert time_left(task, today=fixed_today) == f"Due today!"

def test_time_left_future_singular(base_task: Task, fixed_today: date) -> None:

    task = cast(Task, ({**base_task, 'due_date': fixed_today + timedelta(days=1), "done": False}))
    assert time_left(task, today=fixed_today) == f"1 day left."


# test_time_left_future_plural