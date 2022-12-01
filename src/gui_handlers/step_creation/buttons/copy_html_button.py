import pyperclip


def copy_html_to_clipboard(html_to_copy):
    pyperclip.copy(html_to_copy)


def copy_element_html_to_clipboard(window):
    element_html = window['-TAG-DESCRIPTION-'].get()
    pyperclip.copy(element_html)
