import PySimpleGUI as sg
from services.object_collections_to_string import convert_collection_to_string_using_method


def create(window, todo_actions):
    answer_from_popup = sg.popup_yes_no('Are you sure you want to erase saved sites htmls?', title="Are you sure?")
    if answer_from_popup == 'no':
        return

    todo_actions.clear()
    window['-ACTION-LIST-'].update(convert_collection_to_string_using_method(collection=todo_actions,
                                                                             method_name='format_for_todo_listbox'))
    window['-TITLE-OF-TEST-'].update("Something")