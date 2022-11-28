import requests
from bs4 import BeautifulSoup
import mechanize
from models.website_tag import WebsiteTag
from models.saved_html import SavedHtml

saved_htmls_anonymous = {}
saved_htmls_logged_in = {}

last_used_html = ''

# def create_dictionaries(attributes):
#     dictionary_with_attributes = {}
#     array_with_attributes = {}
#
#     for attribute in attributes:
#         dictionary_with_attributes[attribute] = {}
#         array_with_attributes[attribute] = []
#     return dictionary_with_attributes, array_with_attributes


def get_saved_site_anonymous(site):
    global last_used_html
    print('zapisane strony', saved_htmls_anonymous.keys())
    if site in saved_htmls_anonymous:
        last_used_html = saved_htmls_anonymous[site]
        print("oddano zapisaną")
        return last_used_html, False

    try:
        reqs = requests.get(site)
    except requests.exceptions.ConnectionError:
        return "Oops!  That was no valid number.  Try again...", True

    soup = BeautifulSoup(reqs.text, features='lxml')
    saved_htmls_anonymous[site] = soup.prettify()
    last_used_html = saved_htmls_anonymous[site]
    print("oddano stronę, którą trzeba było wyszukać")
    return reqs.text, False


def get_saved_site_logged_in(site, username_field, username_value, password_field, password_value, login_path, domain):
    global last_used_html
    if site in saved_htmls_logged_in:
        htmls = saved_htmls_logged_in[site]
        for saved_html in htmls:
            if username_value == saved_html.username and password_value == saved_html.password:
                last_used_html = saved_html.html
                return last_used_html, False

    browser = mechanize.Browser()
    if domain.endswith('/') and login_path.startswith("/"):
        full_login_path = domain + login_path[1:]
    else:
        full_login_path = domain + login_path

    try:
        ad = browser.open(f"{full_login_path}")
    except:
        return 'Could not connect to server', True

    browser.select_form(nr=0)
    browser[username_field] = username_value
    browser[password_field] = password_value
    browser.submit()

    ad = browser.open(site)
    request_from_site = ad.read()
    soup = BeautifulSoup(request_from_site, features='lxml')
    html_from_site = soup.prettify()

    if site in saved_htmls_logged_in:
        saved_htmls_logged_in[site].append(SavedHtml(site, username_value, password_value, html_from_site))
    else:
        saved_htmls_logged_in[site] = [SavedHtml(site, username_value, password_value, html_from_site)]

    # print('czekansko', saved_htmls_logged_in)
    # print(saved_htmls_logged_in[site][0].html)
    # print(saved_htmls_logged_in[site][0].username)
    # print(saved_htmls_logged_in[site][0].password)
    last_used_html = html_from_site
    print("oddano stronę, którą trzeba było wyszukać")
    return request_from_site, False

def get_last_used_html():
    return last_used_html

# def get_browser_attributes(site):
#     html = get_saved_site(site)
#
#     soup = BeautifulSoup(html, features='lxml')
#     attributes = ['class', 'id', 'name']
#     dictionary_with_attributes, array_with_attributes = create_dictionaries(attributes)
#
#     for tag in soup.find_all():
#         for attribute in attributes:
#             found_attribute = tag.get(attribute)
#             if found_attribute is not None:
#                 if type(found_attribute) == list:
#                     found_attribute = ' '.join(found_attribute)
#                 if found_attribute not in dictionary_with_attributes[attribute]:
#                     array_with_attributes[attribute].append(found_attribute)
#                     dictionary_with_attributes[attribute][found_attribute] = True
#     return array_with_attributes


# def get_logged_browser_attributes(site, username_field, username_value, password_field,
#                                   password_value, login_path, domain):
#     br = mechanize.Browser()
#     if domain.endswith('/') and login_path.startswith("/"):
#         full_login_path = domain + login_path[1:]
#     else:
#         full_login_path = domain + login_path
#     ad = br.open(f"{full_login_path}")
#     br.select_form(nr=0)
#     br[username_field] = username_value
#     br[password_field] = password_value
#     br.submit()
#
#     ad = br.open(site)
#     return ad.read()


def get_tag(response, tag, tag_attributes=None):
    soup = BeautifulSoup(response, features='lxml')

    if tag_attributes is None:
        found_tags = soup.find_all(tag)
    elif tag_attributes is not None:
        found_tags = soup.find_all(tag, attrs=tag_attributes)
    elif tag is None:
        found_tags = soup.find_all()

    tags = []
    for new_tag in found_tags:
        tags.append(WebsiteTag(new_tag, type_of_tag=new_tag.name))

    return tags


def get_tag_logged_in(site, username_field, username_value, password_field, password_value, login_path, tag, domain,
                      tag_attributes=None):
    response, thrown_exception = get_saved_site_logged_in(site, username_field, username_value, password_field, password_value,
                                        login_path, domain)
    if thrown_exception is True:
        return response, thrown_exception

    return get_tag(response, tag=tag, tag_attributes=tag_attributes), thrown_exception


def get_tag_anonymous(site, tag, tag_attributes=None):
    html, thrown_exception = get_saved_site_anonymous(site)
    if thrown_exception is True:
        return html, thrown_exception
    tags = get_tag(html, tag=tag, tag_attributes=tag_attributes)

    return tags, thrown_exception


# def get_attributes_from_html(html):
#     soup = BeautifulSoup(html, features='lxml')
#
#     attributes = ['class', 'id', 'name']
#     dictionary_with_attributes, array_with_attributes = create_dictionaries(attributes)
#
#     for tag in soup.find_all():
#         for attribute in attributes:
#             found_attribute = tag.get(attribute)
#             if found_attribute is not None:
#                 if type(found_attribute) == list:
#                     found_attribute = ' '.join(found_attribute)
#                 if found_attribute not in dictionary_with_attributes[attribute]:
#                     array_with_attributes[attribute].append(found_attribute)
#                     dictionary_with_attributes[attribute][found_attribute] = True
#     return array_with_attributes
