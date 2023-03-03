from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


class Utils:

    @staticmethod
    def options_chrome():
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("window-size=1920x1080")
        # Pass the argument 1 to allow and 2 to block
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        return options

    @staticmethod
    def options_firefox():
        options = FirefoxOptions()
        options.add_argument('--headless')
        options.set_preference("permissions.default.desktop-notification", 1)
        return options

    @staticmethod
    def capabilities_firefox():
        cap = DesiredCapabilities().FIREFOX
        set_cap = cap['marionette']
        return set_cap

    @staticmethod
    def capabilities_chrome():
        cap = DesiredCapabilities().CHROME
        set_cap = cap
        return set_cap



