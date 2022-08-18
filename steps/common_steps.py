from behave import *


# @given("visited page {page_url}")
# def step(context, page_url):
#     context.driver.get(f'https://{page_url}')
@given('visiting url {url}')
def step(context, url):
    context.driver.get(f'https://{url}')


@given("click on button with id {id}")
def step(context, id):


@then('it should have a title {text}')
def step(context, text):
    assert context.driver.title == text


@then("{page} Should Be Open")
def step(context, page):
    assert context.title == page


@given("logged as admin")
def step_impl(context):
    context.driver.get(context.url)
    LoginPage().username_input(context).send_keys("jar")
    LoginPage().password_input(context).send_keys("jarjarjar")
    LoginPage().login_submit_button(context).click()