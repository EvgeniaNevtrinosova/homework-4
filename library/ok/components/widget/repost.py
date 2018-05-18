from library.ok.components.widget import Widget


class RepostButton(Widget):
    REPOST_BUTTON = '{}/li[2]'.format(Widget.WIDGET_LIST)
    REPOST_CONFIRM = '//a[@class="u-menu_li js-doNotHide"]'

    def click(self):
        self.driver.find_element_by_xpath(self.REPOST_BUTTON).click()
        return self

    def confirm(self):
        self.driver.find_element_by_xpath(self.REPOST_CONFIRM).click()
        return self
