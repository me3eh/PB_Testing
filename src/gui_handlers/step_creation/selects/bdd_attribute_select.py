def change_bdd_attribute(values, event, window, given_when_actions, then_actions):
    bdd_attribute = values[event]
    actions = given_when_actions if bdd_attribute in ['Given', 'When'] else then_actions

    actions_in_text = get_string_from_action_names(actions)
    window['-ACTIONS-CHOICE-'].update(values=actions_in_text, value=actions_in_text[0])


def get_string_from_action_names(actions):
    return list(map(lambda obj: obj.text, actions))
