import PySimpleGUI as sg
from sqlite import database
from shared_info.constants import OK_PNG

def save(window):
    url_input = window['-INPUT-ANYTHING-'].get()
    checked_url = window['-USER-URLS-'].get()
    if not checked_url:
        sg.popup("Not checked anything in scanned_urls section")
    else:
        index = window['-USER-URLS-'].get_indexes()[0]
        values = window['-USER-URLS-'].get_list_values()
        if url_input in values:
            sg.popup("Nope, that is already in used urls")
        else:
            database.rename_url(values[index], url_input)
            values[index] = url_input
            window['-USER-URLS-'].update(values)
            window['-USER-URLS-'].widget.selection_set(index)
            sg.popup_notify(f"Saved {url_input} to used urls",
                            icon=OK_PNG,
                            title='Added')
