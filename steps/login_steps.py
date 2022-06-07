from behave import *
from help_in_browser import *
import time

@when("we press button with text {text}")
def step(context, text):

    context.driver.implicitly_wait(10)
    # time.sleep(5)

    help_in_browser = HelpInBrowser(context)
    help_in_browser.find_button_with_text(text).click()
