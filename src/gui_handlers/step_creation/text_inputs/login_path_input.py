from services.url_autocompletion import UrlAutocompletion

url_autocomplete = UrlAutocompletion()


def autocomplete(values, window, urls_from_project):
    text = values['-LOGIN-PATH-'].lower()

    prediction_list = url_autocomplete.find_occurences(text_to_find=text, collection=urls_from_project)

    window['-LOGIN-PATH-BOX-'].update(values=prediction_list)
    window['-LOGIN-PATH-BOX-'].update(set_to_index=0)

    visibility = len(prediction_list) > 0
    window['-LOGIN-PATH-BOX-CONTAINER-'].update(visible=visibility)
