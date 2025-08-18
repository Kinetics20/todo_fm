import pytest

from src.task import Task, has_tag


@pytest.mark.parametrize("tag", ["python", " sql ", "SQL"])
def test_has_tag_match_tag(tag: str, base_task: Task) -> None:
    assert has_tag(base_task, tag) is True


def test_has_tag_does_not_match_tag(base_task: Task) -> None:
    assert has_tag(base_task, "java") is False


def test_has_tag_task_without_tags(base_task: Task) -> None:
    base_task["tags"] = []
    assert has_tag(base_task, "home") is False
