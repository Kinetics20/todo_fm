from datetime import date

from pytest_mock import MockerFixture

import src.task as module_task
from src.task import StatusEnum, Task, mark_completed


def test_mark_completed_updates_status_and_completed_at(base_task: Task, mocker: MockerFixture) -> None:
    class FakeDate(date):
        @classmethod
        def today(cls) -> "FakeDate":
            return cls(2025, 10, 10)

    mocker.patch.object(module_task, "date", FakeDate)

    mark_completed(base_task)

    assert base_task["status"] == StatusEnum.COMPLETED
    assert base_task["completed_at"] == date(2025, 10, 10)
