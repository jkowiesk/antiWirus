import time
import os
import datetime

path = os.getcwd()

for file in os.listdir():
    if file == "notatki":
        info = os.stat(file)


t = datetime.datetime.strptime(time.ctime(info.st_mtime), "%a %b %d %H:%M:%S %Y")


print(t)