from configparser import ConfigParser


def browse_files(values, event):
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    project_path = values[event]
    config.set('main', 'project_path', project_path)

    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)
