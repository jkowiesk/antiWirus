from ..package.antiwirus_io import read_from_index_file, write_to_index_file
from io import StringIO
from ..package.index_file import IndexFile, File


def test_read_from_index_file_basic_input():
    handle = StringIO(
        "name,path,size,ftype,mod_date,scan_date\n"
        + "test1,/home/kuba/test,33,file,2020-12-25 19:30:56,2020-12-25 19:30:56\n"
        + "test2,/home/kuba/test,100,file,2020-12-24 19:30:56,2020-12-24 19:30:57\n"
    )

    files = read_from_index_file(handle)

    assert files[0].name == "test1"
    assert files[1].name == "test2"


def test_write_to_index_file():
    handle = StringIO()

    index = IndexFile()

    index.add_file("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:56", "2020-12-25 19:30:56")
    index.add_file("test2", "/home/kuba/test", "100", "file", "2020-12-25 19:30:52", "2020-12-25 19:30:30")

    write_to_index_file(handle, index.files_list())

    a = (handle.getvalue().splitlines())

    assert handle.getvalue().splitlines() == [
        "name,path,size,ftype,mod_date,scan_date",
        "test1,/home/kuba/test,33,file,2020-12-25 19:30:56,2020-12-25 19:30:56",
        "test2,/home/kuba/test,100,file,2020-12-25 19:30:52,2020-12-25 19:30:30"
    ]
