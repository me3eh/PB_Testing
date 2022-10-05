import PySimpleGUI as sg
from configparser import ConfigParser
from sqlite.base import database_retrieve_urls

def save_configuration(config):
    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)


def launch_configuration():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    domain = config.get('main', 'domain')
    layout = [
        [
            sg.Text('Main domain testing'),
            sg.Column([[]], k='layout_principal', expand_x=True)
        ],
        [
            sg.Input(f'{domain}', k="-DOMAIN-INPUT-"),
            sg.Column([[]], k='layout_principal', expand_x=True)
        ],
        [
            sg.Button('Save configuration', k="-SAVE-"),
            sg.Column([[]], k='layout_principal', expand_x=True)
        ],
        [
            sg.Text('Urls from your project'),
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Text('Urls used in testing')
        ],
        [
            sg.Listbox(values=database_retrieve_urls(), k='-SCANNED-URLS-', size=(20, 20)),
            sg.Column(
                [
                    [
                        sg.Button("==>", k='-ADD-')
                    ],
                    [
                        sg.Button("<==", k='-REMOVE')
                    ]
                ]
            ),
            sg.Listbox(values=database_retrieve_urls(), k='-SCANNED-URLS-2-', size=(20, 20)),
        ]
    ]
    window = sg.Window("Configuration for testing", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == '-SAVE-':
            new_domain = window["-DOMAIN-INPUT-"].get()
            config.set('main', 'domain', new_domain)
            save_configuration(config)
            sg.popup("Everything set", auto_close_duration=1, auto_close=True, title=':D')
