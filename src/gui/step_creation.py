import PySimpleGUI as sg
from site_scraping import site_info
from configparser import ConfigParser

actions = ['visit site', 'fill input', 'click button', 'click link']

actions_need_to_be_done = ['visit site {url}']

def login_inputs_disabled(window, value_of_checkbox):
    window['-USERNAME-FIELD-'].update(disabled=value_of_checkbox)
    window['-USERNAME-VALUE-'].update(disabled=value_of_checkbox)
    window['-PASSWORD-FIELD-'].update(disabled=value_of_checkbox)
    window['-PASSWORD-VALUE-'].update(disabled=value_of_checkbox)
    window['-LOGIN-PATH-'].update(disabled=value_of_checkbox)

def get_values_for_configuration(window):
    return [
        { "domain": window['-DOMAIN-'].get() },
        { "login_path": window['-LOGIN-PATH-'].get() },
        { "last_site": window['-LAST-SITE-'].get() },
        { "username_field": window['-USERNAME-FIELD-'].get() },
        { "password_field": window['-PASSWORD-FIELD-'].get() },
        { "username_value": window['-USERNAME-VALUE-'].get() },
        {"password_value":  window['-PASSWORD-VALUE-'].get() }
    ]
def save_configuration(config, values_for_config):
    for value in values_for_config:
        config.set('main', f'{list(value.keys())[0]}', f"{list(value.values())[0]}")
    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

