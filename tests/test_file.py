from ..package.file import File
from datetime import datetime


def test_files_init():
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:56", "2020-12-25 19:30:56")

    assert file.name == "test1"
    assert file.scan_date() == datetime.strptime("2020-12-25 19:30:56", "%Y-%m-%d %H:%M:%S")


def test_file_if_modified():
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")

    assert file.is_modified()


def test_file_if_mod_None():
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")

    assert file.is_modified()


def test_file_extension_common():
    file = File("test.txt", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")
    assert file.extension() == "txt"


def test_file_extension_without_extension():
    file = File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")
    assert not file.extension()


def test_file_if_is_in_list():
    file_list = [File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")]
    file = File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")
    assert file in file_list


def test_delete_file_in_list():
    file_list = [File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")]
    file = File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")
    file_list.remove(file)
    assert len(file_list) == 0


def test_change_files_name_in_list():
    file_list = [File("test", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59")]
    for file in file_list:
        file.name = "gitara"
    assert file_list[0].name == "gitara"
