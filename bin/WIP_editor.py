# # import requests
# # from bs4 import BeautifulSoup
# #
# # url = 'http://localhost:8080/login'
# # reqs = requests.get(url)
# # soup = BeautifulSoup(reqs.text)
# #
# # urls = []
# # for link in soup.find_all():
# #     if not link.get('class') == None:
# #         print(link.get('class'))
# import urwid
#
# class MenuButton(urwid.Button):
#     def __init__(self, caption, callback):
#         super(MenuButton, self).__init__("")
#         urwid.connect_signal(self, 'click', callback)
#         self._w = urwid.AttrMap(urwid.SelectableIcon(
#             [u'  \N{BULLET} ', caption], 2), None, 'selected')
#
# class SubMenu(urwid.WidgetWrap):
#     def __init__(self, caption, choices):
#         super(SubMenu, self).__init__(MenuButton(
#             [caption, u"\N{HORIZONTAL ELLIPSIS}"], self.open_menu))
#         line = urwid.Divider(u'\N{LOWER ONE QUARTER BLOCK}')
#         listbox = urwid.ListBox(urwid.SimpleFocusListWalker([
#             urwid.AttrMap(urwid.Text([u"\n  ", caption]), 'heading'),
#             urwid.AttrMap(line, 'line'),
#             urwid.Divider()] + choices + [urwid.Divider()]))
#         self.menu = urwid.AttrMap(listbox, 'options')
#
#     def open_menu(self, button):
#         top.open_box(self.menu)
#
# class Choice(urwid.WidgetWrap):
#     def __init__(self, caption):
#         super(Choice, self).__init__(
#             MenuButton(caption, self.item_chosen))
#         self.caption = caption
#
#     def item_chosen(self, button):
#         response = urwid.Text([u'  You chose ', self.caption, u'\n'])
#         done = MenuButton(u'Ok', exit_program)
#         response_box = urwid.Filler(urwid.Pile([response, done]))
#         top.open_box(urwid.AttrMap(response_box, 'options'))
#
# def exit_program(key):
#     raise urwid.ExitMainLoop()
#
# menu_top = SubMenu(u'Main Menu', [
#     SubMenu(u'Applications', [
#         SubMenu(u'Accessories', [
#             Choice(u'Text Editor'),
#             Choice(u'Terminal'),
#         ]),
#     ]),
#     SubMenu(u'System', [
#         SubMenu(u'Preferences', [
#             Choice(u'Appearance'),
#         ]),
#         Choice(u'Lock Screen'),
#     ]),
# ])
#
# palette = [
#     (None,  'light gray', 'black'),
#     ('heading', 'black', 'light gray'),
#     ('line', 'black', 'light gray'),
#     ('options', 'dark gray', 'black'),
#     ('focus heading', 'white', 'dark red'),
#     ('focus line', 'black', 'dark red'),
#     ('focus options', 'black', 'light gray'),
#     ('selected', 'white', 'dark blue')]
# focus_map = {
#     'heading': 'focus heading',
#     'options': 'focus options',
#     'line': 'focus line'}
#
# class HorizontalBoxes(urwid.Columns):
#     def __init__(self):
#         super(HorizontalBoxes, self).__init__([], dividechars=1)
#
#     def open_box(self, box):
#         if self.contents:
#             del self.contents[self.focus_position + 1:]
#         self.contents.append((urwid.AttrMap(box, 'options', focus_map),
#             self.options('given', 24)))
#         self.focus_position = len(self.contents) - 1
#
# top = HorizontalBoxes()
# top.open_box(menu_top.menu)
# urwid.MainLoop(urwid.Filler(top, 'middle', 10), palette).run()


#!/usr/bin/env python3

import __init__
import os
import time

from scenario_helper.file_helper import read_from_file
from scenario_helper.menu_helper import MenuHelper, GivenMenu
from scenario_helper.scenario import Scenario

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # urls = read_from_file("resources_for_testing/url.txt")

    main_menu_exit = False
    side_menu_exit = False
    # given_menu_exit = False

    scenario = Scenario()
    feature_name = "something about this feature"
    filename = "new_test"
    menu_helper = MenuHelper()
    given_menu = GivenMenu()
    while not main_menu_exit:
        cls()
        main_menu_list = [f"File name: {filename}.feature", "",
                          f"Feature: {feature_name}",
                          f"  {scenario.get_scenario_name()}",
                          f"    {scenario.get_given()}",
                          f"    {scenario.get_when()}",
                          f"    {scenario.get_then()}"]
        file_text = '\n'.join(str(x) for x in main_menu_list[1:]) + "\n\n"
        main_menu_text = main_menu_list[0] + "\n\n" + file_text

        print(main_menu_text)

        menu_entry_index = menu_helper.main_menu_selection()

        if menu_entry_index == 0:
            filename = input("Change filename:")
        elif menu_entry_index == 1:
            feature_name = input("Change feature:")
        elif menu_entry_index == 2:
            scenario.set_scenario_name(input("Change scenario:"))
        elif menu_entry_index == 3:
            while not side_menu_exit:
                side_menu = menu_helper.side_menu_selection()
                if menu_helper.is_last_side_menu(side_menu):
                    side_menu_exit = True
                if side_menu == 0:
                    option_given = input("Write given: ")
                    scenario.set_given(option_given)
                    side_menu_exit = True
                if side_menu == 1:
                    choice = given_menu.selection()
                    if not given_menu.is_last(choice):
                        output = given_menu.get_choice(choice).output()
                        scenario.set_given(output)
                        side_menu_exit = True
                    else:
                        side_menu_exit = False
            side_menu_exit = False
        elif menu_helper.get_value_from_main_menu(index=menu_entry_index) == "Save file":
            with open(f'features/{filename}.feature', 'w') as f:
                f.write(file_text)
            cls()
            print("Succesfully saved")
            time.sleep(1)

        elif menu_helper.is_last_main_menu(index=menu_entry_index):
            main_menu_exit = True


if __name__ == "__main__":
    main()
    cls()
    print("Bye bye")
