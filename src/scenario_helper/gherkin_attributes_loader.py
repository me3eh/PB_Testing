import os
import re


def load_gherkin_attributes():
    steps_files = os.listdir("steps")

    given, when, then = [], [], []

    for files in steps_files:
        with open(f'steps/{files}', 'r') as f:
            file_inside = f.read()

            given.append(re.findall("(?<=\@given\()(.*?)(?=\))", file_inside))
            when.append(re.findall("(?<=\@when\()(.*?)(?=\))", file_inside))
            then.append(re.findall("(?<=\@then\()(.*?)(?=\))", file_inside))
    return given, when, then
