from simple_term_menu import TerminalMenu
from actions import Actions
from file_helper import read_from_file


def terminal_menu(choices):
    return TerminalMenu(choices).show()


def object_to_string(specified_object):
    return str(specified_object)


class MenuHelper:
    def __init__(self):
        self.main_menu = ["Edit filename", "Edit feature", "Edit scenario",
                          "Edit given", "Edit when", "Edit then", "Save file", "Quit"]
        self.side_menu = ["Write custom", "Select chosen", "Go back"]

    def main_menu_selection(self):
        return terminal_menu(self.main_menu)

    def side_menu_selection(self):
        return terminal_menu(self.side_menu)

    def is_last_side_menu(self, index):
        return len(self.side_menu) - 1 == index

    def is_last_main_menu(self, index):
        return len(self.main_menu) - 1 == index

    def get_value_from_main_menu(self, index):
        return self.main_menu[index]


class GivenMenu:
    def __init__(self):

        self.choices = [Actions('visiting url ', 'url'),
                        Actions('logged as admin'),
                        Actions('logged as user'),
                        Actions('logged as user'),
                        Actions('click on button with id ', 'id'),
                        'Abort']

    def selection(self):
        return terminal_menu(map(object_to_string, self.choices))

    def get_choices(self):
        return self.choices

    def get_choice(self, index):
        return self.choices[index]

    def is_last(self, index_checking):
        return len(self.choices) - 1 == index_checking
