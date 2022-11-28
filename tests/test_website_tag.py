from models.website_tag import WebsiteTag
from collections import namedtuple


def test_website_tag():
    Attribute = namedtuple('Attribute', ('attrs', 'text'))
    attribute = Attribute(attrs={'id': 'less go'}, text='cos')
    web = WebsiteTag(whole_html=attribute, type_of_tag='element')
    assert web.attributes_to_html() == "//element[@id='less go']"
