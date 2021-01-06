from antywirus.file import File
from datetime import datetime


def test_files_init():
    file = File("test1", "/home/kuba/test","33", "2020-12-25 19:30:56", "2020-12-25 19:30:56")

    assert file.name() == "test1"
    assert file.scan_date() == datetime.strptime("2020-12-25 19:30:56", "%Y-%m-%d %H:%M:%S")

def test_file_if_modified():
    file = File("test1", "/home/kuba/test","33", "2020-12-25 19:30:59", "2020-12-25 19:30:56")

    assert file.is_modified() == True