import time
import unittest
from selenium import webdriver

# Scenario:
# As a user, I can search for the title 'Titanic' on https://www.imdb.com/ and want to see the first title.

# Steps:
# 1. Go to https://www.imdb.com/
# 2. In a search drop-down select 'titles'
# 3. Type Titanic
# 4. Click on a first 'Titanic' title
# Expected result: User gets first title Titanic on https://www.imdb.com/


class IMDbTitanicSearchTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testTitleSearch(self):
        self.browser.get('http://www.imdb.com')
        time.sleep(2)
        dropdown = self.browser.find_element_by_xpath(
            "//label[@role='button' and @aria-label='All']")
        dropdown.click()
        time.sleep(2)
        menu_titles = self.browser.find_element_by_xpath(
            "//a[@role='menuitem' and @aria-label='Titles']")
        menu_titles.click()
        time.sleep(2)
        search_box = self.browser.find_element_by_xpath(
            "//input[@name='q' and @id='suggestion-search']")
        search_box.send_keys('Titanic')
        search_box.submit()
        time.sleep(2)

        first_title = self.browser.find_element_by_xpath(
            "//table[@class='findList']/tbody/tr[1]/td[2]/a")
        first_title.click()
        time.sleep(2)

        # Check that a selected title contains 'Titanic' in name
        self.browser.find_element_by_xpath(
            "//h1[contains(text(), '{0}')]".format('Titanic'))
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
