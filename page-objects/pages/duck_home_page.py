from pages.base_page import BasePage
from resources.locators import DuckHomePageLocators

class DuckHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://duckduckgo.com/')

    def search_info(self, video_text):
        self.enter_text(DuckHomePageLocators.search_field, video_text)
        self.click(DuckHomePageLocators.search_button)