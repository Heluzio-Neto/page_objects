import unittest

from selenium.webdriver import Firefox

from pages.duck_home_page import DuckHomePage

class TestDuckHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = Firefox()
        self.home_page = DuckHomePage(self.driver)

    def test_search_info(self):
        self.home_page.search_info("instituto sidia")
        resultado_obtido = self.home_page.get_title()
        self.assertIn('sidia', resultado_obtido)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()