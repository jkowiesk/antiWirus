import time
import datetime


class File():
    def __init__(self, name: str, path: str, size: int, mod_date: int, scan_date: int):
        self.name = name
        self.path = path
        self.set_size(size)
        self.set_mod_date(mod_date)
        self.set_scan_date(scan_date)

    def size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def mod_date(self):
        return self._mod_date

    def set_mod_date(self, mod_date):
        time_format = "%a %b %d %H:%M:%S %Y"
        mod_date = time.ctime(mod_date)
        mod_date = datetime.datetime.strptime(mod_date, time_format)
        self._mod_date = mod_date

    def scan_date(self):
        return self._scan_date

    def set_scan_date(self, scan_date):
        time_format = "%a %b %d %H:%M:%S %Y"
        scan_date = time.ctime(scan_date)
        scan_date = datetime.datetime.strptime(scan_date, time_format)
        self._scan_date = scan_date

    def modified(self):
        """
        Return true if file was modified and false if not
        """
        return True if self.mod_date() == self.scan_date() else False