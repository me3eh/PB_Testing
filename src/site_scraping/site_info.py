import requests
from bs4 import BeautifulSoup
from configparser import ConfigParser


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

    attributes = ['class', 'id']
    dictionary_with_attributes, array_with_attributes = create_dictionaries(attributes)

    for tag in soup.find_all('div'):
        for attribute in attributes:
            found_attribute = tag.get(attribute)
            if found_attribute is not None:
                if type(found_attribute) == list:
                    found_attribute = ' '.join(found_attribute)
                if found_attribute not in dictionary_with_attributes[attribute]:
                    array_with_attributes[attribute].append(found_attribute)
                    dictionary_with_attributes[attribute][found_attribute] = True
    return array_with_attributes


config = ConfigParser()
config.read('resources_for_testing/config.ini')

domain = config.get('main', 'domain')

url = domain + '/person/Magdalena+Wo%C5%BAniak-426878'

x = get_browser_attributes(url)
print(list(x))
print(x)
