from library.ok.components.main.top_menu.events import EventsPopup
from library.selenium import Component


class TopMenu(Component):
    @property
    def events_button(self):
        return EventsPopup(self.driver)

    # TODO: other buttons
