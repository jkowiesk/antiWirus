import time
import os
import datetime

path = os.getcwd()

for file in os.listdir():
    if file == "viruses":
        info1 = os.stat(file)
    if file == "__init__.py":
        info2 = os.stat(file)
    # if file == "eicarcom2.zip":
    #     info3 = os.stat(file)

print(info1)
print(info2)
# print(info3)

t = time.ctime(info1.st_mtime)
t = datetime.datetime.strptime(t, "%a %b %d %H:%M:%S %Y")
print(t)