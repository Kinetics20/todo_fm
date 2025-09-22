from src.task_list import TaskList, filter_by_tag


def test_filter_by_tag_exist(base_task_list: TaskList) -> None:
    filtered_task_list = filter_by_tag(base_task_list, "javascript")

    assert len(filtered_task_list) == 1
    assert "javascript" in filtered_task_list[0]["tags"]


def test_filtered_by_tag_not_exist(base_task_list: TaskList) -> None:
    filtered_task_list = filter_by_tag(base_task_list, "java")

    assert len(filtered_task_list) == 0
