def disable_save_buttons(window):
    window['-ADD-ACTION-'].update(disabled=True)
    # window['-SAVE-ACTION-'].update(disabled=True)


def enable_save_buttons(window):
    window['-ADD-ACTION-'].update(disabled=False)
    # window['-SAVE-ACTION-'].update(disabled=False)
