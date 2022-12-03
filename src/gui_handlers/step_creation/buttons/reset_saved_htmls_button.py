import PySimpleGUI as sg


def reset(site_info_module):
    answer_from_popup = sg.popup_yes_no('Are you sure you want to erase saved sites htmls?', title="Are you sure?")
    if answer_from_popup == 'no':
        return

    site_info_module.clear_saved_htmls()
