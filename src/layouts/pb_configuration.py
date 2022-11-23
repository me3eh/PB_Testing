import PySimpleGUI as sg
from sqlite import database


def get_layout():
    return [
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
                                   k='-USER-URLS-', size=(20, 20))
                    ]
                ], k='layout_principal', expand_x=True),
        ],
        [
            sg.Input("Yas", k='-INPUT-ANYTHING-'),
            sg.Button("Save that", k='-SAVE-URL-FROM-INPUT-'),
            sg.Button("Add that", k='-ADD-URL-FROM-INPUT-', button_color='green'),
            sg.Button("Delete selected", k='-DELETE-SELECTED-', button_color='red')
        ]
    ]