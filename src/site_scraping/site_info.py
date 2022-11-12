import requests
from bs4 import BeautifulSoup
import mechanize
from website_elements.website_tag import WebsiteTag

saved_htmls = {}
last_used_html = ''

def create_dictionaries(attributes):
    dictionary_with_attributes = {}
    array_with_attributes = {}

    for attribute in attributes:
        dictionary_with_attributes[attribute] = {}
        array_with_attributes[attribute] = []
    return dictionary_with_attributes, array_with_attributes


def get_saved_site(site):
    global last_used_html
    print('zapisane strony', saved_htmls.keys())
    if site in saved_htmls:
        last_used_html = saved_htmls[site]
        print("oddano zapisaną")
        return last_used_html

    reqs = requests.get(site)
    soup = BeautifulSoup(reqs.text, features='lxml')
    saved_htmls[site] = soup.prettify()
    last_used_html = saved_htmls[site]
    print("oddano stronę, którą trzeba było wyszukać")
    return reqs.text

def get_last_used_html():
    return last_used_html

def get_browser_attributes(site):
    html = get_saved_site(site)

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


def get_logged_browser_attributes(site, username_field, username_value, password_field, password_value, login_path, domain):
    br = mechanize.Browser()
    ad = br.open(f"{domain}{login_path}")
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
    html = get_saved_site(site)
    tags = get_tag(html, tag=tag)

    return tags


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
