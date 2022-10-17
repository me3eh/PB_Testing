import os
import re


def gherkin_prefix_regex(attribute):
    return f"(?<=\@{attribute}\([\"|\'])(.*?)(?=[\"|\']\))"


def load_gherkin_attributes():
    steps_files = os.listdir("steps")

    given, when, then = [], [], []

    for index, files in enumerate(steps_files):
        with open(f'steps/{files}', 'r') as f:
            file_inside = f.read()

            given += re.findall(gherkin_prefix_regex(attribute='given'), file_inside)
            when += re.findall(gherkin_prefix_regex(attribute='when'), file_inside)
            then += re.findall(gherkin_prefix_regex(attribute='then'), file_inside)

    return given, when, then
