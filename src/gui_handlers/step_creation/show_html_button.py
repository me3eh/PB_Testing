import os


def show_html_in_external_app(html_to_show):
    with open("html_viewer.html", 'w') as f:
        f.write(html_to_show)
    os.system('code html_viewer.html')
