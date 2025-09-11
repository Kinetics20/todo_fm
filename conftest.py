import uuid
from datetime import date, timedelta

import pytest
from _pytest.monkeypatch import MonkeyPatch

from src.task import PriorityEnum, StatusEnum, Task


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
        "tags": ["python", "sql"],
        "completed_at": None,
    }
