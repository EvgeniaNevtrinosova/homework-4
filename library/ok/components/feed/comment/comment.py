from library.ok.components.feed.comment import EditButton
from library.ok.components.widget import CommentButton
from library.selenium import Component


class Comment(Component):
    AUTHOR = '/div[@class="d_comment_w_center"]/div[@class="d_comment_right_w"]/div[@class="d_comment_owner_w"]/span[1]'
    EDITED_ICON = '//a[@title="Отлкактирон"]'

    @property
    def author(self):
        return self.driver.find_element_by_xpath(self.AUTHOR).text

    @property
    def edit_button(self):
        return EditButton(self.driver)

    def edit(self, new_text):
        self.edit_button.click()
        CommentButton(self.driver).add_comment(new_text).submit()
        return self

    def is_edited(self):
        return len(self.driver.find_elements_by_xpath(self.EDITED_ICON)) > 0
