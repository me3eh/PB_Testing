import PySimpleGUI as sg
from services.object_collections_to_string import convert_collection_to_string_using_method


def create(window, todo_actions):
    message = 'Are you sure you want to create new plan?\nEverything that you have done already, will be lost\n' \
              'Consider saving it, to use it later'
    answer_from_popup = sg.popup_yes_no(message, title="Are you sure?", image=sg.EMOJI_BASE64_YIKES, keep_on_top=True)

    if answer_from_popup == 'no':
        return

    todo_actions.clear()
    window['-ACTION-LIST-'].update(convert_collection_to_string_using_method(collection=todo_actions,
                                                                             method_name='format_for_todo_listbox'))
    window['-TITLE-OF-TEST-'].update("Something")
    window['-ACTION-BDD-ATTRIBUTE-'].update(value="Given")