def create_step():
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    domain = config.get('main', 'domain')
    username_field = config.get('main', 'username_field')
    password_field = config.get('main', 'password_field')
    username_value = config.get('main', 'username_value')
    password_value = config.get('main', 'password_value')
    last_site = config.get('main', 'last_site')
    login_path = config.get('main', 'login_path')

    current_tags = []

    layout = [
        [
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Text("Plan name", expand_x=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Input("Something"),
                sg.Column([[]], k='layout_principal', expand_x=True)
            ],
            [
                sg.HorizontalSeparator()
            ],
            sg.Column(
                [
                    [
                        sg.Text("Main domain")
                    ],
                    [
                        sg.Input(domain, key='-DOMAIN-', size=(20, 20))
                    ],
                    [
                        sg.Text("Url for logging in")
                    ],
                    [
                        sg.Input(login_path, key='-LOGIN-PATH-', size=(20, 20), disabled=True,
                                 disabled_readonly_background_color='red')
                    ],
                    [
                        sg.Text("Site for scraping")
                    ],
                    [
                        sg.Input(last_site, key='-LAST-SITE-', size=(20, 20))
                    ]
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text("Username input name for logging in")
                    ],
                    [
                        sg.Input(username_field, key='-USERNAME-FIELD-', disabled=True,
                                 disabled_readonly_background_color='red')
                    ],
                    [
                        sg.Text("Username value for logging in")
                    ],
                    [
                        sg.Input(username_value, key='-USERNAME-VALUE-', disabled=True,
                                 disabled_readonly_background_color='red')
                    ]
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text("Password input name for logging in")
                    ],
                    [
                        sg.Input(password_field, key='-PASSWORD-FIELD-', disabled=True,
                                 disabled_readonly_background_color='red')
                    ],
                    [
                        sg.Text("Password value for logging in")
                    ],
                    [
                        sg.Input(password_value, key='-PASSWORD-VALUE-', disabled=True,
                                 disabled_readonly_background_color='red')
                    ]
                ]
            ),
            sg.Column([
                [
                    sg.Button("Save your changes", key='-SAVE-CHANGES-TO-CONFIG-'),
                ],
                [
                    sg.FileSaveAs("Save configuration", key='-SAVE-CONFIGURATION-', enable_events=True,
                                  file_types=[((("PB_CONFIG"), ("*.pb_config")))])
                ],
                [
                    sg.FileBrowse("Load configuration", key='-LOAD-CONFIGURATION-', enable_events=True,
                                  file_types=[((("PB_CONFIG"), ("*.pb_config")))])
                ]
            ])
        ],
        [
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Checkbox('Logged in', default=False, expand_x=True, enable_events=True, k='-LOGGED-IN-')
        ],
        [
            sg.HorizontalSeparator()
        ],
        [
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Text("Plan of actions", expand_x=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Listbox(actions_need_to_be_done, size=(20, 20), k='-ACTION-LIST-', expand_x=True),
                sg.Column([[sg.Button("lol lmoa")]], k='layout_principal'),
                sg.Column([[]], k='layout_principal', expand_x=True)
            ],
            [
                sg.Column([
                    [
                        sg.Text("Here are listed ")
                    ],
                    [
                        sg.Listbox(["There is nothing here...yet"], size=(40, 20), k='-TAG-LIST-', enable_events=True),
                    ]
                ]),
                sg.Column([
                    [
                      sg.Multiline("", disabled=True, background_color='#faea5a', size=(40, 10), key='-TAG-DESCRIPTION-')
                    ],
                    [
                        sg.Text("Write here your info for input", key='-HELPER-INPUT-LABEL-')
                    ],
                    [
                        sg.Input("Additional", key='-HELPER-INPUT-')
                    ]
                ], expand_x=True),
                sg.Combo(actions, default_value=actions[0], key='-ACTIONS-CHOICE-', readonly=True,
                         enable_events=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                [
                    sg.Button("Add new action", k='-ADD-ACTION-'),
                    sg.Column([[]], expand_x=True),
                    sg.Button("Generate plan", k='-GENERATE-PLAN-', button_color='purple')
                ]
            ]
        ],
    ]
    window = sg.Window("Step creator", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        print(event)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-ACTION-':
            actions.append("need_to_do")
            window['-ACTION-LIST-'].update(actions)
        elif event == '-SAVE-CHANGES-TO-CONFIG-':
            values = get_values_for_configuration(window)
            save_configuration(config, values)
            sg.popup_notify("Saved your configuration")
        elif event == '-LOGGED-IN-':
            value_of_checkbox = not values[event]
            login_inputs_disabled(window, value_of_checkbox)
        elif event == '-ACTIONS-CHOICE-':
            domain = window['-DOMAIN-'].get()
            username_field = window['-USERNAME-FIELD-'].get()
            username_value = window['-USERNAME-VALUE-'].get()
            password_field = window['-PASSWORD-FIELD-'].get()
            password_value = window['-PASSWORD-VALUE-'].get()
            login_path = window['-LOGIN-PATH-'].get()
            target_site = window['-LAST-SITE-'].get()

            if domain.endswith('/') and target_site.startswith("/"):
                site = domain + target_site[1:]
            else:
                site = domain + target_site
            # c = []
            if values[event] == 'fill input':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_input_logged_in(site, username_field, username_value, password_field, password_value,
                                                      login_path)
                else:
                    current_tags = site_info.get_input_anonymous(site)
            elif values[event] == 'click button':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_buttons_logged_in(site, username_field, username_value, password_field, password_value,
                                                login_path)
                else:
                    current_tags = site_info.get_buttons_anonymous(site)
            elif values[event] == 'click link':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_links_logged_in(site, username_field, username_value, password_field, password_value,
                                                      login_path)
                else:
                    current_tags = site_info.get_links_anonymous(site)
            listed = list(map(str, current_tags))
            window['-TAG-LIST-'].update(listed)
        elif event == '-TAG-LIST-':
            index = window['-TAG-LIST-'].get_indexes()[0]
            if len(current_tags) != 0:
                window['-TAG-DESCRIPTION-'].update(current_tags[index].whole_html.prettify())
        elif event == '-SAVE-CONFIGURATION-':
            config = ConfigParser()
            if 'main' not in config:
                config.add_section('main')

            domain = window['-DOMAIN-'].get()
            username_field = window['-USERNAME-FIELD-'].get()
            username_value = window['-USERNAME-VALUE-'].get()
            password_field = window['-PASSWORD-FIELD-'].get()
            password_value = window['-PASSWORD-VALUE-'].get()
            login_path = window['-LOGIN-PATH-'].get()
            last_site = window['-LAST-SITE-'].get()
            logged_in_checkbox_checked = window['-LOGGED-IN-'].get()

            config.set('main', 'domain', domain)
            config.set('main', 'username_field', username_field)
            config.set('main', 'password_field', password_field)
            config.set('main', 'username_value', username_value)
            config.set('main', 'password_value', password_value)
            config.set('main', 'last_site', last_site)
            config.set('main', 'login_path', login_path)
            config.set('main', 'logged_in', repr(logged_in_checkbox_checked))
            with open(values[event], 'w') as f:
                config.write(f)
            with open('resources_for_testing/config.ini', 'w') as f:
                config.write(f)
        elif event == '-LOAD-CONFIGURATION-':
            config = ConfigParser()
            config.read(values[event])

            domain = config.get('main', 'domain')
            username_field = config.get('main', 'username_field')
            username_value = config.get('main', 'username_value')
            password_field = config.get('main', 'password_field')
            password_value = config.get('main', 'password_value')
            login_path = config.get('main', 'login_path')
            last_site = config.get('main', 'last_site')
            logged_in = config.get('main', 'logged_in')

            window['-DOMAIN-'].update(domain)
            window['-USERNAME-FIELD-'].update(username_field)
            window['-USERNAME-VALUE-'].update(username_value)
            window['-PASSWORD-FIELD-'].update(password_field)
            window['-PASSWORD-VALUE-'].update(password_value)
            window['-LOGIN-PATH-'].update(login_path)
            window['-LAST-SITE-'].update(last_site)
            window['-LOGIN-PATH-'].update(login_path)
            window['-LOGGED-IN-'].update(eval(logged_in))
            login_inputs_disabled(window, not eval(logged_in))

            with open('resources_for_testing/config.ini', 'w') as f:
                config.write(f)
        elif event == '-GENERATE-PLAN-':
            print(window['-ACTION-LIST-'].get_list_values())
