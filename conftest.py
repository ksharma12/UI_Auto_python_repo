import configparser
import allure
import os
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Utils.Common_Operations import Common_Operations

# ini_file_read_write = IniFile_Reader_Writer_Operations(r'../conf.ini')  # ../conf.ini
# browser = ini_file_read_write.get_multiple_values_from_key_in_section("BASIC_CONFIGS", "browser")

this_folder = os.path.dirname(os.path.abspath(__file__))
init_file = os.path.join(this_folder, 'conf.ini')
config = configparser.RawConfigParser()
res = config.read(init_file)
browsers = config.get('BASIC_CONFIGS', 'browser').split(",")
headless = config.get('BASIC_CONFIGS', 'headless')
implicit_wait = config.get('BASIC_CONFIGS', 'implicit_wait')
test_site_url = config.get('BASIC_CONFIGS', 'test_site_url')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver_ops = get_browser
    if item.rep_call.failed:
        allure.attach(driver_ops.get_screenshot_as_png(), name="Bug_screenshot", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=browsers, scope="function")
def get_browser(request):
    from Selenium_Operations.Driver_Operations import Driver_Operations
    global driver
    if request.param == "chrome":
        if bool(headless):
            options = Options()
            options = headless_mode_configuration_chrome(options)
            driver = webdriver.Chrome('chromedriver', options=options)
        elif not bool(headless):
            driver = webdriver.Chrome()
    if request.param == "firefox":
        if bool(headless):
            options = FirefoxOptions()
            # cap = DesiredCapabilities().FIREFOX['marionette']  # with mac
            options = headless_mode_configuration_firefox(options=options)
            # driver = webdriver.Firefox(capabilities=cap, options=options)  # with mac
            driver = webdriver.Firefox(options=options)  # with windows
        elif not bool(headless):
            driver = webdriver.Firefox()
    driver_ops = Driver_Operations(driver)
    request.cls.driver = driver

    driver_ops.get_url(test_site_url)
    driver_ops.set_driver_implicit_wait(
        int(implicit_wait))
    yield driver
    driver_ops.quit_browser()


def headless_mode_configuration_chrome(options):
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")
    # Pass the argument 1 to allow and 2 to block
    # options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    return options


def headless_mode_configuration_firefox(options):
    options.add_argument('--headless')
    # options.set_preference("permissions.default.desktop-notification", 1)
    return options
