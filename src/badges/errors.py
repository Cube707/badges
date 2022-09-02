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


class ServerError(BadgesBaseError):
    """the server of an external service returned an error"""

    pass


class ParameterError(BadgesBaseError, TypeError, ValueError):
    """missconfiguration when calling a badges-function"""

    pass


class BadgeCreationError(BadgesBaseError):
    """it was not possible to create the requested badge"""

    pass
