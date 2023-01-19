def check(window, event):
    list_values_of_tag_list = window['-TAG-LIST-'].get_list_values()
    if len(list_values_of_tag_list) == 0:
        return

    index = window['-TAG-LIST-'].get_indexes()
    if len(index) == 0:
        return
    index = index[0]

    final_index = (index - 1) if event == '-MOVE-UP-TAG-' else (index + 1)
    if len(list_values_of_tag_list) > final_index >= 0:
        window['-TAG-LIST-'].update(set_to_index=[])
        window['-TAG-LIST-'].widget.selection_set(final_index)
