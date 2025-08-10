import re

import pytest

from src.task import Priority, normalize_priority


@pytest.mark.parametrize(
    'input_value, expected_priority',
    [
        (Priority.LOW, Priority.LOW),
        (Priority.MEDIUM, Priority.MEDIUM),
        (Priority.HIGH, Priority.HIGH),
        ('low', Priority.LOW),
        ('medium', Priority.MEDIUM),
        ('high', Priority.HIGH),
    ]

)
def test_normalize_priority_valid(
        input_value, expected_priority
):
    result = normalize_priority(input_value)
    assert isinstance(result, Priority)
    assert result == expected_priority


@pytest.mark.parametrize(
    'input_value',
    [
        'LOW',
        'urgent',
        123,
        None,
        '',
        []
    ]
)
def test_normalize_priority_invalid_values(input_value):
    pattern = re.escape(f'Priority must be one of: {[p.value for p in Priority]}')
    with pytest.raises(ValueError, match=pattern):
        normalize_priority(input_value)




