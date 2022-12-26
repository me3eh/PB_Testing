from models.website_tag import WebsiteTag
from shared_info.constants import ERROR_PNG
import PySimpleGUI as sg
import copy


def action_create(type_of_action,
                  input_for_action,
                  bdd_attribute,
                  selected_tag,
                  current_tags,
                  saved_action_selected,
                  saved_actions,
                  xpath,
                  last_site_saved):
    if type_of_action in ['visiting site', 'assert url of site',
                          'assert title of site', 'waiting for amount of seconds']:
        return WebsiteTag(value_for_bdd=type_of_action,
                          attribute=input_for_action,
                          bdd_attribute=bdd_attribute)
    if type_of_action == 'use saved actions':
        if len(saved_actions) <= 0:
            sg.popup_notify("Try to generate some first :D", icon=ERROR_PNG,
                            title='No available saved actions')
            return None
        action = saved_actions[saved_action_selected]
        return WebsiteTag(value_for_bdd=action.action_name,
                          attribute='',
                          bdd_attribute=action.bdd_attribute.title(),
                          this_is_saved_action=True)

    if len(selected_tag) == 0:
        return None
    current_chosen = copy.deepcopy(current_tags[selected_tag[0]])

    current_chosen.xpath = xpath
    current_chosen.value_for_bdd = type_of_action
    current_chosen.attribute = input_for_action
    current_chosen.bdd_attribute = bdd_attribute
    current_chosen.site_html = last_site_saved
    return current_chosen
