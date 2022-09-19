import PySimpleGUI as sg
import re
from file_helper import write_to_file

scenario = "lel"
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

attributes_index = 0

def get_string():
    whole_text = f"Scenario: {scenario}\n"
    for given in givens:
        whole_text += f"\tGiven {given}\n"
    for when in whens:
        whole_text += f"\tWhen {when}\n"
    for then in thens:
        whole_text += f"\tThen {then}\n"
    return whole_text


def add_new():
    return [[sg.Button(f'key up', key=f"")]]


def get_values_from_listbox(listbox):
    array = listbox.get_values()


def attribute_inputs_refresh(window, text):
    global attributes_index
    x = re.findall("(?<=:)(.*?)(?= )", text)
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
    return [sg.Column([[sg.Text(f"Attribute: {index}", key=f'-LABEL-{index}-')],
                [sg.Input("", key=f"-INPUT-ATTRIBUTE-{index}-", size=(20, 4)),
                 sg.Button("Insert", key=f'-INSERT-ATTRIBUTE-{index}-')]], visible=False, key=f'-ATTRIBUTE-{index}-')]


def new_attribute_input():
    return [new_column(index) for index in range(2)]


def array_into_string_join(array, prefix):
    return '\n'.join(f'\t\t{prefix} {x}' for x in array) + "\n"


def save_to_file(window):
    givens_to_file = window['-GIVENS-'].get_list_values()
    whens_to_file = window['-WHENS-'].get_list_values()
    thens_to_file = window['-THENS-'].get_list_values()
    feature_name = window['-FEATURE-NAME-'].get()
    filename = window['-FILENAME-'].get()
    whole_text = f'Feature: {feature_name}'
    whole_text += "\n\tScenario: yep yep\n"
    whole_text += array_into_string_join(array=givens_to_file, prefix='Given')
    whole_text += array_into_string_join(array=whens_to_file, prefix='When')
    whole_text += array_into_string_join(array=thens_to_file, prefix='Then')
    write_to_file(f'features/{filename}.feature', whole_text)
    sg.popup("Yas")


def gui_for_scenarios():
    layout = [
        [sg.Text('FileName'), sg.Column([[]], k='layout_principal', expand_x=True), sg.Text("Feature name")],
        [
            sg.Input('dad', enable_events=True, key='-FILENAME-'), sg.Column([[]], k='layout_principal', expand_x=True),
            sg.Input('mom', enable_events=True, key='-FEATURE-NAME-')
        ],
        [
            sg.Column(
                [
                    [sg.Text("All GIVENs in scenario")],
                    [sg.Listbox(values=givens, size=(60, 7), key='-GIVENS-', enable_events=True)]
                ]
            )
        ],
        [
            sg.Column(
                [
                    [sg.Text("All WHENs in scenario")],
                    [sg.Listbox(values=whens, size=(60, 7), key='-WHENS-', enable_events=True)]
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
                    [sg.pin(sg.Col([[sg.Listbox(values=[], size=(20, 4), enable_events=True, key='-BOX-',
                                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],
                       key='-BOX-CONTAINER-', pad=(0, 0), visible=False))]
                ]
            )
        ],
        [
            sg.Column(
                [
                    [sg.Text("All THENs in scenario")],
                    [sg.Listbox(values=thens, size=(60, 7), key='-THENS-', enable_events=True)]
                ]
            ),
            sg.Column(
                new_attribute_input(), key='-ATTRIBUTES-'
            )
        ],

        [sg.Button("Add new given", key="-ADD-GIVENS-"),
         sg.Button("Add new when", key="-ADD-WHENS-"),
         sg.Button("Add new then", key="-ADD-THENS-")],
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
        print(values)

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if "-ADD-" in event:
            c = event.replace("-ADD", "")
            list_of_elements = window[c].get_list_values()
            list_of_elements.append("yeppers")
            window[c].update(values=list_of_elements)
        if event in specials:
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
            if text:
                prediction_list = [item for item in choices if item.startswith(text)]

            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)

            attribute_inputs_refresh(window, text)

        elif event == '-SAVE-':
            text_in_input = values['-INPUT-HERE-']
            for s in specials:
                if window[s].get():
                    c = window[s].get_list_values()
                    c[window[s].get_indexes()[0]] = text_in_input
                    window[s].update(values=c)
                    window['-INPUT-HERE-'].update("")

            attribute_inputs_refresh(window, text_in_input)
        elif '-INSERT-ATTRIBUTE-' in event:
            index = re.findall("(?<=-)(\d+)(?=-)", event)[0]
            input_string = values['-INPUT-HERE-']
            attribute_replacement = values[f'-INPUT-ATTRIBUTE-{index}-']
            attribute = re.findall("(?<=:)(.*?)(?= )", input_string)[0]
            new_input_string = input_string.replace(f':{attribute}', attribute_replacement)
            window['-INPUT-HERE-'].update(new_input_string)
            attribute_inputs_refresh(window, new_input_string)

        elif event == '-SAVE-TO-FILE-':
            save_to_file(window)

    window.close()


if __name__ == "__main__":
    gui_for_scenarios()
