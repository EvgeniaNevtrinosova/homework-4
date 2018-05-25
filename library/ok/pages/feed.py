from library.ok import OkPage
from library.ok.components.feed.feed_list import FeedList
from library.ok.components.post import PostForm


class FeedPage(OkPage):
    PATH = '/feed'
    POSTS = '//div[@class="feed-list"]/div[@class="feed-w"]'

    @property
    def feed_list(self):
        return FeedList(self.driver)

    @property
    def post_form(self):
        return PostForm(self.driver)

    def get_post_form_by_index(self, index):
        post = self.driver.find_elem
        return PostForm(post)

    def get_posts(self):
        return self.driver.find_elements_by_xpath(self.POSTS)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return self
