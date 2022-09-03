# full name imports to keep autocomplete clean and
# reduce collisions between packages
import requests


class BadgesBaseError(Exception):
    pass


class ServerError(BadgesBaseError, requests.RequestException):
    """the server of an external service returned an error"""


class ParameterError(BadgesBaseError, TypeError, ValueError):
    """missconfiguration when calling a badges-function"""


class BadgeCreationError(BadgesBaseError):
    """it was not possible to create the requested badge"""
