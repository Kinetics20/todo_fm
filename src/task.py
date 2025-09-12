import uuid
from collections.abc import Iterable
from datetime import date, timedelta
from enum import Enum, IntEnum, auto
from typing import TypedDict


class PriorityEnum(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StatusEnum(IntEnum):
    NEW = auto()
    COMPLETED = auto()
    IN_PROGRESS = auto()
    OVERDUE = auto()


class Task(TypedDict):
    id: str
    description: str
    created_at: date
    due_date: date | None
    priority: PriorityEnum
    status: StatusEnum
    tags: list[str]
    completed_at: date | None


def normalize_priority(priority: PriorityEnum | str) -> PriorityEnum:
    if isinstance(priority, PriorityEnum):
        return priority
    try:
        return PriorityEnum(priority)
    except ValueError as err:
        raise ValueError(f"Priority must be one of: {[p.value for p in PriorityEnum]}") from err


def normalize_status(status: StatusEnum | int) -> StatusEnum:
    if isinstance(status, StatusEnum):
        return status
    try:
        return StatusEnum(status)
    except ValueError as err:
        raise ValueError(f"Status must be one of: {[s.value for s in StatusEnum]}") from err


def validate_description(description: str) -> str:
    if not isinstance(description, str) or len(description.strip()) < 3:
        raise ValueError("Description must be a non-empty string equal or longer than 3 characters.")
    return description.strip()


def validate_due_date(due_date: date | None, *, today: date) -> date | None:
    if due_date is not None and not isinstance(due_date, date):
        raise ValueError("Due date must be a date object or None.")
    if due_date is not None and due_date < today:
        raise ValueError("Due date cannot be earlier than the created at date.")
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
    priority: PriorityEnum | str = PriorityEnum.MEDIUM,
    status: StatusEnum | int = StatusEnum.NEW,
    tags: list[str] | None = None,
    *,
    today: date | None = None,
) -> Task:
    today = date.today() if today is None else today

    description = validate_description(description)
    due_date = validate_due_date(due_date, today=today)
    priority = normalize_priority(priority)
    status = normalize_status(status)
    tags = unique_tags(tags)

    if due_date is not None and due_date > today and status == StatusEnum.OVERDUE:
        raise ValueError("Status cannot be OVERDUE if due_date is greater than today.")

    return {
        "id": str(uuid.uuid4()),
        "description": description,
        "created_at": today,
        "due_date": due_date,
        "priority": priority,
        "status": status,
        "tags": tags,
        "completed_at": None,
    }


def is_overdue(task: Task, *, today: date | None = None) -> bool:
    today = date.today() if today is None else today

    return (task["due_date"] is not None) and (task["due_date"] < today) and (task["status"] > StatusEnum.COMPLETED)


def has_tag(task: Task, tag: str) -> bool:
    return tag.strip().lower() in task["tags"]


def mark_completed(task: Task) -> None:
    task["status"] = StatusEnum.COMPLETED
    task["completed_at"] = date.today()


def time_left(task: Task, today: date | None = None) -> str:
    today = date.today() if today is None else today

    if task["status"] == StatusEnum.COMPLETED:
        return "Task already completed."

    if task["due_date"] is None:
        return "Infinite time left."

    delta = (task["due_date"] - today).days

    if delta < 0:
        return f"Overdue by {abs(delta)} day{'s' if abs(delta) != 1 else ''}."
    elif delta == 0:
        return "Due today!"
    else:
        return f"{delta} day{'s' if delta != 1 else ''} left."


def add_tag(task: Task, tag: str) -> None:
    # if not tag.strip():
    #     # raise ValueError('Tag cannot be empty.')
    #     return

    if not has_tag(task, tag):
        task["tags"].append(tag.strip().lower())


def remove_tag(task: Task, tag: str) -> None:
    task["tags"].remove(tag.strip().lower())


def postpone(task: Task, days: int, *, today: date | None = None) -> None:
    if days == 0:
        return

    base = task["due_date"] or (today or date.today())
    task["due_date"] = base + timedelta(days=days)


if __name__ == "__main__":
    task_ = create_task("123", date(2025, 12, 13), PriorityEnum.HIGH, 1)
    add_tag(task_, " Python ")
    print(task_)
    print(time_left(task_))
