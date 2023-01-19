from services import actions_to_steps_transform
import PySimpleGUI as sg
from shared_info.constants import OK_PNG
from services.save_steps_to_file import check_if_step_is_already_defined, save_plan_to_file, delete_already_existing_step


def generate_plan(window, todo_actions, plan_is_an_action):
    test_title = window['-TITLE-OF-TEST-'].get()
    test_title = test_title.replace("'", "`")
    bdd_attribute = window['-ACTION-BDD-ATTRIBUTE-'].get()

    index_found, file_of_found_index = check_if_step_is_already_defined(bdd_attribute.lower(), test_title)
    whole_plan = actions_to_steps_transform.create(todo_actions, test_title, bdd_attribute.lower())

    popup_notification = 'Created'

    if index_found is not None:
        delete_already_existing_step(index_found, file_of_found_index)
        popup_notification = f'Deleted step in {file_of_found_index}.py and put in file'

    save_plan_to_file(whole_plan, plan_is_an_action)
    sg.popup_notify(popup_notification, icon=OK_PNG)
