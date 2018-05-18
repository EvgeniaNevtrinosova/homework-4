from library.ok import OkPage
from library.ok.components.post import PostForm


class PostPage(OkPage):
    PATH = '/post'

    @property
    def post_form(self):
        return PostForm(self.driver)
