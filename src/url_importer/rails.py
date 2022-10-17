import url_importer.shell_command as sc

def import_urls():
    command = 'rails routes -g=GET'
    project_name = 'Rails'

    if not sc.command_validity(command=command):
        print(f"{project_name} Project? No")
        return False

    print(f"{project_name} Project? Yes")

    urls = sc.execute_command_rails(command)

    print(urls)
    return True
