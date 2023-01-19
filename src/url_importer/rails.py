from configparser import ConfigParser
from sqlite.database import save_urls
import subprocess


def import_urls():
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    project_path = config.get('main', 'project_path')

    command = 'rails routes -g=GET'

    project_name = 'Rails'

    if not _command_validity(cwd=project_path, command=command):
        print(f"{project_name} Project? No")
        return False

    print(f"{project_name} Project? Yes")

    urls = _execute_command(command, cwd=project_path)

    save_urls(urls)

    return True



def _command_validity(cwd, command):
    process = subprocess.Popen(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait(timeout=10)

    if process.returncode != 0:
        return False
    return True


def _execute_command(command, cwd):
    urls = []
    format_string = '(.:format)'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd)
    out, err = p.communicate()

    # starting from second position, because there are headers in this command
    for word in out.split('\n'.encode())[1:]:
        if len(word) > 0:
            checked_line = word.split()[2].decode()
            urls.append(checked_line.replace(format_string, ""))
    return urls
