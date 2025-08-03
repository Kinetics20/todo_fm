import uuid
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



def create_task(
        description: str,
        due_date: date | None = None,
        priority: Priority | str = Priority.MEDIUM,
        tags: list[str] | None = None
) -> Task:
    if not isinstance(description, str) and len(description.strip()) <= 3:
        raise ValueError('Description must be a non-empty string equal or longer than 3 characters.')

    if not isinstance(due_date, date) and due_date is not None:
        raise ValueError('Due date must be a date object or None.')

    created_at = date.today()

    if due_date is not None and due_date < created_at:
        raise ValueError('Due date cannot be earlier than the created at date.')

    if isinstance(priority, str):
        try:
            priority = Priority(priority)
        except ValueError:
            raise ValueError(f'Priority must be one of: {[p.value for p in Priority]}')

    if tags is None:
        tags = []

    return {
        'id': str(uuid.uuid4()),
        'description': description,
        'created_at': created_at,
        'due_date': due_date,
        'priority': priority,
        'done': False,
        'tags': tags
    }

if __name__ == '__main__':
    task = create_task('123', date(2025, 8, 10), Priority.HIGH)
    print(task)

