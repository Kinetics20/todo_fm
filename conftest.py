import uuid
from datetime import date, timedelta

import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.task import PriorityEnum, StatusEnum, Task
from src.task_list import TaskList


@pytest.fixture
def fixed_today() -> date:
    """Constant value for tests" (2025-09-11)."""
    return date(2025, 9, 11)


@pytest.fixture
def valid_description() -> str:
    """Check valid description."""
    return "Description for tests."


@pytest.fixture
def valid_tags() -> list[str]:
    """Check valid tags."""
    return ["work", " urgent  ", "work", "Home", "   "]


@pytest.fixture
def predictable_uuid(monkeypatch: MonkeyPatch) -> str:
    """Check predictable uuid."""

    class Dummy:
        def __init__(self, value: str):
            self.value = value

        def __str__(self) -> str:
            return self.value

    dummy = Dummy("00000000-0000-0000-0000-000000000000")
    monkeypatch.setattr(uuid, "uuid4", lambda: dummy)
    return "00000000-0000-0000-0000-000000000000"


@pytest.fixture
def base_task(fixed_today: date) -> Task:
    """Create base task."""
    return {
        "id": "1",
        "description": "test",
        "created_at": fixed_today,
        "due_date": fixed_today + timedelta(days=2),
        "priority": PriorityEnum.MEDIUM,
        "status": StatusEnum.NEW,
        "tags": ["python", "sql", "javascript"],
        "completed_at": None,
    }

@pytest.fixture
def task_priority_low(fixed_today: date) -> Task:
    """Create base task low priority."""
    return {
        "id": "1",
        "description": "low priority task",
        "created_at": fixed_today - timedelta(days=4),
        "due_date": fixed_today + timedelta(days=4),
        "priority": PriorityEnum.LOW,
        "status": StatusEnum.IN_PROGRESS,
        "tags": ["python", "sql", "javascript"],
        "completed_at": None,
    }


@pytest.fixture
def task_completed(fixed_today: date) -> Task:
    """Create completed task."""
    return {
        "id": "2",
        "description": "valid task",
        "created_at": fixed_today,
        "due_date": fixed_today + timedelta(days=2),
        "priority": PriorityEnum.MEDIUM,
        "status": StatusEnum.COMPLETED,
        "tags": ["python", "sql"],
        "completed_at": fixed_today,
    }


@pytest.fixture
def task_overdue(fixed_today: date) -> Task:
    """Create overdue task."""
    return {
        "id": "3",
        "description": "valid task",
        "created_at": fixed_today - timedelta(days=10),
        "due_date": fixed_today - timedelta(days=2),
        "priority": PriorityEnum.MEDIUM,
        "status": StatusEnum.OVERDUE,
        "tags": ["python", "sql"],
        "completed_at": None,
    }


@pytest.fixture
def task_priority_high(fixed_today: date) -> Task:
    """Create task with high priority."""
    return {
        "id": "4",
        "description": "test",
        "created_at": fixed_today,
        "due_date": fixed_today + timedelta(days=10),
        "priority": PriorityEnum.HIGH,
        "status": StatusEnum.NEW,
        "tags": ["python", "sql"],
        "completed_at": None,
    }


@pytest.fixture
def base_task_list(base_task: Task, task_completed: Task) -> TaskList:
    """Create base task list"""
    return [base_task, task_completed]


@pytest.fixture
def task_list(
        base_task: Task,
        task_priority_low: Task,
        task_completed: Task,
        task_overdue: Task,
        task_priority_high: Task,
) -> TaskList:
    """Create task list"""
    return [base_task, task_priority_low, task_completed, task_overdue, task_priority_high]
