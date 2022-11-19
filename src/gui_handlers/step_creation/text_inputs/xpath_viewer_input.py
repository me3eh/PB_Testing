from services import xpath_check
from gui_handlers.step_creation.buttons import save_action_buttons


def check_if_xpath_unique(last_used_html, window):
    xpath = window['-XPATH-INPUT-'].get()
    matches, matches_number = xpath_check.get_number_of_match(html=last_used_html, xpath=xpath)
    if matches_number == 1:
        window['-XPATH-INPUT-'].update(background_color='#32CD32')
    else:
        window['-XPATH-INPUT-'].update(background_color='#ff3e19')

    window['-XPATH-ELEMENTS-'].update(f"Found {matches_number} tags matching this xpath")

    if matches_number == 1:
        save_action_buttons.enable_save_buttons(window)
    else:
        save_action_buttons.disable_save_buttons(window)
