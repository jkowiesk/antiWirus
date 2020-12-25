import csv
from io import StringIO
from file import File


# name: str, path: str, size: int, mod_time: int, scan_time: int
def read_from_index_file(handle):
    reader = csv.reader(handle, delimiter=",")
    reader.readline()
    files = []
    for row in reader:
        name = row["name"]
        path = row["path"]
        size = row["size"]
        mod_date = row["mod_date"]
        scan_date = row["scan_date"]
        file = File(name, path, size, mod_date, scan_date)
        files.append(file)
    return files
