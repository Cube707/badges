import logging
from urllib.parse import urlencode

import requests

from badges import Badge, errors


SHIELDSIO_API_URL = "https://img.shields.io/static/v1"
SHIELDSIO_MAX_HEADER_SIZE = 8192

log = logging.getLogger("badges")


def _create_badge(text: str, color: str, icon: str, label: str = "") -> Badge:
    """internal version that assuems all parameters are valid and tidy.
    Returns the Badge or `None` if not succesfull"""

    params = {
        "logo": icon,
        "label": label,
        "labelColor": "gray",
        "message": text,
        "color": color,
    }
    if (size := len(urlencode(params))) > SHIELDSIO_MAX_HEADER_SIZE:
        raise errors.IconfileToBigError(
            f"HTTP headers have a size of {size} bytes, which is to bigger than the "
            f"allowed {SHIELDSIO_MAX_HEADER_SIZE} bytes"
        )
    log.debug(f"HTTP-header-size: {size}")

    try:
        # ToDo: should we even call the API?
        # it doesn't report misconfigs anyway..
        # It should suffice to call it when we actually need svg data
        resp = requests.get(SHIELDSIO_API_URL, params)
    except requests.RequestException:
        raise errors.ServerError("shield.io can not be reached, maybe its down?")
    # checking returncode not needed, shield.io always returns 200

    badge = Badge(text, resp.url)
    log.info(f"created {badge}")

    return badge
