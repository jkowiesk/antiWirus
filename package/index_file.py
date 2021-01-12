from .file import File
from .antiwirus_io import read_from_index_file, write_to_index_file
import os
CWD = os.getcwd()


class IndexFile():
    def __init__(self, files_list=None, path=f"{CWD}/index_file", scan_path=None):
        self.set_files_list(files_list)
        self.set_path(path)
        self.set_scan_path(scan_path)

    def path(self):
        return self._path

    def set_path(self, path):
        self._path = path

    def files_list(self):
        return self._files_list

    def set_files_list(self, files_list):
        if files_list:
            self._files_list = files_list
        else:
            self._files_list = []

    def scan_path(self):
        return self._scan_path

    def set_scan_path(self, scan_path):
        if scan_path:
            self._scan_path = scan_path
        else:
            self._scan_path = None

    def delete_file(self, old_file):
        self._files_list.remove(old_file)

    def change_file(self, old_file, new_file):
        self.delete_file(old_file)
        self.add_file(new_file)

    def add_file(self, new_file):
        if new_file:
            self._files_list.append(new_file)
        else:
            return None

    def get_index_file(self):
        with open(self.path(), "r") as handle:
            files = read_from_index_file(handle)
        self.set_files_list(files)

    def dump_to_index_file(self):
        with open(self.path(), "w") as handle:
            write_to_index_file(handle, self._files_list)
