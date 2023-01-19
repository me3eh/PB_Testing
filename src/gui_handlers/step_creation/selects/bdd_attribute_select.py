from services.object_collections_to_string import convert_collection_to_string_using_variable


def change_bdd_attribute(values, event, window, given_when_actions, then_actions, current_tags):
    bdd_attribute = values[event]
    actions = given_when_actions if bdd_attribute in ['Given', 'When'] else then_actions

    actions_in_text = convert_collection_to_string_using_variable(collection=actions, variable_name='text')
    window['-ACTIONS-CHOICE-'].update(values=actions_in_text, value=actions_in_text[0])
    window['-TAG-LIST-'].update(values=[])
    current_tags.clear()

