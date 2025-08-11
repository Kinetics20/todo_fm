import pytest

from src.task import unique_tags


@pytest.mark.parametrize('tags', [None, [], set()])
def test_unique_tags_no_tags_return_empty(tags):
    assert unique_tags(tags) == []

@pytest.mark.parametrize(
    'tags, out',
    [
        (['', '   ', 'work'], ['work']),
        (['  home  ', 'work'], ['home', 'work']),
        (['  Urgent', 'urgent'], ['urgent'])
    ]
)
def test_unique_tags_strips_and_removes_empty(tags, out):
    assert unique_tags(tags) == out


def test_unique_tags_removes_duplicates_preserves_order():
    tags = ['home', 'work', 'urgent', 'work', 'home']
    assert unique_tags(tags) == ['home', 'work', 'urgent']