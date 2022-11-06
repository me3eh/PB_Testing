import PySimpleGUI as sg
from site_scraping import site_info
from configparser import ConfigParser
from text_to_test_transform import test
from website_elements.website_tag import WebsiteTag

OK_PNG = b'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'
ERROR_PNG = b'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'
# GIVEN_ATTRIBUTE_INFO = "<-- Given - preparing site for doing something (for example loggin in)"
GIVEN_ATTRIBUTE_INFO = "Template"
# WHEN_ATTRIBUTE_INFO = "<-- When - doing some actions on our site (clicking on buttons)"
# THEN_ATTRIBUTE_INFO = "<-- Then - asserting that action took place (title was revealed after visiting site)"

actions = ['visiting site', 'filling input', 'clicking button', 'clicking link']
bdd_attributes = ['Given', 'When', 'Then']

todo_actions = [WebsiteTag(bdd_attribute='Given', value_for_bdd='visiting site', attribute='https://google.com')]
# todo_actions_for_listbox = list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))

# def change_bdd_attribute(window, bdd_attribute):
#     textbox = window['-BDD-ATTRIBUTE-INFO-']
#     if bdd_attribute == 'Given':
#         textbox.update(GIVEN_ATTRIBUTE_INFO)
#     elif bdd_attribute == 'When':
#         textbox.update(WHEN_ATTRIBUTE_INFO)
#     elif bdd_attribute == 'Then':
#         textbox.update(THEN_ATTRIBUTE_INFO)

def create_todo_actions_for_listbox():
    return list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))

def login_inputs_disabled(window, value_of_checkbox):
    components_to_switch_disable = ['-USERNAME-FIELD-', '-USERNAME-VALUE-', '-PASSWORD-FIELD-', '-PASSWORD-VALUE-',
                                    '-LOGIN-PATH-']
    for key in components_to_switch_disable:
        window[key].update(disabled=value_of_checkbox)

def get_values_for_configuration(window):
    return [
        {"domain": window['-DOMAIN-'].get()},
        {"login_path": window['-LOGIN-PATH-'].get()},
        {"last_site": window['-LAST-SITE-'].get()},
        {"username_field": window['-USERNAME-FIELD-'].get()},
        {"password_field": window['-PASSWORD-FIELD-'].get()},
        {"username_value": window['-USERNAME-VALUE-'].get()},
        {"password_value": window['-PASSWORD-VALUE-'].get()}
    ]


def save_configuration(config, values_for_config):
    for value in values_for_config:
        config.set('main', f'{list(value.keys())[0]}', f"{list(value.values())[0]}")
    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)


def create_step():
    # global todo_actions_for_listbox

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
                sg.Input("Something", key='-TITLE-OF-TEST-'),
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
                sg.Listbox(create_todo_actions_for_listbox(), size=(20, 20), k='-ACTION-LIST-', expand_x=True),
                sg.Column([[]], k='layout_principal', expand_x=True)
            ],
            [
                sg.Column([
                    [
                        sg.Text("Available actions for your plan"),
                        sg.Combo(actions, default_value=actions[0], key='-ACTIONS-CHOICE-', readonly=True,
                                 enable_events=True),
                        sg.Combo(bdd_attributes, default_value=bdd_attributes[0], key='-BDD-ATTRIBUTE-', readonly=True,
                                 enable_events=True),
                        sg.Text(GIVEN_ATTRIBUTE_INFO, key='-BDD-ATTRIBUTE-INFO-')
                    ],
                    [
                        sg.Listbox(["There is nothing here...yet"], size=(40, 20), k='-TAG-LIST-', enable_events=True),
                    ]
                ]),
                sg.Column([
                    [
                        sg.Multiline("", disabled=True, background_color='#faea5a', size=(40, 10),
                                     key='-TAG-DESCRIPTION-')
                    ],
                    [
                        sg.Text("Write here your info for input", key='-HELPER-INPUT-LABEL-')
                    ],
                    [
                        sg.Input("Additional", key='-HELPER-INPUT-')
                    ]
                ], expand_x=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                [
                    sg.Button("Add new action", k='-ADD-ACTION-'),
                    sg.Button("Save action", k='-SAVE-ACTION-'),
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
        print(values)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-ACTION-':
            bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
            attribute = WebsiteTag(bdd_attribute=bdd_attribute, value_for_bdd='visiting site',
                                   attribute='https://google.com')
            todo_actions.append(attribute)
            # todo_actions_for_listbox = list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
            window['-ACTION-LIST-'].update(create_todo_actions_for_listbox())
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
            if values[event] == 'visiting site':
                current_tags = []
            if values[event] == 'filling input':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='input')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='input')
            elif values[event] == 'clicking button':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='button')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='button')
            elif values[event] == 'clicking link':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='a')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='a')
            listed = list(map(lambda obj: obj.format_for_listbox_with_available_actions(), current_tags))
            window['-TAG-LIST-'].update(listed)
        elif event == '-TAG-LIST-':
            index = window['-TAG-LIST-'].get_indexes()
            if len(index) == 0:
                print("yups")
            else:
                if len(current_tags) != 0:
                    window['-TAG-DESCRIPTION-'].update(current_tags[index[0]].whole_html.prettify())
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
            test_title = window['-TITLE-OF-TEST-'].get()
            test.create(todo_actions, test_title, 'Given')
            sg.popup_notify("Created", icon=OK_PNG)
        elif event == '-SAVE-ACTION-':

            bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
            type_of_action = values['-ACTIONS-CHOICE-']
            input_for_action = values['-HELPER-INPUT-']
            selected_action_index = window['-ACTION-LIST-'].get_indexes()
            selected_tag = window['-TAG-LIST-'].get_indexes()
            if len(selected_action_index) == 0:
                sg.popup_notify("You didnt chose anything from todo_actions listbox to change", icon=ERROR_PNG)
            else:
                if type_of_action == 'visiting site':
                    todo_actions[selected_action_index[0]] = WebsiteTag(value_for_bdd='visiting site',
                                                                        attribute=input_for_action,
                                                                        bdd_attribute=bdd_attribute)
                    # todo_actions_for_listbox = list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
                    window['-ACTION-LIST-'].update(create_todo_actions_for_listbox())
                else:
                    if len(selected_tag) == 0:
                        sg.popup_notify("You didnt chose anything from available actions listbox to change",
                                        icon=ERROR_PNG)
                    else:
                        current_chosen = current_tags[selected_tag[0]]
                        current_chosen.value_for_bdd = type_of_action
                        current_chosen.attribute = input_for_action

                        todo_actions[selected_action_index[0]] = current_chosen
                        # todo_actions_for_listbox = list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
                        window['-ACTION-LIST-'].update(create_todo_actions_for_listbox())
        # elif event == '-BDD-ATTRIBUTE-':
        #     change_bdd_attribute(window, values[event])
