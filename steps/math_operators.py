from behave import *
from src.pb_testing import my_functions


@given('Number {first_number} and Number {second_number}')
def step(context, first_number, second_number):
    context.first_number = int(first_number)
    context.second_number = int(second_number)


@when('we add them')
def step(context):
    context.output = my_functions.adding_two_numbers(context.first_number, context.second_number)


@then('We will receive Number {expected_output}')
def step(context, expected_output):
    assert int(expected_output) == context.output
