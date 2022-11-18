import lxml.html as PARSER
import requests

def get_number_of_match(html, xpath):
    if html is not None:
        root = PARSER.fromstring(html)
        exists = root.xpath(xpath)
        if exists:
            return exists, len(exists)
        else:
            return 0, 0

# c = requests.get('http://localhost:3000/da')
# s = get_number_of_match(c.text, "//a[@href='#' and @onclick='return toggleEnvDump()']")
# print(s)