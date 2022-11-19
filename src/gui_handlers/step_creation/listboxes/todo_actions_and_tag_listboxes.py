def only_one_selected(event, window):
    event_to_unselect = '-ACTION-LIST-' if event == '-TAG-LIST-' else '-TAG-LIST-'
    window[event_to_unselect].update(set_to_index=[])
