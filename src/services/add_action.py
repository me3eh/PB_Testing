from models.website_tag import WebsiteTag


def action_create(type_of_action,
                  input_for_action,
                  bdd_attribute,
                  selected_tag,
                  current_tags,
                  xpath):
    print("huhi")
    if type_of_action in ['visiting site', 'assert url of site',
                          'assert title of site', 'waiting for amount of seconds']:
        return WebsiteTag(value_for_bdd=type_of_action,
                          attribute=input_for_action,
                          bdd_attribute=bdd_attribute)

    if len(selected_tag) == 0:
        return None

    current_chosen = current_tags[selected_tag[0]]
    current_chosen.xpath = xpath
    current_chosen.value_for_bdd = type_of_action
    current_chosen.attribute = input_for_action
    return current_chosen
