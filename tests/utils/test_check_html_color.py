import pytest

from badges.utils import check_html_color


@pytest.mark.parametrize(
    ("color", "expected"),
    [
        ("#f00", True),
        ("#ff0000", True),
        ("#ff0000ff", True),
        ("#", False),
        ("#f0", False),
        ("#f00f", False),
        ("#f00f0", False),
        ("#ff0000f", False),
        ("#ff0000ff0", False),
        ("#ff0000ff00", False),
        ("red", True),
        ("Red", False),
        ("re", False),
        ("rede", False),
        ("green slime", False),
    ],
)
def test_normal_operation(color, expected):
    assert expected == check_html_color(color)
