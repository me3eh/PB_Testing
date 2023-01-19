def create(plan, title, bdd_attribute='given'):
    whole_plan = ''
    actions_plan = ''
    for action in plan:
        action_in_text = f'{action.get_command()}\n'
        actions_plan += f'\t\t{action_in_text}'

    whole_plan += f"\n\n@{bdd_attribute} ('{title}')\n"
    whole_plan += "def step(context):\n"
    whole_plan += "\tcontext.execute_steps(u'''\n"
    whole_plan += f"{actions_plan}"
    whole_plan += "\t''')"

    return whole_plan
