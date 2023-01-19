import re


def check_if_step_is_already_defined(bdd_attribute, name_of_actions):
    for name_of_file in ['new_steps', 'new_actions']:
        with open(f"steps/{name_of_file}.py", "r") as f:
            file_inside = f.read()

        result = _check_if_found_in_file(file_inside, bdd_attribute, name_of_actions)

        if result is not None:
            return result, name_of_file

    return None, None


def _check_if_found_in_file(whole_text, bdd_attribute, name_of_actions):
    headers_in_file = re.findall('@given.*|@when.*|@then.*', whole_text)

    saved_index = None
    for index, p in enumerate(headers_in_file):
        b = re.findall(f'@{bdd_attribute}.*{name_of_actions}', p)
        if len(b) != 0:
            saved_index = index

    return saved_index


def _types(bdd_attribute):
    amount_of_dots = "\'{3}"
    return f"([#]? *@{bdd_attribute}.*?{amount_of_dots}\))"


def delete_already_existing_step(index, file):
    with open(f"steps/{file}.py", "r") as f:
        file_inside = f.read()
    regex_getting_whole_steps_from_file = f'(from.*?\n)|{_types("given")}|{_types("when")}|{_types("then")}'
    steps_in_array = re.findall(regex_getting_whole_steps_from_file, file_inside, flags=re.DOTALL)

    # index + 1 because we split file with from behave import library
    steps_in_array.pop(index + 1)

    full_string = ''
    for index, step in enumerate(steps_in_array):
        part_string = ''
        for part_of_step in step:
            part_string += part_of_step
        if index != 0:
            full_string += '\n\n'

        full_string += f'{part_string}'

    with open(f"steps/{file}.py", "w") as f:
        f.write(full_string)


def save_plan_to_file(whole_plan, plan_is_an_action):
    if plan_is_an_action is True:
        with open("steps/new_actions.py", "a") as f:
            f.write(whole_plan)
    else:
        with open("steps/new_steps.py", "a") as f:
            f.write(whole_plan)
