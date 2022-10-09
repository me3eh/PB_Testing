import PySimpleGUI as sg
from configparser import ConfigParser
from sqlite import database
from site_scraping.site_info import get_browser_attributes

attributes = ['ids', 'css_classes', 'input_names']

def save_configuration(config):
    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

def fill_attribute_listbox(window):
    checked_url = window['-USER-URLS-'].get()
    if not checked_url:
        sg.popup("Not checked anything")
    else:
        attribute = window['-ATTRIBUTE-SELECT-'].get()
        print(attribute)
        print(checked_url[0])
        values = database.retrieve_attribute(attribute=attribute, url=checked_url[0])
        print(values)
        if values and values[0][0] != None:
            window['-ATTRIBUTES-LISTBOX-'].update(eval(values[0][0]))
        else:
            window['-ATTRIBUTES-LISTBOX-'].update([])

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
                ]
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
            sg.Column(
                [
                    [
                        sg.Button("Check attributes", k='-CHECK-')
                    ]
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text('Choose attributes')
                    ],
                    [
                        sg.Combo(attributes, default_value=attributes[0], key='-ATTRIBUTE-SELECT-', readonly=True,
                                 enable_events=True)
                    ],
                    [
                        sg.Listbox(values=[], k='-ATTRIBUTES-LISTBOX-', size=(20, 20))
                    ]
                ]
            )
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
        if event == '-SAVE-':
            new_domain = window["-DOMAIN-INPUT-"].get()
            config.set('main', 'domain', new_domain)
            save_configuration(config)
            sg.popup("Everything set", auto_close_duration=1, auto_close=True, title=':D')
        elif event == '-ATTRIBUTE-SELECT-':
            fill_attribute_listbox(window)
        elif event == '-USER-URLS-':
            fill_attribute_listbox(window)

        elif event == '-CHECK-':
            checked_url = window['-USER-URLS-'].get()[0]
            if not checked_url:
                sg.popup("Not checked anything")
            else:
                domain = config.get('main', 'domain')
                browser_attributes = get_browser_attributes(domain + '/' + ''.join(checked_url))
                print(browser_attributes)
                database.save_attributes(checked_url, css_classes=browser_attributes['class'],
                                         ids=browser_attributes['id'], input_names=browser_attributes['name'])
                print(domain + '/' + ''.join(checked_url))
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
        elif event == '-SAVE-ANYTHING-':
            input = window['-INPUT-ANYTHING-'].get()
            checked_url = window['-USER-URLS-'].get()
            if not checked_url:
                sg.popup("Not checked anything in scanned_urls section")
            else:
                index = window['-USER-URLS-'].get_indexes()[0]
                values = window['-USER-URLS-'].get_list_values()
                if input in values:
                    sg.popup("Nope, that is already in used urls")
                else:
                    database.rename_url(values[index], input)
                    values[index] = input
                    window['-USER-URLS-'].update(values)
                    window['-USER-URLS-'].widget.selection_set(index)
        elif event == '-ADD-ANYTHING-':
            input = window['-INPUT-ANYTHING-'].get()
            selected_index = window['-USER-URLS-'].get_indexes()
            selected = False
            if selected_index:
                selected_index = selected_index[0]
                selected = True
            values = window['-USER-URLS-'].get_list_values()
            if input in values:
                sg.popup("Nope, that is already in used urls")
            else:
                values.append(input)
                window['-USER-URLS-'].update(values)
                if selected:
                    window['-USER-URLS-'].widget.selection_set(selected_index)
                database.add_url(input)
        elif event == '-DELETE-SELECTED-':
            selected_index = window['-USER-URLS-'].get_indexes()
            if not selected_index:
                sg.popup("Not checked anything in scanned_urls section")
            else:
                values = window['-USER-URLS-'].get_list_values()
                database.delete_url(values[selected_index[0]])
                del values[selected_index[0]]
                window['-USER-URLS-'].update(values)
            window['-ATTRIBUTES-LISTBOX-'].update([])
