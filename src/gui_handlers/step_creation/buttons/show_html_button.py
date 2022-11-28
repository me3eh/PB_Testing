import os
from configparser import ConfigParser


def show_html_in_external_app(html_to_show):
    with open("html_viewer.html", 'w') as f:
        f.write(html_to_show)
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    program_for_opening_html = config.get('main', 'program_for_opening_html')
    os.system(f'{program_for_opening_html} html_viewer.html')
