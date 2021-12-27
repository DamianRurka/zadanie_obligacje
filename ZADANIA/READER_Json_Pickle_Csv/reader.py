import json
import pickle
import csv
import os
import sys

class BaseFileHandler:
    @classmethod
    def open(cls, src):
        with open(src, 'r') as file:
            retval = cls.loader(file)
        return retval

    @classmethod
    def save(cls, dst, obj):
        with open(dst, f'w{cls.byte}') as file:
            cls.saver(obj, file)

class FileJsonHandler(BaseFileHandler):
    _type = 'json'
    byte = ""
    loader = json.load
    saver = json.dump

class FilePickleHandler(BaseFileHandler):
    _type = 'pickle'
    byte = "b"
    loader = pickle.load
    saver = pickle.dump

class FileCSVHandler:
    _type = "csv"
    def open(self, src):
        with open(src, "r") as file:
            reader = csv.reader(file)
            retval = [line for line in reader]
        return retval

    def save(self, dst, obj):
        with open(dst, "w") as file:
            writer = csv.writer(file)
            for row in obj:
                writer.writerow(row)

class DataManipulator:
    def __init__(self, zmiany, data):
        self.zmiany = [z.split(",") for z in zmiany]
        self.data = data

    def make_changes(self):
        for idx in self.zmiany:
            self.data[int(idx[0])][int(idx[1])] = idx[2]

def sprawdz_typ_pliku(src):
    return os.path.splitext(src)[-1][1:]

def stworz_katalog(dst):
    if not os.path.isdir(os.path.split(dst)[0]) and os.path.split(dst)[0]:
        os.makedirs(os.path.split(dst)[0])

src = sys.argv[1]
dst = sys.argv[2]
changes = sys.argv[3:]


if sprawdz_typ_pliku(src) == "json":
    loader = FileJsonHandler()
if sprawdz_typ_pliku(src) == "pickle":
    loader = FilePickleHandler()
if sprawdz_typ_pliku(src) == "csv":
    loader = FileCSVHandler()
if sprawdz_typ_pliku(dst) == "json":
    writer = FileJsonHandler()
if sprawdz_typ_pliku(dst) == "pickle":
    writer = FilePickleHandler()
if sprawdz_typ_pliku(dst) == "csv":
    writer = FileCSVHandler()

stworz_katalog(dst)

saved_file = loader.open(src)
bf = DataManipulator(changes, saved_file)
bf.make_changes()
print(bf.data)
writer.save(dst, bf.data)


# python reader.py ".\lead_shot.csv" ".\edytowany.csv"  "3,3, 112" "3,2, 333"
# python reader.py ".\lead_shot.csv" ".\edytowany.json"  "3,3, 112" "3,2, 333"
# python reader.py ".\lead_shot.csv" ".\edytowany.pickle"  "3,3, 112" "3,2, 333"