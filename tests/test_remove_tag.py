import re

import pytest

from src.task import Task, remove_tag


def test_remove_tag_existing_tag(base_task: Task) -> None:
    remove_tag(base_task, "python")

    assert base_task["tags"] == ["sql"]


def test_remove_tag_normalizes_case_and_spaces(base_task: Task) -> None:
    remove_tag(base_task, " Python ")

    assert base_task["tags"] == ["sql"]


def test_remove_tag_empty_tag(base_task: Task) -> None:
    with pytest.raises(ValueError, match=re.escape("list.remove(x): x not in list")):
        remove_tag(base_task, "")
