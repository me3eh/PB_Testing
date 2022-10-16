import requests
from bs4 import BeautifulSoup
import re
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

    br = mechanize.Browser()
    # br.add_proxy_password(user='lol', password="lailtu")
    ad = br.open("http://youshstg.myshopify.com/products")
    # follow second link with element text matching regular expression
    # response1 = br.follow_link(text_regex=r"cheese\s*shop", nr=1)
    print(br.title())
    # print(response1.geturl())
    # print(response1.info())  # headers
    # print(response1.read())  # body
    # c= br.forms()[0]
    # breakpoint()
    # print(br.forms())
    # for form in br.forms():
    #     print(form)
    # Browser passes through unknown attributes (including methods)
    # to the selected HTMLForm.
    # br.select_form(nr=0)
    # br['password'] = 'lailtu'
    # print(ad.read())
    # br['user'] = 'yikes'
    soup = BeautifulSoup(ad.read(), features='lxml')
    print(len(soup.find_all('form')))
    for tag in soup.find_all('input'):
        print(tag)
    for tag in soup.find_all('form'):
        print(tag)
    # br["cheeses"] = ["mozzarella", "caerphilly"]  # (the method here is __setitem__)
    # Submit current form.  Browser calls .close() on the current response on
    # navigation, so this closes response1
    # response2 = br.submit()
    # print(response2.read())
    # # print currently selected form (don't call .submit() on this, use br.submit())
    # print(br.form)
    #
    # response3 = br.back()  # back to cheese shop (same data as response1)
    # # the history mechanism returns cached response objects
    # # we can still use the response, even though it was .close()d
    # response3.get_data()  # like .seek(0) followed by .read()
    # response4 = br.reload()  # fetches from server
    #
    # for form in br.forms():
    #     print(form)
    # # .links() optionally accepts the keyword args of .follow_/.find_link()
    # for link in br.links(url_regex="python.org"):
    #     print(link)
    #     br.follow_link(link)  # takes EITHER Link instance OR keyword args
    #     br.back()
if __name__ == "__main__":

    url = 'http://youshstg.myshopify.com' + '/products/yoush'

    x = get_logged_browser_attributes(url)
    # print(list(x))
    # print(x)
