from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion


class CustomCompleter(Completer):

    def array_to_hash(self, _list):
        for element in _list:
            self.data_dict[element] = element

    def __init__(self, collection):
        self.data_dict = {}
        self.array_to_hash(collection)
        self.data_list = collection

    def get_completions(self, document, complete_event):
        matches = [name for name in self.data_dict.keys() if document.text.lower() in name.lower()]
        for m in matches:
            yield Completion(self.data_dict[m], start_position=-len(document.text_before_cursor), display=m)

    def input(self, prefix, info_text):
        return prompt(f'{info_text} \n{prefix}: ', completer=self)
