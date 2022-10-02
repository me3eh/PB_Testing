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

    # Install any addon for firefox. It will have ending xpi
    # profile.install_addon("ublock_origin-1.42.4-an+fx.xpi", temporary=True)

    context.driver = profile
    # context.driver.implicitly_wait(2)


def after_feature(context, feature):
    context.driver.quit()
