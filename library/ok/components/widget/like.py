from library.ok.components.widget import Widget


class LikeButton(Widget):
    LIKE_BUTTON = '{}/li[2]'.format(Widget.WIDGET_LIST)

    def like(self):
        self.driver.find_element_by_xpath(self.LIKE_BUTTON).click()
        return self
