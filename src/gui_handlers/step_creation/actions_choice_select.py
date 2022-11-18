import save_action_buttons

def find_all_selections(window, values, event, site_info, current_tags):
    domain = window['-DOMAIN-'].get()
    username_field = window['-USERNAME-FIELD-'].get()
    username_value = window['-USERNAME-VALUE-'].get()
    password_field = window['-PASSWORD-FIELD-'].get()
    password_value = window['-PASSWORD-VALUE-'].get()
    login_path = window['-LOGIN-PATH-'].get()
    target_site = window['-LAST-SITE-'].get()

    if domain.endswith('/') and target_site.startswith('/'):
        site = domain + target_site[1:]
    else:
        site = domain + target_site

    window['-XPATH-INPUT-'].update('', background_color='white')
    window['-TAG-DESCRIPTION-'].update('')

    need_to_search_for_tags = True
    tags_found = []
    tag = None
    tag_attributes = None

    if values[event] in ['visiting site', 'waiting for amount of seconds']:
        tags_found = []
        save_action_buttons.enable_save_buttons(window)
        need_to_search_for_tags = False

    elif values[event] == 'filling input':
        tag = 'input'
        # if values['-LOGGED-IN-']:
        #     tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
        #                                              password_value, login_path, tag='input', domain=domain)
        # else:
        #     tags_found = site_info.get_tag_anonymous(site, tag='input')

    elif values[event] == 'clicking button':
        tag = 'button'
        # if values['-LOGGED-IN-']:
        #     tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
        #                                                password_value, login_path, tag='button', domain=domain)
        # else:
        #     tags_found = site_info.get_tag_anonymous(site, tag='button')
    elif values[event] == 'clicking link':
        tag = 'a'
        # if values['-LOGGED-IN-']:
        #     tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
        #                                                password_value, login_path, tag='a', domain=domain)
        # else:
        #     tags_found = site_info.get_tag_anonymous(site, tag='a')
    elif values[event] == 'attaching file to file input':
        tag = 'input'
        tag_attributes = {'type': 'file'}
        # if values['-LOGGED-IN-']:
        #     tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
        #                                              password_value, login_path, tag='input', domain=domain,
        #                                              tag_attributes={'type': 'file'})
        # else:
        #     tags_found = site_info.get_tag_anonymous(site, tag='input', tag_attributes={'type': 'file'})
    elif values[event] == 'selecting option from select':
        tag = 'select'
        # if values['-LOGGED-IN-']:
        #     tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
        #                                              password_value, login_path, tag='select', domain=domain)
        # else:
        #     tags_found = site_info.get_tag_anonymous(site, tag='select')

    if need_to_search_for_tags is True:
        if values['-LOGGED-IN-']:
            tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
                                                     password_value, login_path, domain=domain,
                                                     tag=tag, tag_attributes=tag_attributes)
        else:
            tags_found = site_info.get_tag_anonymous(site, tag=tag, tag_attributes=tag_attributes)


    current_tags.clear()
    current_tags.extend(tags_found)
    listed = list(map(lambda obj: obj.format_for_listbox_with_available_actions(), tags_found))
    window['-TAG-LIST-'].update(listed)

# def search_for_tags(site, username_field, username_value, password_field, password_value, login_path, domain, tag,
#                     tag_attributes, site_info, values):
#     tags_found = []
#     if values['-LOGGED-IN-']:
#         tags_found = site_info.get_tag_logged_in(site, username_field, username_value, password_field,
#                                                  password_value, login_path, domain=domain,
#                                                  tag=tag, tag_attributes=tag_attributes)
#     else:
#         tags_found = site_info.get_tag_anonymous(site, tag=tag, tag_attributes=tag_attributes)
#     return tags_found