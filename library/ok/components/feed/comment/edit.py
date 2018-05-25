from library.ok.components.widget import Widget


class EditButton(Widget):
    EDIT_BUTTON = '{}/li[2]'.format(Widget.WIDGET_LIST)

    def click(self):
        self.driver.find_element_by_xpath(self.EDIT_BUTTON).click()
        return self
