from ..package.antiwirus import AntiWirus, ScanPathError
import os
import pytest
PATH = os.getcwd()


def test_antiwirus_init():
    antivirus = AntiWirus()


def test_easy_scan():
    path = f"{PATH}/tests/no_viruses"
    antywirus = AntiWirus()
    viruses = antywirus.easy_scan(path)
    assert not viruses


def test_easy_scan_viruses():
    path = f"{PATH}/tests/viruses"
    antywirus = AntiWirus()
    viruses = antywirus.easy_scan(path)
    assert len(viruses) == 4

def test_scan_path_error():
    antivirus = AntiWirus()
    with pytest.raises(ScanPathError):
        antivirus.update_index_file()

