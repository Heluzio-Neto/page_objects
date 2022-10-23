import unittest

from selenium.webdriver import Firefox

from pages.google_home_page import GoogleHomePage


class TestGoogleHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.home_page = GoogleHomePage(self.driver)

    def test_search_info(self):
        self.home_page.search_info("instituto flexpeak")
        resultado_obtido = self.home_page.get_title()
        self.assertIn('flexpeak', resultado_obtido)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()