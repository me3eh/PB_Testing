import PySimpleGUI as sg
scenario = "lel"
givens = ['when visiting site <url>', 'logged as']
whens = ['visiting site <url>', 'bgi']
thens = ['yikes', 'anormous']
completions = {
    '-GIVENS-': ['when visiting site <url>', 'logged as'],
    '-WHENS-': ['visiting site <url>', 'bgi'],
    '-THENS-': ['yikes', 'anormous']
}
specials = ['-GIVENS-', '-WHENS-', '-THENS-']
choices = ['di', 'da']


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


def ddd():
    layout = [
        [sg.Text('FileName'), sg.Column([[]], k='layout_principal', expand_x=True), sg.Text("Feature name")],
        [sg.Input('dad', enable_events=True, key='-Filename-') ,sg.Column([[]], k='layout_principal', expand_x=True),  sg.Input('mom', enable_events=True, key='Feature name')],
        # [[sg.Column(add_new(0, "given"), key='-Column-given-')]],
        # [[sg.Column(add_new(1, "when"), key='-Column-when-')]],
        # [[sg.Column(add_new(2, "then"), key='-Column-then-')]],
        # [sg.Multiline(get_string(), size=(60, 20), disabled=True, key="test_text"), sg.Column([[]], key='functional')],
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
                    [sg.Text("All Special Commands Will Go Here")],
                    [sg.Input("Here", key="-INPUT-HERE-", size=(20, 4), enable_events=True), sg.Button("Save", key='-SAVE-')],
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
            )
        ],

        [sg.Button("Add new given", key="-ADD-GIVENS-"),
         sg.Button("Add new when", key="-ADD-WHENS-"),
         sg.Button("Add new then", key="-ADD-THENS-")],
        [sg.Button("Add new given", key="save-to-file"),
         sg.Button("Add new then", key="Exit")]
    ]
    window = sg.Window("Creating scenario",
                       layout,
                       resizable=True,
                       finalize=True,
                       return_keyboard_events=True)
    list_element: sg.Listbox = window.Element('-BOX-')
    sel_item, prediction_list = 0, []
    global choices
    while True:             # Event Loop
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
        # elif event.startswith('Right'):
        #     if len(values['-BOX-']) > 0:
        #         window['-INPUT-HERE-'].update(value=values['-BOX-'])
        #         window['-BOX-CONTAINER-'].update(visible=False)
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '-BOX-':
            print(values['-BOX-'])
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
        elif event == '-SAVE-':
            for s in specials:
                if window[s].get():
                    c = window[s].get_list_values()
                    c[window[s].get_indexes()[0]] = values['-INPUT-HERE-']
                    print(c)
                    window[s].update(values=c)
                    window['-INPUT-HERE-'].update("")
    window.close()


if __name__ == "__main__":
    ddd()
