import PySimpleGUI as sg
from site_scraping import site_info
from configparser import ConfigParser
from text_to_test_transform import test
from website_elements.website_tag import WebsiteTag
from gui_handlers.step_creation import delete_action_button
from layouts import step_creation
from website_elements.action_name import ActionName
from gui_handlers.step_creation import xpath_viewer_input, move_action_arrows_buttons, tag_list_listbox
from gui_handlers.step_creation import todo_actions_listbox, show_html_button, copy_html_button
from gui_handlers.step_creation import save_configuration_button, load_configuration_button
import sys
OK_PNG = b'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'
ERROR_PNG = b'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'
# GIVEN_ATTRIBUTE_INFO = "<-- Given - preparing site for doing something (for example loggin in)"
GIVEN_ATTRIBUTE_INFO = "Template"
# WHEN_ATTRIBUTE_INFO = "<-- When - doing some actions on our site (clicking on buttons)"
# THEN_ATTRIBUTE_INFO = "<-- Then - asserting that action took place (title was revealed after visiting site)"

given_when_actions = [ActionName('visiting site', attribute_needed=False),
                      ActionName('filling input', attribute_needed=True),
                      ActionName('clicking button', attribute_needed=True),
                      ActionName('clicking link', attribute_needed=True)]
then_actions = [ActionName('assert url of site', attribute_needed=False),
                ActionName('assert title of site', attribute_needed=False)]
actions = given_when_actions
bdd_attributes = ['Given', 'When', 'Then']

todo_actions = [WebsiteTag(bdd_attribute='Given', value_for_bdd='visiting site', attribute='https://google.com')]


# todo_actions_for_listbox = list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))

# def change_bdd_attribute(window, bdd_attribute):
#     textbox = window['-BDD-ATTRIBUTE-INFO-']
#     if bdd_attribute == 'Given':
#         textbox.update(GIVEN_ATTRIBUTE_INFO)
#     elif bdd_attribute == 'When':
#         textbox.update(WHEN_ATTRIBUTE_INFO)
#     elif bdd_attribute == 'Then':
#         textbox.update(THEN_ATTRIBUTE_INFO)

def create_todo_actions_for_listbox():
    return list(map(lambda obj: obj.format_for_todo_listbox(), todo_actions))


def get_string_from_action_names():
    return list(map(lambda obj: obj.text, actions))


def login_inputs_disabled(window, value_of_checkbox):
    components_to_switch_disable = ['-USERNAME-FIELD-', '-USERNAME-VALUE-', '-PASSWORD-FIELD-', '-PASSWORD-VALUE-',
                                    '-LOGIN-PATH-']
    for key in components_to_switch_disable:
        window[key].update(disabled=value_of_checkbox)


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

def action_create(type_of_action,
                  selected_action_index,
                  input_for_action,
                  bdd_attribute,
                  window,
                  selected_tag,
                  current_tags):
    if type_of_action == 'visiting site':
        return WebsiteTag(value_for_bdd='visiting site',
                          attribute=input_for_action,
                          bdd_attribute=bdd_attribute)
    elif type_of_action == 'assert url of site':
        return WebsiteTag(value_for_bdd='assert url of site',
                          attribute=input_for_action,
                          bdd_attribute=bdd_attribute)
    elif type_of_action == 'assert title of site':
        return WebsiteTag(value_for_bdd='assert title of site',
                          attribute=input_for_action,
                          bdd_attribute=bdd_attribute)
    else:
        if len(selected_tag) == 0:
            return False
        else:
            current_chosen = current_tags[selected_tag[0]]
            current_chosen.value_for_bdd = type_of_action
            current_chosen.attribute = input_for_action
            return current_chosen


