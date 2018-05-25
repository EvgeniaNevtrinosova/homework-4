from library.ok import LoggedInTestCase
from library.ok.pages import FeedPage


class RepostTestCase(LoggedInTestCase):
    def test_repost_topic(self):
        next(FeedPage(self.driver).open().feed_list.posts).repost()
        self.driver.refresh()
        # TODO: Check if topic reposts
