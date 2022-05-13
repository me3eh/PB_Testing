class HelpInBrowser:
    def __init__(self, context):
        self.context = context

    def find_by_id(self, style):
        return self.context.driver.find_element_by_id(style)

    def find_button_with_text(self, text):
        s = self.context.driver.find_element_by_xpath(f"//button[text()='{text}']")
        # print(s)
        # return s
    def find_something_with_text(self, text):
        s = self.context.driver.find_element_by_xpath(f"//*[contains(text()=, {text})]")
