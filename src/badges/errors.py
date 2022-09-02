# full name imports to keep autocomplete clean and
# reduce collisions between packages
import requests.exceptions


class BadgesBaseError(Exception):
    pass


class ConnectionError(BadgesBaseError, requests.exceptions.ConnectionError):
    """it was not possible to connect to an external service"""


class ConnectionTimeoutError(BadgesBaseError, requests.exceptions.Timeout):
    """a request to an external service timed out"""


class ServerError(BadgesBaseError):
    """the server of an external service returned an error"""


class ParameterError(BadgesBaseError, TypeError, ValueError):
    """missconfiguration when calling a badges-function"""


class BadgeCreationError(BadgesBaseError):
    """it was not possible to create the requested badge"""
