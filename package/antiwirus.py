from .index_file import IndexFile, File
from .antiwirus_io import get_file_object, get_files_str
from .rules import RULES
import os


class AntiWirus():
    def __init__(self):
        self.set_index_file()
        self.set_rules(RULES)

    def index_file(self):
        return self._index_file

    def set_index_file(self, path=None, scan_path=None):
        self._index_file = IndexFile(None, path, scan_path)

    def is_index_file_loaded(self):
        if self._index_file.path():
            return True
        else:
            return False

    def remove_index_file(self):
        os.remove(f"{self._index_file.path()}/.index_file")
        self.set_index_file(path=self._index_file.path())

    def rules(self):
        return self._rules

    def set_rules(self, rules):
        self._rules = rules

    def set_index_file_path(self, new_path):
        self.index_file().set_path(new_path)

    def get_files_to_index_file(self, scan_path):
        files = self._get_files(scan_path)
        self.index_file().set_scan_path(scan_path)
        self.index_file().set_files_list(files)
        self.index_file().dump_to_index_file()

    def get_scan_path(self):
        if self._index_file.files_list():
            paths = []
            for file in self._index_file.files_list():
                paths.append(file.path)
            self._index_file.set_scan_path(min(paths))

    def from_file_to_list(self):
        self.index_file().get_index_file()

    def dumb_list_to_flie(self):
        self.index_file().dump_to_index_file()

    def update_index_file(self):
        scan_path = self.index_file().scan_path()
        if scan_path:
            self.get_file_object(scan_path)
        else:
            raise Exception

    def fast_scan(self):
        scan_path = self.index_file().scan_path()
        files = self._get_files(scan_path)
        viruses = []
        for file in files:
            if file.is_modified():
                file_str = get_files_str(file)
                for rule in self.rules():
                    if rule(file, file_str):
                        viruses.append((file, file_str, rule))
        return viruses

    def easy_scan(self, path):
        files = self._get_files(path)
        viruses = []
        for file in files:
            if file.is_modified():
                file_str = get_files_str(file)
                for rule in self.rules():
                    if rule(file, file_str):
                        viruses.append((file, file_str, rule))
        return viruses

    def repair_fast_scan(self, viruses):
        for file, file_str, rule in viruses:
            new_file = rule(file, file_str, mode="repair")
            self.index_file().change_file(file, new_file)

    def repair_easy_scan(self, viruses):
        for file, file_str, rule in viruses:
            new_file = rule(file, file_str, mode="repair")

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
