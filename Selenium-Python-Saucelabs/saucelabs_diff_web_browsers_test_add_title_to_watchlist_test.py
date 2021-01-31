import json
import time
import unittest
from selenium import webdriver


# The test contains scripts and dependencies for running UI automated Selenium tests on Sauce Labs using Python and Unittest.
# This test scenario is designed for a web app running against Windows 10 and the following browsers: Chrome, Edge, and Firefox.
# The description and steps you may find below.

# Description:
# As a user, I want to add 'Skyfall' title to my Watchlist on https://www.imdb.com/
# Steps:
# 1. Go to http://www.imdb.com and sign in with a personal Google account
# 2. Check that watchlist is empty (if not - raise an exception)
# 3. Select dropdown All
# 4. Search for Skyfall in Titles
# 5. Add it to a Watchlist
# 6. Go to a Watchlist and check the title was added
# 7. In the end, remove Skyfall from the Watchlist (this step is required as a clean up for executing on different browsers)

# Expected result: User added 'Skyfall' title to their Watchlist on https://www.imdb.com/


class IMDbAddTitleToWatchlistTestCase(unittest.TestCase):

    def setUp(self):

        # reading the sensitive data from JSON config file
        data = None

        with open("config.json") as json_data_file:
            data = json.load(json_data_file)

        self.imdbcreds = data['imdbcreds']
        saucecreds = data['saucecreds']

        sauceOptions = {
            'screenResolution': '1280x768',
            'seleniumVersion': '3.141.59',
            'build': 'Python + UnitTest',
            'name': 'Add a title to Watchlist',
            'username': saucecreds['username'],
            'accessKey': saucecreds['accessKey'],
            'maxDuration': 1800,
            'commandTimeout': 300,
            'idleTimeout': 1000
        }

        # Define browser and/or WebDriver capabilities such as
        # the browser name, browser version, platform name, platform version
        chromeOpts = {
            'platformName': 'Windows 10',
            'browserName': 'chrome',
            'browserVersion': 'latest',
            'sauce:options': sauceOptions
        }

        firefoxOpts = {
            'platformName': 'Windows 10',
            'browserName': 'firefox',
            'browserVersion': 'latest',
            'sauce:options': sauceOptions
        }

        edgeOpts = {
            'platformName': 'Windows 10',
            'browserName': 'MicrosoftEdge',
            'browserVersion': 'latest',
            'sauce:options': sauceOptions
        }

        self.capabilities = [edgeOpts, firefoxOpts, chromeOpts]

    def testCrossBrowser(self):

        # Create an instance of the driver
        for c in self.capabilities:
            browser = webdriver.Remote(
                command_executor='https://ondemand.saucelabs.com:443/wd/hub', desired_capabilities=c)
            testSignInTitleSearchAddToWatchlist(
                self.imdbcreds['email'], self.imdbcreds['password'], browser)


def testSignInTitleSearchAddToWatchlist(email, password, browser):

    browser.get('http://www.imdb.com')
    time.sleep(2)
    signin = browser.find_element_by_xpath(
        "//nav[@id='imdbHeader']/div[2]/div[6]/a/div")
    signin.click()
    time.sleep(1)

    sign_in_with_imdb = browser.find_element_by_xpath(
        "//div[@id='signin-options']/div/div/a/span[2]")
    sign_in_with_imdb.click()
    time.sleep(1)

    email_box = browser.find_element_by_xpath(
        "//input[@id='ap_email' and @name='email']")
    email_box.send_keys(email)
    time.sleep(1)

    pwd_box = browser.find_element_by_xpath(
        "//input[@id='ap_password' and @name='password']")
    pwd_box.send_keys(password)
    time.sleep(1)

    signin_button = browser.find_element_by_xpath(
        "//input[@id='signInSubmit']")
    signin_button.submit()
    time.sleep(1)

    watchlist_button = browser.find_element_by_xpath(
        "//nav[@id='imdbHeader']/div[2]/div[5]/a/div")
    watchlist_button.click()
    time.sleep(1)

# Check that Watchlist is empty
    try:
        browser.find_element_by_xpath(
            "//div[@class='empty-react-watchlist']")
    except:
        raise Exception('List is not empty!')
    time.sleep(2)

# Search for Skyfall
    dropdown = browser.find_element_by_xpath(
        "//label[@role='button' and @aria-label='All']")
    dropdown.click()
    time.sleep(2)

    menu_titles = browser.find_element_by_xpath(
        "//a[@role='menuitem' and @aria-label='Titles']")
    menu_titles.click()
    time.sleep(2)

    search_box = browser.find_element_by_xpath(
        "//input[@name='q' and @id='suggestion-search']")
    search_box.send_keys('Skyfall')
    search_box.submit()
    time.sleep(3)

    first_title = browser.find_element_by_xpath(
        "//table[@class='findList']/tbody/tr[1]/td[2]/a")
    first_title.click()
    time.sleep(2)

    add_to_watchlist_button = browser.find_element_by_xpath(
        "//div[@id='title-overview-widget']/div[1]/div[2]/div/div[2]/div[1]/div")
    add_to_watchlist_button.click()
    time.sleep(3)

    watchlist_button = browser.find_element_by_xpath(
        "//nav[@id='imdbHeader']/div[2]/div[5]/a/div")
    watchlist_button.click()
    time.sleep(2)

# Find element in Watchlist
    try:
        browser.find_element_by_xpath(
            "//div[@class='lister-list mode-detail']")
        browser.execute_script('sauce:job-result=passed')
    except:
        browser.execute_script('sauce:job-result=failed')
        raise Exception('List is not empty!')
    time.sleep(2)

# clean up
    remove_from_watchlist = browser.find_element_by_xpath(
        "//div[@id='page-1']/div/div/div[1]/div")
    remove_from_watchlist.click()
    time.sleep(2)

    browser.quit()


if __name__ == '__main__':
    unittest.main()
