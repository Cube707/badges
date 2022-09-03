import pytest

from badges.utils import check_simpleicon


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("github", True),
        ("guthib", False),
    ],
)
def test_normal_operation(name, expected):
    assert expected == check_simpleicon(name)
