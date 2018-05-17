from library.ok import LoggedInTestCase
from library.ok.pages import FeedPage


class RepostTestCase(LoggedInTestCase):
    def test_repost_topic(self):
        FeedPage(self.driver).open().repost_form.click().submit()
        self.driver.refresh()
        # TODO: Check if topic reposts
