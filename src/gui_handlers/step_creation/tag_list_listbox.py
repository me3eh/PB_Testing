import xpath_viewer_input

def pick_tag(window, current_tags, last_used_html):
    index = window['-TAG-LIST-'].get_indexes()
    if len(index) == 0:
        print("yups")
    else:
        if len(current_tags) != 0:
            selected_tag = current_tags[index[0]]
            window['-TAG-DESCRIPTION-'].update(selected_tag.whole_html.prettify())
            window['-XPATH-INPUT-'].update(selected_tag.xpath)
            xpath_viewer_input.check_if_xpath_unique(last_used_html=last_used_html, window=window)

