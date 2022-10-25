import url_importer.shell_command as sc
from sqlite.database import save_urls


def import_urls():
    command = 'python3 manage.py show_urls'
    project_name = 'Django'

    if not sc.command_validity(command=command):
        print(f"{project_name} Project? No")
        return False

    print(f"{project_name} Project? Yes")

    urls = sc.execute_command_django(command)

    save_urls(urls)

    # print(urls)
    return True
