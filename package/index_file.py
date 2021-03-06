"""
index_file.py - simple "database" type class

Contains a list of File objects, an absolute scan path,
and an absolute path to the folder where the ".index_file" file is located.
It allows you to perform various operations on files, replace the old with a new one, delete or simply add to the list.
Thanks to the antiwirus_io module, it can also create, read and overwrite the ".index_file" file.
"""
from .file import File
from .antiwirus_io import read_from_index_file, write_to_index_file
from .settings import CWD


class IndexFile():
    def __init__(self, files_list=None, path=None, scan_path=None):
        self.set_files_list(files_list)
        self.set_path(path)
        self.set_scan_path(scan_path)

    def path(self):
        return self._path

    def set_path(self, path=f"{CWD}"):
        if path:
            self._path = path
        else:
            self._path = None

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

    def get_scan_date(self, file_scan_date):
        for file in self._files_list:
            if file == file_scan_date:
                return file.scan_date()
        return None

    def delete_file(self, old_file):
        """
        Deletes file
        """
        self._files_list.remove(old_file)

    def change_file(self, old_file, new_file):
        """
        Deletes old file and adds new one to it
        """
        self.delete_file(old_file)
        self.add_file(new_file)

    def add_file(self, new_file):
        """
        Adds new file to list
        """
        if new_file:
            self._files_list.append(new_file)
        else:
            return None

    def get_index_file(self):
        """
        Reads from index file
        """
        path = f"{self.path()}/.index_file"
        with open(path, "r") as handle:
            files = read_from_index_file(handle)
        self.set_files_list(files)

    def dump_to_index_file(self):
        """
        Writes files to index file
        """
        path = f"{self.path()}/.index_file"
        with open(path, "w") as handle:
            write_to_index_file(handle, self._files_list)
