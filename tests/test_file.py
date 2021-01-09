from ..package.file import File
from datetime import datetime


def test_files_init():
    file = File("test1", "/home/kuba/test","33", "file", "2020-12-25 19:30:56", "2020-12-25 19:30:56")

    assert file.name == "test1"
    assert file.scan_date() == "2020-12-25 19:30:56"


def test_file_if_modified():
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")

    assert file.is_modified()


def test_file_if_mod_None():
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")

    assert file.is_modified()