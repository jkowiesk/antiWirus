import time
from datetime import datetime


class File():
    def __init__(self, name: str, path: str, size: str, ftype: str, mod_date: datetime = None, scan_date: datetime = None):
        self.name = name
        self.path = path
        self.size = size
        self.ftype = ftype
        self.set_mod_date(mod_date)
        self.set_scan_date(scan_date)

    def mod_date(self):
        return self._mod_date

    def set_mod_date(self, mod_date):
        if mod_date:
            if type(mod_date) == str:
                mod_date = datetime.strptime(mod_date, "%Y-%m-%d %H:%M:%S")
            self._mod_date = mod_date
        else:
            self._mod_date = None

    def scan_date(self):
        return self._scan_date

    def set_scan_date(self, scan_date):
        if scan_date:
            if type(scan_date) == str:
                scan_date = datetime.strptime(scan_date, "%Y-%m-%d %H:%M:%S")
            self._scan_date = scan_date
        else:
            self._scan_date = None

    def is_modified(self) -> bool:
        """
        Return true if file was modified after last scan, or false if not
        """
        if self.scan_date():
            return True if self.mod_date() > self.scan_date() else False
        else:
            return True

        # return True if (self.mod_date() > self.scan_date()) else False

    def extension(self):
        """
        Picks out only extension from files name and returns it,
        if no extension returns None
        """
        name_list = self.name.split(".")
        return name_list[-1] if len(name_list) > 1 else None

    def __eq__(self, other):
        self_full_path = f"{self.path}/{self.name}"
        other_full_path = f"{other.path}/{other.name}"
        return True if self_full_path == other_full_path else False
