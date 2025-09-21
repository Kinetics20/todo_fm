from src.task import StatusEnum, Task
from src.task_list import TaskList, remove_completed


def test_remove_completed_exist(base_task_list: TaskList) -> None:
    remove_completed(base_task_list)
    assert len(base_task_list) == 1
    assert base_task_list[0]["status"] != StatusEnum.COMPLETED


def test_remove_completed_not_exist(base_task: Task, task_priority_high: Task) -> None:
    task_list_not_completed = [base_task, task_priority_high]
    remove_completed(task_list_not_completed)

    assert len(task_list_not_completed) == 2
