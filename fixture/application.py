from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = WebDriver(firefox_binary=FirefoxBinary("/Applications/FirefoxESR.app/Contents/MacOS/firefox-bin"))
        elif browser == "ie":
            # IE is for tests on Windows
            self.wd = webdriver.Ie()
        elif browser == "chrome":
            self.wd = webdriver.Chrome(executable_path='/Users/Julia/Projects/BrowserDriver/chromedriver')
        elif browser == "opera":
            self.wd == webdriver.Opera(executable_path='/Users/Julia/Projects/BrowserDriver/operadriver')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
