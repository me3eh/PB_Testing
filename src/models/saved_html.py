class SavedHtml:
    def __init__(self, link, username, password, html):
        self.link = link
        self.username = username
        self.password = password
        self.html = html

    def to_string(self):
        return f'{self.link} with username:{self.username} and password: {self.password}'
