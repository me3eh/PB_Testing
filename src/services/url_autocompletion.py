previous_saved_text = ''
previous_saved_collection = []


def find_occurences(text_to_find, collection):
    global previous_saved_text
    global previous_saved_collection

    if previous_saved_text == text_to_find:
        return previous_saved_collection

    previous_saved_text = text_to_find

    if text_to_find:
        previous_saved_collection = [item for item in collection if text_to_find.lower() in item.lower()]

    return previous_saved_collection
