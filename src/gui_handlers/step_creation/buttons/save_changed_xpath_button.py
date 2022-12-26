import PySimpleGUI as sg
from shared_info.constants import ERROR_PNG, OK_PNG


def save_changed(window, todo_actions):
    index = window['-ACTION-LIST-'].get_indexes()
    new_xpath = window['-XPATH-INPUT-'].get()
    if len(index) == 0:
        sg.popup_notify('Nothing selected in actions', icon=ERROR_PNG, title='Not permitted')
        return

    todo_action = todo_actions[index[0]]

    if todo_action.element_html is None:
        sg.popup_notify('Selected action doesn\' include xpath', icon=ERROR_PNG, title='Not permitted')

    todo_action.xpath = new_xpath
    sg.popup_notify('Saved given xpath to selected action', icon=OK_PNG, title='Saved xpath')
