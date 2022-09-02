import pytest
import requests

from badges import errors
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


def test_ConnectionError(monkeypatch: pytest.MonkeyPatch):
    def raise_ConnectionError(url="", timeout=0):
        raise requests.exceptions.ConnectionError

    with monkeypatch.context() as m:
        m.setattr(requests, "get", raise_ConnectionError)
        with pytest.raises(errors.ConnectionError):
            check_simpleicon("github")


def test_ConnectionTimeoutError(monkeypatch: pytest.MonkeyPatch):
    def raise_Timeout(url="", timeout=0):
        raise requests.exceptions.Timeout

    with monkeypatch.context() as m:
        m.setattr(requests, "get", raise_Timeout)
        with pytest.raises(errors.ConnectionTimeoutError):
            check_simpleicon("github")
