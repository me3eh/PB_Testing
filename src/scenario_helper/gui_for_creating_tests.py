import PySimpleGUI as sg
import re
from file_helper import write_to_file
from scenario import Scenario
from gherkin_attributes_loader import load_gherkin_attributes

GIVEN_COLOR = 'red'
WHEN_COLOR = 'blue'
THEN_COLOR = ('yellow', "black")
SCENARIO_COLOR = 'purple'

scenarios = [
    Scenario(scenario_name='scenario1')
]

scenario = ["scenarios1", 'scenarios2']
givens, whens, thens = load_gherkin_attributes()

completions = {
    '-GIVENS-': givens,
    '-WHENS-': whens,
    '-THENS-': thens
}
specials = ['-GIVENS-', '-WHENS-', '-THENS-']
choices = ['di', 'da']
urls = ['/yup', '/something_else']
ids = ['maciek', 'mateusz', 'lukasz', 'dawid']
css_classes = ['yikes', '.huhi.niech_bedzie']
input_names = ['input', 'password']
attributes_index = 0


def scenario_name(scenario):
    return scenario.get_scenario_name()

def autocomplete(text, choices_array, list_element, window, name_of_container):
    prediction_list = []
    if text:
        prediction_list = [item for item in choices_array if item.startswith(text)]
    else:
        prediction_list = choices_array

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
                                    sg.Listbox([], size=(20, 4), enable_events=True, key=f'-BOX-ATTRIBUTE-{index}-',
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


def delete_selected_from_listbox(listbox):
    index = listbox_get_selection(listbox)
    values = listbox.get_list_values()
    if values:
        values.pop(index)
    listbox.update(values)


def change_widget_id_to_attribute(widget_id):
    type = widget_id.replace("-", "")
    type = type.lower()
    if type != 'scenario':
        type = type.lower()[:-1]
    return type

def listbox_get_selection(listbox):
    return listbox.get_indexes()[0]


def listbox_set_selection(listbox, index):
    listbox.widget.selection_set(index)


def new_attribute_input():
    return [new_column(index) for index in range(2)]


def array_into_string_join(array, prefix):
    return '\n'.join(f'\t\t{prefix} {x}' for x in array) + "\n"


def get_preview_of_test(feature_name):
    whole_text = f'Feature: {feature_name}\n'
    for scenario in scenarios:
        whole_text += scenario.get_as_string()
    return whole_text


def save_to_file(window):
    feature_name = window['-FEATURE-NAME-'].get()
    filename = window['-FILENAME-'].get()
    whole_text = get_preview_of_test(feature_name)
    write_to_file(f'features/{filename}.feature', whole_text)
    sg.popup("Saved to file", auto_close=True, auto_close_duration=2)


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
                                enable_events=True)]
                ]
            )
        ],
        [
            sg.Column(
                [
                    [sg.Text("All WHENs in scenario")],
                    [sg.Listbox(values=scenarios[0].get_whens(), size=(60, 7), key='-WHENS-',
                                enable_events=True)]
                ]
            ),
            sg.Column(
                [
                    [
                        sg.Text("All Special Commands Will Go Here")
                    ],
                    [
                        sg.Input("Here", key="-INPUT-HERE-", size=(60, 4), enable_events=True),
                        sg.Button("Save", key='-SAVE-')
                    ],
                    [
                        sg.pin(
                            sg.Col(
                                [
                                    [
                                        sg.Listbox(values=[], size=(60, 4), enable_events=True, key='-BOX-',
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
                                enable_events=True)]
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
        [
            sg.Button("Delete", key="-DELETE-"),
            sg.Button("Save to file", key="-SAVE-TO-FILE-"),
            sg.Button("Preview", key="-PREVIEW-"),
            sg.Button("Exit", key="Exit")
        ]
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

            type = change_widget_id_to_attribute(widget_id=c)
            if type == 'scenario':
                listbox = window['-SCENARIOS-']
                scenarios.append(Scenario("some_scenario"))
                actual_index = listbox_get_selection(listbox)
                window['-SCENARIOS-'].update(values=list(map(scenario_name, scenarios)))
                listbox_set_selection(listbox=listbox, index=actual_index)
            else:
                eval(f"actual_scenario.add_{type}()")
                array_with_selected_type_values = eval(f"actual_scenario.get_{type}s()")
                window[c].update(values=array_with_selected_type_values)
        elif "-DELETE-" in event:
            found = False
            index = listbox_get_selection(window['-SCENARIOS-'])
            actual_scenario = scenarios[index]

            for s in specials:
                if window[s].get():
                    type = s.replace("-", "").lower()[:-1]
                    print(type)
                    index = listbox_get_selection(window[s])
                    print(index)
                    eval(f"actual_scenario.remove_{type}_index({index})")
                    delete_selected_from_listbox(listbox=window[s])

                    found = True
            if not found:
                scenario_listbox = window['-SCENARIOS-']
                if len(scenarios) == 1:
                    sg.popup("Cannot delete last scenario", auto_close=True, auto_close_duration=3)
                else:
                    index = listbox_get_selection(scenario_listbox)
                    scenarios.pop(index)
                    delete_selected_from_listbox(listbox=scenario_listbox)

        elif event in specials:
            ar = specials.copy()
            ar.remove(event)
            for listbox in ar:
                window[listbox].set_value([])
            choices = completions[event]
            # text = values[event][0]
            # window['-INPUT-HERE-'].update(text)
            # attribute_inputs_refresh(window, text)

        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '-BOX-':
            text = values['-BOX-'][0]
            window['-INPUT-HERE-'].update(value=text)
            window['-BOX-CONTAINER-'].update(visible=False)
            attribute_inputs_refresh(window, text)
        elif '-BOX-ATTRIBUTE-' in event:
            print("event", event)
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]
            text = values[f'-BOX-ATTRIBUTE-{index}-'][0]

            window[f'-INPUT-ATTRIBUTE-{index}-'].update(value=text)
            window[f'-BOX-ATTRIBUTE-CONTAINER-{index}-'].update(visible=False)
            # attribute_inputs_refresh(window, text)
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
                    type = change_widget_id_to_attribute(widget_id=s)
                    actual_index_of_scenario = listbox_get_selection(listbox=window['-SCENARIOS-'])
                    selected_in_listbox = listbox_get_selection(listbox=window[s])
                    eval(f'scenarios[actual_index_of_scenario].set_{type}(text_in_input, selected_in_listbox)')
                    only_scenario_selected = False
            if only_scenario_selected:
                update_values_in_listbox_and_retrieve_selection(listbox=window['-SCENARIOS-'],
                                                                new_text=text_in_input)

            attribute_inputs_refresh(window, text_in_input)
        elif '-INSERT-ATTRIBUTE-' in event:
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]
            input_string = values['-INPUT-HERE-']
            attribute_replacement = values[f'-INPUT-ATTRIBUTE-{index}-']
            attribute = re.findall("(?<={)(.*?)(?=})", input_string)[0]
            new_input_string = input_string.replace('{'+attribute+'}', attribute_replacement)
            window['-INPUT-HERE-'].update(new_input_string)
            attribute_inputs_refresh(window, new_input_string)
        elif '-INPUT-ATTRIBUTE-' in event:
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]

            attribute_label = window[f'-LABEL-{index}-'].get()
            attribute_label = attribute_label.replace("Attribute: ", "")
            # collection = eval(f"{attribute_label}")
            text = values[event]
            collection = None
            if attribute_label == 'element_id':
                collection = ids
            if attribute_label == 'css_classes':
                collection = css_classes
            if attribute_label == 'input_name':
                collection = input_names
            if attribute_label == 'url':
                collection = urls

            if collection != None:
                autocomplete(text=text, choices_array=collection, list_element=window.Element(f'-BOX-ATTRIBUTE-{index}-'),
                             window=window, name_of_container=f'-BOX-ATTRIBUTE-CONTAINER-{index}-')
        elif '-SCENARIOS-' == event:
            index = listbox_get_selection(window['-SCENARIOS-'])

            actual_scenario = scenarios[index]

            for listbox in specials:
                window[listbox].set_value([])

            window['-GIVENS-'].update(values=actual_scenario.get_givens())
            window['-WHENS-'].update(values=actual_scenario.get_whens())
            window['-THENS-'].update(values=actual_scenario.get_thens())
        elif '-PREVIEW-' == event:
            feature_name = window['-FEATURE-NAME-'].get()
            sg.popup(get_preview_of_test(feature_name), title="Preview of your test",
                     auto_close=True, auto_close_duration=5)
        elif event == '-SAVE-TO-FILE-':
            save_to_file(window)
    window.close()


if __name__ == "__main__":
    gui_for_scenarios()
