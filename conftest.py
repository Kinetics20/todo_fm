import uuid
from datetime import date

import pytest

from src.task import Priority


@pytest.fixture
def fixed_today() -> date:
    """Constant value for tests" (2025-08-15)."""
    return date(2025, 8, 18)


@pytest.fixture
def valid_description() -> str:
    """Check valid description."""
    return "Description for tests."


@pytest.fixture
def valid_tags() -> list[str]:
    """Check valid tags."""
    return ["work", " urgent  ", "work", "Home", "   "]


@pytest.fixture
def predictable_uuid(monkeypatch):
    """Check predictable uuid."""

    class Dummy:
        def __init__(self, value: str):
            self.value = value

        def __str__(self):
            return self.value

    dummy = Dummy("00000000-0000-0000-0000-000000000000")
    monkeypatch.setattr(uuid, "uuid4", lambda: dummy)
    return "00000000-0000-0000-0000-000000000000"


@pytest.fixture
def base_task(fixed_today):
    return {
        "id": "1",
        "description": "test",
        "created_at": fixed_today,
        "due_date": None,
        "priority": Priority.MEDIUM,
        "done": False,
        "tags": [],
    }
