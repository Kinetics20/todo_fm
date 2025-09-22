from src.task import StatusEnum, Task
from src.task_list import TaskList, remove_overdue


def test_remove_overdue_exist(base_task: Task, task_overdue: Task) -> None:
    task_list = [base_task, task_overdue]
    remove_overdue(task_list)

    assert len(task_list) == 1
    assert task_list[0]["status"] != StatusEnum.OVERDUE


def test_remove_overdue_not_exist(base_task_list: TaskList) -> None:
    remove_overdue(base_task_list)
    assert len(base_task_list) == 2
