from badges import Badge
from badges.api import _create_badge


def test__normal_operation():
    badge = _create_badge("GitHub", "#0D0D0D", "github")
    assert isinstance(badge, Badge)
    # ToDo: what else to test here?
