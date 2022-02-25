import tempfile
import zipfile
import os
from contextlib import contextmanager


@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def _find_safe(href_zip: str):
    with zipfile.ZipFile(href_zip, "r") as archive:
        for name in archive.namelist():
            dir_name = os.path.dirname(name)
            if dir_name.endswith("SAFE"):
                return dir_name


def read_zipped_href(href: str):

    href_zip = f"{href.split('.zip')[0]}.zip"
    href_safe = _find_safe(href_zip)
    href_rel = os.path.normpath("/".join(href.split(".zip")[1:])).split(os.sep)
    href_rel = os.path.join(href_safe, *href_rel)

    zipfile.ZipFile(href_zip).extract(href_rel, os.getcwd())
    return os.path.join(os.getcwd(), href_rel)


def get_vsizip_href(href: str):

    href_zip = f"{href.split('.zip')[0]}.zip"
    href_safe = _find_safe(href_zip)
    href_rel = os.path.normpath("/".join(href.split(".zip")[1:])).split(os.sep)
    href_rel = os.path.join(href_safe, *href_rel)
    href_full = os.path.join(href_zip, href_rel)
    href_vsizip = "/vsizip" + os.path.normpath(href_full)

    return href_vsizip
