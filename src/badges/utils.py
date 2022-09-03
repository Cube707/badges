import logging
from base64 import b64encode
from io import FileIO
from mimetypes import guess_type

import requests

from badges import _html_colors, errors


log = logging.getLogger("badges")


def convert_imagefile(file: FileIO) -> str | None:
    """takes a given I/O buffer and returnes a data-string
    ready to be added to the url-parameters"""

    type, _ = guess_type(file.name)
    if type is None:
        log.warning("couldn't detect file-type, guessing its a 'svg'")
        type = "image/svg+xml"
    else:
        log.debug(f"file was detected to have '{type=}'")

    data = b64encode(file.read())
    return f"data:{type};base64,{data.decode('ascii')}"


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
