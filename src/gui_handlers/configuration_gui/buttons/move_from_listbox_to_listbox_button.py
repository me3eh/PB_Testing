from sqlite import database
import PySimpleGUI as sg


def move(window):
    checked_url = window['-SCANNED-URLS-'].get()
    if not checked_url:
        sg.popup("Not checked anything in scanned_urls section")
    else:
        urls = window['-USER-URLS-'].get_list_values()
        if checked_url[0] in urls:
            sg.popup("Url already exists")
        else:
            new_urls = urls + checked_url
            window['-USER-URLS-'].update(new_urls)
            database.add_url(checked_url[0])
