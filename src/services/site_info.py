import requests
from bs4 import BeautifulSoup
import mechanize
from models.website_tag import WebsiteTag
from models.saved_html import SavedHtml


class SiteInfo:
    def __init__(self):
        self.saved_htmls_anonymous = {}
        self.saved_htmls_logged_in = {}
        self.last_used_html = ''

    def get_saved_site_anonymous(self, site):
        if site in self.saved_htmls_anonymous:
            self.last_used_html = self.saved_htmls_anonymous[site]
            print("oddano zapisaną")
            return self.last_used_html, False

        try:
            reqs = requests.get(site)
        except requests.exceptions.ConnectionError:
            return "Oops!  That was no valid number.  Try again...", True

        soup = BeautifulSoup(reqs.text, features='lxml')
        self.saved_htmls_anonymous[site] = soup.prettify()
        self.last_used_html = self.saved_htmls_anonymous[site]
        print("oddano stronę, którą trzeba było wyszukać")
        return reqs.text, False


    def get_saved_site_logged_in(self, site, username_field, username_value, password_field, password_value, login_path, domain):
        # global last_used_html
        if site in self.saved_htmls_logged_in:
            htmls = self.saved_htmls_logged_in[site]
            for saved_html in htmls:
                if username_value == saved_html.username and password_value == saved_html.password:
                    self.last_used_html = saved_html.html
                    return self.last_used_html, False

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

        if site in self.saved_htmls_logged_in:
            self.saved_htmls_logged_in[site].append(SavedHtml(site, username_value, password_value, html_from_site))
        else:
            self.saved_htmls_logged_in[site] = [SavedHtml(site, username_value, password_value, html_from_site)]

        self.last_used_html = html_from_site
        print("oddano stronę, którą trzeba było wyszukać")
        return request_from_site, False

    def get_last_used_html(self):
        return self.last_used_html

    def get_tag(self, response, tag, tag_attributes=None):
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

    def get_tag_logged_in(self, site, username_field, username_value, password_field, password_value, login_path, tag,
                          domain, tag_attributes=None):
        response, thrown_exception = self.get_saved_site_logged_in(site, username_field, username_value, password_field,
                                                                   password_value, login_path, domain)
        if thrown_exception is True:
            return response, thrown_exception

        return self.get_tag(response, tag=tag, tag_attributes=tag_attributes), thrown_exception

    def get_tag_anonymous(self, site, tag, tag_attributes=None):
        html, thrown_exception = self.get_saved_site_anonymous(site)
        if thrown_exception is True:
            return html, thrown_exception
        tags = self.get_tag(html, tag=tag, tag_attributes=tag_attributes)

        return tags, thrown_exception
