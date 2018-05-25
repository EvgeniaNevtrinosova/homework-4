from library.ok.components.widget import Widget


class CommentButton(Widget):
    COMMENT = '{}/li[1]'.format(Widget.WIDGET_LIST)
    TEXT = '//div[@id="ok-e-d"]'
    SUBMIT = '//div[@id="ok-e-d_button"]'

    def click(self):
        self.driver.find_element_by_xpath(self.COMMENT).click()
        return self

    def add_comment(self, text):
        self.driver.find_element_by_xpath(self.TEXT).send_keys(text)
        return self

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        return self
