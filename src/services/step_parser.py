import re
import os
from models.saved_actions import SavedActions


def import_actions():
    path = "steps/new_actions.py"
    file_exists = os.path.exists(path)
    if file_exists is False:
        return []

    with open(path, "r") as f:
        new_actions = f.read()
    a = re.findall('@given.*|@when.*|@then.*', new_actions)

    saved_actions = []
    for action in a:
        bdd_attribute = _get_string_between_two_characters(action, start='@', end='\(')
        action_name = _get_string_between_two_characters(action, start='\(', end='\)')
        saved_actions.append(SavedActions(bdd_attribute, eval(action_name)))
    return saved_actions


def _get_string_between_two_characters(whole_string, start, end):
    try:
        marker1 = start
        marker2 = end
        regex_pattern = marker1 + '(.+?)' + marker2
        str_found = re.search(regex_pattern, whole_string).group(1)
        return str_found
    except AttributeError:
        # str_found = 'Nothing found between two markers'
        return None
