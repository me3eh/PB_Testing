import time
from simple_term_menu import TerminalMenu
import os
from scenario import Scenario
import signal

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    feature_name = "After clicking 1, this could be edited"
    scenario = Scenario()
    main_menu_items = ["Edit feature", "Edit scenario", "Edit gb ", "Edit when", "Edit then", "Quit"]
    filename = "new_test"
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_purple", "bold")
    main_menu_style = ("bg_purple", "fg_yellow")
    main_menu_exit = False

    # edit_menu_title = "  Edit Menu\n"
    # edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    edit_menu_back = False
    # edit_menu = TerminalMenu(
    #     edit_menu_items,
    #     title=edit_menu_title,
    #     menu_cursor=main_menu_cursor,
    #     menu_cursor_style=main_menu_cursor_style,
    #     menu_highlight_style=main_menu_style,
    #     cycle_cursor=True,
    #     clear_screen=True,
    # )

    while not main_menu_exit:
        main_menu_list = [f"{filename}", f"Feature: {feature_name}",
                          f"  Scenario: {scenario.get_scenario_name()}",
                          f"    Given: {scenario.get_given()}",
                          f"    When: {scenario.get_when()}",
                          f"    Then: {scenario.get_then()}"]
        main_menu_title = '\n'.join(str(x) for x in main_menu_list) + "\n\n"
        main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=main_menu_style,
            cycle_cursor=True,
            clear_screen=True,
        )
        main_sel = main_menu.show()

        if main_sel == 0:
            cls()
            print(main_menu_title)
            feature_name = input("Give the feature name: ")
        elif main_sel == 1:
            print("option 2 selected")
            time.sleep(5)
        elif main_sel == 2:
            print(main_menu_title)
            feature_name = input("Give the feature name: ")
            # print("option 3 selected")
            # time.sleep(5)
        elif main_sel == 5:
            main_menu_exit = True
            print("Quit Selected")


if __name__ == "__main__":
    main()