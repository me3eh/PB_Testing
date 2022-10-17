from configparser import ConfigParser


def create_config_file():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    if 'main' not in config:
        config.add_section('main')
    config.set('main', 'domain', 'http://localhost:3000')
    config.set('main', 'username_field', 'username')
    config.set('main', 'password_field', 'password')
    config.set('main', 'username_value', 'http://localhost:3000')
    config.set('main', 'password_value', 'http://localhost:3000')

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    print("Config file created")
