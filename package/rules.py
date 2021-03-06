from .file import File
from .antiwirus_io import (read_from_index_file,
                           get_secrets,
                           repair_dangerous_string)
import json
import os
from .settings import CWD
RULES = []

path = f"{CWD}/secrets.json"

secrets = get_secrets()


def rule_dangerous_string(file, file_str, mode=""):
    """
    Dangerous string in file
    """
    if mode == "repair":
        for dangerous_string in secrets["dangerous_strings"]:
            if dangerous_string in file_str:
                with open(f"{file.path}/{file.name}", "w") as handle:
                    repair_dangerous_string(handle, file_str, dangerous_string)
                return file
    else:
        for dangerous_string in secrets["dangerous_strings"]:
            if dangerous_string in file_str:
                return True
        return False


def rule_dangerous_extension(file, file_str, mode=""):
    """
    Dangerous file extension
    """
    if mode == "repair":
        path = f"{file.path}/{file.name}"
        if file.extension() in secrets["extensions"]:
            os.remove(path)
        return None
    else:
        if file.extension() in secrets["extensions"]:
            return True
        return None


RULES = [rule_dangerous_string,
         rule_dangerous_extension]