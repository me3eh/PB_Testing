from configparser import ConfigParser


def create_config_file():
    config = ConfigParser()

    config.read('resources_for_testing/config.ini')
    if 'login' not in config:
        config.add_section('login')
    if 'site_info' not in config:
        config.add_section('site_info')
    config.set('site_info', 'domain', 'http://localhost:3000')

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)

    print("Config file created")
