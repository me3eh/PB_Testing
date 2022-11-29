class WebsiteTag:
    def __init__(self, whole_html=None, bdd_attribute='Given', value_for_bdd=None, attribute=None, type_of_tag=None,
                 this_is_saved_action=False):
        self.id = None
        self.css_class = None
        self.attrs = None
        self.text = None
        self.type_of_tag = type_of_tag
        self.xpath = None
        self.whole_html = None
        self.this_is_saved_action = this_is_saved_action

        if whole_html is not None:
            self.attrs = whole_html.attrs
            self.id = self.attrs['id'] if 'id' in self.attrs else None
            self.css_class = ' '.join(self.attrs['class']) if 'class' in self.attrs else None
            self.text = whole_html.text if whole_html.text != '' else None
            self.whole_html = whole_html
            self.xpath = self.attributes_to_html()
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
        if self.id is not None:
            return f"id = {self.id} "
        return ""

    def _css_class(self):
        if self.css_class is not None:
            return f"css_class='{self.css_class}' "
        return ""

    def _text_inside(self):
        if self.text is not None:
            return f"text = {self.text}"
        return ""

    def attributes_to_html(self):
        full_xpath = f"//{self.type_of_tag}"
        if self.attrs is not None and len(self.attrs) > 0:
            # full_xpath = f"//{self.type_of_tag}"
            for index, a in enumerate(self.attrs.items()):
                if index != 0:
                    full_xpath += ' and '
                else:
                    full_xpath += '['

                if type(a[1]) == list:
                    attribute_in_string = ' '.join(a[1])
                else:
                    attribute_in_string = a[1]

                full_xpath += f"@{a[0]}={repr(attribute_in_string)}"
            full_xpath += ']'
        return full_xpath

    def get_attribute_from_gui(self):
        if self.value_for_bdd in ['clicking button', 'clicking link', 'clicking input', 'clicking checkbox',
                                  'clicking radio button'] or self.this_is_saved_action is True:
            return ''
        elif self.value_for_bdd in ['visiting site']:
            return f' with url={self.attribute}'
        elif self.value_for_bdd in ['waiting for amount of seconds']:
            return f' {self.attribute} seconds'
        elif self.value_for_bdd in ['assert title of site', 'assert url of site']:
            return f' is {self.attribute}'
        return f' with text={self.attribute}'

    def get_command(self):
        if self.value_for_bdd == 'visiting site':
            return f'{self.bdd_attribute} visiting site {self.attribute}'
        elif self.value_for_bdd == 'filling input':
            return f'{self.bdd_attribute} filling input with xpath {self.xpath} with text {self.attribute}'
        elif self.value_for_bdd in ['clicking button', 'clicking link', 'clicking input', 'clicking checkbox',
                                    'clicking radio button']:
            return f'{self.bdd_attribute} clicking on element with xpath {self.xpath}'
        elif self.value_for_bdd == 'waiting for amount of seconds':
            return f'{self.bdd_attribute} waiting for amount of seconds {self.attribute}'
        elif self.value_for_bdd == 'selecting option from select':
            return f'{self.bdd_attribute} selecting option {self.attribute} from select with xpath {self.xpath}'
        elif self.value_for_bdd == 'assert title of site':
            return f'{self.bdd_attribute} it should have a title {self.attribute}'
        elif self.value_for_bdd == 'assert url of site':
            return f'{self.bdd_attribute} it should have an url {self.attribute}'
        elif self.value_for_bdd == 'assert input is disabled':
            return f'{self.bdd_attribute} input with xpath {self.xpath} should be disabled'
        elif self.value_for_bdd == 'assert input is not visible':
            return f'{self.bdd_attribute} input with xpath {self.xpath} should be not visible'
        elif self.value_for_bdd == 'assert input is visible':
            return f'{self.bdd_attribute} input with xpath {self.xpath} should be visible'
        elif self.this_is_saved_action is True:
            return f'{self.bdd_attribute} {self.value_for_bdd}'
        elif self.value_for_bdd == 'assert element has certain text':
            return f'{self.bdd_attribute} element with xpath {self.xpath} should have text {self.attribute}'

    def format_for_listbox_with_available_actions(self):
        return f"<{self.type_of_tag} {self._id()}{self.attrs}{self._text_inside()}>"

    def format_for_todo_listbox(self):
        return f"{self.bdd_attribute} {self.value_for_bdd}{self.get_attribute_from_gui()}"
