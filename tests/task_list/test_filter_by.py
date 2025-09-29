from datetime import timedelta, date

from src.task import PriorityEnum, StatusEnum
from src.task_list import TaskList, filter_by


def test_filter_by_priority_medium(task_list: TaskList) -> None:
    filtered_task_list = filter_by(task_list, priority=PriorityEnum.MEDIUM)

    assert len(filtered_task_list) == 3
    assert filtered_task_list[0]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[1]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[2]['priority'] == PriorityEnum.MEDIUM


def test_filter_by_priority_medium_status_new(task_list: TaskList) -> None:
    filtered_task_list = filter_by(task_list, priority=PriorityEnum.MEDIUM, status=StatusEnum.NEW)

    assert len(filtered_task_list) == 1
    assert filtered_task_list[0]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[0]['status'] == StatusEnum.NEW


def test_filter_by_priority_medium_status_new_tag_python(task_list: TaskList) -> None:
    filtered_task_list = filter_by(task_list, priority=PriorityEnum.MEDIUM, status=StatusEnum.NEW, tag='python')

    assert len(filtered_task_list) == 1
    assert filtered_task_list[0]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[0]['status'] == StatusEnum.NEW
    assert filtered_task_list[0]['tags'] == ['python', 'sql', 'javascript']


def test_filter_by_priority_medium_status_new_tag_python_due_date(task_list: TaskList) -> None:
    filtered_task_list = filter_by(
        task_list,
        priority=PriorityEnum.MEDIUM,
        status=StatusEnum.NEW,
        tag='python',
        due_date=date(2025, 9, 11) + timedelta(days=2)
    )

    assert len(filtered_task_list) == 1
    assert filtered_task_list[0]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[0]['status'] == StatusEnum.NEW
    assert filtered_task_list[0]['tags'] == ['python', 'sql', 'javascript']
    assert filtered_task_list[0]['due_date'] == date(2025, 9, 13)
