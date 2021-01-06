import time
from datetime import datetime


class File():
    def __init__(self, name: str, path: str, size: int, ftype: int, mod_date: int, scan_date: int):
        self.set_name(name)
        self.set_path(path)
        self.set_size(size)
        self.set_ftype(ftype)
        self.set_mod_date(mod_date)
        self.set_scan_date(scan_date)

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def path(self):
        return self._path

    def set_path(self, path):
        self._path = path

    def size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def ftype(self):
        return self._ftype

    def set_ftype(self, ftype):
        self._ftype = ftype

    def mod_date(self):
        return self._mod_date

    def set_mod_date(self, mod_date):
        # import ctime
        # time_format = "%a %b %d %H:%M:%S %Y"
        # mod_date = time.ctime(mod_date)
        # mod_date = datetime.datetime.strptime(mod_date, time_format)
        # self._mod_date = mod_date
        mod_date = datetime.strptime(mod_date, "%Y-%m-%d %H:%M:%S")
        self._mod_date = mod_date

    def scan_date(self):
        return self._scan_date

    def set_scan_date(self, scan_date):
        scan_date = datetime.strptime(scan_date, "%Y-%m-%d %H:%M:%S")
        self._scan_date = scan_date

    def is_modified(self) -> bool:
        """
        Return true if file was modified after last scan, or false if not
        """
        return True if self.mod_date() > self.scan_date() else False
