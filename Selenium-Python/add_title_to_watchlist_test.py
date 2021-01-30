import json
import time
import unittest
from selenium import webdriver


# Scenario:
# As a user, I want to add 'Skyfall' title to my Watchlist on https://www.imdb.com/

# 1. Go to http://www.imdb.com and sign in with a personal Google account
# 2. Check that watchlist is empty (if not - raise an exception)
# 3. Select dropdown All
# 4. Search for Skyfall in Titles
# 5. Add it to a Watchlist
# 6. Go to a Watchlist and check the title was added
# 7. In the end, remove Skyfall from the Watchlist

# Expected result: User added 'Skyfall' title to their Watchlist on https://www.imdb.com/


class IMDbAddTitleToWatchlistTestCase(unittest.TestCase):

    def setUp(self):

        data = None

        with open("config.json") as json_data_file:
            data = json.load(json_data_file)

        self.imdbcreds = data['imdbcreds']
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def testSignInTitleSearchAddToWatchlist(self):
        self.browser.get('http://www.imdb.com')
        time.sleep(2)
        signin = self.browser.find_element_by_xpath(
            "//nav[@id='imdbHeader']/div[2]/div[6]/a/div")
        signin.click()
        time.sleep(1)

        sign_in_with_imdb = self.browser.find_element_by_xpath(
            "//div[@id='signin-options']/div/div/a/span[2]")
        sign_in_with_imdb.click()
        time.sleep(1)

        email_box = self.browser.find_element_by_xpath(
            "//input[@id='ap_email' and @name='email']")
        email_box.send_keys(self.imdbcreds['email'])
        time.sleep(1)

        pwd_box = self.browser.find_element_by_xpath(
            "//input[@id='ap_password' and @name='password']")
        pwd_box.send_keys(self.imdbcreds['password'])
        time.sleep(1)

        signin_button = self.browser.find_element_by_xpath(
            "//input[@id='signInSubmit']")
        signin_button.submit()
        time.sleep(1)

        watchlist_button = self.browser.find_element_by_xpath(
            "//nav[@id='imdbHeader']/div[2]/div[5]/a/div")
        watchlist_button.click()
        time.sleep(1)

# start check that Watchlist is empty

        try:
            self.browser.find_element_by_xpath(
                "//div[@class='empty-react-watchlist']")
        except:
            raise Exception('List is not empty!')
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
        search_box.send_keys('Skyfall')
        search_box.submit()
        time.sleep(3)

        first_title = self.browser.find_element_by_xpath(
            "//table[@class='findList']/tbody/tr[1]/td[2]/a")
        first_title.click()
        time.sleep(2)

        add_to_watchlist_button = self.browser.find_element_by_xpath(
            "//div[@id='title-overview-widget']/div[1]/div[2]/div/div[2]/div[1]/div")
        add_to_watchlist_button.click()
        time.sleep(3)

        watchlist_button = self.browser.find_element_by_xpath(
            "//nav[@id='imdbHeader']/div[2]/div[5]/a/div")
        watchlist_button.click()
        time.sleep(2)

# find element in watchlist
        try:
            self.browser.find_element_by_xpath(
                "//div[@class='lister-list mode-detail']")
        except:
            raise Exception('List is not empty!')
        time.sleep(2)

# clean up
        remove_from_watchlist = self.browser.find_element_by_xpath(
            "//div[@id='page-1']/div/div/div[1]/div")
        remove_from_watchlist.click()
        time.sleep(2)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
