import requests
from bs4 import BeautifulSoup
import mechanize
from website_elements.website_tag import WebsiteTag

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

def get_logged_browser_attributes(site, username_field, username_value, password_field, password_value, login_path):
    br = mechanize.Browser()
    ad = br.open(f"http://127.0.0.1:8000{login_path}")
    br.select_form(nr=0)
    br[username_field] = username_value
    br[password_field] = password_value
    br.submit()
    ad = br.open(site)
    return ad.read()

def get_tag(response, tag):
    soup = BeautifulSoup(response, features='lxml')
    inputs = soup.find_all(tag)
    tags = []
    for input in inputs:
        tags.append(WebsiteTag(input, type_of_tag=tag))
    return tags

def get_tag_logged_in(site, username_field, username_value, password_field, password_value, login_path, tag):
    response = get_logged_browser_attributes(site, username_field, username_value, password_field, password_value,
                                             login_path)
    return get_tag(response, tag=tag)

def get_tag_anonymous(site, tag):
    print("szukanie strny")
    reqs = requests.get(site)
    print("juz znaazlo")
    tags = get_tag(reqs.text, tag=tag)

    return tags

# def get_input_logged_in(site, username_field, username_value, password_field, password_value, login_path):
#     response = get_logged_browser_attributes(site, username_field, username_value, password_field, password_value,
#                                              login_path)
#     return get_inputs(response)

# def get_input_anonymous(site):
#     reqs = requests.get(site)
#
#     inputs = get_inputs(reqs.text)
#     # if len(inputs) >= 1:
#
#     # breakpoint()
#     return get_inputs(reqs.text)

# def get_buttons_logged_in(site, username_field, username_value, password_field, password_value, login_path):
#     response = get_logged_browser_attributes(site, username_field, username_value, password_field, password_value,
#                                              login_path)
#     return get_buttons(response)
#


# def get_buttons_anonymous(site):
#     reqs = requests.get(site)
#     return get_buttons(reqs.text)

# def get_links_logged_in(site, username_field, username_value, password_field, password_value, login_path):
#     response = get_logged_browser_attributes(site, username_field, username_value, password_field, password_value,
#                                              login_path)
#     return get_buttons(response)


# def get_links_anonymous(site):
#     reqs = requests.get(site)
#     return get_links(reqs.text)


# def get_inputs(response):
#     soup = BeautifulSoup(response, features='lxml')
#     inputs = soup.find_all("input")
#     tags = []
#     # print("inputs", inputs)
#     # print("ilosc inputow", len(inputs))
#     for input in inputs:
#         # css_class = input.attrs['class'] if 'class' in input.attrs else None
#         # ids = input.attrs['id'] if 'id' in input.attrs else None
#         tags.append(WebsiteTag(input))
#     return tags

# def get_buttons(response):
#     soup = BeautifulSoup(response, features='lxml')
#     buttons = soup.find_all("button")
#     tags = []
#     for button in buttons:
#         css_class = button.attrs['class'] if 'class' in button.attrs else None
#         ids = button.attrs['id'] if 'id' in button.attrs else None
#         tags.append(WebsiteTag(button))
#     # print('kekw', tags)
#     return tags

# def get_links(response):
#     soup = BeautifulSoup(response, features='lxml')
#     links = soup.find_all("a")
#     tags = []
#     for link in links:
#         print('class' in link.attrs)
#         css_class = link.attrs['class'] if 'class' in link.attrs else None
#         id = link.attrs['id'] if 'id' in link.attrs else None
#         tags.append(WebsiteTag(link))
#     return tags

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

