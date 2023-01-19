from behave import *
# from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@given('visiting url {url}')
@when('visiting url {url}')
@given('visiting site {url}')
@when('visiting site {url}')
def step(context, url):
    if "https://" in url or 'http://' in url:
        context.driver.get(url)
    else:
        context.driver.get(f'https://{url}')


@given('filling input with xpath {xpath} with text {text}')
@when('filling input with xpath {xpath} with text {text}')
@given('attaching file input with xpath {xpath} with file {text}')
@when('attaching file input with xpath {xpath} with file {text}')
def step(context, xpath, text):
    context.driver.find_element(By.XPATH, xpath).send_keys(text)


@given('selecting option {text} from select with xpath {xpath}')
@when('selecting option {text} from select with xpath {xpath}')
def step(context, text, xpath):
    element = context.driver.find_element(By.XPATH, xpath)
    select = Select(element)
    select.select_by_visible_text(text)


@given('waiting for amount of seconds {time_amount}')
@when('waiting for amount of seconds {time_amount}')
def step(context, time_amount):
    time.sleep(int(time_amount))


@given('clicking on element with xpath {xpath}')
@when('clicking on element with xpath {xpath}')
def step(context, xpath):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


@then('it should have a title {text}')
def step(context, text):
    title = context.driver.title
    assert title == text, f"Current web title was: '{title}', it is expected to be '{text}'."


@then('it should have an url {url}')
def step(context, url):
    actual_url = context.driver.current_url
    expected_url = url
    assert actual_url == expected_url, f"Current web url was: '{actual_url}', it is expected to be '{expected_url}'."


@then('input with xpath {xpath} should be disabled')
def step(context, xpath):
    input_tag = context.driver.find_element(by=By.XPATH, value=xpath)
    assert not input_tag.is_enabled(), f"Current element with name:{xpath} was: enabled"


@then('element with xpath {xpath} should have text {text}')
def step(context, xpath, text):
    element = context.driver.find_element(by=By.XPATH, value=xpath)

    assert element.text == text


@then('element with xpath {xpath} contains text {text}')
def step(context, xpath, text):
    element = context.driver.find_element(by=By.XPATH, value=xpath)

    assert text in element.text


@then('input with name {input_name} should not be visible')
def step(context, input_name):
    element = context.driver.find_element(by=By.NAME, value=input_name)
    assert not element.is_displayed(), f"Current element with name:{input_name} is: visible"


@then('element with xpath {xpath} should not be visible')
def step(context, xpath):
    element = context.driver.find_element(by=By.XPATH, value=xpath)
    assert not element.is_displayed(), f"Current element with xpath:{xpath} is: visible"


@then('element with xpath {xpath} should be visible')
def step(context, xpath):
    element = context.driver.find_element(by=By.XPATH, value=xpath)
    assert element.is_displayed(), f"Current element with xpath:{xpath} is: not visible"
