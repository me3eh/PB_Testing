from behave import *
from help_in_browser import *
import time
@given('site {site}')
def step(context, site):
    context.driver.get(f'https://{site}')

@when('we visit {som}')
def step(context, som):
    help_in_browser = HelpInBrowser(context)

    context.driver.implicitly_wait(10)
    context.driver.get(f'https://{som}')
    # context.driver.implicitly_wait(2)

    # find_by_id(context, "key").send_keys("1")
    # help_in_browser.find_button_with_text("ZGADZAM SIĘ").click()
    # context.driver.find_element_by_xpath('//button[text()="Encode"]').click()

    # context.driver.implicitly_wait(10)

    # time.sleep(5)


@when("we press button with text {text}")
def step(context, text):

    context.driver.implicitly_wait(10)
    time.sleep(5)

    help_in_browser = HelpInBrowser(context)
    help_in_browser.find_something_with_text(text).click()



@then('it should have a title {text}')
def step(context, text):
    assert context.driver.title == text
