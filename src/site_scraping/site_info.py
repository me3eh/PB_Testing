import requests
from bs4 import BeautifulSoup
import mechanize

def create_dictionaries(attributes):
    dictionary_with_attributes = {}
    array_with_attributes = {}

    for attribute in attributes:
        dictionary_with_attributes[attribute] = {}
        array_with_attributes[attribute] = []
    return dictionary_with_attributes, array_with_attributes


def get_browser_attributes(site):
    reqs = requests.get(site)

    soup = BeautifulSoup(reqs.text, features='lxml')

    attributes = ['class', 'id', 'name']
    dictionary_with_attributes, array_with_attributes = create_dictionaries(attributes)

    for tag in soup.find_all():
        for attribute in attributes:
            found_attribute = tag.get(attribute)
            if found_attribute is not None:
                if type(found_attribute) == list:
                    found_attribute = ' '.join(found_attribute)
                if found_attribute not in dictionary_with_attributes[attribute]:
                    array_with_attributes[attribute].append(found_attribute)
                    dictionary_with_attributes[attribute][found_attribute] = True
    return array_with_attributes

def get_logged_browser_attributes(site):
    username_field = "username"
    username_value = "jar"
    password_field = "password"
    password_value = "jarjarjar"
    login_path = "/login"
    br = mechanize.Browser()
    br.add_proxy_password("jar", "jarjarjar")

    ad = br.open(f"http://127.0.0.1:8000{login_path}")
    # print(br.title())
    br.select_form(nr=0)
    br[username_field] = username_value
    br[password_field] = password_value
    response2 = br.submit()
    ad = br.open(f"http://127.0.0.1:8000/admin/")
    # print(ad.read())
    a = get_attributes_from_html(html=ad.read())
    print(a)

def get_attributes_from_html(html):
    soup = BeautifulSoup(html, features='lxml')

    attributes = ['class', 'id', 'name']
    dictionary_with_attributes, array_with_attributes = create_dictionaries(attributes)

    for tag in soup.find_all():
        for attribute in attributes:
            found_attribute = tag.get(attribute)
            if found_attribute is not None:
                if type(found_attribute) == list:
                    found_attribute = ' '.join(found_attribute)
                if found_attribute not in dictionary_with_attributes[attribute]:
                    array_with_attributes[attribute].append(found_attribute)
                    dictionary_with_attributes[attribute][found_attribute] = True
    return array_with_attributes
if __name__ == "__main__":
    get_logged_browser_attributes('s')
    url = 'http://youshstg.myshopify.com' + '/products/yoush'

    # x = get_logged_browser_attributes(url)
