def change(event, values, window):
    print(window['-ACTIONS-CHOICE-'].get())
    input_visible = window['-HELPER-INPUT-'].visible
    window['-HELPER-INPUT-'].update(visible=not input_visible)
    print('yikes')
