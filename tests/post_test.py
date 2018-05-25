from library.ok.pages import PostPage, FeedPage
from library.ok import LoggedInTestCase


class PostTestCase(LoggedInTestCase):
    TEXT = 'lalalallalalalalaa'
    TEXT2 = ''
    SPACES = ' ' * 7

    def test_create_topic(self):
        PostPage(self.driver).open().post_form.add_text(self.TEXT).submit()
        # TODO: Check if new topic creates

    def test_create_empty_topic(self):
        post_page = PostPage(self.driver).open()
        assert not post_page.post_form.is_enabled()

    def test_repost_topic(self):
        FeedPage(self.driver).open().repost_form.click().submit()
        self.driver.refresh()
        # TODO: Check if topic reposts

    def test_create_comment(self):
        raise NotImplementedError()

    def test_class(self):
        feed_page = FeedPage(self.driver).open()
        old_classes = feed_page.get_amount_of_classes()
        feed_page.class_click()
        new_classes = feed_page.get_amount_of_classes()
        self.assertEquals(old_classes + 1, new_classes)

    def test_create_post_with_spaces(self):
        assert not PostPage(self.driver).open().post_form.add_text(self.SPACES).submit().is_enabled()

    def test_only_picture_repost(self):
        raise NotImplementedError()
