import url_importer.shell_command as sc

def import_urls():
    command = 'rails routes'
    project_name = 'Rails'

    if not sc.validity_command(command=command, project_name=project_name):
        return False
    print(f"{project_name} Project? Yes")

    sc.execute_command_and_put_into_file_rails(command, column_read=0)

    return True
