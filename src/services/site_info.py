from bs4 import BeautifulSoup
import mechanize
from models.website_tag import WebsiteTag
from models.saved_html import SavedHtml
from services.helper_methods import get_full_url
import urllib


class SiteInfo:
    def __init__(self):
        self.saved_htmls_anonymous = {}
        self.saved_htmls_logged_in = {}
        self.last_used_html = ''

    def get_saved_site_anonymous(self, site):
        if site in self.saved_htmls_anonymous:
            self.last_used_html = self.saved_htmls_anonymous[site]

            return self.last_used_html, False

        browser = mechanize.Browser()
        try:
            ad = browser.open(site)
        except mechanize.HTTPError:
            return 'Could not connect to this url. Probably wrong endpoint or server is not up', True
        except mechanize._mechanize.BrowserStateError:
            return 'Could not connect to this url. Check if domain name checks outs :D', True


        response = ad.read()
        soup = BeautifulSoup(response, features='lxml')
        self.saved_htmls_anonymous[site] = soup.prettify()
        self.last_used_html = self.saved_htmls_anonymous[site]

        return response, False

    def get_saved_site_logged_in(self, site, username_field, username_value, password_field, password_value,
                                 login_path, domain):
        if site in self.saved_htmls_logged_in:
            htmls = self.saved_htmls_logged_in[site]
            for saved_html in htmls:
                if username_value == saved_html.username and password_value == saved_html.password:
                    self.last_used_html = saved_html.html
                    return self.last_used_html, False

        browser = mechanize.Browser()

        full_login_path = get_full_url(domain, login_path)

        try:
            ad = browser.open(f"{full_login_path}")
        except mechanize.HTTPError:
            return 'Could not connect to this url. Probably wrong endpoint or server is not up', True
        except mechanize._mechanize.BrowserStateError:
            return 'Could not connect to this url. Check if domain name checks outs :D', True

        browser.select_form(nr=0) #probably not a wise choice, but most of sites have only one form in login :D
        try:
            browser[username_field] = username_value
            browser[password_field] = password_value
            browser.submit()
        except mechanize._form_controls.ControlNotFoundError:
            return 'Could not use given credentials. Probably username input name or password input name is wrong', True
        except mechanize._mechanize.BrowserStateError:
            return 'Could not connect to this url. Check if domain name checks outs :D', True

        ad = browser.open(site)
        request_from_site = ad.read()
        soup = BeautifulSoup(request_from_site, features='lxml')
        html_from_site = soup.prettify()
        if site in self.saved_htmls_logged_in:
            self.saved_htmls_logged_in[site].append(SavedHtml(site, username_value, password_value, html_from_site))
        else:
            self.saved_htmls_logged_in[site] = [SavedHtml(site, username_value, password_value, html_from_site)]

        self.last_used_html = html_from_site

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

    def clear_saved_htmls(self):
        self.saved_htmls_anonymous.clear()
        self.saved_htmls_logged_in.clear()

    # def information_about_saved_sites(self):
    #     print('Saved sites, when user not logged in', list(self.saved_htmls_anonymous.keys()))
    #
    #     if len(self.saved_htmls_logged_in.values()) != 0:
    #         breakpoint()
    #         print('Saved sites, when user logged in',
    #               list(map(lambda obj: obj.to_string(), list(self.saved_htmls_logged_in.values()))),
    #               '\n')
    #     else:
    #         print('Saved sites, when user logged in', [], '\n')
