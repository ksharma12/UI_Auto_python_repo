import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from Utils.IniFile_Reader_Writer_Operations import IniFile_Reader_Writer_Operations

ini_file_read_write = IniFile_Reader_Writer_Operations("../conf.ini")
browser = ini_file_read_write.get_multiple_values_from_key_in_section("BASIC_CONFIGS", "browser")


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
        allure.attach(driver_ops.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=browser, scope="function")
def get_browser(request):
    from Selenium_Operations.Driver_Operations import Driver_Operations
    global driver
    if request.param == "chrome":
        if bool(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "headless")):
            options = Options()
            options = headless_mode_configuration_chrome(options)
            driver = webdriver.Chrome('chromedriver', options=options)
        elif not bool(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "headless")):
            driver = webdriver.Chrome()
    if request.param == "firefox":
        if bool(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "headless")):
            cap = DesiredCapabilities().FIREFOX
            desired_capabilities_firefox(cap)
            options = FirefoxOptions()
            options = headless_mode_configuration_firefox(options)
            driver = webdriver.Firefox(capabilities=cap, options=options)
        elif not bool(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "headless")):
            driver = webdriver.Firefox()
    driver_ops = Driver_Operations(driver)
    request.cls.driver = driver
    driver_ops.get_url(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "test_site_url"))
    driver_ops.set_driver_implicit_wait(
        int(ini_file_read_write.get_value_from_key_in_section("BASIC_CONFIGS", "implicit_wait")))
    yield driver
    driver_ops.quit_browser()


def headless_mode_configuration_chrome(options):
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("window-size=1920x1080")
    return options


def headless_mode_configuration_firefox(options):
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # options.add_argument("start-maximized")
    # options.add_argument("disable-infobars")
    # options.add_argument("--disable-extensions")
    # options.add_argument("window-size=1920x1080")
    return options


def desired_capabilities_firefox(cap):
    cap["marionette"] = False
