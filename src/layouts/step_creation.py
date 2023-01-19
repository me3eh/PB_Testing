import PySimpleGUI as sg
import os

INFORMATION_ABOUT_UNIQUENESS = 'To have your save buttons enabled, you need to have xpath of your element unique :D'

input_width = 20
number_items_to_show = 4


bdd_attributes = ['Given', 'When', 'Then']

def get_layout(domain,
               login_path,
               last_site,
               username_field,
               username_value,
               password_field,
               password_value,
               actions,
               todo_actions,
               imported_actions
               ):
    path_of_project = os.getcwd()
    return [
        [
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Text("Plan name", expand_x=True),
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Combo(bdd_attributes, default_value=bdd_attributes[0], key='-ACTION-BDD-ATTRIBUTE-', readonly=True),
                sg.Input("Something", key='-TITLE-OF-TEST-'),
                sg.Column([[]], k='layout_principal', expand_x=True),
            ],
            [
                sg.HorizontalSeparator()
            ],
            sg.Column(
                [
                    [
                        sg.Column([
                            [
                                sg.Text("Main domain"),
                            ],
                            [
                                sg.Input(domain, key='-DOMAIN-', size=(30, 20)),
                                sg.Column([[]], expand_y=True)
                            ],
                            [
                                sg.Col(
                                    [
                                        [
                                            sg.Listbox(values=[], size=(input_width, number_items_to_show),
                                                       enable_events=True,
                                                       select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                                                       no_scrollbar=True,
                                                       background_color=sg.theme_background_color())
                                        ]
                                    ], key='-NOT-USED-ONLY-FOR-PROPER-LAYOUT-', pad=(0, 0), visible=True
                                )
                            ]
                        ]),
                        sg.Column(
                            [
                                [
                                    sg.Text("Site for scraping"),
                                ],
                                [
                                    sg.Input(last_site, key='-LAST-SITE-', size=(80, 20), enable_events=True)
                                ],
                                [
                                    sg.Col(
                                        [
                                            [
                                                sg.Listbox(values=[], size=(80, number_items_to_show),
                                                           enable_events=True,
                                                           key='-LAST-SITE-BOX-',
                                                           select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                                                           no_scrollbar=True)
                                            ]
                                        ], key='-LAST-SITE-BOX-CONTAINER-', pad=(0, 0), visible=True
                                    )
                                ]
                            ]
                        ),
                        sg.Column(
                            [
                                [
                                    sg.Text("Url for logging in")
                                ],
                                [
                                    sg.Input(login_path, key='-LOGIN-PATH-', size=(20, 20), disabled=True,
                                             disabled_readonly_background_color='red', enable_events=True)
                                ],
                                [
                                    sg.Col(
                                        [
                                            [
                                                sg.Listbox(values=[], size=(input_width, number_items_to_show),
                                                           enable_events=True,
                                                           key='-LOGIN-PATH-BOX-',
                                                           select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                                                           no_scrollbar=True)
                                            ]
                                        ], key='-LOGIN-PATH-BOX-CONTAINER-', pad=(0, 0), visible=True
                                    )
                                ],
                            ]
                        )
                    ],
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text("Username input name for logging in")
                    ],
                    [
                        sg.Input(username_field, key='-USERNAME-FIELD-', disabled=True, size=(15, 1),
                                 disabled_readonly_background_color='red')
                    ],
                    [
                        sg.Text("Username value for logging in")
                    ],
                    [
                        sg.Input(username_value, key='-USERNAME-VALUE-', disabled=True, size=(15, 1),
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
                        sg.Input(password_field, key='-PASSWORD-FIELD-', disabled=True, size=(15, 1),
                                 disabled_readonly_background_color='red')
                    ],
                    [
                        sg.Text("Password value for logging in")
                    ],
                    [
                        sg.Input(password_value, key='-PASSWORD-VALUE-', disabled=True, size=(15, 1),
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
                                  initial_folder=f'{path_of_project}/resources_for_testing/saved_plans',
                                  file_types=[((("PB_CONFIG"), ("*.pb_config")))])
                ],
                [
                    sg.FileBrowse("Load configuration", key='-LOAD-CONFIGURATION-', enable_events=True,
                                  initial_folder=f'{path_of_project}/resources_for_testing/saved_plans',
                                  file_types=[((("PB_CONFIG"), ("*.pb_config")))])
                ]
            ]),
            sg.Column([
                [
                    sg.Button("Erase saved htmls", key='-RESET-SAVED-HTMLS-', button_color='black')
                ],
                [
                    sg.Button("Create new plan", key='-CREATE-NEW-TEST-', button_color='red')
                ]
            ])
        ],
        [
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Checkbox('Logged in', default=False, enable_events=True, k='-LOGGED-IN-'),
            sg.Column([[]], k='layout_principal', expand_x=True)
        ],
        [
            sg.HorizontalSeparator()
        ],
        [
            [
                sg.Column([
                    [
                        sg.Text("Available actions for your plan"),
                        sg.Combo(actions, default_value=actions[0], key='-ACTIONS-CHOICE-', readonly=True,
                                 enable_events=True),
                        sg.pin(sg.Combo(imported_actions, key='-SAVED-ACTIONS-', readonly=True,
                                        enable_events=True, visible=False, size=(40, 1))),
                        sg.pin(sg.Button('Reload actions', key='-RELOAD-ACTIONS-', visible=False)),
                        sg.Combo(bdd_attributes, default_value=bdd_attributes[0], key='-BDD-ATTRIBUTE-', readonly=True,
                                 enable_events=True)
                    ]
                ]),
            ],
            [
                sg.Column([[]], expand_x=True),
                sg.Listbox([], size=(40, 19), k='-TAG-LIST-', enable_events=True),
                sg.Column([
                    [
                        sg.Button("\u25B3", key='-MOVE-UP-TAG-'),
                    ],
                    [
                        sg.Button("\u25BD", key='-MOVE-DOWN-TAG-'),
                    ]
                ]),
                sg.Column([[]], expand_x=True),
                sg.Column([
                    [
                        sg.Text("Tag description:")
                    ],
                    [
                        sg.Multiline("", disabled=True, size=(40, 15), background_color='#faea5a',
                                     key='-TAG-DESCRIPTION-')
                    ],
                    [
                        sg.Text("")
                    ]
                ]),
                sg.Column([
                    [
                        sg.Text("Xpath of element:", key='-XPATH-INFO-')
                    ],
                    [
                        sg.Multiline("", key='-XPATH-INPUT-', size=(40, 15)),
                        sg.Column(
                            [
                                [
                                    sg.Button('Show whole html in external app', key='-SHOW-HTML-')
                                ],
                                [
                                    sg.Column(
                                        [
                                            [
                                                sg.Button('Copy html of element', key='-COPY-HTML-ELEMENT-'),
                                                sg.Button('Copy html of whole site', button_color='green',
                                                          key='-COPY-HTML-'),
                                            ]
                                        ]
                                    )
                                ],
                                [
                                    sg.Button('Check if xpath exists in html', button_color='blue',
                                              key='-XPATH-EXISTS-')
                                ],
                                [
                                    sg.Button("Save xpath or info for input", k='-SAVE-CHANGED-XPATH-')
                                ]
                            ]
                        )
                    ],
                    [
                        sg.Text("", key='-XPATH-ELEMENTS-')
                    ]
                ])
            ],
            [
                sg.Button("Add new action", k='-ADD-ACTION-', tooltip=INFORMATION_ABOUT_UNIQUENESS),
                # sg.Button("Save action", k='-SAVE-ACTION-', tooltip=INFORMATION_ABOUT_UNIQUENESS),
                sg.Button("Delete selected action", k='-DELETE-ACTION-', button_color='red'),
                sg.Column([[]], expand_x=True),
                sg.pin(
                    sg.Column([
                        [
                            sg.Text("Write here your info for input", key='-HELPER-INPUT-LABEL-')
                        ],
                        [
                            sg.Input("Additional", key='-HELPER-INPUT-'),
                            sg.FileBrowse('Choose folder of your project', target='-HELPER-INPUT-', visible=False,
                                          key='-HELPER-INPUT-FILE-BROWSE-'),
                            sg.Button('Insert in input current domain', visible=False, button_color='#007373',
                                      key='-HELPER-INPUT-CURRENT-DOMAIN-'),
                            sg.Button('Insert in input current domain with endpoint', visible=False, button_color='#008080',
                                      key='-HELPER-INPUT-CURRENT-DOMAIN-WITH-ENDPOINT-')
                        ]
                    ],  key='-INPUT-WRAPPER-'), expand_x=True
                )
            ],
            [
              sg.HorizontalSeparator()
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Text("Plan of actions", expand_x=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                sg.Listbox(todo_actions, size=(20, 18), k='-ACTION-LIST-', expand_x=True, enable_events=True),
                sg.Column([[]], k='layout_principal'),
                sg.Column([
                    [
                        sg.Button("\u25B2", key='-MOVE-UP-'),
                    ],
                    [
                        sg.Button("\u25BC", key='-MOVE-DOWN-'),
                    ]
                ], expand_x=True)
            ],
            [
                sg.Column([[]], k='layout_principal', expand_x=True),
                [
                    sg.Column([[]], expand_x=True),
                    sg.Button("Generate plan as action", k='-GENERATE-PLAN-AS-ACTION-', button_color='green'),
                    sg.Button("Generate plan", k='-GENERATE-PLAN-', button_color='purple')
                ]
            ]
        ]
    ]
