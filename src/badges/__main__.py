import logging

import click

from badges import __version__, api, utils


log = logging.getLogger("badges")


def _validate_color(ctx, param, val):
    if param.name == "color" and val is not None:
        if not utils.check_html_color(val):
            raise click.BadParameter(f"'{val}' is not a valid html-color")
    return val


def _validate_simpleicon(ctx, param, val):
    if param.name == "icon_name" and val is not None:
        if not utils.check_simpleicon(val):
            raise click.BadParameter(f"'{val}' doesn't exist on simpleicon.org")
    return val


def _change_logging(ctx, param, val):
    if param.name == "quiet" and val:
        log.setLevel(logging.CRITICAL)
    if param.name == "verbos" and val:
        log.setLevel(logging.DEBUG)


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


@cli.command
@click.option(
    "-t",
    "--text",
    type=str,
    required=True,
    help="The text displayed on the right side of the badge.",
)
@click.option(
    "-c",
    "--color",
    type=str,
    required=True,
    callback=_validate_color,
    help="Background color to be used behind the text.",
)
@click.option(
    "-i",
    "--icon-name",
    type=str,
    callback=_validate_simpleicon,
    help="Icon-name from https://simpleicons.org/ ",
    default=None,
)
@click.option(
    "-f",
    "--icon-file",
    type=click.Path(exists=True, dir_okay=False),
    help="A icon-file to be used, should be a svg, put png is also acceptable.",
    default=None,
)
@click.option(
    "-l",
    "--label",
    type=str,
    help="Label to be put next to the icon.",
    default="",
)
@click.option(
    "-o",
    "--output",
    type=click.File("w", atomic=True),
    help="File to save the generated svg to.",
    default="-",
)
@click.option(
    "-s",
    "--style",
    help="Style of the generate badge.",
    type=click.Choice(
        ["plastic", "flat", "flat-square", "for-the-badge", "social"],
        case_sensitive=False,
    ),
    default="flat",
)
@click.option(
    "--url",
    "output_type",
    flag_value="url",
    help="Outputs as URL.",
)
@click.option(
    "--svg",
    "output_type",
    flag_value="svg",
    help="Output as svg data.",
    default=True,
)
@click.option(
    "-v",
    "--verbos",
    is_flag=True,
    help="Enbale extensive logging.",
    expose_value=False,
    is_eager=True,
    callback=_change_logging,
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Disable logging.",
    expose_value=False,
    is_eager=True,
    callback=_change_logging,
)
@click.help_option("-h", "--help")
def create(text, color, icon_name, icon_file, output, label, output_type, style):
    """Create a badge. Uses the given options to querry the shield.io API and
    returnes either the URL or the full svg data.
    """

    if icon_name is not None:
        icon = icon_name

    if icon_file is not None:
        icon = icon_name
        pass  # ToDo

    if icon_name is not None and icon_file is not None:
        log.warning(
            "you are using both 'icon-name' and 'icon-file', but can only use one! "
            "I am going to use 'icon-file'"
        )

    if icon_name is None and icon_file is None and label == "":
        log.warning(
            "missing 'icon-name', 'icon-file' and 'label', the badge might look wird."
        )

    badge = api._create_badge(text, color, icon, label)
    if badge is None:
        log.error("badge could not be created.")
        return

    if output_type == "url":
        output.write(badge.get_url(style))
    if output_type == "svg":
        output.write(badge.get_svg(style))


if __name__ == "__main__":
    cli()
