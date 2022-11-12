def pick_tag(window, current_tags):
    index = window['-TAG-LIST-'].get_indexes()
    if len(index) == 0:
        print("yups")
    else:
        if len(current_tags) != 0:
            selected_tag = current_tags[index[0]]
            window['-TAG-DESCRIPTION-'].update(selected_tag.whole_html.prettify())
            window['-XPATH-INPUT-'].update(selected_tag.xpath)
