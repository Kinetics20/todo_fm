from datetime import date

import pytest

from src.task import validate_due_date


@pytest.mark.parametrize(
    'due_date, today',
    [
        (None, date(2025, 8, 5)),
        (date(2025, 8, 8), date(2025, 8, 8)),
        (date(2025, 8, 20), date(2025, 8, 15))],
)
def test_validate_due_date_valid_values(due_date, today):
    assert validate_due_date(due_date, today=today) == due_date
