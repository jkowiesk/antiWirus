from ..package.antiwirus_io import (read_from_index_file, write_to_index_file,
                                    repair_dangerous_string, get_secrets)
from io import StringIO
from ..package.index_file import IndexFile, File
import os

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

    file1 = File("test1", "/home/kuba/test", "33", "file", "2020-12-25 19:30:56")
    file2 = File("test2", "/home/kuba/test", "100", "file", "2020-12-25 19:30:52")

    index.add_file(file1)
    index.add_file(file2)

    write_to_index_file(handle, index.files_list())

    a = handle.getvalue().splitlines()

    assert handle.getvalue().splitlines() == [
        "name,path,size,ftype,mod_date,scan_date",
        "test1,/home/kuba/test,33,file,2020-12-25 19:30:56,",
        "test2,/home/kuba/test,100,file,2020-12-25 19:30:52,"
    ]


def test_secrets_import(monkeypatch):
    path = f"{os.getcwd()}"

    if "tests" in path:
        path = f"{path}/../.."

    monkeypatch.setattr("os.getcwd", lambda : f"{path}")

    rules = get_secrets()

    dangerous_strings = rules["dangerous_strings"][0]

    assert dangerous_strings == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"


def test_repair_dangerous_string():
    handle = StringIO()

    file_str = "jdsaijdsaijdsaijsdafdkVIRUSsljfsd"
    virus_str = "VIRUS"

    repair_dangerous_string(handle, file_str, virus_str)

    assert handle.getvalue().splitlines() == [
        "jdsaijdsaijdsaijsdafdksljfsd"
    ]