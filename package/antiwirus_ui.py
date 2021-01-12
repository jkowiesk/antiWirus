from .antiwirus import AntiWirus


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
        for option in options:
            print(option)

    def _get_options(self):
        choices = {
            0: "set new index file",
            1: "fast scan"
            2: "easy scan"
            3: "help"
            4: "quit"
        }
        return choices

    def _get_option_from_user():
        option = input("Choose an option: ")
        return option

    def _run(self):
        while True:
            self._print_options()
            options = self._get_options()
            try:
                option = options[self._get_option_from_user]
            except KeyError as e:
                print(f"Invalid operation: {e}. Please choose a valid one")
                continue
            self._dispatch(option)

    def main(self):
        self._greet_user()
        self._run()