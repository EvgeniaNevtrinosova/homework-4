from library.ok.components.feed import Post
from library.selenium import Component


class FeedList(Component):
    FEED_LIST = '//div[@class="feed-list"]'
    POST = 'div[@class="feed-w"]'

    @property
    def posts(self):
        return [Post(self.driver, post) for post in
                self.driver.find_elements_by_xpath('{}/{}'.format(FeedList.FEED_LIST, self.POST))]
