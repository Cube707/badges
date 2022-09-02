import pytest

from badges.utils import check_html_color


@pytest.mark.parametrize(
    ("color", "expected"),
    [
        ("#", False),
        ("red", True),
        ("Red", False),
        ("#f00", True),
        ("#f0", False),
        ("#ff0000", True),
        ("#ff0000f", False),
        ("green slime", False),
    ],
)
def test_normal_operation(color, expected):
    assert expected == check_html_color(color)
