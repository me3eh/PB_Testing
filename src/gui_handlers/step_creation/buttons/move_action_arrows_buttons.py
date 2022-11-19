def move_action(event, window, sg, error_picture, todo_actions):
    index_tuple = window['-ACTION-LIST-'].get_indexes()
    if len(index_tuple) == 0:
        sg.popup_notify("First click on any action and after that click on arrows",
                        icon=error_picture,
                        title='Arrows for changing actions order')
        return

    index = index_tuple[0]
    final_index = (index - 1) if event == '-MOVE-UP-' else (index + 1)
    if len(todo_actions) > final_index >= 0:
        todo_action = todo_actions.pop(index)
        todo_actions.insert(final_index, todo_action)
        window['-ACTION-LIST-'].update(create_todo_actions_for_listbox(todo_actions))
        window['-ACTION-LIST-'].widget.selection_set(final_index)


def create_todo_actions_for_listbox(todo_actions):
    return list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))
