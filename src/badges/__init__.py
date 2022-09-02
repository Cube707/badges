from typing import overload

import requests

from . import errors


__doc__ = "package to create static, standartised badges via the shields.io API"
__version__ = "0.0.0-dev0"
__all__ = ["Badge", "errors"]


class Badge:
    """A class representing a created badge.

    You can either pass a Response object after calling a shields.io
    URL or initalize manually. The class will to it's best to validate
    the parameters.

    Args:
        name (str): The name of the badge (identical to its text)
        response (requests.Response): from shields.io
        url (str, optional): manually pass a URL
        svg (str, optional): manually pass svg data

    Raises:
        ParameterError: if a configuration error is detected
    """

    name: str
    svg_data: str

    @overload
    def __init__(self, name: str, *, response: requests.Response):
        ...

    @overload
    def __init__(self, name: str, *, url: str, svg: str):
        ...

    def __init__(
        self,
        name: str,
        *,
        response: requests.Response = None,
        url: str = None,
        svg: str = None,
    ) -> None:
        self.name = name
        if response is not None:
            if not isinstance(response, requests.Response):
                raise errors.ParameterError(
                    "Badge() argument 'response' must be of type 'Response'"
                )
            self._url = response.url
            self.svg_data = response.text
        else:
            if url is None:
                raise errors.ParameterError(
                    "Badge() missing 1 required keyword argument: 'url'"
                )
            if svg is None:
                raise errors.ParameterError(
                    "Badge() missing 1 required keyword argument: 'svg'"
                )
            self._url = url
            self.svg_data = svg

    def __repr__(self) -> str:
        return f"<Badge object '{self.name}'>"

    @property
    def url(self) -> str:
        "the badge URL on shields.io"
        return self.url_flat

    @property
    def url_plastic(self) -> str:
        "the platic style badge URL on shields.io"
        return self._url + "&style=plastic"

    @property
    def url_flat(self) -> str:
        "the flat style badge URL on shields.io"
        return self._url + "&style=flat"

    @property
    def url_flat_square(self) -> str:
        "the flat-square style badge URL on shields.io"
        return self._url + "&style=flat-square"

    @property
    def url_for_the_badge(self) -> str:
        "the for-the-badge style badge URL on shields.io"
        return self._url + "&style=for-the-badge"

    @property
    def url_social(self) -> str:
        "the social style badge URL on shields.io"
        return self._url + "&style=social"
