from .file import File
from .antiwirus_io import read_from_index_file, get_secrets
import json
import os
RULES = []

path = f"{os.getcwd()}/secrets.json"

secrets = get_secrets(path)


def rule_dangerous_string(file, str):



RULES = [rule_virus_in_string]