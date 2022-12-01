def delete_action(window, plan):
    selected_action = window['-ACTION-LIST-'].get_indexes()

    if len(selected_action) == 0:
        return False
    plan.pop(selected_action[0])
    window['-ACTION-LIST-'].update(list(map(lambda obj: obj.format_for_todo_listbox(), plan)))
    remain_selection_of_action(index=selected_action[0], plan=plan, window=window)


def remain_selection_of_action(index, plan, window):
    if len(plan) != 0:
        if len(plan) - 1 >= index:
            window['-ACTION-LIST-'].widget.selection_set(index)
        else:
            window['-ACTION-LIST-'].widget.selection_set(len(plan) - 1)
