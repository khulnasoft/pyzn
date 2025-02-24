import os
from datetime import datetime, timedelta
from typing import Optional

import click
from click import BadParameter

from pyzn.application.command import UpdateVersionDownloads, ImportTotalDownloads
from pyzn.domain.model import Password
from pyzn.infrastructure import container


@click.group()
def cli():
    pass


@cli.command("import:downloads:day")
@click.option("--day", help="The day to import downloads", default=lambda: os.environ.get("PYZN_DOWNLOADS_DAY", ""))
def import_day_downloads_action(day: Optional[str]):
    try:
        date = datetime.now() - timedelta(days=1)
        if day is not None and day.strip() != "":
            date = datetime.strptime(day, "%Y-%m-%d")
    except ValueError:
        raise BadParameter("Date format should be YYYY-mm-dd")
    click.echo("Importing downloads...")
    container.command_bus.publish(UpdateVersionDownloads(date.date()))
    click.echo("Done")


@cli.command("import:total_downloads")
@click.option("--file", prompt=True, help="The file path. It should have project, total downloads format")
def import_total_downloads_from_csv(file: str):
    click.echo("Importing downloads...")
    container.command_bus.publish(ImportTotalDownloads(file))
    click.echo("Done")
