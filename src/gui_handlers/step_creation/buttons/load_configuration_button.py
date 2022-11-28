from configparser import ConfigParser
import pickle

def load_configuration(window, values, event, todo_actions, method_to_disable_inputs):
    config = ConfigParser()
    config.read(values[event])

    domain = config.get('main', 'domain')
    username_field = config.get('main', 'username_field')
    username_value = config.get('main', 'username_value')
    password_field = config.get('main', 'password_field')
    password_value = config.get('main', 'password_value')
    login_path = config.get('main', 'login_path')
    last_site = config.get('main', 'last_site')
    logged_in = config.get('main', 'logged_in')

    window['-DOMAIN-'].update(domain)
    window['-USERNAME-FIELD-'].update(username_field)
    window['-USERNAME-VALUE-'].update(username_value)
    window['-PASSWORD-FIELD-'].update(password_field)
    window['-PASSWORD-VALUE-'].update(password_value)
    window['-LOGIN-PATH-'].update(login_path)
    window['-LAST-SITE-'].update(last_site)
    window['-LOGIN-PATH-'].update(login_path)
    window['-LOGGED-IN-'].update(eval(logged_in))
    method_to_disable_inputs(window, not eval(logged_in))

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    pickled = None
    with open(f'{values[event]}.pickle', 'rb') as f:
        pickled = f.read()
    new_todo_actions = pickle.loads(pickled)
    todo_actions.clear()
    todo_actions.extend(new_todo_actions)
    window['-ACTION-LIST-'].update(list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions)))


