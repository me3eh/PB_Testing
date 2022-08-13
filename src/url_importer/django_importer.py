
import os
import subprocess

def call():
    url_check_command = 'python3 manage.py show_urls'

    process = subprocess.Popen(url_check_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process.wait()

    if process.returncode != 0:
        print("Django Project? No")
        return False

    stream = os.popen(url_check_command)

    with open("resources_for_testing/urls.txt", 'w') as file:
        for word in stream.readlines():
            urls = word.split()[0]
            file.write(urls)
            file.write("\n")
    print("Django Project? Yes")

    return True