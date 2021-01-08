import csv
import os
import time
from .file import File
from datetime import datetime


def read_from_index_file(handle):
    reader = csv.DictReader(handle, delimiter=",")
    files = []
    for row in reader:
        name = row["name"]
        path = row["path"]
        size = row["size"]
        ftype = row["ftype"]
        mod_date = row["mod_date"]
        scan_date = row["scan_date"]
        file = File(name, path, size, ftype, mod_date, scan_date)
        files.append(file)
    return files


def write_to_index_file(handle, files):
    field_names = ['name', 'path', 'size', 'ftype', 'mod_date', 'scan_date']
    writer = csv.DictWriter(handle, fieldnames=field_names)
    writer.writeheader()
    for file in files:
        writer.writerow({'name': file.name, 'path': file.path, 'size': file.size, 'ftype': file.ftype, 'mod_date': file.mod_date(), 'scan_date': file.scan_date()})


def get_file_object(file_name, path):
    os.chdir(path)
    info = os.stat(file_name)

    time_format = "%a %b %d %H:%M:%S %Y"
    file_mod_date = time.ctime(info.st_mtime)
    file_mod_date = datetime.strptime(file_mod_date, time_format)

    file_size = str(info.st_size)

    file_type = "folder" if info.st_mode == 16893 else "file"

    name, path, size, ftype, mod_date = file_name, path, file_size, file_type, file_mod_date

    file = File(name, path, size, ftype, mod_date)

    return file
