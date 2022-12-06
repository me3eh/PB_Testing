import lxml.html as PARSER


def get_number_of_match(html, xpath):
    if html is not None or html != '':
        root = PARSER.fromstring(html)

        try:
            exists = root.xpath(xpath)
        except Exception as e:
            print(type(e).__name__)
            return None, None

        if exists:
            return exists, len(exists)
        else:
            return 0, 0
