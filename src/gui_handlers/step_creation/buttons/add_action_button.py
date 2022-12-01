from services.add_action import action_create
from shared_info.constants import ERROR_PNG
import PySimpleGUI as sg


def add_action(window, values, todo_actions, current_tags, saved_actions):
    bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
    type_of_action = values['-ACTIONS-CHOICE-']
    input_for_action = values['-HELPER-INPUT-']
    saved_actions_index = window['-SAVED-ACTIONS-'].widget.current()
    selected_action_index = window['-ACTION-LIST-'].get_indexes()
    selected_tag = window['-TAG-LIST-'].get_indexes()
    xpath_of_element = window['-XPATH-INPUT-'].get()

    new_action = action_create(type_of_action,
                               input_for_action,
                               bdd_attribute,
                               selected_tag,
                               current_tags,
                               saved_action_selected=saved_actions_index,
                               saved_actions=saved_actions,
                               xpath=xpath_of_element)

    if new_action is None:
        sg.popup_notify("Click on any of tags and after that click button 'Add new action'",
                        icon=ERROR_PNG,
                        title='Nothing added')
        return

    todo_actions.append(new_action)
    window['-ACTION-LIST-'].update(create_todo_actions_for_listbox(todo_actions))


def create_todo_actions_for_listbox(todo_actions):
    return list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
