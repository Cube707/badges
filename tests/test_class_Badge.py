import pytest
import requests

from badges import Badge, errors


@pytest.fixture(scope="module")
def response():
    params = {
        "label": "",
        "labelColor": "gray",
        "logo": "github",
        "message": "GitHub",
        "color": "#0D0D0D",
    }
    return requests.get("https://img.shields.io/static/v1", params)


def test_creation_manual():
    b = Badge("GitHub", url="https://example.org", svg="")
    assert "<Badge object 'GitHub'>" == str(b)
    assert "https://example.org&style=flat" == b.url
    assert "" == b.svg_data


def test_creation_response(response):
    b = Badge("GitHub", response=response)
    assert "<Badge object 'GitHub'>" == str(b)
    assert response.url + "&style=flat" == b.url
    assert response.text == b.svg_data


def test_styles(response):
    b = Badge("GitHub", response=response)
    url = response.url
    assert url + "&style=plastic" == b.url_plastic
    assert url + "&style=flat" == b.url_flat
    assert url + "&style=flat-square" == b.url_flat_square
    assert url + "&style=for-the-badge" == b.url_for_the_badge
    assert url + "&style=social" == b.url_social


def test_error_WrongType():
    with pytest.raises(
        errors.ParameterError, match="argument 'response' must be of type 'Response'"
    ):
        Badge("GitHub", response={"url": "https://example.org"})


def test_error_MissingURL():
    with pytest.raises(
        errors.ParameterError, match="missing 1 required keyword argument: 'url'"
    ):
        Badge("GitHub")


def test_error_MissingSVG():
    with pytest.raises(
        errors.ParameterError, match="missing 1 required keyword argument: 'svg'"
    ):
        Badge("GitHub", url="https://example.org")
