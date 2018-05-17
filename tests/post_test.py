from library.ok.pages import PostPage
from library.ok import LoggedInTestCase


class PostTestCase(LoggedInTestCase):
    TEXT = 'lalalallalalalalaa'
    TEXT2 = ''

    def test_create_topic(self):
        PostPage(self.driver).open().post_form.add_text(self.TEXT).submit()
        # TODO: Check if new topic creates

    def test_create_empty_topic(self):
        post_page = PostPage(self.driver).open()
        assert not post_page.post_form.is_enabled()
