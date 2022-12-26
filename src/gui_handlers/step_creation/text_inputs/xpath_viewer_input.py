from services import xpath_check
from gui_handlers.step_creation.buttons import save_action_buttons
import PySimpleGUI as sg
from shared_info.constants import ERROR_PNG


def check_if_xpath_unique(last_used_html, window, todo_actions):
    xpath = window['-XPATH-INPUT-'].get()
    action_list_index = window['-ACTION-LIST-'].get_indexes()
    action_list_checked = len(action_list_index) != 0
    if action_list_checked:
        todo_action_checked = todo_actions[action_list_index[0]]
        matches, matches_number = xpath_check.get_number_of_match(html=todo_action_checked.site_html, xpath=xpath)
    else:
        matches, matches_number = xpath_check.get_number_of_match(html=last_used_html, xpath=xpath)

    if matches_number == 1:
        window['-XPATH-INPUT-'].update(background_color='#32CD32')
    elif matches_number is None:
        sg.popup_notify("Fix it and try again", title="Xpath is not correct", icon=ERROR_PNG)
        return
    else:
        window['-XPATH-INPUT-'].update(background_color='#ff3e19')

    window['-XPATH-ELEMENTS-'].update(f"Found {matches_number} tags matching this xpath")

    # if matches_number == 1:
    #     save_action_buttons.enable_save_buttons(window)
    # else:
    #     save_action_buttons.disable_save_buttons(window)
