from behave import *


@given("visited page {page_url}")
def step(context, page_url):
    context.driver.get(f'https://{page_url}')


@when("in input {id} {text_written}")
def step(context, id, text_written):
    skip()

@when("Submitted Credentials")
def step(context, id, text_written):
    skip()



@then('it should have a title {text}')
def step(context, text):
    assert context.driver.title == text

@then("{page} Should Be Open")
def step(context, page):
    assert context.title == page