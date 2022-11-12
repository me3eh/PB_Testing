import lxml.html as PARSER


def get_number_of_match(html, xpath):
    root = PARSER.fromstring(html)
    exists = root.xpath(xpath)
    if exists:
        return exists, len(exists)
        # print(etree.tostring(exists[0], pretty_print=True))
    else:
        return 0, 0
