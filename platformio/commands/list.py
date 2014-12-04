# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.

import click

from platformio.platforms.base import PlatformFactory


@click.command("list", short_help="List installed platforms")
def cli():

    installed_platforms = PlatformFactory.get_platforms(
        installed=True).keys()
    installed_platforms.sort()

    for platform in installed_platforms:
        p = PlatformFactory.newPlatform(platform)
        click.echo("{name:<20} with packages: {pkgs}".format(
            name=click.style(p.get_name(), fg="cyan"),
            pkgs=", ".join(p.get_installed_packages())
        ))
