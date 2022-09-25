from scenario_helper.scenario import Scenario


def test_get_as_string():
    scenario = Scenario()

    text_given = "something given"
    text_when = "something when"
    text_then = "something then"
    scenario.set_given(text_given, 0)
    scenario.set_when(text_when, 0)
    scenario.set_then(text_then, 0)

    final_output = scenario.get_as_string()
    testing_text = f"\tScenario: something\n" \
                   f"\t\tGiven {text_given}\n" \
                   f"\t\tWhen {text_when}\n" \
                   f"\t\tThen {text_then}\n"
    assert testing_text == final_output


def test_convert_array_to_string():
    array_with_elements = ["something", "anything"]
    prefix = "yas"
    scenario = Scenario()
    final_string = scenario.convert_array_to_string(array_with_elements, prefix)

    expected_output = f"\t\t{prefix} {array_with_elements[0]}\n\t\tAnd {array_with_elements[1]}\n"

    assert final_string == expected_output
