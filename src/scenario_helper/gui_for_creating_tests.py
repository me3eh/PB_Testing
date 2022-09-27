import PySimpleGUI as sg
import re
from file_helper import write_to_file
from scenario import Scenario

GIVEN_COLOR = 'red'
WHEN_COLOR = 'blue'
THEN_COLOR = ('yellow', "black")
SCENARIO_COLOR = 'purple'

scenarios = [
    Scenario(scenario_name='scenario1'),
    Scenario(scenario_name='scenario2')
]

scenario = ["scenarios1", 'scenarios2']
givens = ['visiting site <url>', 'logged as']
whens = ['visiting site <url>', 'bgi']
thens = ['yikes', 'anormous']

completions = {
    '-GIVENS-': ['visiting site <url>', 'logged as'],
    '-WHENS-': ['visiting site <url>', 'bgi'],
    '-THENS-': ['yikes', 'anormous']
}
specials = ['-GIVENS-', '-WHENS-', '-THENS-']
choices = ['di', 'da']
ids = ['maciek', 'mateusz', 'lukasz', 'dawid']
attributes_index = 0


def scenario_name(scenario):
    return scenario.get_scenario_name()

def autocomplete(text, choices_array, list_element, window, name_of_container):
    prediction_list = []
    if text:
        prediction_list = [item for item in choices_array if item.startswith(text)]

    list_element.update(values=prediction_list)
    list_element.update(set_to_index=0)

    if len(prediction_list) > 0:
        window[name_of_container].update(visible=True)
    else:
        window[name_of_container].update(visible=False)


def attribute_inputs_refresh(window, text):
    global attributes_index
    x = re.findall("(?<={)(.*?)(?=})", text)
    attributes_length = len(x)

    subtraction = attributes_length - attributes_index
    if subtraction > 0:
        for index in range(subtraction):
            if attributes_index <= 1:
                window[f'-ATTRIBUTE-{attributes_index}-'].update(visible=True)
                attributes_index = attributes_index + 1
    elif subtraction < 0:
        for index in range(-1 * subtraction):
            attributes_index = attributes_index - 1
            window[f'-ATTRIBUTE-{attributes_index}-'].update(visible=False)

    for index in range(attributes_index):
        window[f'-LABEL-{index}-'].update(f'Attribute: {x[index]}')


def new_column(index):
    return [
        sg.Column(
            [
                [
                    sg.Text(f"Attribute: {index}", key=f'-LABEL-{index}-')
                ],
                [
                    sg.Input("", key=f"-INPUT-ATTRIBUTE-{index}-", size=(20, 4), enable_events=True),
                    sg.Button("Insert", key=f'-INSERT-ATTRIBUTE-{index}-')
                ],
                [
                    sg.pin(
                        sg.Col(
                            [
                                [
                                    sg.Listbox([], size=(20, 4), enable_events=True, key=f'-BOX-ATTRIBUTE-{index}',
                                               select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)
                                ]
                            ], key=f'-BOX-ATTRIBUTE-CONTAINER-{index}-', pad=(0, 0), visible=False
                        )
                    )
                ]
            ], visible=False, key=f'-ATTRIBUTE-{index}-')]


def update_values_in_listbox_and_retrieve_selection(listbox, new_text):
    all_values = listbox.get_list_values()
    old_value_index = listbox_get_selection(listbox)
    all_values[old_value_index] = new_text
    listbox.update(values=all_values)
    listbox_set_selection(listbox, old_value_index)


def listbox_get_selection(listbox):
    return listbox.get_indexes()[0]


def listbox_set_selection(listbox, index):
    listbox.widget.selection_set(index)


def new_attribute_input():
    return [new_column(index) for index in range(2)]


def array_into_string_join(array, prefix):
    return '\n'.join(f'\t\t{prefix} {x}' for x in array) + "\n"


def save_to_file(window):
    feature_name = window['-FEATURE-NAME-'].get()
    filename = window['-FILENAME-'].get()
    whole_text = f'Feature: {feature_name}\n'
    for scenario in scenarios:
        whole_text += scenario.get_as_string()
    write_to_file(f'features/{filename}.feature', whole_text)
    sg.popup("Yas")


