from src.task import PriorityEnum
from src.task_list import TaskList, filter_by


def test_filter_by_priority_medium(task_list: TaskList) -> None:
    filtered_task_list = filter_by(task_list, priority=PriorityEnum.MEDIUM)

    assert len(filtered_task_list) == 3
    assert filtered_task_list[0]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[1]['priority'] == PriorityEnum.MEDIUM
    assert filtered_task_list[2]['priority'] == PriorityEnum.MEDIUM


