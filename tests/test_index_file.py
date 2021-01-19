from ..package.index_file import IndexFile, File
from datetime import datetime


def test_change_file():
    file1 = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    file_list = [file1]
    index = IndexFile(file_list)
    file2 = File("test2", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    index.change_file(file1, file2)

    assert len(index.files_list()) == 1
    assert index.files_list()[0] == file2


def test_index_files_init():
    index_file = IndexFile()


def test_index_add_file():
    index_file = IndexFile()
    file = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    index_file.add_file(file)
    assert index_file.files_list()[0] == file


def test_index_file_change_file():
    index_file = IndexFile()
    file1 = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    file2 = File("test2", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    index_file.add_file(file1)
    index_file.change_file(file1, file2)
    assert index_file.files_list()[0] == file2


def test_get_scan_date():
    index_file = IndexFile()
    file1 = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    file2 = File("test2", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59",)
    index_file.add_file(file1)
    index_file.add_file(file2)
    assert index_file.get_scan_date(file1) == datetime.strptime("2020-12-25 19:30:56", "%Y-%m-%d %H:%M:%S")
    assert not index_file.get_scan_date(file2)