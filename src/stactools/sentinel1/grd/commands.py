import logging
import os

import click

from stactools.sentinel1.grd.stac import create_item, create_item_from_zip

logger = logging.getLogger(__name__)


@click.group("grd")
def grd_cmd():
    """Commands for working with sentinel1 GRD data"""
    pass


@grd_cmd.command(
    "create-item",
    short_help="Convert a Sentinel1 GRD scene into a STAC item",
)
@click.argument("src")
@click.argument("dst")
@click.option("--zip/--no-zip", default=False)
def create_item_command(src, dst, zip):
    """Creates a STAC Collection

    Args:
        src (str): path to the scene
        dst (str): path to the STAC Item JSON file that will be created
    """
    if not zip:
        item = create_item(src)
    else:
        item = create_item_from_zip(src)

    item_path = os.path.join(dst, "{}.json".format(item.id))
    item.set_self_href(item_path)

    item.save_object()
