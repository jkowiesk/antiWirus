from ..package.antiwirus import AntiWirus
import os
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
