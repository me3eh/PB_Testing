def pick_tag(window, todo_actions):
    index = window['-ACTION-LIST-'].get_indexes()
    if len(index) == 0:
        print("yups")
        return

    if len(todo_actions) != 0:
        selected_tag = todo_actions[index[0]]
        if selected_tag.whole_html is not None:
            window['-TAG-DESCRIPTION-'].update(selected_tag.whole_html.prettify())
            window['-XPATH-INPUT-'].update(selected_tag.xpath)
        else:
            window['-TAG-DESCRIPTION-'].update('Current action does not have any tag')
            window['-XPATH-INPUT-'].update('Current action does not have any xpath')
