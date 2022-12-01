import PySimpleGUI as sg
import sys
from configparser import ConfigParser

from services.site_info import SiteInfo
from models.website_tag import WebsiteTag
from layouts import step_creation
from models.action_name import ActionName

from gui_handlers.step_creation.text_inputs import *
from gui_handlers.step_creation.listboxes import *
from gui_handlers.step_creation.selects import *
from gui_handlers.step_creation.buttons import *
from sqlite import database
from shared_info.constants import ERROR_PNG, OK_PNG
from object_collections_to_string import *

urls_from_project = database.retrieve_urls('urls_and_attributes')
input_text = ''
site_info = SiteInfo()
imported_actions = []


imported_actions_as_string = []

given_when_actions = [
    ActionName('waiting for amount of seconds', attribute_needed=True),
    ActionName('visiting site', attribute_needed=False),
    ActionName('filling input', attribute_needed=True),
    ActionName('clicking button', attribute_needed=True),
    ActionName('clicking link', attribute_needed=True),
    ActionName('clicking input', attribute_needed=True),
    ActionName('clicking checkbox', attribute_needed=True),
    ActionName('clicking radio button', attribute_needed=True),
    ActionName('attaching file to file input', attribute_needed=True),
    ActionName('selecting option from select', attribute_needed=True),
    ActionName('use saved actions', attribute_needed=False)
]
then_actions = [
    ActionName('assert url of site', attribute_needed=False),
    ActionName('assert title of site', attribute_needed=False),
    ActionName('assert input is disabled', attribute_needed=False),
    ActionName('assert input is not visible', attribute_needed=False),
    ActionName('assert input is visible', attribute_needed=False),
    ActionName('assert element has certain text', attribute_needed=False)
]
actions = given_when_actions

todo_actions = [WebsiteTag(bdd_attribute='Given', value_for_bdd='visiting site', attribute='https://google.com')]


def get_values_for_configuration(window):
    return [
        {"domain": window['-DOMAIN-'].get()},
        {"login_path": window['-LOGIN-PATH-'].get()},
        {"last_site": window['-LAST-SITE-'].get()},
        {"username_field": window['-USERNAME-FIELD-'].get()},
        {"password_field": window['-PASSWORD-FIELD-'].get()},
        {"username_value": window['-USERNAME-VALUE-'].get()},
        {"password_value": window['-PASSWORD-VALUE-'].get()}
    ]


def save_configuration(config, values_for_config):
    for value in values_for_config:
        config.set('main', f'{list(value.keys())[0]}', f"{list(value.values())[0]}")
    with open('resources_for_testing/config.ini', 'w') as f:
        config.write(f)


