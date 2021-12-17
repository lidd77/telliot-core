""" Telliot CLI

A simple interface for interacting with telliot_core's functionality.
Configure telliot_core's settings via this interface's command line flags
or in the configuration file.
"""
import click

from telliot_core.cli.commands.catalog import catalog
from telliot_core.cli.commands.config import config
from telliot_core.cli.commands.query import query
from telliot_core.cli.commands.read import read
from telliot_core.utils.versions import show_telliot_versions


@click.group(invoke_without_command=True)
@click.pass_context
@click.option(
    "--chain_id",
    type=int,
    help="Override chain ID (the default is provided by main config file).",
)
@click.option("--version", is_flag=True, help="Display telliot-core version and exit.")
def main(ctx: click.Context, version: bool, chain_id: int) -> None:
    ctx.ensure_object(dict)
    ctx.obj["chain_id"] = chain_id
    if version:
        show_telliot_versions()
        return

    """Telliot command line interface"""
    show_telliot_versions()
    if ctx.invoked_subcommand is None:
        print(ctx.command.get_help(ctx))


main.add_command(config)
main.add_command(read)
main.add_command(query)
main.add_command(catalog)

if __name__ == "__main__":
    main()
