def change(window, event, values):
    checkbox_checked = window['-GET-SELECTED-'].get()
    if checkbox_checked:
        url_input = window['-INPUT-ANYTHING-']
        selected_text = values[event]
        url_input.update(selected_text)
