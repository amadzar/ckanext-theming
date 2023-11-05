import click


@click.group(short_help="theming CLI.")
def theming():
    """theming CLI.
    """
    pass


@theming.command()
@click.argument("name", default="theming")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [theming]
