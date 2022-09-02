# full name imports to keep autocomplete clean and
# reduce collisions between packages
import requests.exceptions


class BadgesBaseError(Exception):
    pass


class ConnectionError(BadgesBaseError, requests.exceptions.ConnectionError):
    """it was not possible to connect to an external service"""

    pass


class ConnectionTimeoutError(BadgesBaseError, requests.exceptions.Timeout):
    """a request to an external service timed out"""

    pass
