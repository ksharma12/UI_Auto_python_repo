import configparser
import os

from behave import *

from Selenium_Operations.Driver_Operations import Driver_Operations
from Selenium_Operations.Element_Operations import Element_Operations

use_step_matcher('parse')


@given('User navigated to url')
def step_impl(context):
    context.ops = Element_Operations(context.driver)
    context.ops.get_url("https://www.way2automation.com/")


@when("Verify user successfully landed on home page")
def step_impl(context):
    print(context.ops.get_window_title())


@then("User moved to resources option")
def step_impl(context):
    print()


@then("User clicked on resources option")
def step_impl(context):
    print("")


@then("Verify landed on dummy registration page")
def step_impl(context):
    print("")


@then('User fill "{name}" in dummy registration form')
def step_impl(context, name):
    print(name)
