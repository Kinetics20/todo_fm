import uuid
from datetime import date, timedelta

import pytest

from src.task import create_task, Priority


@pytest.fixture
def fixed_today() -> date:
    """Constant value for tests" (2025-08-15)."""
    return date(2025, 8, 15)


@pytest.fixture
def valid_description() -> str:
    """Check valid description."""
    return 'Description for tests.'


@pytest.fixture
def valid_tags() -> list[str]:
    """Check valid tags."""
    return ['work', ' urgent  ', 'work', 'Home', '   ']


@pytest.fixture
def predictable_uuid(monkeypatch):
    """Check predictable uuid."""
    class Dummy:
        def __init__(self, value: str):
            self.value = value

        def __str__(self):
            return self.value

    dummy = Dummy('00000000-0000-0000-0000-000000000000')
    monkeypatch.setattr(uuid, 'uuid4', lambda: dummy)
    return '00000000-0000-0000-0000-000000000000'


def test_create_task_happy_path(fixed_today, valid_description, valid_tags, predictable_uuid):
    due = fixed_today + timedelta(days=3)
    task = create_task(
        description=valid_description,
        due_date=due,
        priority=Priority.LOW,
        tags=valid_tags,
        today=fixed_today
    )

    assert task['id'] == predictable_uuid
    assert task['description'] == valid_description
    assert task['created_at'] == fixed_today
    assert task['due_date'] == due
    assert task['priority'] == Priority.LOW
    assert task['done'] == False
    assert task['tags'] == ['work', 'urgent', 'home']