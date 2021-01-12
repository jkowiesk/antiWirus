from ..package.antiwirus import AntiWirus
import os
PATH = os.getcwd()


def test_antiwirus_init():
    antivirus = AntiWirus()


def test_secrets_import():
    antivirus = AntiWirus()

    rules = antivirus.rules()

    dangerous_strings = rules["dangerous_strings"][0]

    assert dangerous_strings == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"


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
