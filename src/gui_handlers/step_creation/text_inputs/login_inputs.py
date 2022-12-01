def disabling(window, value_for_disabling):
    components_to_switch_disable = ['-USERNAME-FIELD-', '-USERNAME-VALUE-', '-PASSWORD-FIELD-', '-PASSWORD-VALUE-',
                                    '-LOGIN-PATH-']
    for key in components_to_switch_disable:
        window[key].update(disabled=value_for_disabling)
