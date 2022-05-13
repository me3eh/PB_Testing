from behave import *
from core import adding


@given('Number {first_number} and Number {second_number}')
def step(context, first_number, second_number):
    context.first_number = int(first_number)
    context.second_number = int(second_number)


@then('We will have Number {final_output}')
def step(context, final_output):
    assert int(final_output) == adding.adding_2(context.first_number, context.second_number)
