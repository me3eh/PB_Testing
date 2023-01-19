from services.helper_methods import get_full_url


def insert_current_domain(window):
    current_domain = window['-DOMAIN-'].get()
    window['-HELPER-INPUT-'].update(current_domain)


def insert_current_domain_with_endpoint(window):
    current_domain = window['-DOMAIN-'].get()
    current_endpoint = window['-LAST-SITE-'].get()
    full_url = get_full_url(current_domain, current_endpoint)
    window['-HELPER-INPUT-'].update(full_url)
