from simple_term_menu import TerminalMenu


def main_menu():
    choices = ["Edit filename", "Edit feature", "Edit scenario", "Edit given", "Edit when", "Edit then", "Quit"]
    return terminal_menu(choices)


def side_menu():
    choices = ["Write custom", "Select chosen", "Go back"]
    return terminal_menu(choices)


def menu_for_given():
    choices = ["visiting <given url>", 'logged as admin', '', 'Abort']
    return terminal_menu(choices)


def terminal_menu(choices):
    return TerminalMenu(choices).show()
