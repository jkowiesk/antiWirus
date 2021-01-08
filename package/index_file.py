from .file import File
from .antiwirus_io import read_from_index_file, write_to_index_file
import os

class IndexFile():
    def __init__(self, files_list=None, path=f"{os.getcwd()}/index_file"):
        self.set_files_list(files_list)
        self.set_path(path)

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

    def add_file(self, name, path, size, ftype, mod_date, scan_date):
        file = File(name, path, size, ftype, mod_date, scan_date)
        self._files_list.append(file)

    def get_index_file(self):
        with open(self.path(), "r") as handle:
            files = read_from_index_file(handle)
        self.set_files_list(files)

    def dump_to_index_file(self):
        with open(self.path(), "w") as handle:
            write_to_index_file(handle, self.files_list())
