from datetime import timedelta, date
from unittest.mock import patch

from src.task import PriorityEnum, create_task, StatusEnum


def test_create_task_happy_path(fixed_today: date, valid_description: str, valid_tags: list[str], predictable_uuid: str) -> None:
    due = fixed_today + timedelta(days=3)
    task = create_task(
        description=valid_description, due_date=due, priority=PriorityEnum.LOW, tags=valid_tags, today=fixed_today
    )

    assert task["id"] == predictable_uuid
    assert task["description"] == valid_description
    assert task["created_at"] == fixed_today
    assert task["due_date"] == due
    assert task["priority"] == PriorityEnum.LOW
    assert task["status"] == StatusEnum.NEW
    assert task["tags"] == ["work", "urgent", "home"]


def test_create_task_all_helpers_called(fixed_today: date) -> None:
    description_in = " Learn  Python "
    due_in = fixed_today + timedelta(days=2)
    priority_in = "high"
    tags_in = [" work ", "Urgent", "HOME"]

    with (
        patch("src.task.validate_description", autospec=True) as m_desk,
        patch("src.task.validate_due_date", autospec=True) as m_due,
        patch("src.task.normalize_priority", autospec=True) as m_pri,
        patch("src.task.unique_tags", autospec=True) as m_tags,
    ):
        create_task(description=description_in, due_date=due_in, priority=priority_in, tags=tags_in)

        m_desk.assert_called_once_with(description_in)
        m_due.assert_called_once_with(due_in, today=fixed_today)
        m_pri.assert_called_once_with(priority_in)
        m_tags.assert_called_once_with(tags_in)
