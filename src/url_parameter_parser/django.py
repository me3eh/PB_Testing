
def check_if_parameter(yep, first_symbol, last_symbol):
    if len(yep) == 0:
        return None

    if yep[0] == first_symbol and yep[-1] == last_symbol:
        return yep
    return None


def find_parameters_in_url(url):
    elements = url.split("/")
    parameters = []
    for element in elements:
        parameter = check_if_parameter(yep=element, first_symbol="<", last_symbol=">")
        if parameter is not None:
            parameters.append(parameter)

        parameter = check_if_parameter(yep=element, first_symbol="(", last_symbol=")")
        if parameter is not None:
            parameters.append(parameter)
    return parameters