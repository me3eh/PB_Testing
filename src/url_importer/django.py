from sqlite.database import save_urls
from configparser import ConfigParser
import subprocess


def import_urls():
    config = ConfigParser()
    config.read('resources_for_testing/config.ini')
    project_path = config.get('main', 'project_path')

    command = 'python3 manage.py show_urls'
    project_name = 'Django'

    if not _command_validity(cwd=project_path, command=command):
        print(f"{project_name} Project? No")
        return False

    print(f"{project_name} Project? Yes")

    urls = _execute_command(command=command, cwd=project_path)
    save_urls(urls)

    return True


def _command_validity(cwd, command):
    process = subprocess.Popen(command, shell=True, env={'PYTHONPATH': cwd}, cwd=cwd,
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait(timeout=10)

    if process.returncode != 0:
        return False
    return True


def _execute_command(command, cwd):
    urls = []
    p = subprocess.Popen(command, shell=True, env={'PYTHONPATH': cwd}, cwd=cwd,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    for word in out.split('\n'.encode()):
        if len(word) > 0:
            url = word.split()[0].decode()
            urls.append(url)

    return urls
