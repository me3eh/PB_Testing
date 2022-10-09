import requests
from bs4 import BeautifulSoup


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


if __name__ == "__main__":

    url = 'http://yoush.co' + '/products/yoush'

    x = get_browser_attributes(url)
    print(list(x))
    print(x)
