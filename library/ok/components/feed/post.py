from library.ok.components.widget import RepostButton, Comment, LikeButton, Widget
from library.selenium import Component


class Post(Component):
    SEEN = '{}/li[4]'.format(Widget.WIDGET_LIST)
    USERNAME = '//div[@class="feed_top"]//div[@class="feed_h"]//span/a'

    def __init__(self, driver, post):
        super(Post, self).__init__(driver)
        self.post = post
        self._find_elements()

    def _find_elements(self):
        self.username = self.post.find_element_by_xpath(self.USERNAME).text
        self.repost_button = RepostButton(self.post)
        self.comment_button = Comment(self.post)
        self.like_button = LikeButton(self.post)
        seen_indicator = self.post.find_elements_by_xpath(self.SEEN)
        self.seen = int(seen_indicator[0].text) if len(seen_indicator) > 0 else None

    def repost(self):
        self.repost_button.click().confirm()
        return self

    def comment(self, text):
        self.comment_button.click().add_comment(text).confirm()
        return self

    def like(self):
        self.like_button.like()
        return self
