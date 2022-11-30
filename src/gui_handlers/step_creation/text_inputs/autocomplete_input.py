from services.url_autocompletion import UrlAutocompletion

url_autocomplete = UrlAutocompletion()


def autocomplete(values, window, urls_from_project, layout_key):
    text = values[layout_key].lower()

    prediction_list = url_autocomplete.find_occurences(text_to_find=text, collection=urls_from_project)

    window[f'{layout_key}BOX-'].update(values=prediction_list)
    window[f'{layout_key}BOX-'].update(set_to_index=0)

    visibility = len(prediction_list) > 0
    window[f'{layout_key}BOX-CONTAINER-'].update(visible=visibility)
