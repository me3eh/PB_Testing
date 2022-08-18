from configparser import ConfigParser


def create_config_file():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    config.add_section('login')
    config.set('login', 'username', 'value1')
    config.set('login', 'password', 'value2')

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)
