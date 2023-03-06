import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utils.Common_Operations import Common_Operations


class Waits_Operations(Common_Operations):

    def __init__(self, driver):
        self.driver = driver
        Common_Operations.__init__(self, self.driver)
        self.explicit_wait = int(self.get_value("../conf.ini", "BASIC_CONFIGS", "explicit_wait"))
        self.fluent_wait = float(self.get_value("../conf.ini", "BASIC_CONFIGS", "fluent_wait"))

    # This function return element once it become clickable and return ele
    def wait_until_element_clickable(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element = wait.until(
                EC.element_to_be_clickable((self.get_locator_signature(locator),
                                            self.get_value("../conf.ini", "LOCATORS", locator))))
            print(f"{element} element is in focus and clickable Now")
            return element
        except:
            print(traceback.print_exc())

    # This function wait for presence of element in dom and return ele
    def wait_until_element_present(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element_present = wait.until(
                EC.presence_of_element_located((self.get_locator_signature(locator),
                                                self.get_value("../conf.ini", "LOCATORS", locator))))
            print(f"{element_present} element is in focus and present Now")
            return element_present
        except:
            print(traceback.print_exc())

    # This function wait for visibility of element in dom and return ele
    def wait_until_element_visible_located(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element_visible = wait.until(
                EC.visibility_of_element_located(
                    (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{element_visible} element is in focus and present Now")
            return element_visible
        except:
            print(traceback.print_exc())

    # This function wait for presence and visibility of element in dom and return ele
    def wait_until_element_present_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element_present = wait.until(
                EC.presence_of_element_located(
                    (self.get_locator_signature(locator), self.get_locator_values(locator))))
            element_present_visible = wait.until(
                EC.visibility_of(element_present))
            print(f"{element_present_visible} element is in focus and present and visible Now")
            return element_present_visible
        except:
            print(traceback.print_exc())

    # This function return True once element become invisible
    def wait_until_element_invisible_locator(self, locator):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.invisibility_of_element_located(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{flag} > is invisible Now")
            return flag
        except:
            print(traceback.print_exc())

    # This function return True once element become invisible
    def wait_until_element_invisible(self, web_element):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.invisibility_of_element(web_element))
            print(f"{flag} > waited until become invisible")
            return flag
        except:
            print(traceback.print_exc())

    # This function return element once element is visible
    def wait_until_element_visible(self, web_element):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element = wait.until(EC.visibility_of(web_element))
            print(f"{element} element is visible now")
            return element
        except:
            print(traceback.print_exc())

    # This function return list of all visible elements once elements are visible
    def wait_until_elements_visible_located(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            elements = wait.until(EC.visibility_of_all_elements_located(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{elements} waited until all {len(elements)} elements are visible")
            return elements
        except:
            print(traceback.print_exc())

    # This function return list of any visible elements once they are visible
    def wait_until_any_element_is_visible(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            elements_list = wait.until(EC.visibility_of_any_elements_located(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{elements_list} waited until {len(elements_list)} elements are visible")
            return elements_list
        except:
            print(traceback.print_exc())

    # This function return list of elements once present in dom
    def wait_until_elements_present(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element_list = wait.until(EC.presence_of_all_elements_located(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{element_list} waited until all {len(element_list)} elements become present")
            return element_list
        except:
            print(traceback.print_exc())

    # This function waited for presence of alert on the web page
    def wait_until_alert_is_present(self):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.alert_is_present())
            print(f"{flag} > waited until alert is present")
            return flag
        except:
            print(traceback.print_exc())

    # Return True once url changed from url passed in arguments
    def wait_until_url_changes(self, url):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.url_changes(url))
            print(f"{flag} > waited until url changed from {url}")
            return flag
        except:
            print(traceback.print_exc())

    # Return True once url is equal to url passed in arguments
    def wait_until_url_is(self, url):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.url_to_be(url))
            print(f"{flag} > waited until url become {url}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true once url matches to url passed in argument
    def wait_until_url_matches_to(self, pattern):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.url_matches(pattern))
            print(f"{flag} > waited until url matches to {pattern}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true once url contains to url passed in argument
    def wait_until_url_contains(self, url_part):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.url_contains(url_part))
            print(f"{flag} > waited until url contains {url_part}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true once passed txt is present in element
    def wait_until_text_to_be_present_in_element(self, locator, text):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(
                EC.text_to_be_present_in_element(
                    (self.get_locator_signature(locator), self.get_locator_values(locator)),
                    text))
            print(f"{flag} > waited until {text} present")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if text is present in attribute of element
    def wait_until_text_to_be_present_in_element_attribute(self, locator, attribute, text):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.text_to_be_present_in_element_attribute(
                (self.get_locator_signature(locator), self.get_locator_values(locator)), attribute, text))
            print(f"{flag} > waited until {text} present in {attribute}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if text is present in value of element    // currently failing
    def wait_until_text_to_be_present_in_element_value(self, locator, text):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.text_to_be_present_in_element_value(
                (self.get_locator_signature(locator), self.get_locator_values(locator)), text))
            print(f"{flag} > waited until {text} present")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if checkbox/radio btn is selected
    def wait_until_element_selected(self, web_element):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.element_to_be_selected(web_element))
            print(f"{web_element} {flag} waited until element is selected")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if checkbox/radio btn is selected
    def wait_until_element_located_selected(self, locator):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.element_located_to_be_selected(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{flag} > waited until element is selected")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if checkbox/radio btn selected state is True/False as per argument given
    def wait_until_element_selected_state_is(self, locator, is_selected):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.element_located_selection_state_to_be(
                (self.get_locator_signature(locator), self.get_locator_values(locator)), is_selected))
            print(f"{flag} > waited until selected state become {is_selected}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if element has required attribute or not
    def wait_until_element_attribute_to_include(self, locator, attribute):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(
                EC.element_attribute_to_include((self.get_locator_signature(locator), self.get_locator_values(locator)),
                                                attribute))
            print(f"{flag} > waited until element include {attribute}")
            return flag
        except:
            print(traceback.print_exc())

    # // failing
    def wait_until_element_visiblty_is(self, web_element, visibility):
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            element = wait.until(EC._element_if_visible(web_element, visibility))
            print(f"{element} waited until element visibility is {visibility}")
            return element
        except:
            print(traceback.print_exc())

    # Return true if title is required title
    def wait_until_title_is(self, title):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.title_is(title))
            print(f"{flag} > waited until window title is {title}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if title part is present in current window title
    def wait_until_title_contains(self, title_part):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.title_contains(title_part))
            print(f"{flag} > waited until window title contain {title_part}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if iframe available and focus switched to it
    def wait_until_frame_avial_switch_to(self, locator):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.frame_to_be_available_and_switch_to_it(
                (self.get_locator_signature(locator), self.get_locator_values(locator))))
            print(f"{flag} > waited until iframe available to switch")
            return flag
        except:
            print(traceback.print_exc())

        # Return true if iframe available and focus switched to it

    # Return true if open windows count is equal to argument passed
    def wait_until_windows_count_is(self, number):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.number_of_windows_to_be(number))
            print(f"{flag} > waited until window count is {number}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if open windows count is equal to argument passed   // failing
    def wait_until_new_window_is_opened(self, current_window_handle):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.new_window_is_opened(current_window_handle))
            print(f"{flag} > waited until new window is opened with handle {current_window_handle}")
            return flag
        except:
            print(traceback.print_exc())

    # Return true if staleness of element is True
    def wait_until_staleness_of_ele(self, element):
        flag = False
        try:
            wait = WebDriverWait(self.driver, timeout=self.explicit_wait, poll_frequency=self.fluent_wait)
            flag = wait.until(EC.staleness_of(element))
            print(f"{flag} > waited until staleness of {element}")
            return flag
        except:
            print(traceback.print_exc())

    # Example of [all_of/any_of/none_off] this can be used to make multiple expected conditions
    # WebDriverWait(browser, 10).until(EC.all_of(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "span[title='VMC OIC-2 batch 2022']")),
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "div#startup")),
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "div#initial-startup"))
    # ))
