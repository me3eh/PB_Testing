from configparser import ConfigParser
import pathlib


def create_config_file():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    if 'main' not in config:
        config.add_section('main')
    config.set('main', 'actual_plan_name', 'Something')
    config.set('main', 'domain', 'http://localhost:3000')
    config.set('main', 'username_field', 'username')
    config.set('main', 'password_field', 'password')
    config.set('main', 'username_value', 'jar')
    config.set('main', 'password_value', 'jarjarjar')
    config.set('main', 'login_path', '/login')
    config.set('main', 'last_site', '/')
    config.set('main', 'project_path', str(pathlib.Path(__file__).parent.parent.parent.parent.parent.parent.resolve()))
    config.set('main', 'program_for_opening_html', 'code')

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    print("Config file created")
