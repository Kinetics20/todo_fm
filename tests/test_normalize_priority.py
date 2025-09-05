import re

import pytest

from src.task import PriorityEnum, normalize_priority


@pytest.mark.parametrize(
    "input_value, expected_priority",
    [
        (PriorityEnum.LOW, PriorityEnum.LOW),
        (PriorityEnum.MEDIUM, PriorityEnum.MEDIUM),
        (PriorityEnum.HIGH, PriorityEnum.HIGH),
        ("low", PriorityEnum.LOW),
        ("medium", PriorityEnum.MEDIUM),
        ("high", PriorityEnum.HIGH),
    ],
)
def test_normalize_priority_valid(input_value, expected_priority):
    result = normalize_priority(input_value)
    assert isinstance(result, PriorityEnum)
    assert result == expected_priority


@pytest.mark.parametrize("input_value", ["LOW", "urgent", 123, None, "", []])
def test_normalize_priority_invalid_values(input_value):
    pattern = re.escape(f"Priority must be one of: {[p.value for p in PriorityEnum]}")
    with pytest.raises(ValueError, match=pattern):
        normalize_priority(input_value)
