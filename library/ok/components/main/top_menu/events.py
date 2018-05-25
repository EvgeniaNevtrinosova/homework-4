from library.selenium import Component


class EventsPopup(Component):
    EVENTS_MENU_ITEM = '//span[@id="HeaderTopNewFeedbackInToolbar"]'
    EVENT = '//div[@id="hook_Block_FeedbackLayerContent"]/div[@class="loader-container"]' \
            '/div[@class="js-feedback-list"]/div'

    def open(self):
        self.driver.find_element_by_xpath(self.EVENTS_MENU_ITEM).click()
        return self

    @property
    def events(self):
        return [Event(event) for event in self.driver.find_elements_by_xpath(self.EVENT)]


class Event(Component):
    AUTHOR = '/div/div[1]/div[5]/div[1]/span/span/span/a'
    COMMENT = '/div/div[1]/div[5]/div[2]'

    @property
    def author(self):
        return self.driver.find_element_by_xpath(self.AUTHOR).text

    @property
    def comment(self):
        return self.driver.find_element_by_xpath(self.COMMENT).text
