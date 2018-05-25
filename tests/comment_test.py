import config
from library.ok.components.feed import Post
from library.ok.pages import FeedPage, PostPage, MainPage
from library.selenium import SeleniumTestCase


class CommentTestCase(SeleniumTestCase):
    POST_TEXT = 'bla bla bla'
    COMMENT_TEXT = 'he he he'
    EDITED_COMMENT_TEXT = 'be be be'

    def test_comment_in_events(self):
        login = config.get('LOGIN')
        login2 = config.get('LOGIN2')

        post_form = PostPage(self.driver).login2().open().post_form
        post_form.add_text(self.POST_TEXT).submit()

        posts = FeedPage(self.driver).login().open().feed_list.posts
        post = next((post for post in posts if post.username == login2), None)
        self.assertIsNotNone(post, 'Post, created user with nickname "{}" not found'.format(login2))

        post.comment(self.COMMENT_TEXT)

        event = next((event for event in
                      MainPage(self.driver).login2().top_menu.events_button.open().events
                      if event.AUTHOR == login), None)
        self.assertIsNotNone(event, 'Event about comment under post by "{}" not found'.format(login))
        self.assertEqual(event.comment, self.COMMENT_TEXT, 'Comment text is wrong')

    def test_comment_edit(self):
        login = config.get('LOGIN')

        PostPage(self.driver).login().open().post_form.add_text(self.POST_TEXT).submit()
        posts = FeedPage(self.driver).open().feed_list.posts
        post = next((post for post in posts if post.username == login), None)
        self.assertIsNotNone(post, 'Post, just now created by us not found')

        post.comment(self.COMMENT_TEXT)
        new_post = Post(self.driver, post)
        comment = next((comment for comment in new_post.comments if comment.author == login), None)
        self.assertIsNotNone(comment, 'Comment, just now created by us not found')

        comment.edit(self.EDITED_COMMENT_TEXT)
        assert comment.is_edited()
