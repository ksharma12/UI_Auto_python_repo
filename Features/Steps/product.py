import time

from behave import *
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher('parse')


@given('User navigated to url')
def step_impl(context):
    context.ele_ops = Element_Operations(context.driver)
    context.ele_ops.get_url("https://www.way2automation.com/")


@when("Verify user successfully landed on home page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then("User moved to resources option")
def step_impl(context):
    context.ele_ops.wait_until_element_present_visible("resources__XPATH")
    context.ele_ops.move_to_element("resources__XPATH").perform_after_actionChains()


@then("User clicked on resources option")
def step_impl(context):
    context.ele_ops.wait_until_element_present_visible("resources_practice_site_1__XPATH")
    context.ele_ops.click("resources_practice_site_1__XPATH")


@then("Verify landed on dummy registration page")
def step_impl(context):
    print(context.ele_ops.get_window_title())


@then('User fill "{name}" in dummy registration form')
def step_impl(context, name):
    context.ele_ops.wait_until_element_present_visible("name__XPATH")
    context.ele_ops.find_element("name__XPATH")
    context.ele_ops.send_keys("name__XPATH", name)
    time.sleep(2)


