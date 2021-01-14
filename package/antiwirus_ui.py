from .antiwirus import AntiWirus
import sys
import os


class AntyWirusUI:
    def __init__(self):
        self._antivirus = AntiWirus()

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
            "0": "set new index file",
            "1": "load existing index file",
            "2": "fast scan",
            "3": "easy scan",
            "h": "help",
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
            self._full_easy_scan()

    def _get_path(self, msg):
        scan_path = input(msg)
        if os.path.exists(scan_path) and os.path.isdir(scan_path):
            return scan_path
        else:
            print("Invalid path. Path does not exist or leads to file")
            self._get_path(msg)

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
        self._antivirus.dumb_list_to_flie()
        print(f"Success !!! Index file is in: {files_path}")

    def _load_existing_file(self):
        if self._antivirus.is_index_file_loaded():
            self._remove_loaded_index_file("continue")

        load_path = self._get_path("Choose a path where is index_file: ")

        self._antivirus.set_index_file(path=load_path)
        self._antivirus.from_file_to_list()
        self._antivirus.get_scan_path()

        print("Successfully loaded index file")

    def _full_easy_scan(self):
        scan_path = self._get_path("Choose a scan path: ")
        viruses = self._antivirus.easy_scan(scan_path)
        print(f"{len(viruses)} dangerous files found")
        if viruses and self._if_repair():
            self._antivirus.repair_easy_scan(viruses)
            print("Successfully repaired all dangerous files")

    def _run(self):
        while True:
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
