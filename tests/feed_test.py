from library.ok import LoggedInTestCase
from library.ok.pages import FeedPage


class PostTestCase(LoggedInTestCase):
    def test_scroll_main_page(self):
        feed_page = FeedPage(self.driver).open()
        old_posts = feed_page.get_posts()
        feed_page.scroll_down()
        new_posts = feed_page.get_posts()

        assert all(new_post == old_post for new_post, old_post in zip(new_posts, old_posts))
        self.assertGreater(len(new_posts), len(old_posts))

    def test_drop_post_from_feed(self):
        assert FeedPage(self.driver).open().feed_list[0].hide().is_deleted()

    def test_hide_one_group_posts(self):
        feed_form = FeedPage(self.driver).open()
        group_name = feed_form.post_form.hide_posts_of_one_group()
        self.assertNotIn(group_name, (post.group_name for post in feed_form.feed_list.posts))
        raise NotImplementedError()

    def test_open_one_post(self):
        raise NotImplementedError()

    def test_follow_group_find_post(self):
        raise NotImplementedError()

    def test_content_not_for_children(self):
        raise NotImplementedError()
