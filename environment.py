from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def before_feature(context, feature):
    headless = False
    options = Options()

    if context.config.userdata.get("headless"):
        headless = True
    if headless:
        options.headless = headless
    profile = webdriver.Firefox(options=options)

    context.driver = profile


def after_feature(context, feature):
    context.driver.quit()
