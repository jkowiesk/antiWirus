from ..package.index_file import IndexFile, File


def test_change_file():
    file1 = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    file_list = [file1]
    index = IndexFile(file_list)
    file2 = File("test2", "/home/kuba/test", "33", "file", "2020-12-25 19:30:59", "2020-12-25 19:30:56")
    index.change_file(file1, file2)

    assert len(index.files_list()) == 1
    assert index.files_list()[0] == file2