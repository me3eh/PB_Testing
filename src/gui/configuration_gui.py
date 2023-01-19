import PySimpleGUI as sg
from layouts import configuration_gui
from sqlite import database
from shared_info.constants import ERROR_PNG
from configparser import ConfigParser
from gui_handlers.configuration_gui.buttons import *
from gui_handlers.configuration_gui.listboxes import *



def launch_configuration():
    project_path = get_project_path_from_config()
    layout = configuration_gui.get_layout(project_path)
    window = sg.Window("Configuration for testing", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-FROM-LISTBOX-TO-LISTBOX-':
            move_from_listbox_to_listbox_button.move(window)
        elif event == '-SAVE-URL-FROM-INPUT-':
            save_url_from_input_button.save(window=window)
        elif event == '-ADD-URL-FROM-INPUT-':
            add_url_from_input_button.save(window=window)
        elif event == '-DELETE-SELECTED-':
            delete_button.delete_selected(window)
        elif event == '_FILEBROWSE_':
            browse_file_button.browse_files(values=values, event=event)
        elif event == '-SCAN-FOR-URLS-FROM-GIVEN-PATH-':
            project_path_scan_urls_button.scan_for_urls(window)
        elif event in ['-SCANNED-URLS-', '-USER-URLS-']:
            change_selected_checkbox.change(window=window, event=event, values=values)




def get_project_path_from_config():
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    project_path = config.get('main', 'project_path')
    return project_path