def gui_for_scenarios():
    layout = [
        [
            sg.Text('FileName'),
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Text("Scenarios"),
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Text("Feature name")],
        [
            sg.Input('dad', enable_events=True, key='-FILENAME-'),
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Column(
                [
                    [
                        sg.Listbox(values=list(map(scenario_name, scenarios)),
                                   default_values=scenario_name(scenarios[0]),
                                   size=(60, 7), key='-SCENARIOS-', enable_events=True)
                    ]
                ],
                k='layout_principal', expand_x=True),
            sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Input('mom', enable_events=True, key='-FEATURE-NAME-')
        ],
        [
            sg.Column(
                [
                    [sg.Text("All GIVENs in scenario")],
                    [sg.Listbox(values=scenarios[0].get_givens(), size=(60, 7), key='-GIVENS-',
                                enable_events=True, background_color=GIVEN_COLOR)]
                ]
            )
        ],
        [
            sg.Column(
                [
                    [sg.Text("All WHENs in scenario")],
                    [sg.Listbox(values=scenarios[0].get_whens(), size=(60, 7), key='-WHENS-',
                                enable_events=True, background_color=WHEN_COLOR)]
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text("All Special Commands Will Go Here")
                    ],
                    [
                        sg.Input("Here", key="-INPUT-HERE-", size=(20, 4), enable_events=True),
                        sg.Button("Save", key='-SAVE-')
                    ],
                    [
                        sg.pin(
                            sg.Col(
                                [
                                    [
                                        sg.Listbox(values=[], size=(20, 4), enable_events=True, key='-BOX-',
                                                   select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)
                                    ]
                                ],
                                key='-BOX-CONTAINER-', pad=(0, 0), visible=False
                            )
                        )
                    ]
                ]
            )
        ],
        [
            sg.Column(
                [
                    [sg.Text("All THENs in scenario")],
                    [sg.Listbox(values=scenarios[0].get_thens(), size=(60, 7), key='-THENS-',
                                enable_events=True, background_color='yellow', text_color='black')]
                ]
            ),
            sg.Column(
                new_attribute_input(), key='-ATTRIBUTES-'
            )
        ],

        [sg.Button("Add new given", key="-ADD-GIVENS-", button_color=GIVEN_COLOR),
         sg.Button("Add new when", key="-ADD-WHENS-", button_color=WHEN_COLOR),
         sg.Button("Add new then", key="-ADD-THENS-", button_color=THEN_COLOR),
         sg.Button("Add new scenario", key="-ADD-SCENARIO-", button_color=SCENARIO_COLOR)],
        [sg.Button("Save to file", key="-SAVE-TO-FILE-"),
         sg.Button("Exit", key="Exit")]
    ]

    window = sg.Window("Creating scenario",
                       layout,
                       resizable=True,
                       finalize=True,
                       return_keyboard_events=True)
    list_element: sg.Listbox = window.Element('-BOX-')
    sel_item, prediction_list = 0, []
    global choices
    global attributes_index
    while True:
        event, values = window.read()
        print(event)

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if "-ADD-" in event:
            c = event.replace("-ADD", "")

            index = listbox_get_selection(window['-SCENARIOS-'])

            actual_scenario = scenarios[index]

            type = c.replace("-", "")
            if type == 'SCENARIO':
                listbox = window['-SCENARIOS-']
                scenarios.append(Scenario("some_scenario"))
                actual_index = listbox_get_selection(listbox)
                window['-SCENARIOS-'].update(values=list(map(scenario_name, scenarios)))
                listbox_set_selection(listbox=listbox, index=actual_index)
            else:
                type = type.lower()[:-1]
                eval(f"actual_scenario.add_{type}()")
                array_with_selected_type_values = eval(f"actual_scenario.get_{type}s()")
                window[c].update(values=array_with_selected_type_values)
        elif event in specials:
            ar = specials.copy()
            ar.remove(event)
            for listbox in ar:
                window[listbox].set_value([])
            choices = completions[event]
            text = values[event][0]
            window['-INPUT-HERE-'].update(text)
            attribute_inputs_refresh(window, text)

        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '-BOX-':
            window['-INPUT-HERE-'].update(value=values['-BOX-'][0])
            window['-BOX-CONTAINER-'].update(visible=False)
        elif event == "-INPUT-HERE-":
            text = values[event]

            autocomplete(text=text, choices_array=choices, list_element=list_element,
                         window=window, name_of_container='-BOX-CONTAINER-')

            attribute_inputs_refresh(window, text)

        elif event == '-SAVE-':
            text_in_input = values['-INPUT-HERE-']
            only_scenario_selected = True
            for s in specials:
                if window[s].get():
                    update_values_in_listbox_and_retrieve_selection(listbox=window[s],
                                                                    new_text=text_in_input)
                    only_scenario_selected = False
            if only_scenario_selected:
                update_values_in_listbox_and_retrieve_selection(listbox=window['-SCENARIOS-'],
                                                                new_text=text_in_input)

            attribute_inputs_refresh(window, text_in_input)
        elif '-INSERT-ATTRIBUTE-' in event:
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]
            input_string = values['-INPUT-HERE-']
            attribute_replacement = values[f'-INPUT-ATTRIBUTE-{index}-']
            attribute = re.findall("(?<=:)(.*?)(?= )", input_string)[0]
            new_input_string = input_string.replace(f':{attribute}', attribute_replacement)
            window['-INPUT-HERE-'].update(new_input_string)
            attribute_inputs_refresh(window, new_input_string)
        elif '-INPUT-ATTRIBUTE-' in event:
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]
            text = values[event]
            autocomplete(text=text, choices_array=ids, list_element=window.Element(f'-BOX-ATTRIBUTE-{index}'),
                         window=window, name_of_container=f'-BOX-ATTRIBUTE-CONTAINER-{index}-')
        elif '-SCENARIOS-' == event:
            index = listbox_get_selection(window['-SCENARIOS-'])

            actual_scenario = scenarios[index]

            for listbox in specials:
                window[listbox].set_value([])

            window['-GIVENS-'].update(values=actual_scenario.get_givens())
            window['-WHENS-'].update(values=actual_scenario.get_whens())
            window['-THENS-'].update(values=actual_scenario.get_thens())

        elif event == '-SAVE-TO-FILE-':
            save_to_file(window)
    window.close()


if __name__ == "__main__":
    gui_for_scenarios()
