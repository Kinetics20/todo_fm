from datetime import date, timedelta

from src.task import Task, postpone


def test_postpone_days_equal_zero(base_task: Task, fixed_today: date) -> None:
    postpone(base_task, 0, today=fixed_today)

    assert base_task['due_date'] == fixed_today + timedelta(days=2)


def test_postpone_days_grater_than_zero(base_task: Task, fixed_today: date) -> None:
    postpone(base_task, 10, today=fixed_today)

    assert base_task['due_date'] == fixed_today + timedelta(days=12)


def test_postpone_no_due_date(base_task: Task, fixed_today: date) -> None:
    base_task['due_date'] = None
    postpone(base_task, 10, today=fixed_today)

    assert base_task['due_date'] == fixed_today + timedelta(days=10)
