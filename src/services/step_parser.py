import re

def is_action_already_exists(bdd_attribute, name_of_action):
    with open("steps/new_steps.py", "r") as f:
        new_steps = f.read()
    with open("steps/new_actions.py", "r") as f:
        new_actions = f.read()

    a = re.findall('@given.*|@when.*|@then.*', new_steps)

    text = 'bawienie_sie_z_railsami'

    saved_index = -1
    for index, p in enumerate(a):
        b = re.findall(f'@given.*{text}', p)
        if len(b) != 0:
            saved_index = index

    print(saved_index)
    po = re.findall('(from.*?\n)|(@given.*?\'{3}\))|(@when.*?\'{3}\))|(@then.*?\'{3}\))', new_steps, flags=re.DOTALL)
    full_string = ''
    for index, s in enumerate(po):
        part_string = ''
        for k in s:
            part_string += k
        full_string += f'\n\n{part_string}'

    with open("steps/new_actions.py", "w") as f:
        f.write(full_string)

# something()
