from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# profile = webdriver.Firefox()
# profile.
# profile.find_element


def css_format(class_name):
    return class_name.replace(" ", '.')


@given('visiting url {url}')
@when('visiting url {url}')
def step(context, url):
    if 'https://' or 'http://' in url:
        context.driver.get(f'{url}')
    else:
        context.driver.get(f'https://{url}')


@given("clicking on element with id {element_id}")
@when("clicking on element with id {element_id}")
def step(context, element_id):
    context.driver.find_element(value=element_id).click()


@given('clicking on element with link {link} inside')
@when('clicking on element with link {link} inside')
def step(context, link):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"a[href*='{link}']"))).click()


@given("clicking on element with css class {css_classes}")
@when("clicking on element with css class {css_classes}")
def step(context, css_classes):
    context.driver.find_element_by_class_name(css_format(css_classes)).click()


@given('filling input with id {element_id} text {text}')
@when('filling input with id {element_id} text {text}')
def step(context, element_id, text):
    context.driver.find_element(value=element_id).send_keys(text)


@given('clicking submit button')
@when('clicking submit button')
def step(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()


@given('clicking on link with link text {link_text}')
@when('clicking on link with link text {link_text}')
def step(context, link_text):
    context.driver.find_element_by_link_text(link_text).click()


@then('it should have a title {text}')
def step(context, text):
    title = context.driver.title
    assert title == text, f"Current web title was: '{title}', it is expected to be '{text}'." \
                          f"Probably problem with minus sign. Copy it and it should be fine"


@then('it should have an url {url}')
def step(context, url):
    actual_url = context.driver.current_url
    expected_url = url
    assert actual_url == expected_url, f"Current web url was: '{actual_url}', it is expected to be '{expected_url}'."


@then('element with id {element_id} should have text {text}')
def step(context, element_id, text):
    actual = context.driver.find_element(value=element_id).text
    expected = text
    assert actual == expected, \
        f"Current text in element was: '{actual}', it is expected to be '{expected}'."


@then('element with css classes {css_classes} should have text {text}')
def step(context, css_classes, text):
    expected = text
    actual = context.driver.find_element_by_class_name(css_format(css_classes)).text
    assert expected == actual, \
        f"Current text in element was: '{actual}', it is expected to be '{expected}'."

