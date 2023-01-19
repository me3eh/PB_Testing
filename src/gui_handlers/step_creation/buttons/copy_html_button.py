import pyperclip
import PySimpleGUI as sg
from shared_info.constants import OK_PNG


def copy_html_to_clipboard(html_to_copy):
    pyperclip.copy(html_to_copy)
    sg.popup_notify('Copied to clipboard html of site', icon=OK_PNG, title='Copied')


def copy_element_html_to_clipboard(window):
    window['-TAG-DESCRIPTION-'].Widget.selection_own()

    try:
        element_html_selected = window['-TAG-DESCRIPTION-'].Widget.selection_get()
    except sg.tk.TclError:
        element_html_selected = window['-TAG-DESCRIPTION-'].get()

    print(element_html_selected)
    pyperclip.copy(element_html_selected)
    sg.popup_notify('Copied to clipboard html of element', icon=OK_PNG, title='Copied')
