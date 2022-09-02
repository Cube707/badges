import requests

from badges.errors import ConnectionError, ConnectionTimeoutError


def check_simpleicon(name: str) -> bool:
    """checks if a given name existis on simpleicon.org"""

    url = f"https://simpleicons.org/icons/{name}.svg"
    try:
        r = requests.get(url, timeout=0.5)
        if r.ok:
            return True
    except requests.exceptions.Timeout:
        raise ConnectionTimeoutError("request to 'simpleicons.org' timed out")
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "couldn't connect to 'simpleicons.org', this shouldn't happen and "
            "means your internet connection is seriously messed up!"
        )
    return False
