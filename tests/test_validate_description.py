import pytest

from src.task import validate_description


@pytest.mark.parametrize(
    'description, output',
    [
        ('task', 'task'),
        ('   task with spaces   ', 'task with spaces'),
        ('TO DO', 'TO DO')
    ]
)
def test_validate_description_valid(description, output):
    result = validate_description(description)
    assert result == output
    assert isinstance(result, str)



@pytest.mark.parametrize(
    'description',
    [
        1,
        'ab',
        ' c   '
    ]
)
def test_validate_description_invalid_values(description):

    with pytest.raises(ValueError, match='Description must be a non-empty string equal or longer than 3 characters.'):
        validate_description(description)
