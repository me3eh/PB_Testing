from gui_handlers.step_creation.buttons import save_action_buttons
import PySimpleGUI as sg
from shared_info.constants import ERROR_PNG
from services.helper_methods import get_full_url

def show_saved_actions(values, event, window):
    visibility = values[event] == 'use saved actions'
    window['-SAVED-ACTIONS-'].update(visible=visibility)
    window['-RELOAD-ACTIONS-'].update(visible=visibility)
    window['-BDD-ATTRIBUTE-'].update(visible=(not visibility))


def find_all_selections(window, values, event, site_info, current_tags):
    domain = window['-DOMAIN-'].get()
    username_field = window['-USERNAME-FIELD-'].get()
    username_value = window['-USERNAME-VALUE-'].get()
    password_field = window['-PASSWORD-FIELD-'].get()
    password_value = window['-PASSWORD-VALUE-'].get()
    login_path = window['-LOGIN-PATH-'].get()
    target_site = window['-LAST-SITE-'].get()

    site = get_full_url(domain, target_site)

    window['-XPATH-INPUT-'].update('', background_color='white')
    window['-TAG-DESCRIPTION-'].update('')

    need_to_search_for_tags = True
    tags_found = []
    tag = tag_attributes = None
    thrown_exception = False

    if values[event] in ['visiting site', 'waiting for amount of seconds', 'use saved actions',
                         'assert url of site', 'assert title of site']:
        tags_found = []
        save_action_buttons.enable_save_buttons(window)
        need_to_search_for_tags = False

    elif values[event] in ['filling input', 'clicking input', 'assert input is not visible', 'assert input is disabled']:
        tag = 'input'
    elif values[event] == 'clicking checkbox':
        tag = 'input'
        tag_attributes = {'type': 'checkbox'}
    elif values[event] == 'clicking submit input':
        tag = 'input'
        tag_attributes = {'type': 'submit'}
    elif values[event] == 'clicking submit button':
        tag = 'button'
        tag_attributes = {'type': 'submit'}
    elif values[event] == 'clicking radio button':
        tag = 'input'
        tag_attributes = {'type': 'radio'}
    elif values[event] == 'clicking button':
        tag = 'button'
    elif values[event] == 'clicking link':
        tag = 'a'
    elif values[event] == 'attaching file to file input':
        tag = 'input'
        tag_attributes = {'type': 'file'}
    elif values[event] == 'selecting option from select':
        tag = 'select'
    elif values[event] == 'assert element has certain text':
        tag = None

    if need_to_search_for_tags is True:
        if values['-LOGGED-IN-']:
            tags_found, thrown_exception = site_info.get_tag_logged_in(site, username_field, username_value,
                                                                       password_field, password_value, login_path,
                                                                       domain=domain, tag=tag,
                                                                       tag_attributes=tag_attributes)
        else:
            tags_found, thrown_exception = site_info.get_tag_anonymous(site, tag=tag, tag_attributes=tag_attributes)
    if thrown_exception is True:
        sg.popup_notify(tags_found, icon=ERROR_PNG, title='No connection')
        return

    current_tags.clear()
    current_tags.extend(tags_found)
    listed = list(map(lambda obj: obj.format_for_listbox_with_available_actions(), tags_found))
    window['-TAG-LIST-'].update(listed)
