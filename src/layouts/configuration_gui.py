import PySimpleGUI as sg
from sqlite import database


def get_layout(project_path):
    return [
        [
            sg.Column([[]], expand_x=True),
            sg.Text('Your project path:'),
            sg.Input(key='_FILEBROWSE_', enable_events=True, visible=True, disabled=True, default_text=project_path),
            sg.FolderBrowse('Choose folder of your project', initial_folder=project_path, target='_FILEBROWSE_'),
            sg.Button('Scan for ', key='-SCAN-FOR-URLS-FROM-GIVEN-PATH-')
        ],
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
                        sg.Listbox(values=database.retrieve_urls('original_urls'), k='-SCANNED-URLS-', size=(80, 20),
                                   enable_events=True)
                    ]
                ], k='layout_principal', expand_x=True),
            sg.Column(
                [
                    [
                        sg.Button("==>", k='-ADD-FROM-LISTBOX-TO-LISTBOX-')
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
                                   k='-USER-URLS-', size=(80, 20))
                    ]
                ], k='layout_principal', expand_x=True),
        ],
        [
            sg.Input("/endpoint", k='-INPUT-ANYTHING-', size=(80, 20)),
            sg.Button("Save that", k='-SAVE-URL-FROM-INPUT-'),
            sg.Button("Add that", k='-ADD-URL-FROM-INPUT-', button_color='green'),
            sg.Button("Delete selected", k='-DELETE-SELECTED-', button_color='red'),
            sg.Checkbox('Get text of selected item', key='-GET-SELECTED-')
        ]
    ]
