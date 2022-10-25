class WebsiteTag:
    def __init__(self, whole_html, type=None, input_name=None, id=None, css_class=None, value=None):
        self.input_name = input_name
        self.id = id
        self.css_class = css_class
        self.value = value
        self.whole_html = whole_html
        self.type = type

    def _input_name(self):
        if self.input_name != None:
            return f"name = {self.input_name} "
        return ""

    def _id(self):
        if self.id != None:
            return f"id = {self.id} "
        return ""

    def _css_class(self):
        if self.css_class != None:
            return f"css_class = {self.css_class} "
        return ""

    def _text_inside(self):
        if self.value != None:
            return f"text = {self.value}"
        return ""

    def __str__(self):
        return f"<input {self._input_name()}{self._id()}{self._css_class()}{self._text_inside()}>"