def create_step():
    sys.setrecursionlimit(6000)
    global actions, input_text

    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    domain = config.get('main', 'domain')
    username_field = config.get('main', 'username_field')
    password_field = config.get('main', 'password_field')
    username_value = config.get('main', 'username_value')
    password_value = config.get('main', 'password_value')
    last_site = config.get('main', 'last_site')
    login_path = config.get('main', 'login_path')

    current_tags = []
    actions_for_layout = convert_collection_to_string_using_variable(collection=actions,
                                                                     variable_name='text')
    todo_actions_for_layout = convert_collection_to_string_using_method(collection=todo_actions,
                                                                        method_name='format_for_todo_listbox')
    layout = step_creation.get_layout(domain,
                                      login_path,
                                      last_site,
                                      username_field,
                                      username_value,
                                      password_field,
                                      password_value,
                                      actions=actions_for_layout,
                                      todo_actions=todo_actions_for_layout,
                                      imported_actions=imported_actions_as_string
                                      )

    window = sg.Window("Step creator", layout, resizable=True, finalize=True)
    window['-LOGIN-PATH-BOX-CONTAINER-'].update(visible=False)
    window['-LAST-SITE-BOX-CONTAINER-'].update(visible=False)
    window['-NOT-USED-ONLY-FOR-PROPER-LAYOUT-'].update(visible=False)
    if len(imported_actions_as_string) > 0:
        window['-SAVED-ACTIONS-'].update(value=imported_actions_as_string[0])
    # reload_actions_button.reload(window, imported_actions)
    while True:
        event, values = window.read()
        # print(event)
        # print(values)
        if event == sg.WIN_CLOSED or event == "Exit":
            values = get_values_for_configuration(window)
            save_configuration(config, values)
            sg.popup_notify("Saved your configuration", title='Saved', icon=OK_PNG)
            break
        elif event == '-ADD-ACTION-':
            add_action_button.add_action(window, values, todo_actions, current_tags, imported_actions)
        elif event == '-SAVE-CHANGES-TO-CONFIG-':
            values = get_values_for_configuration(window)
            save_configuration(config, values)
            sg.popup_notify("Saved your configuration", title='Saved', icon=OK_PNG)
        elif event == '-LOGGED-IN-':
            value_of_checkbox = not values[event]
            login_inputs.disabling(window=window, value_for_disabling=value_of_checkbox)
        elif event == '-ACTIONS-CHOICE-':
            actions_choice_select.find_all_selections(window, values, event, site_info, current_tags)
            actions_choice_select.show_saved_actions(values, event, window)
            choosing_action_selects.change(event=event, values=values, window=window)
        elif event == '-TAG-LIST-':
            tag_list_listbox.pick_tag(window=window, current_tags=current_tags,
                                      last_used_html=site_info.get_last_used_html())
            todo_actions_and_tag_listboxes.only_one_selected(event, window)
        elif event == '-SAVE-CONFIGURATION-':
            save_configuration_button.save_configuration(window, values, event, todo_actions)
        elif event == '-LOAD-CONFIGURATION-':
            load_configuration_button.load_configuration(window, values, event, todo_actions)
        elif event == '-GENERATE-PLAN-':
            generate_plan_button.generate_plan(window, todo_actions, plan_is_an_action=False)
        elif event == '-GENERATE-PLAN-AS-ACTION-':
            generate_plan_button.generate_plan(window, todo_actions, plan_is_an_action=True)
            reload_actions_button.reload(window, imported_actions)
        elif event == '-RELOAD-ACTIONS-':
            reload_actions_button.reload(window, imported_actions)
        elif event == '-DELETE-ACTION-':
            delete_action_button.delete_action(window, todo_actions)
        elif event == '-BDD-ATTRIBUTE-':
            bdd_attribute_select.change_bdd_attribute(values, event, window, given_when_actions, then_actions)
            choosing_action_selects.change(event=event, values=values, window=window)
        elif event in ['-MOVE-UP-', '-MOVE-DOWN-']:
            move_action_arrows_buttons.move_action(event=event, window=window, sg=sg,
                                                   error_picture=ERROR_PNG, todo_actions=todo_actions)
        elif event == '-XPATH-EXISTS-':
            xpath_viewer_input.check_if_xpath_unique(last_used_html=site_info.get_last_used_html(), window=window)
        elif event == '-ACTION-LIST-':
            todo_actions_listbox.pick_tag(window=window, todo_actions=todo_actions)
            todo_actions_and_tag_listboxes.only_one_selected(event, window)
        elif event == '-SHOW-HTML-':
            show_html_button.show_html_in_external_app(site_info.get_last_used_html())
        elif event == '-COPY-HTML-':
            copy_html_button.copy_html_to_clipboard(site_info.get_last_used_html())
        elif event == '-COPY-HTML-ELEMENT-':
            copy_html_button.copy_element_html_to_clipboard(window)
        elif event == '-LAST-SITE-':
            autocomplete_input.autocomplete(values, window, urls_from_project, layout_key=event)
        elif event == '-LOGIN-PATH-':
            autocomplete_input.autocomplete(values, window, urls_from_project, layout_key=event)
        elif event == '-LOGIN-PATH-BOX-':
            window['-LOGIN-PATH-'].update(value=values['-LOGIN-PATH-BOX-'][0])
            window['-LOGIN-PATH-BOX-CONTAINER-'].update(visible=False)
        elif event == '-LAST-SITE-BOX-':
            window['-LAST-SITE-'].update(value=values['-LAST-SITE-BOX-'][0])
            window['-LAST-SITE-BOX-CONTAINER-'].update(visible=False)
        elif event == '-HELPER-INPUT-CURRENT-DOMAIN-':
            current_domain_helper_button.insert_current_domain(window)
        elif event == '-HELPER-INPUT-CURRENT-DOMAIN-WITH-ENDPOINT-':
            current_domain_helper_button.insert_current_domain_with_endpoint(window)
        elif event == '-RESET-SAVED-HTMLS-':
            site_info.clear_saved_htmls()
