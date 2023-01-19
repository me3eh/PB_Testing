from configparser import ConfigParser
import pickle


def save_configuration(window, values, event, todo_actions):
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')

    if 'main' not in config:
        config.add_section('main')

    actual_plan_name = window['-TITLE-OF-TEST-'].get()
    domain = window['-DOMAIN-'].get()
    username_field = window['-USERNAME-FIELD-'].get()
    username_value = window['-USERNAME-VALUE-'].get()
    password_field = window['-PASSWORD-FIELD-'].get()
    password_value = window['-PASSWORD-VALUE-'].get()
    login_path = window['-LOGIN-PATH-'].get()
    last_site = window['-LAST-SITE-'].get()
    logged_in_checkbox_checked = window['-LOGGED-IN-'].get()

    config.set('main', 'actual_plan_name', actual_plan_name)
    config.set('main', 'domain', domain)
    config.set('main', 'username_field', username_field)
    config.set('main', 'password_field', password_field)
    config.set('main', 'username_value', username_value)
    config.set('main', 'password_value', password_value)
    config.set('main', 'last_site', last_site)
    config.set('main', 'login_path', login_path)
    config.set('main', 'logged_in', repr(logged_in_checkbox_checked))
    with open(values[event], 'w') as f:
        config.write(f)

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    pickled = pickle.dumps(todo_actions)
    with open(f'{values[event]}.pickle', 'wb') as f:
        f.write(pickled)
