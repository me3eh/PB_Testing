from behave import *


@given('haha2')
def step(context, xpath, text):
    context.driver.find_element(By.XPATH, xpath).send_keys(text)


#@given('haha')
# def step(context, xpath, text):
#    context.driver.find_element(By.XPATH, xpath).send_keys(text)