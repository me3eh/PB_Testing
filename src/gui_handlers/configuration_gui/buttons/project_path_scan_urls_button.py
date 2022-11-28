from url_importer import django, rails
from sqlite import database
ide_environments = [django, rails]


def scan_for_urls(window):
    for ide in ide_environments:
        if ide.import_urls() is True:
            break
    urls = database.retrieve_urls('original_urls')

    window['-SCANNED-URLS-'].update(values=urls)
    window['-USER-URLS-'].update(values=urls)
