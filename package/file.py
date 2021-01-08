import time
from datetime import datetime


class File():
    def __init__(self, name: str, path: str, size: str, ftype: str, mod_date: str, scan_date: str = None):
        self.name = name
        self.path = path
        self.size = size
        self.ftype = ftype
        self.set_mod_date(mod_date)
        self.set_scan_date(scan_date)

    def mod_date(self):
        return self._mod_date

    def set_mod_date(self, mod_date):
        # mod_date = datetime.strptime(mod_date, "%Y-%m-%d %H:%M:%S")
        self._mod_date = mod_date

    def scan_date(self):
        return self._scan_date

    def set_scan_date(self, scan_date):
        if scan_date:
            # scan_date = datetime.strptime(scan_date, "%Y-%m-%d %H:%M:%S")
            self._scan_date = scan_date
        else:
            self._scan_date = None

    def is_modified(self) -> bool:
        """
        Return true if file was modified after last scan, or false if not
        """
        return True if self.mod_date() > self.scan_date() else False
