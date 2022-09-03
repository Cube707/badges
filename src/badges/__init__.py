from typing import Literal

import requests

from . import errors


__doc__ = "package to create static, standartised badges via the shields.io API"
__version__ = "0.0.1-dev0"
__all__ = ["Badge", "errors"]


class Badge:
    """A class representing a created badge.

    You can either pass a Response object after calling a shields.io
    URL or initalize manually. The class will to it's best to validate
    the parameters.

    Args:
        name (str): The name of the badge (identical to its text)
        url (str): the URL of the badge
    """

    name: str

    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self._url = url

    def __repr__(self) -> str:
        return f"<Badge object '{self.name}'>"

    def get_svg(
        self,
        style: Literal[
            "plastic", "flat", "flat-square", "for-the-badge", "social"
        ] = "flat",
    ) -> str:
        r = requests.get(self.get_url(style))
        if not r.ok:
            raise errors.ServerError(f"shield.io returned status-code: {r.status_code}")
        return r.text

    def get_url(
        self,
        style: Literal[
            "plastic", "flat", "flat-square", "for-the-badge", "social"
        ] = "flat",
    ) -> str:
        "get the url for a specific style"
        return getattr(self, f"url_{style.replace('-','_')}")

    @property
    def url(self) -> str:
        "the default url"
        return self.get_url()

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
