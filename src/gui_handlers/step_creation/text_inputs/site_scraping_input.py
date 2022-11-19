from services import url_autocompletion


def autocomplete(values, window, urls_from_project):
    text = values['-LAST-SITE-'].lower()

    prediction_list = url_autocompletion.find_occurences(text_to_find=text, collection=urls_from_project)

    window['-LAST-SITE-BOX-'].update(values=prediction_list)
    window['-LAST-SITE-BOX-'].update(set_to_index=0)

    visibility = len(prediction_list) > 0
    window['-LAST-SITE-BOX-CONTAINER-'].update(visible=visibility)
