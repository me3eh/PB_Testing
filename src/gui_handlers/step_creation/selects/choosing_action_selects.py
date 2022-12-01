def change(event, values, window):
    print(window['-ACTIONS-CHOICE-'].get())

    file_browse_input_not_visible = False
    autocomplete_with_current_domain_visible = False

    if window['-ACTIONS-CHOICE-'].get() == 'attaching file to file input':
        file_browse_input_not_visible = True

    if window['-ACTIONS-CHOICE-'].get() == 'visiting site':
        autocomplete_with_current_domain_visible = True

    window['-HELPER-INPUT-FILE-BROWSE-'].update(visible=file_browse_input_not_visible)
    window['-HELPER-INPUT-CURRENT-DOMAIN-'].update(visible=autocomplete_with_current_domain_visible)
    window['-HELPER-INPUT-CURRENT-DOMAIN-WITH-ENDPOINT-'].update(visible=autocomplete_with_current_domain_visible)
