from shared_info.constants import ERROR_PNG, OK_PNG
from sqlite import database
import PySimpleGUI as sg


def save(window):
    url_input = window['-INPUT-ANYTHING-'].get()
    selected_index = window['-USER-URLS-'].get_indexes()
    selected = False
    if selected_index:
        selected_index = selected_index[0]
        selected = True
    values = window['-USER-URLS-'].get_list_values()
    if url_input in values:
        sg.popup_notify("Add url with another naming to that",
                        icon=ERROR_PNG,
                        title='That url already exists in listbox')
    else:
        values.append(url_input)
        window['-USER-URLS-'].update(values)
        if selected:
            window['-USER-URLS-'].widget.selection_set(selected_index)
        database.add_url(url_input)
        sg.popup_notify(f"Added {url_input} to used urls",
                        icon=OK_PNG,
                        title='Added')
