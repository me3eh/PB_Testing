import lxml.html as PARSER


def get_number_of_match(html, xpath):
    if html is not None or html != '':
        root = PARSER.fromstring(html)

        exists = root.xpath(xpath)
        if exists:
            return exists, len(exists)
        else:
            return 0, 0
