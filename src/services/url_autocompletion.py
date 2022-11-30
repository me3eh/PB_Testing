previous_saved_text = ''
previous_saved_collection = []


class UrlAutocompletion:
    def __init__(self):
        self.previous_saved_text = ''
        self.previous_saved_collection = []

    def find_occurences(self, text_to_find, collection):
        if self.previous_saved_text == text_to_find:
            return self.previous_saved_collection

        self.previous_saved_text = text_to_find

        if text_to_find:
            self.previous_saved_collection = [item for item in collection if text_to_find.lower() in item.lower()]

        return self.previous_saved_collection
