from .index_file import IndexFile, File
from .antiwirus_io import get_file_object, get_files_str, get_secrets
import os

RULES = get_secrets()

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

    def set_index_file_path(self, new_path):
        self.index_file().set_path(new_path)

    def get_files_to_index(self, scan_path):
        files = self._get_files(scan_path)
        self.index_file().set_files_list(files)
        self.index_file().dump_to_index_file()

    def update_index_file(self):
        pass

    def from_file_to_list(self):
        self.index_file().get_index_file()

    def easy_scan(self, path):
        files = self._get_files(path)
        for file in files:
            for rule in self.rules():
                file_str = get_files_str()
                if rule(file, file_str):
                    pass

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
