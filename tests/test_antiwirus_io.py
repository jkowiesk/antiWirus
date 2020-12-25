from antywirus.antiwirus_io import read_from_index_file
from io import StringIO

def test_read_from_index_file_basic_input():
    handle = StringIO(
        "name,path,size,mod_date,scan_date\n"
        + "marek,/home/kuba/marek,2020-12-25 19:30:56,2020-12-25 19:30:56\n"
        + "franek,/home/kuba/marek,2020-12-24 19:30:56,2020-12-24 19:30:57\n"
    )