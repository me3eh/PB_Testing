from selenium import webdriver


def before_feature(context, feature):
    profile = webdriver.Firefox()

    # Install any addon for firefox. It will have ending xpi
    # profile.install_addon("ublock_origin-1.42.4-an+fx.xpi", temporary=True)

    context.driver = profile
    # context.driver.implicitly_wait(2)
    # context.driver.get("https://google.com")

def after_feature(context, feature):
    context.driver.quit()
