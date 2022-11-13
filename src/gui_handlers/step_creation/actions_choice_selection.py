import save_action_buttons

def find_all_selections(window, values, event, site_info, current_tags):
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
    tags_found = []

    window['-XPATH-INPUT-'].update('', background_color='white')
    window['-TAG-DESCRIPTION-'].update('')
    if values[event] == 'visiting site':
        tags_found = []
        save_action_buttons.enable_save_buttons(window)

    if values[event] == 'filling input':
        if values['-LOGGED-IN-']:
            tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                       password_value, login_path, tag='input', domain=domain)
        else:
            tags_found = site_info.get_tag_anonymous(site, tag='input')
    elif values[event] == 'clicking button':
        if values['-LOGGED-IN-']:
            tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                       password_value, login_path, tag='button', domain=domain)
        else:
            tags_found = site_info.get_tag_anonymous(site, tag='button')
    elif values[event] == 'clicking link':
        if values['-LOGGED-IN-']:
            tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                       password_value, login_path, tag='a', domain=domain)
        else:
            tags_found = site_info.get_tag_anonymous(site, tag='a')
    current_tags.clear()
    current_tags.extend(tags_found)
    listed = list(map(lambda obj: obj.format_for_listbox_with_available_actions(), tags_found))
    window['-TAG-LIST-'].update(listed)
