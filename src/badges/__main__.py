import logging

import click

from badges import __version__


log = logging.getLogger("badges")


@click.group
@click.help_option("-h", "--help")
@click.version_option(
    __version__,
    "-V",
    "--version",
    message="%(prog)s v%(version)s",
)
def cli():
    logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":
    cli()
