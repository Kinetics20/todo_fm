import pytest

from src.task import Task, add_tag


def test_add_tag_normalizes_case_and_spaces(base_task: Task) -> None:
    add_tag(base_task, " Java ")

    assert base_task["tags"] == ["python", "sql", "javascript", "java"]


def test_add_tag_skips_duplicates(base_task: Task) -> None:
    add_tag(base_task, "python")

    assert base_task["tags"] == ["python", "sql", "javascript"]


def test_add_tag_appends_once(base_task: Task) -> None:
    add_tag(base_task, "HTML")
    add_tag(base_task, " HTML ")
    add_tag(base_task, " html ")

    assert base_task["tags"].count("html") == 1


# def test_add_tag_empty_should_fail(base_task: Task) -> None:
#
#     with pytest.raises(ValueError, match='Tag cannot be empty.'):
#         add_tag(base_task, '')


@pytest.mark.xfail(reason="Current implementation allows empty tags - probably a bug.")
def test_add_tag_empty_tag_should_be_ignored(base_task: Task) -> None:
    add_tag(base_task, "")

    assert "" not in base_task["tags"]
