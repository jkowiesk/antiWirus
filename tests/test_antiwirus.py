from ..package.antiwirus import AntiWirus

def test_antiwirus_init():
    antivirus = AntiWirus()

def test_secrets_import():
    antivirus = AntiWirus()

    rules = antivirus.rules()

    assert rules["dangerous_strings"] == "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"