import re

import pytest

from src.task import StatusEnum, normalize_status


@pytest.mark.parametrize(
    "status, expected_status",
    [
        (StatusEnum.COMPLETED, StatusEnum.COMPLETED),
        (3, StatusEnum.COMPLETED),
        (4, StatusEnum.OVERDUE),
    ],
)
def test_normalize_status_valid(status: StatusEnum | int, expected_status: StatusEnum) -> None:
    assert normalize_status(status) == expected_status


def test_normalize_status_invalid() -> None:
    pattern = f"Status must be one of: {[s.value for s in StatusEnum]}"
    with pytest.raises(ValueError, match=re.escape(pattern)):
        normalize_status(2000)
