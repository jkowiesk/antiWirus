"""
antiwirus.py - class with all the most important methods

Contains an IndexFile object and a list of rules type functions.
It is the only class that communicates with the interface.
Class has methods that enable fast scanning, simple scanning,
repairing - cutting out viruses and updating the IndexFile object.
"""
from .index_file import IndexFile, File
from .antiwirus_io import get_file_object, get_files_str
from .rules import RULES
from datetime import datetime
import time
import os


class ScanPathError(Exception):
    pass


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
        self._index_file.set_path(new_path)

    def get_files_to_index_file(self, scan_path):
        files = self._get_files(scan_path)
        self._index_file.set_scan_path(scan_path)
        self._index_file.set_files_list(files)
        self._index_file.dump_to_index_file()

    def get_scan_path(self):
        """
        Get scans path for index file
        """
        if self._index_file.files_list():
            paths = []
            for file in self._index_file.files_list():
                paths.append(file.path)
            self._index_file.set_scan_path(min(paths))

    def is_index_scan_path(self):
        """
        Returns True if index file contains scan path lese False
        """
        if self._index_file.scan_path():
            return True
        else:
            return False

    def set_index_scan_path(self, scan_path):
        self._index_file.set_scan_path(scan_path)

    def from_file_to_list(self):
        self._index_file.get_index_file()

    def dump_list_to_flie(self):
        self._index_file.dump_to_index_file()

    def update_index_file(self):
        """
        Updates index file
        """
        scan_path = self._index_file.scan_path()
        if scan_path:
            self.get_files_to_index_file(scan_path)
        else:
            raise ScanPathError("Scan path of index does not exist")

    def _set_files_scan_time(self):
        scan_date = time.time()
        time_format = "%a %b %d %H:%M:%S %Y"
        scan_date = time.ctime(scan_date)
        scan_date = datetime.strptime(scan_date, time_format)
        files = []
        for file in self._index_file.files_list():
            file.set_scan_date(scan_date)
            files.append(file)
        self._index_file.set_files_list(files)

    def fast_scan(self) -> list:
        """
        Checks if files was modified and scans them if they were. Returns viruses list with rule which file failed,
        what file contains and file object
        """
        scan_path = self._index_file.scan_path()
        files = self._get_files(scan_path)
        viruses = []
        for file in files:
            if file.is_modified():
                file_str = get_files_str(file)
                for rule in self.rules():
                    if rule(file, file_str):
                        viruses.append((file, file_str, rule))
        return viruses

    def easy_scan(self, path) -> list:
        """
        Scans files and returns viruses list with rule which file failed, what file
        contains and file object
        """
        files = self._get_files_easy_scan(path)
        viruses = []
        for file in files:
            file_str = get_files_str(file)
            for rule in self.rules():
                if rule(file, file_str):
                    viruses.append((file, file_str, rule))
        return viruses

    def repair_fast_scan(self, viruses):
        """
        Repairs virused files for fast scan
        """
        for file, file_str, rule in viruses:
            new_file = rule(file, file_str, mode="repair")
            self._index_file.change_file(file, new_file)
        self._set_files_scan_time()

    def repair_easy_scan(self, viruses):
        """
        Repairs virused files for easy scan
        """
        for file, file_str, rule in viruses:
            rule(file, file_str, mode="repair")

    def _get_files_easy_scan(self, path) -> list:
        """
        Returns list of files in given path and adds scan date
        """
        os.chdir(path)
        files = []
        for file_name in os.listdir():
            try:
                file = get_file_object(file_name, path)
            except FileNotFoundError:
                continue
            if file.ftype == "folder":
                files += self._get_files_easy_scan(f"{path}/{file.name}")
            else:
                files.append(file)
        return files

    def _get_files(self, path) -> list:
        """
        Returns list of files in given path
        """
        os.chdir(path)
        files = []
        for file_name in os.listdir():
            file = get_file_object(file_name, path)
            scan_date = self._index_file.get_scan_date(file)
            file.set_scan_date(scan_date)
            if file.ftype == "folder":
                files += self._get_files(f"{path}/{file.name}")
            else:
                files.append(file)
        return files
