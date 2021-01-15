from .antiwirus import AntiWirus
import sys
import os
from time import time, sleep

global CYCLE_TIME

CYCLE_TIME = 60


class AntyWirusUI:
    def __init__(self):
        self._antivirus = AntiWirus()
        self._prev = time()

    def _greet_user(self):
        message = "Welcome to AntiWirus"
        print("#" * len(message))
        print(message)
        print("#" * len(message))

    def _print_options(self):
        print("| Operations |")
        options = self._get_options()
        for option, text in options.items():
            msg = f"{option} - {text}"
            print(msg)

    def _get_options(self):
        options = {
            "0": "setup new index file",
            "1": "load existing index file",
            "2": "update index file",
            "3": "fast scan",
            "4": "easy scan",
            "q": "quit"
        }
        return options

    def _get_option_from_user(self):
        option = input("Choose an option: ")
        return option

    def _do_option(self, option: str):
        if option == "q":
            sys.exit()
        elif option == "0":
            self._set_new_index_file()
        elif option == "1":
            self._load_existing_file()
        elif option == "2":
            self._update_index_file_and_dump()
        elif option == "3":
            self._full_fast_scan()
        elif option == "4":
            self._full_easy_scan()

    def _get_path(self, msg):
        path = input(msg)
        while not (os.path.exists(path) and os.path.isdir(path)):
            print("Invalid path. Path does not exist or leads to file")
            path = input(msg)
        return path

    def _get_load_path(self):
        load_path = input("Choose a path where is index_file: ")
        path_exists = os.path.exists(load_path)
        path_dir = os.path.isdir(load_path)
        path_contains_index = os.path.exists(f"{load_path}/.index_file")

        while not (path_exists and path_dir and path_contains_index):
            if not (path_exists and path_dir):
                print("Invalid path. Path does not exist or leads to file")
            elif not path_contains_index:
                print("Invalid path. Path folder does not contain index file")
            load_path = input("Choose a path where is index_file: ")
            path_exists = os.path.exists(load_path)
            path_dir = os.path.isdir(load_path)
            path_contains_index = os.path.exists(f"{load_path}/.index_file")

        return load_path

    def _remove_loaded_index_file(self, mode=""):
        anwser = input("Do u want to remove loaded index file [Y/n]?: ")
        if anwser == "y" or anwser == "Y":
            self._antivirus.remove_index_file()
        elif anwser == "n" or anwser == "N":
            if mode == "continue":
                return None
            self._run()
        else:
            print('Indvalid character. Only valid characters are "y" - yes and "n" - no')
            self._remove_loaded_index_file()

    def _remove_existing_index_file(self, files_path):
        anwser = input("There is already index file in this path. Do u want to replace it [Y/n]?: ")
        if anwser == "y" or anwser == "Y":
            self._antivirus.set_index_file_path(files_path)
            self._antivirus.remove_index_file()
        elif anwser == "n" or anwser == "N":
            self._run()
        else:
            print('Indvalid character. Only valid characters are "y" - yes and "n" - no')
            self._remove_existing_index_file(files_path)

    def _if_repair(self):
        anwser = input("Do u want to treat it [Y/n]?: ")
        if anwser == "y" or anwser == "Y":
            return True
        elif anwser == "n" or anwser == "N":
            return False
        else:
            print('Indvalid character. Only valid characters are "y" - yes and "n" - no')
            self._remove_existing_index_file(files_path)

    def _set_new_index_file(self):
        if self._antivirus.is_index_file_loaded():
            self._remove_loaded_index_file()

        files_path = self._get_path("Choose a path for index file: ")

        while not os.path.exists(files_path):
            self._remove_existing_index_file(files_path)

        scan_path = self._get_path("Choose a path for fast scan: ")

        self._antivirus.set_index_file(files_path, scan_path)
        self._antivirus.dump_list_to_flie()
        print(f"Success !!! Index file is in: {files_path}")

    def _load_existing_file(self):
        if self._antivirus.is_index_file_loaded():
            self._remove_loaded_index_file("continue")

        load_path = self._get_load_path()

        self._antivirus.set_index_file(path=load_path)
        self._antivirus.from_file_to_list()
        self._antivirus.get_scan_path()

        print("Successfully loaded index file")

    def _update_index_file(self):
        if not self._antivirus.is_index_file_loaded():
            print("First load the index file")
            self._run()
        if not self._antivirus.is_index_scan_path():
            scan_path = self._get_path("Choose a path for fast scan: ")
            self._antivirus.set_index_scan_path(scan_path)
        self._antivirus.update_index_file()
        print("Successfully updated index file")

    def _update_index_file_and_dump(self):
        if not self._antivirus.is_index_file_loaded():
            print("First load the index file")
            self._run()
        if not self._antivirus.is_index_scan_path():
            scan_path = self._get_path("Choose a path for fast scan: ")
            self._antivirus.set_index_scan_path(scan_path)
        self._antivirus.update_index_file()
        self._antivirus.dump_list_to_flie()
        print("Successfully updated index file")

    def _full_easy_scan(self):
        scan_path = self._get_path("Choose a scan path: ")
        viruses = self._antivirus.easy_scan(scan_path)
        print(f"{len(viruses)} dangerous files found")
        if viruses and self._if_repair():
            self._antivirus.repair_easy_scan(viruses)
            print("Successfully repaired all dangerous files")

    def _full_fast_scan(self):
        self._update_index_file()
        viruses = self._antivirus.fast_scan()
        print(f"{len(viruses)} dangerous files found")
        self._antivirus.repair_fast_scan(viruses)
        print("Successfully repaired all dangerous files")
        self._antivirus.dump_list_to_flie()

    def _full_fast_scan_cycle(self):
        print("Cycle scan ...")
        sleep(1)
        self._update_index_file()
        viruses = self._antivirus.fast_scan()
        print(f"{len(viruses)} dangerous files found")
        self._antivirus.repair_fast_scan(viruses)
        print("Successfully repaired all dangerous files")
        self._antivirus.dump_list_to_flie()

    def _run(self):
        while True:
            if time() - self._prev >= CYCLE_TIME and self._antivirus.is_index_file_loaded():
                self._prev = time()
                self._full_fast_scan_cycle()
                sleep(1)
            self._print_options()
            options = self._get_options()
            try:
                option = self._get_option_from_user()
                test = options[option]
            except KeyError as e:
                print(f"Invalid operation: {e}. Please choose a valid one")
                continue
            self._do_option(option)

    def main(self):
        self._greet_user()
        self._run()
