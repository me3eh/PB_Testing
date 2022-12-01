from services.step_parser import import_actions
from services.object_collections_to_string import convert_collection_to_string_using_method


def reload(window, imported_actions):
    new_actions = import_actions()
    actions_as_string = convert_collection_to_string_using_method(collection=new_actions,
                                                                  method_name='information_for_saved_actions')
    imported_actions.clear()
    imported_actions.extend(new_actions)
    window['-SAVED-ACTIONS-'].update(values=actions_as_string)
    if len(actions_as_string) != 0:
        window['-SAVED-ACTIONS-'].update(value=actions_as_string[0])

