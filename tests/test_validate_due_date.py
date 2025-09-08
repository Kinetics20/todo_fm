from datetime import date, timedelta

import pytest

from src.task import validate_due_date


@pytest.mark.parametrize(
    "due_date, today",
    [(None, date(2025, 8, 5)), (date(2025, 8, 8), date(2025, 8, 8)), (date(2025, 8, 20), date(2025, 8, 15))],
)
def test_validate_due_date_valid_values(due_date: date, today: date) -> None:
    assert validate_due_date(due_date, today=today) == due_date


@pytest.mark.parametrize("due_date", ["2025-08-15", 20250815, True])
def test_validate_due_date_invalid_values(due_date: date) -> None:
    with pytest.raises(ValueError, match="Due date must be a date object or None."):
        validate_due_date(due_date, today=date(2025, 11, 8))


@pytest.mark.parametrize(
    "due_date, today",
    [
        (date(2025, 8, 9), date(2025, 8, 10)),
        (date(2024, 12, 31), date(2025, 1, 1)),
        (date(2025, 8, 15) - timedelta(days=1), date(2025, 8, 15)),
    ],
)
def test_validate_due_date_past_date(due_date: date, today: date) -> None:
    with pytest.raises(ValueError, match="Due date cannot be earlier than the created at date."):
        validate_due_date(due_date, today=today)
