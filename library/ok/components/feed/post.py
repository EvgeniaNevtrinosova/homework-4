from library.ok.components.feed.comment import Comment
from library.ok.components.widget import RepostButton, CommentButton, LikeButton, Widget
from library.selenium import Component


class Post(Component):
    SEEN = '{}/li[4]'.format(Widget.WIDGET_LIST)
    USERNAME = '//div[@class="feed_top"]//div[@class="feed_h"]//span/a'
    COMMENT = '//div[@class="disc-comments-w"]//*[contains(@class, "d_comment_w")]'
    SUCCESSFUL_DELETE = '//i[@class="tico_img ic ic_ok"]'
    HIDE_POST = '//a[@class="feed_close"]'
    CLASS_COUNTER = '//span[@class="widget_count js-count"]'
    GROUP_NAME = '//a[@class="group-link o"]'
    DELETE_POSTS_OF_GROUP_CHECKBOX = '//input[@class=irc hf_act"]'
    ACCEPT_DELETE = '//button[@class="button-pro form-actions_yes"]'

    def __init__(self, driver, post):
        super(Post, self).__init__(driver)
        self.post = post
        self._username = None
        self._repost_button = None
        self._comment_button = None
        self._like_button = None
        self._seen = None
        self._comments = None
        self._group_name = None

    def find_elements(self):
        self._username = self.username
        self._repost_button = self.repost_button
        self._comment_button = self.comment_button
        self._like_button = self.like_button
        self._seen = self.seen
        self._comments = self.comments
        self._group_name = self.group_name
        return self

    @property
    def username(self):
        return self._username if self._username else self.post.find_element_by_xpath(self.USERNAME).text

    @property
    def repost_button(self):
        return self._repost_button if self._repost_button else RepostButton(self.post)

    @property
    def comment_button(self):
        return self._comment_button if self._comment_button else CommentButton(self.post)

    @property
    def like_button(self):
        return self._like_button if self._like_button else LikeButton(self.post)

    @property
    def seen(self):
        seen_indicator = self.post.find_elements_by_xpath(self.SEEN)
        return self._seen if self._seen else (
            int(seen_indicator[0].text) if len(seen_indicator) > 0 and seen_indicator[0] != '' else 0)

    @property
    def comments(self):
        return self._comments if self._comments else (
            Comment(comment) for comment in self.post.find_elements_by_xpath(self.COMMENT))

    @property
    def group_name(self):
        return self._group_name if self._group_name else self.post.find_elements_by_xpath(self.GROUP_NAME)

    def repost(self):
        self.repost_button.click().confirm()
        return self

    def comment(self, text):
        self.comment_button.click().add_comment(text).submit()
        return self

    def like(self):
        self.like_button.like()
        return self

    def hide(self):
        self.driver.find_element_by_xpath(self.HIDE_POST).click()
        return self

    def hide_posts_of_one_group(self):
        group_name = self.driver.find_element_by_xpath(self.GROUP_NAME).text
        self.driver.find_element_by_xpath(self.HIDE_POST).click()
        self.driver.find_element_by_xpath(self.DELETE_POSTS_OF_GROUP_CHECKBOX).click()
        self.driver.find_element_by_xpath(self.ACCEPT_DELETE).click()
        return group_name

    def is_deleted(self):
        return len(self.driver.find_elements_by_xpath(self.SUCCESSFUL_DELETE)) > 0

    def get_amount_of_classes(self):
        return int(self.driver.find_element_by_xpath(self.CLASS_COUNTER).text)

    def class_click(self):
        self.driver.find_element_by_xpath(self.CLASS_COUNTER).click()
