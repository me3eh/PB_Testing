from autocompleter import CustomCompleter


class Actions:
    def __init__(self, text, parameter=None, collection_for_completer=None):
        self.text = text
        self.parameter = parameter
        self.collection_for_completer = collection_for_completer

    def output(self):
        if self.parameter is None:
            return self.text
        else:
            prefix = "value for " + self.parameter
            input_for_parameter = CustomCompleter(self.collection_for_completer).input(prefix=prefix)
            return self.text + input_for_parameter

    def information(self):
        return self.text

    def __str__(self):
        if self.parameter == None:
            return f"{self.text}"
        else:
            return f"{self.text} <{self.parameter}>"
