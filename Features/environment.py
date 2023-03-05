import configparser
import os
import time
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from Features.Steps import utils
from Features.Steps.utils import Utils
from Selenium_Operations.Driver_Operations import Driver_Operations
from Utils.Common_Operations import Common_Operations


# def before_all(context):
#     print("Executes before everything.")


# def before_feature(context, feature):
#     print(" Executes before every feature.")


# def before_scenario(context, scenario):
#     for tag in scenario.tags:
#         (platform, browser, headlessMode) = tag.split('_')
#         if browser == "chrome" and headlessMode == "headOn" and platform == "windows":
#             context.options = Utils.options_chrome()
#             context.driver = webdriver.Chrome('chromedriver', options=context.options)
#         elif browser == "firefox" and headlessMode == "headOn" and platform == "windows":
#             context.options = Utils.options_firefox()
#             context.capabilities = DesiredCapabilities().FIREFOX['marionette']
#             context.driver = webdriver.Firefox(capabilities=context.capabilities, options=context.options)
#         elif browser == "chrome" and headlessMode == "headOff" and platform == "windows":
#             context.driver = webdriver.Chrome()
#         elif browser == "firefox" and headlessMode == "headOff" and platform == "windows":
#             context.driver = webdriver.Firefox()
#         driver_ops = Driver_Operations(context.driver)
#         driver_ops.set_driver_implicit_wait(10)

def before_scenario(context, scenario):
    for tag in scenario.tags:
        if tag == "ChromeHeadless" in scenario.tags:
            context.options = Utils.options_chrome()
            context.driver = webdriver.Chrome('chromedriver', options=context.options)
        elif tag == "FirefoxHeadless" in scenario.tags:
            context.options = Utils.options_firefox()
            context.capabilities = DesiredCapabilities().FIREFOX['marionette']
            context.driver = webdriver.Firefox(capabilities=context.capabilities, options=context.options)
        elif tag == "ChromeOnly" in scenario.tags:
            context.driver = webdriver.Chrome()
        elif tag == "FirefoxOnly" in scenario.tags:
            context.driver = webdriver.Firefox()
        driver_ops = Driver_Operations(context.driver)
        common_ops = Common_Operations(context.driver)
        #driver_ops.set_driver_implicit_wait(int(common_ops.get_value("conf.ini", "BASIC_CONFIGS", "implicit_wait")))


# def before_step(context, step):
#     print("   Executes before every step.")


# def before_tag(context, tag):
#     print("    Executes before every tag.")


# def after_all(context):
#     print("Executes after everything.")


# def after_feature(context, feature):
#     print(" Executes after every feature.")


def after_scenario(context, driver):
    driver_ops = Driver_Operations(context.driver)
    driver_ops.quit_browser()


def after_step(context, step):
    if step.status == 'failed':
        allure.attach(context.driver.get_screenshot_as_png(), name="screenshot",
                      attachment_type=allure.attachment_type.PNG)

# def after_tag(context, tag):
#     print("    Executes after every tag.")
