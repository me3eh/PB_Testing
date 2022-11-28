from behave import *
# from selenium import webdriver
import time

# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def css_format(class_name):
    return class_name.replace(" ", '.')


@given('visiting url {url}')
@when('visiting url {url}')
@given('visiting site {url}')
@when('visiting site {url}')
def step(context, url):
    if "https://" in url or 'http://' in url:
        context.driver.get(url)
    else:
        context.driver.get(f'https://{url}')



# @given("clicking on element with css class {css_classes}")
# @when("clicking on element with css class {css_classes}")
# def step(context, css_classes):
#     context.driver.find_element_by_class_name(css_format(css_classes)).click()
#
#
# @given('filling input with id {element_id} text {text}')
# @when('filling input with id {element_id} text {text}')
# def step(context, element_id, text):
#     context.driver.find_element(value=element_id).send_keys(text)

@given('filling input with xpath {xpath} with text {text}')
@when('filling input with xpath {xpath} with text {text}')
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

# @given('click on checkbox option')

# @when('sleep {time}')
# def step(context, time):
#     time.sleep(time)

# @given('filling input with name {element_name} text {text}')
# @when('filling input with name {element_name} text {text}')
# def step(context, element_name, text):
#     input_tag = context.driver.find_element(by=By.NAME, value=element_name)
#     input_tag.send_keys(text)


# @given('clicking submit button')
# @when('clicking submit button')
# def step(context):
#     context.driver.find_element_by_xpath("//button[@type='submit']").click()


# @given("clicking on element with id {element_id}")
# @when("clicking on element with id {element_id}")
# def step(context, element_id):
#     context.driver.find_element(value=element_id).click()


# @given('clicking on element with link {link} inside')
# @when('clicking on element with link {link} inside')
# def step(context, link):
#     WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"a[href*='{link}']"))).click()


@given('clicking on element with xpath {xpath}')
@when('clicking on element with xpath {xpath}')
def step(context, xpath):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


# @given('clicking on link with link text {link_text}')
# @when('clicking on link with link text {link_text}')
# def step(context, link_text):
#     context.driver.find_element_by_link_text(link_text).click()


@then('it should have a title {text}')
def step(context, text):
    title = context.driver.title
    assert title == text, f"Current web title was: '{title}', it is expected to be '{text}'."


@then('it should have an url {url}')
def step(context, url):
    actual_url = context.driver.current_url
    expected_url = url
    assert actual_url == expected_url, f"Current web url was: '{actual_url}', it is expected to be '{expected_url}'."


# @then('element with id {element_id} should have text {text}')
# def step(context, element_id, text):
#     actual = context.driver.find_element(value=element_id).text
#     expected = text
#     assert actual == expected, \
#         f"Current text in element was: '{actual}', it is expected to be '{expected}'."


# @then('element with css classes {css_classes} should have text {text}')
# def step(context, css_classes, text):
#     expected = text
#     actual = context.driver.find_element_by_class_name(css_format(css_classes)).text
#     assert expected == actual, \
#         f"Current text in element was: '{actual}', it is expected to be '{expected}'."


@then('input with xpath {xpath} should be disabled')
def step(context, xpath):
    input_tag = context.driver.find_element(by=By.XPATH, value=xpath)
    assert not input_tag.is_enabled(), f"Current element with name:{xpath} was: enabled"


@then('element with xpath {xpath} should have text {text}')
def step(context, xpath, text):
    element = context.driver.find_element(by=By.XPATH, value=xpath)

    assert element.text == text, f"Current element with name:{xpath}"
# @then('element with id {element_id} should be disabled')
# def step(context, element_id):
#     element = context.driver.find_element(by=By.ID, value=element_id)
#     assert not element.is_enabled(), f"Current element with id:{element_id} was: enabled"


# @then('element with css classes {css_classes} should be disabled')
# def step(context, css_classes):
#     element = context.driver.find_element_by_class_name(css_format(css_classes)).text
#     assert not element.is_enabled(), f"Current element with id:{css_classes} was: enabled"


# @then('input with name {input_name} should be visible')
# def step(context, input_name):
#     input_tag = context.driver.find_element(by=By.NAME, value=input_name)
#     assert input_tag.is_displayed(), f"Current element with name:{input_name} was: enabled"


# @then('element with id {element_id} should be visible')
# def step(context, element_id):
#     element = context.driver.find_element(by=By.ID, value=element_id)
#     assert element.is_displayed(), f"Current element with id:{element_id} is not visible"


# @then('element with css classes {css_classes} should be visible')
# def step(context, css_classes):
#     element = context.driver.find_element_by_class_name(css_format(css_classes)).text
#     assert element.is_displayed(), f"Current element with id:{css_classes} is not visible"


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


# @then('element with css classes {css_classes} should not be visible')
# def step(context, css_classes):
#     element = context.driver.find_element_by_class_name(css_format(css_classes)).text
#     assert not element.is_displayed(), f"Current element with css_class:{css_classes} is: visible"