def create_step():
    sys.setrecursionlimit(6000)
    global actions

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

    layout = step_creation.get_layout(domain,
                                      login_path,
                                      last_site,
                                      username_field,
                                      username_value,
                                      password_field,
                                      password_value,
                                      get_string_from_action_names(),
                                      bdd_attributes,
                                      GIVEN_ATTRIBUTE_INFO,
                                      create_todo_actions_for_listbox()
                                      )

    window = sg.Window("Step creator", layout, resizable=True, finalize=True)

    while True:
        event, values = window.read()
        print(event)
        # print(values)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == '-ADD-ACTION-':
            bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
            type_of_action = values['-ACTIONS-CHOICE-']
            input_for_action = values['-HELPER-INPUT-']
            selected_action_index = window['-ACTION-LIST-'].get_indexes()
            selected_tag = window['-TAG-LIST-'].get_indexes()
            new_action = action_create(
                type_of_action,
                selected_action_index,
                input_for_action,
                bdd_attribute,
                window,
                selected_tag,
                current_tags
            )
            todo_actions.append(new_action)
            window['-ACTION-LIST-'].update(create_todo_actions_for_listbox())
        elif event == '-SAVE-CHANGES-TO-CONFIG-':
            values = get_values_for_configuration(window)
            save_configuration(config, values)
            sg.popup_notify("Saved your configuration")
        elif event == '-LOGGED-IN-':
            value_of_checkbox = not values[event]
            login_inputs_disabled(window, value_of_checkbox)
        elif event == '-ACTIONS-CHOICE-':
            domain = window['-DOMAIN-'].get()
            username_field = window['-USERNAME-FIELD-'].get()
            username_value = window['-USERNAME-VALUE-'].get()
            password_field = window['-PASSWORD-FIELD-'].get()
            password_value = window['-PASSWORD-VALUE-'].get()
            login_path = window['-LOGIN-PATH-'].get()
            target_site = window['-LAST-SITE-'].get()

            if domain.endswith('/') and target_site.startswith("/"):
                site = domain + target_site[1:]
            else:
                site = domain + target_site
            if values[event] == 'visiting site':
                current_tags = []
            if values[event] == 'filling input':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='input')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='input')
            elif values[event] == 'clicking button':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='button')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='button')
            elif values[event] == 'clicking link':
                if values['-LOGGED-IN-']:
                    current_tags = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                               password_value, login_path, tag='a')
                else:
                    current_tags = site_info.get_tag_anonymous(site, tag='a')
            listed = list(map(lambda obj: obj.format_for_listbox_with_available_actions(), current_tags))
            window['-TAG-LIST-'].update(listed)
        elif event == '-TAG-LIST-':
            tag_list_listbox.pick_tag(window=window, current_tags=current_tags)
        elif event == '-SAVE-CONFIGURATION-':
            save_configuration_button.save_configuration(window, values, event, todo_actions)
        elif event == '-LOAD-CONFIGURATION-':
            load_configuration_button.load_configuration(window, values, event, todo_actions,
                                                         method_to_disable_inputs=login_inputs_disabled)
        elif event == '-GENERATE-PLAN-':
            test_title = window['-TITLE-OF-TEST-'].get()
            test.create(todo_actions, test_title, 'given')
            sg.popup_notify("Created", icon=OK_PNG)
        elif event == '-SAVE-ACTION-':
            bdd_attribute = window['-BDD-ATTRIBUTE-'].get()
            type_of_action = values['-ACTIONS-CHOICE-']
            input_for_action = values['-HELPER-INPUT-']
            selected_action_index = window['-ACTION-LIST-'].get_indexes()
            selected_tag = window['-TAG-LIST-'].get_indexes()
            if len(selected_action_index) == 0:
                sg.popup_notify("You didnt chose anything from todo_actions listbox to change", icon=ERROR_PNG)
            else:
                new_action = action_create(type_of_action, selected_action_index, input_for_action,
                                           bdd_attribute, window, selected_tag, current_tags)
                if not new_action:
                    sg.popup_notify("You didnt chose anything from available actions listbox to change",
                                    icon=ERROR_PNG)
                else:
                    todo_actions[selected_action_index[0]] = new_action
                    window['-ACTION-LIST-'].update(create_todo_actions_for_listbox())
        elif event == '-DELETE-ACTION-':
            delete_action_button.delete_action(window, todo_actions)
        elif event == '-BDD-ATTRIBUTE-':
            bdd_attribute = values[event]
            print(bdd_attribute)
            if bdd_attribute in ['Given', 'When']:
                actions = given_when_actions
            else:
                actions = then_actions
            print(actions)
            actions_in_text = get_string_from_action_names()
            window['-ACTIONS-CHOICE-'].update(values=actions_in_text, value=actions_in_text[0])
        elif event in ['-MOVE-UP-', '-MOVE-DOWN-']:
            move_action_arrows_buttons.move_action(event=event, window=window, sg=sg,
                                                   error_picture=ERROR_PNG, todo_actions=todo_actions)
        elif event == '-XPATH-EXISTS-':
            xpath_viewer_input.check_if_xpath_unique(last_used_html=site_info.get_last_used_html(), window=window)
        elif event == '-ACTION-LIST-':
            todo_actions_listbox.pick_tag(window=window, todo_actions=todo_actions)
        elif event == '-SHOW-HTML-':
            show_html_button.show_html_in_external_app(site_info.get_last_used_html())
        elif event == '-COPY-HTML-':
            copy_html_button.copy_html_to_clipboard(site_info.get_last_used_html())
