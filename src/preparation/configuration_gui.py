import PySimpleGUI as sg
from layouts import pb_configuration
from sqlite import database
from shared_info.constants import ERROR_PNG


def launch_configuration():
    layout = pb_configuration.get_layout()
    window = sg.Window("Configuration for testing", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-FROM-LISTBOX-TO-LISTBOX-':
            checked_url = window['-SCANNED-URLS-'].get()
            if not checked_url:
                sg.popup("Not checked anything in scanned_urls section")
            else:
                urls = window['-USER-URLS-'].get_list_values()
                print(urls)
                print(checked_url)
                if checked_url[0] in urls:
                    sg.popup("Url already exists")
                else:
                    new_urls = urls + checked_url
                    window['-USER-URLS-'].update(new_urls)
                    database.add_url(checked_url[0])
        elif event == '-SAVE-URL-FROM-INPUT-':
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
        elif event == '-ADD-URL-FROM-INPUT-':
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
        elif event == '-DELETE-SELECTED-':
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