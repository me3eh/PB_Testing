def change(event, values, window):

    file_browse_input_not_visible = False
    autocomplete_with_current_domain_visible = False

    if window['-ACTIONS-CHOICE-'].get() == 'attaching file to file input':
        file_browse_input_not_visible = True

    if window['-ACTIONS-CHOICE-'].get() in ['visiting site', 'assert url of site']:
        autocomplete_with_current_domain_visible = True

    window['-HELPER-INPUT-FILE-BROWSE-'].update(visible=file_browse_input_not_visible)
    window['-HELPER-INPUT-CURRENT-DOMAIN-'].update(visible=autocomplete_with_current_domain_visible)
    window['-HELPER-INPUT-CURRENT-DOMAIN-WITH-ENDPOINT-'].update(visible=autocomplete_with_current_domain_visible)
    # window['-INPUT-WRAPPER-'].update(visible=False)
    # _hide_input(window)


# def _hide_input(window):
#     window['-TAG-LIST-'].widget.get_

