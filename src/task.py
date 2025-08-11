import uuid
from collections.abc import Iterable
from datetime import date
from enum import Enum
from typing import TypedDict


class Priority(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Task(TypedDict):
    id: str
    description: str
    created_at: date
    due_date: date | None
    priority: Priority
    done: bool
    tags: list[str]


def normalize_priority(
        priority: Priority | str
) -> Priority:
    if isinstance(priority, Priority):
        return priority
    try:
        return Priority(priority)
    except ValueError:
        raise ValueError(f'Priority must be one of: {[p.value for p in Priority]}')


def validate_description(description: str) -> str:
    if not isinstance(description, str) or len(description.strip()) < 3:
        raise ValueError('Description must be a non-empty string equal or longer than 3 characters.')
    return description.strip()


def validate_due_date(due_date: date | None, *, today: date) -> date | None:
    if due_date is not None and not isinstance(due_date, date):
        raise ValueError('Due date must be a date object or None.')
    if due_date is not None and due_date < today:
        raise ValueError('Due date cannot be earlier than the created at date.')
    return due_date


def unique_tags(tags: Iterable[str] | None) -> list[str]:
    if tags is None:
        return []

    seen: set[str] = set()
    out: list[str] = []

    for tag in (t.strip().lower() for t in tags):
        if tag and tag not in seen:
            seen.add(tag)
            out.append(tag)
    return out


def create_task(
        description: str,
        due_date: date | None = None,
        priority: Priority | str = Priority.MEDIUM,
        tags: list[str] | None = None,
        *,
        today: date | None = None
) -> Task:
    today = date.today() if today is None else today

    description = validate_description(description)
    due_date = validate_due_date(due_date, today=today)
    priority = normalize_priority(priority)
    tags = unique_tags(tags)

    return {
        'id': str(uuid.uuid4()),
        'description': description,
        'created_at': today,
        'due_date': due_date,
        'priority': priority,
        'done': False,
        'tags': tags
    }


if __name__ == '__main__':
    task = create_task('123', date(2025, 8, 10), Priority.HIGH)
    print(task)
