from autocompleter import CustomCompleter
from file_helper import read_from_file


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
            input_for_parameter = CustomCompleter(self.get_collection()).input(prefix=prefix, info_text=self.text)
            return self.text + input_for_parameter

    def get_collection(self):
        if self.collection_for_completer is None:
            return read_from_file("resources_for_testing/"+self.parameter+".txt")
        else:
            return self.collection_for_completer

    def __str__(self):
        if self.parameter is None:
            return f"{self.text}"
        else:
            return f"{self.text} <{self.parameter}>"
