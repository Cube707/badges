import requests

from badges import _html_colors, errors


def check_internet_conection(host="https://google.com") -> bool:
    """checks if internet-connection is available"""
    try:
        requests.get(host)
    except Exception:
        return False
    return True


def check_simpleicon(name: str) -> bool:
    """checks if a given name existis on simpleicon.org"""

    url = f"https://simpleicons.org/icons/{name}.svg"
    try:
        r = requests.get(url, timeout=0.5)
        if r.ok:
            return True
    except requests.exceptions.Timeout:
        raise errors.ConnectionTimeoutError("request to 'simpleicons.org' timed out")
    except requests.exceptions.ConnectionError:
        raise errors.ConnectionError(
            "couldn't connect to 'simpleicons.org', this shouldn't happen and "
            "means your internet connection is seriously messed up!"
        )
    return False


def check_html_color(color: str) -> bool:
    """checks is a given color string is usable css.
    Hex values and color-names are checked for validity.
    """
    if color in _html_colors.COLOR_NAME_TO_RGB:
        return True
    return bool(_html_colors.RE_HEX_COLOR.fullmatch(color))
