from url_parameter_parser import django

def test_find_parameters_in_url_when_parameters_in_url():
    parameter = "<pp>"
    assert django.find_parameters_in_url(f"/lel/{parameter}") == [parameter]

def test_find_parameters_in_url_when_no_parameters():
    assert django.find_parameters_in_url("/") == []

def test_find_parameters_in_url_when_several_parameters_in_url():
    first_parameter = "<object_id>"
    second_parameter = "(Pside_something[0-9])"

    assert django.find_parameters_in_url(f"/ss/{first_parameter}/{second_parameter}") == [first_parameter,
                                                                                          second_parameter]

def test_check_if_parameter_with_proper_parameters():
    object_checking = "<c>"
    assert django.check_if_parameter(object_checking, "<", ">") == object_checking

def test_check_if_parameter_with_inproper_parameters():
    object_checking = "c>"
    assert django.check_if_parameter(object_checking, "<", ">") == None

def test_check_if_parameter_when_using_on_empty_string():
    assert django.check_if_parameter('', "<", ">") == None
