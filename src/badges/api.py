import logging

import requests

from badges import Badge


SHIELDSIO_API_URL = "https://img.shields.io/static/v1"
log = logging.getLogger("badges")


def _create_badge(text: str, color: str, icon: str, label: str = "") -> Badge | None:
    """internal version that assuems all parameters are valid and tidy.
    Returns the Badge or `None` if not succesfull"""

    params = {
        "logo": icon,
        "label": label,
        "labelColor": "gray",
        "message": text,
        "color": color,
    }
    resp = requests.get(SHIELDSIO_API_URL, params)
    if not resp.ok:
        log.warning(
            f"shield.io responden with status-code {resp.status_code}"
        )  # ToDo: should this stay??
        return None

    badge = Badge(text, resp.url)
    log.info(f"created {badge}")

    return badge
