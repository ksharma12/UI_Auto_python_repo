import time

from selenium.webdriver.common.by import By

from Selenium_Operations.Element_Operations import Element_Operations


class dummy_registration(Element_Operations):
    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def fill_registration_form(self, name, phoneNumber, email, country, city, username, password):
        self.set_fullscreen_window()
        self.wait_until_element_present_visible("name__XPATH")
        self.send_keys("name__XPATH", name)
        self.wait_until_element_present_visible("phone__CSS")
        self.send_keys("phone__CSS", phoneNumber)
        self.wait_until_element_present_visible("email__NAME")
        self.send_keys("email__NAME", email)
        self.wait_until_element_present_visible("country__XPATH")
        self.select_by_value("country__XPATH", country)
        self.wait_until_element_present_visible("city__XPATH")
        self.send_keys("city__XPATH", city)
        self.wait_until_element_present_visible("username__XPATH")
        self.send_keys("username__XPATH", username)
        self.wait_until_element_present_visible("password__XPATH")
        self.send_keys("password__XPATH", password)
