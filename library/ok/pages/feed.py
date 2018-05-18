from library.ok import OkPage
from library.ok.components.feed.feed_list import FeedList


class FeedPage(OkPage):
    PATH = '/feed'

    @property
    def feed_list(self):
        return FeedList(self.driver)
