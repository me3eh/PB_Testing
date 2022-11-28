from shared_info.constants import ERROR_PNG
from sqlite import database
import PySimpleGUI as sg


def delete_selected(window):
    selected_index = window['-USER-URLS-'].get_indexes()
    if not selected_index:
        sg.popup_notify("Not checked anything in scanned_urls section",
                        icon=ERROR_PNG,
                        title='Click on something first in used_url listbox')
    else:
        values = window['-USER-URLS-'].get_list_values()
        database.delete_url(values[selected_index[0]])
        values.pop(selected_index[0])
        window['-USER-URLS-'].update(values)
        if len(values) != 0:
            index_to_select = len(values) - 1 if selected_index[0] >= len(values) else selected_index
            window['-USER-URLS-'].widget.selection_set(index_to_select)
