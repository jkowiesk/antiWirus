import csv
from antywirus.file import File


def read_from_index_file(handle):
    reader = csv.DictReader(handle, delimiter=",")
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


def write_to_index_file(handle, files):
    field_names = ['name', 'path', 'size', 'mod_date', 'scan_date']
    writer = csv.DictWriter(handle, fieldnames=field_names)
    writer.writeheader()
    for file in files:
        writer.writerow({'name': file.name(), 'path': file.path(), 'size': file.size(), 'mod_date': file.mod_date(), 'scan_date': file.scan_date()})
