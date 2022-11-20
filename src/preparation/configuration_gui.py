import PySimpleGUI as sg
from sqlite import database


def launch_configuration():
    layout = [
        [
            sg.Column(
                [
                    [
                        sg.Text('Urls from your project'),
                    ],
                    [
                        sg.Text('', expand_y=True),
                    ],
                    [
                        sg.Listbox(values=database.retrieve_urls('original_urls'), k='-SCANNED-URLS-', size=(20, 20))
                    ]
                ], k='layout_principal', expand_x=True),
            sg.Column(
                [
                    [
                        sg.Button("==>", k='-ADD-')
                    ]
                ], expand_x=True
            ),
            sg.Column(
                [
                    [
                        sg.Text('Urls used in testing'),
                    ],
                    [
                        sg.Text('', expand_y=True),
                    ],
                    [
                        sg.Listbox(values=database.retrieve_urls('urls_and_attributes'), enable_events=True,
                                   k='-USER-URLS-', size=(20, 20))
                    ]
                ], k='layout_principal', expand_x=True),
        ],
        [
            sg.Input("Yas", k='-INPUT-ANYTHING-'),
            sg.Button("Save that", k='-SAVE-ANYTHING-'),
            sg.Button("Add that", k='-ADD-ANYTHING-', button_color='green'),
            sg.Button("Delete selected", k='-DELETE-SELECTED-', button_color='red')
        ]
    ]
    window = sg.Window("Configuration for testing", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-':
            checked_url = window['-SCANNED-URLS-'].get()
            if not checked_url:
                sg.popup("Not checked anything in scanned_urls section")
            else:
                urls = window['-USER-URLS-'].get_list_values()
                print(urls)
                print(checked_url)
                if checked_url[0] in urls:
                    sg.popup("Not checked anything in scanned_urls section")
                else:
                    new_urls = urls + checked_url
                    window['-USER-URLS-'].update(new_urls)
                    database.add_url(new_urls)
        elif event == '-SAVE-ANYTHING-':
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
        elif event == '-ADD-ANYTHING-':
            url_input = window['-INPUT-ANYTHING-'].get()
            selected_index = window['-USER-URLS-'].get_indexes()
            selected = False
            if selected_index:
                selected_index = selected_index[0]
                selected = True
            values = window['-USER-URLS-'].get_list_values()
            if url_input in values:
                sg.popup("Nope, that is already in used urls")
            else:
                values.append(url_input)
                window['-USER-URLS-'].update(values)
                if selected:
                    window['-USER-URLS-'].widget.selection_set(selected_index)
                database.add_url(url_input)
        elif event == '-DELETE-SELECTED-':
            selected_index = window['-USER-URLS-'].get_indexes()
            if not selected_index:
                sg.popup("Not checked anything in scanned_urls section")
            else:
                values = window['-USER-URLS-'].get_list_values()
                database.delete_url(values[selected_index[0]])
                del values[selected_index[0]]
                window['-USER-URLS-'].update(values)
