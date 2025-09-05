from datetime import date, timedelta
from typing import cast

from src.task import Task, is_overdue, StatusEnum


def test_is_overdue_due_in_past_not_done(fixed_today: date, base_task: Task) -> None:
    task = cast(Task, {**base_task, "due_date": fixed_today - timedelta(days=5), "status": StatusEnum.IN_PROGRESS})

    assert is_overdue(task, today=fixed_today) is True


def test_is_overdue_due_in_past_but_done(fixed_today: date, base_task: Task) -> None:
    task = cast(Task, {**base_task, "due_date": fixed_today - timedelta(days=5), "status": StatusEnum.COMPLETED})

    assert is_overdue(task, today=fixed_today) is False


def test_is_overdue_due_today_not_done(fixed_today: date, base_task: Task) -> None:
    task = cast(Task, {**base_task, "due_date": fixed_today, "status": StatusEnum.IN_PROGRESS})

    assert is_overdue(task, today=fixed_today) is False


def test_is_overdue_due_in_future_not_done(fixed_today: date, base_task: Task) -> None:
    task = cast(Task, {**base_task, "due_date": fixed_today + timedelta(days=5), "status": StatusEnum.IN_PROGRESS})

    assert is_overdue(task, today=fixed_today) is False


def test_is_overdue_no_due_date(fixed_today: date, base_task: Task) -> None:
    task = cast(Task, {**base_task, "due_date": None, "status": StatusEnum.IN_PROGRESS})

    assert is_overdue(task, today=fixed_today) is False
