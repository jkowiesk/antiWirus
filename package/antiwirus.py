from .index_file import IndexFile, File
from .antiwirus_io import get_file_object
from .rules import RULES
import os


class AntiWirus():
    def __init__(self):
        self.set_index_file()
        self.set_rules(RULES)

    def index_file(self):
        return self._index_file

    def set_index_file(self):
        self._index_file = IndexFile()

    def rules(self):
        return self._rules

    def set_rules(self, rules):
        self._rules = rules

    def scan_for_files_to_index(self, scan_path):
        files = self._get_files(scan_path)
        self.index_file().set_files_list(files)

    def index_to_file(self):
        self.index_file().dump_to_index_file()

    def from_file_to_index(self):
        self.index_file().get_index_file()

    def _get_files(self, path):
        os.chdir(path)
        files = []
        for file_name in os.listdir():
            file = get_file_object(file_name, path)
            if file.ftype == "folder":
                files += self._get_files(f"{path}/{file.name}")
            else:
                files.append(file)
        return files
