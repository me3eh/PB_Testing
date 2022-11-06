class WebsiteTag:
    def __init__(self, whole_html=None, bdd_attribute='Given', value_for_bdd=None, attribute=None, type_of_tag=None):
        self.id = None
        self.css_class = None
        self.attrs = None
        self.text = None
        self.type_of_tag = type_of_tag
        if whole_html != None:
            self.attrs = whole_html.attrs
            self.id = self.attrs['id'] if 'id' in self.attrs else None
            self.css_class = self.attrs['class'] if 'class' in self.attrs else None
            self.text = whole_html.text if whole_html.text != '' else None
            self.whole_html = whole_html
        self.bdd_attribute = bdd_attribute
        self.value_for_bdd = value_for_bdd
        self.attribute = attribute

    def set_whole_html(self, whole_html):
        self.attrs = whole_html.attrs
        self.id = self.attrs['id'] if 'id' in self.attrs else None
        self.css_class = self.attrs['class'] if 'class' in self.attrs else None
        self.text = whole_html.text if whole_html.text != '' else None
        self.whole_html = whole_html

    def _id(self):
        if self.id != None:
            return f"id = {self.id} "
        return ""

    def _css_class(self):
        if self.css_class != None:
            return f"css_class = {self.css_class} "
        return ""

    def _text_inside(self):
        if self.text != None:
            return f"text = {self.text}"
        return ""

    def attributes_to_html(self):
        print(self.attrs)
        if self.attrs != None and len(self.attrs) > 0:
            full_xpath = f"//{self.type_of_tag}"
            for index, a in enumerate(self.attrs.items()):
                if index != 0:
                    full_xpath += ' and '
                else:
                    full_xpath += '['
                if a[0] == 'class':
                    for index, class_attribute in enumerate(a[1]):
                        if index != 0:
                            full_xpath += ' and '
                        full_xpath += f"contains(@class, '{class_attribute}')"
                else:
                    full_xpath += f"@{a[0]}='{a[1]}'"
            full_xpath += ']'
            return full_xpath
        else:
            return ''

    def get_attribute_from_gui(self):
        if self.value_for_bdd == 'visiting site':
            return f' {self.attribute}'
        return f' with text {self.attribute}'

    def get_command(self):
        if self.value_for_bdd == 'visiting site':
            return f'{self.bdd_attribute} visiting site {self.attribute}'
        if self.value_for_bdd == 'filling input':
            return f'{self.bdd_attribute} filling input with xpath {self.attributes_to_html()} with text {self.attribute}'
        if self.value_for_bdd == 'clicking button':
            return f'{self.bdd_attribute} clicking on element with xpath {self.attributes_to_html()}'

    def format_for_listbox_with_available_actions(self):
        return f"<{self.type_of_tag} {self._id()}{self._css_class()}{self._text_inside()}>"

    def format_for_todo_listbox(self):
        return f"{self.bdd_attribute} {self.value_for_bdd}{self.get_attribute_from_gui()} {self.attributes_to_html()}"
