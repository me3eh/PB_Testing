# import mechanicalsoup
# from bs4 import BeautifulSoup
#
# browser = mechanicalsoup.StatefulBrowser()
# browser.open("http://localhost:8000")
#
# browser.select_form('form[class="login-form"]')
# username = "jar"
# password = username*3
# browser["username"] = username
# browser["password"] = password
#
# # Uncomment to launch a real web browser on the current page.
# # browser.launch_browser()
# # Uncomment to display a summary of the filled-in form
# # browser.form.print_summary()
# response = browser.submit_selected()
#
# soup = BeautifulSoup(response.text, features="lxml")
# urls = []
# for link in soup.find_all():
#     if not link.get('id') == None:
#         print(link.get('id'))
from configparser import ConfigParser
config = ConfigParser()

config.read('resources_for_testing/config.ini')
# print(config.get('main', 'key1'))
config.add_section('main')
config.set('main', 'key1', 'value1')
config.set('main', 'key2', 'value2')
config.set('main', 'key3', 'value3')
#
with open('resources_for_testing/config.ini', 'w') as f:
    config.write(f)