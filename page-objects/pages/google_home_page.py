from pages.base_page import BasePage
from resources.locators import GoogleHomePageLocators

class GoogleHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('http://www.google.com.br')

    def search_info(self, video_text):
        self.enter_text(GoogleHomePageLocators.search_field, video_text)
        self.click(GoogleHomePageLocators.search_button)