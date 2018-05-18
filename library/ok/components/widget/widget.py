from library.selenium import Component


class Widget(Component):
    WIDGET_LIST = '//ul[@class="widget-list"]'
    NAME = '//span[@class="widget_tx"]'
    COUNTER = '//span[@class="widget_count"]'

    @property
    def name(self):
        return self.driver.find_element_by_xpath(self.NAME).text

    @property
    def counter(self):
        return int(self.driver.find_element_by_xpath(self.COUNTER).text)
