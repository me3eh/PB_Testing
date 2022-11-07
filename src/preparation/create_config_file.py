from configparser import ConfigParser


def create_config_file():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    if 'main' not in config:
        config.add_section('main')
    config.set('main', 'domain', 'http://localhost:3000')
    config.set('main', 'username_field', 'username')
    config.set('main', 'password_field', 'password')
    config.set('main', 'username_value', 'jar')
    config.set('main', 'password_value', 'jarjarjar')
    config.set('main', 'login_path', '/login')
    config.set('main', 'last_site', 'https://gram.pl')

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    print("Config file created")
