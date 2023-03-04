import logging
from selenium.webdriver import ActionChains
import traceback
from selenium.webdriver.support.select import Select
from Selenium_Operations.Driver_Operations import Driver_Operations
from Selenium_Operations.Waits_Operations import Waits_Operations
from Utils.Common_Operations import Common_Operations
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Element_Operations(Waits_Operations, Common_Operations, Driver_Operations):

    def __init__(self, driver):
        self.driver = driver
        Common_Operations.__init__(self, self.driver)
        Waits_Operations.__init__(self, self.driver)
        Driver_Operations.__init__(self, self.driver)
        self.actions = ActionChains(self.driver)

    # WebElement Operations
    # This function return web element
    def find_element(self, locator):
        try:
            web_element = self.driver.find_element(self.get_locator_signature(locator),
                                                   self.get_value("../conf.ini", "LOCATORS", locator))
            self.highlight_element(web_element)
            log.logger.info(f"{web_element} in focus now")
            print(f"{web_element} in focus now")
            return web_element
        except:
            print(traceback.print_exc())
            assert False

    # This function return list of web elements
    def find_elements(self, locator):
        try:
            web_elements = self.driver.find_elements(self.get_locator_signature(locator),
                                                     self.get_value("../conf.ini", "LOCATORS", locator))
            self.highlight_element(web_elements)
            log.logger.info(f"{web_elements} in focus now")
            print(f"{web_elements} in focus now")
            return web_elements
        except:
            print(traceback.print_exc())
            assert False

    # This function click on web element
    def click(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele.click()
            flag = True
            log.logger.info(f"{ele} clicked successfully")
            print(f"{ele} clicked successfully")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function click on web element via js script
    def click_js(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.execute_js_script("arguments[0].click();", ele)
            flag = True
            log.logger.info(f"{ele} clicked successfully via js script")
            print(f"{ele} clicked successfully via js script")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function click on web element via actions
    def click_action(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            print("clicked successfully via action class")
            log.logger.info(f"{ele} clicked successfully via js script")
            self.actions.click(on_element=ele)
            flag = True
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function select dropdown/checkbox/radio_btn by value
    def select_by_value(self, locator, value):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            select = Select(dropdown_ele)
            self.highlight_element(dropdown_ele)
            select.select_by_value(value=value)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown selected successfully via value")
            print(f"{dropdown_ele} dropdown selected successfully via value")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function select dropdown/checkbox/radio_btn by index
    def select_by_index(self, locator, index):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.select_by_index(index=index)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown selected successfully via index")
            print(f"{dropdown_ele} dropdown selected successfully via index")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function select dropdown/checkbox/radio_btn by visible text
    def select_by_visible_text(self, locator, visible_text):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.select_by_visible_text(text=visible_text)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown selected successfully via visible text")
            print(f"{dropdown_ele} dropdown selected successfully via visible text")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function deselect dropdown/checkbox/radio_btn by value
    def deselect_by_value(self, locator, value):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.deselect_by_value(value=value)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown deselected successfully via value")
            print(f"{dropdown_ele} dropdown deselected successfully via value")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function deselect dropdown/checkbox/radio_btn by index
    def deselect_by_index(self, locator, index):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.deselect_by_index(index=index)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown deselected successfully via index")
            print(f"{dropdown_ele} dropdown deselected successfully via index")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function deselect dropdown/checkbox/radio_btn by index
    def deselect_by_visible_text(self, locator, visible_text):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.deselect_by_visible_text(text=visible_text)
            flag = True
            log.logger.info(f"{dropdown_ele} dropdown deselected successfully via visible text")
            print(f"{dropdown_ele} dropdown deselected successfully via visible text")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function deselect all options in dropdown/checkbox/radio_btn
    def deselect_all_options(self, locator):
        flag = False
        try:
            dropdown_ele = self.find_element(locator)
            self.highlight_element(dropdown_ele)
            select = Select(dropdown_ele)
            select.deselect_all()
            flag = True
            log.logger.info(f"{dropdown_ele} all dropdown options deselected successfully")
            print(f"{dropdown_ele} all dropdown options deselected successfully")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function get element text
    def get_element_text(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_text = ele.text
            log.logger.info(f"{ele} element text is {ele_text}")
            print(f"{ele} element text is {ele_text}")
            return ele_text
        except:
            print(traceback.print_exc())
            assert False

    # This function send keys to web element[input]
    def send_keys(self, locator, send_keys_value):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele.send_keys(send_keys_value)
            log.logger.info(f"{ele} element input value is {send_keys_value}")
            print(f"{ele} element input value is {send_keys_value}")
            flag = True
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function get web element css property
    def get_element_value_of_css_property(self, locator, css_property_name):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_css_property_value = ele.value_of_css_property(css_property_name)
            log.logger.info(f"{ele} element css property values is {ele_css_property_value}")
            print(f"{ele} element css property values is {ele_css_property_value}")
            return ele_css_property_value
        except:
            print(traceback.print_exc())
            assert False

    # This function get web element size
    def get_element_size(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_size = ele.size
            log.logger.info(f"{ele} element size is {str(ele_size)} and there items are {ele_size.items()}")
            print(f"{ele} element size is {str(ele_size)} and there items are {ele_size.items()}")
            return ele_size
        except:
            print(traceback.print_exc())
            assert False

    # This function get web element attribute
    def get_element_attribute(self, locator, attribute_name):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_attribute = ele.get_attribute(name=attribute_name)
            log.logger.info(f"{ele} element attribute is {str(ele_attribute)}")
            print(f"{ele} element attribute is {str(ele_attribute)}")
            return ele_attribute
        except:
            print(traceback.print_exc())
            assert False

    # This function get web element location
    def get_element_location(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_location = ele.location
            log.logger.info(f"{ele} element location is {str(ele_location)} and there items are {ele_location.items()}")
            print(f"{ele} element location is {str(ele_location)} and there items are {ele_location.items()}")
            return ele_location
        except:
            print(traceback.print_exc())
            assert False

    # This function get web element tag name
    def get_element_tag_name(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_tag_name = ele.tag_name
            log.logger.info(f"{ele} element tagname is {str(ele_tag_name)}")
            print(f"{ele} element tagname is {str(ele_tag_name)}")
            return ele_tag_name
        except:
            print(traceback.print_exc())
            assert False

    # The submit() function is applicable only for <form> and makes handling of form easier
    def submit(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            # print(f"element tagname is {str(ele.tag_name)}")
            # log.logger.info(f"{ele} element tagname is {str(ele_tag_name)}")
            ele.submit()
            flag = True
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # The submit() function is applicable only for <form> and makes handling of form easier
    def get_element_accessible_name(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_accessible_name = ele.accessible_name
            log.logger.info(f"{ele} element accessible name is {ele_accessible_name}")
            print(f"{ele} element accessible name is {ele_accessible_name}")
            return ele_accessible_name
        except:
            print(traceback.print_exc())
            assert False

    # This function clear input field
    def clear(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele.clear()
            log.logger.info(f"{ele} element cleared")
            print(f"{ele} element cleared {ele}")
            flag = True
        except:
            print(traceback.print_exc())
            assert False
        return flag

    # This function return true if element is selected
    def check_element_is_selected(self, locator):
        flag = False
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_selected = ele.is_selected()
            if ele_selected:
                log.logger.info(f"{ele} is selected")
                print(f"{ele} is selected")
            elif not ele_selected:
                log.logger.info(f"{ele} is not selected")
                print(f"{ele} is not selected")
            return ele_selected
        except:
            print(traceback.print_exc())
            assert False

    # This function return true if element is enabled
    def check_element_is_enabled(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_enabled = ele.is_enabled()
            if ele_enabled:
                log.logger.info(f"{ele} is not selected")
                print(f"{ele} is enabled")
            elif not ele_enabled:
                log.logger.info(f"{ele} is not enabled")
                print(f"{ele} is not enabled")
            return ele_enabled
        except:
            print(traceback.print_exc())
            assert False

    # This function return true if element is displayed
    def check_element_is_displayed(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_displayed = ele.is_displayed()
            if ele_displayed:
                log.logger.info(f"{ele} is displayed")
                print(f"{ele} is displayed")
            elif not ele_displayed:
                log.logger.info(f"{ele} is not displayed")
                print(f"{ele} is not displayed")
            return ele_displayed
        except:
            print(traceback.print_exc())
            assert False

    # This function return aria role of the element
    def get_element_aria_rol(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_aria_role = ele.aria_role
            log.logger.info(f"{ele} element aria role is {ele_aria_role}")
            print(f"{ele} element aria role is {ele_aria_role}")
            return ele_aria_role
        except:
            print(traceback.print_exc())
            assert False

    # This function return dom attribute
    def get_element_inside_dom_attribute(self, locator, dom_attribute_name):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_get_dom_attribute = ele.get_dom_attribute(name=dom_attribute_name)
            log.logger.info(f"element tagname is {str(ele_get_dom_attribute)}")
            print(f"element tagname is {str(ele_get_dom_attribute)}")
            return ele_get_dom_attribute
        except:
            print(traceback.print_exc())
            assert False

    # This function return element property
    def get_element_property(self, locator, property_name):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_get_property = ele.get_property(property_name)
            log.logger.info(f"element property is {ele_get_property}")
            print(f"element property is {ele_get_property}")
            return ele_get_property
        except:
            print(traceback.print_exc())
            assert False

    # This function return element location via scroll into view
    def get_element_location_via_scroll_into_view(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_location_once_scrolled_into_view = ele.location_once_scrolled_into_view
            log.logger.info(f"{ele} element location when scrolled into view is {ele_location_once_scrolled_into_view}")
            print(f"{ele} element location when scrolled into view is {ele_location_once_scrolled_into_view}")
            return ele.location_once_scrolled_into_view
        except:
            print(traceback.print_exc())
            assert False

    # This function return element size and location
    def get_element_size_and_location(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_rect = ele.rect
            log.logger.info(f"{ele} element rect is {ele_rect}")
            print(f"{ele} element rect is {ele_rect}")
            return ele_rect
        except:
            print(traceback.print_exc())
            assert False

    # This function return element shadow root inside element
    def get_shadow_root_inside_element(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_shadow_root = ele.shadow_root
            log.logger.info(f"{ele} element shadow root returned")
            print(f"{ele} element shadow root returned")
            return ele_shadow_root
        except:
            print(traceback.print_exc())
            assert False

    # This function return screenshot of element as base64
    def get_element_screenshot_as_base64(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_screenshot_as_base64 = ele.screenshot_as_base64
            log.logger.info(f"{ele} element screenshot as base64 taken")
            print(f"{ele} element screenshot as base64 taken")
            return ele_screenshot_as_base64
        except:
            print(traceback.print_exc())
            assert False

    # This function return screenshot of element as png
    def get_element_screenshot_as_png(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            ele_screenshot_as_png = ele.screenshot_as_png
            log.logger.info(f"{ele} element screenshot as png taken")
            print(f"{ele} element screenshot as png taken")
            return ele_screenshot_as_png
        except:
            print(traceback.print_exc())
            assert False

    # This function moved focus/curser to ele
    def move_to_element(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.move_to_element(to_element=ele)
            log.logger.info(f"{ele} moved to element")
            print(f"{ele} moved to element")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function moved focus/curser to ele via js script
    def move_to_element_js(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            move_to_ele_script = "if(document.createEvent){var evObj = document.createEvent('MouseEvents');evObj.initEvent('mouseover',true, false); arguments[0].dispatchEvent(evObj);} else if(document.createEventObject) { arguments[0].fireEvent('onmouseover');}"
            self.driver.execute_script(move_to_ele_script, ele)
            log.logger.info(f"{ele} moved to element via js script")
            print(f"{ele} moved to element via js script")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function reset actions
    def reset_actions(self):
        try:
            self.actions.reset_actions()
            log.logger.info(f"actions reset successfully")
            print(f"actions reset successfully")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function send keyboard keys via action
    def send_keys_via_actions(self, keys_to_send):
        try:
            self.actions.send_keys(keys_to_send)
            log.logger.info(f"actions send keys successfully")
            print(f"actions send keys successfully")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function scrolled to required ele
    def scroll_to_element(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.scroll_to_element(ele)
            log.logger.info(f"{ele} actions scrolled to successfully")
            print(f"{ele} actions scrolled to successfully")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function scrolled page by x_axis and y_axis
    def scroll_by_amount(self, delta_x, delta_y):
        try:
            self.actions.scroll_by_amount(delta_x=delta_x, delta_y=delta_y)
            log.logger.info(f"actions scrolled to {delta_x} and {delta_y}")
            print(f"actions scrolled to {delta_x} and {delta_y}")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function right-clicked on ele
    def right_click(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.context_click(on_element=ele)
            log.logger.info(f"{ele} actions right clicked")
            print(f"{ele} actions right clicked")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function drag source ele and drop to target ele
    def drag_and_drop_element(self, source_locator, target_locator):
        try:
            source_ele = self.find_element(source_locator)
            self.highlight_element(source_ele)
            target_ele = self.find_element(target_locator)
            self.highlight_element(target_ele)
            self.actions.drag_and_drop(source=source_ele, target=target_ele)
            log.logger.info(f"{source_ele} drag and dropped to {target_ele}")
            print(f"{source_ele} drag and dropped to {target_ele}")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function drag source ele and drop via offset
    def drag_and_drop_element_via_offset(self, source_locator, x_offset, y_offset):
        try:
            source_ele = self.find_element(source_locator)
            self.highlight_element(source_ele)
            self.actions.drag_and_drop_by_offset(source=source_ele, xoffset=x_offset, yoffset=y_offset)
            log.logger.info(f"{source_ele} drag and dropped to x_axis {x_offset} and y_axis {y_offset}")
            print(f"{source_ele} drag and dropped to x_axis {x_offset} and y_axis {y_offset}")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function click and hold on ele
    def click_and_hold(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.click_and_hold(on_element=ele)
            log.logger.info(f"{ele} clicked and hold")
            print(f"{ele} clicked and hold")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function double click on ele
    def double_click(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.double_click(on_element=ele)
            log.logger.info(f"{ele} double clicked")
            print(f"{ele} double clicked")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function perform release
    def release(self, locator):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.release(on_element=ele)
            log.logger.info(f"{ele} released on ele")
            print(f"{ele} released on ele")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function perform key down action
    def key_down(self, locator, value):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.key_down(value=value, element=ele)
            log.logger.info(f"{ele} key down action performed")
            print(f"{ele} key down action performed")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function perform key up action
    def key_up(self, locator, value):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.key_up(value=value, element=ele)
            log.logger.info(f"{ele} key up action performed")
            print(f"{ele} key up action performed")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function pause
    def pause(self, seconds):
        try:
            self.actions.pause(seconds=seconds)
            log.logger.info(f"paused for {seconds} seconds")
            print(f"paused for {seconds} seconds")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function scrolled to origin at x_axis and y_axis
    def scroll_to_origin(self, locator, delta_x, delta_y):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.scroll_from_origin(scroll_origin=ele, delta_x=delta_x, delta_y=delta_y)
            log.logger.info(f"{ele} scrolled to origin at {delta_x} and {delta_y}")
            print(f"{ele} scrolled to origin at {delta_x} and {delta_y}")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function send keys to element via action
    def send_keys_to_element_via_action(self, locator, keys_to_send):
        try:
            ele = self.find_element(locator)
            self.highlight_element(ele)
            self.actions.send_keys_to_element(ele, keys_to_send)
            log.logger.info(f"{ele} {keys_to_send} keys send successfully")
            print(f"{ele} {keys_to_send} keys send successfully")
            return self
        except:
            print(traceback.print_exc())
            assert False

    # This function return element id
    def get_element_id(self, locator):
        try:
            ele = self.find_element(locator)
            ele_id = ele.id
            log.logger.info(f"{ele} element id is {ele_id}")
            print(f"{ele} element id is {ele_id}")
            return ele_id
        except:
            print(traceback.print_exc())
            assert False

    # This function perform action chains
    def perform_after_actionChains(self):
        try:
            return self.actions.perform()
        except:
            print(traceback.print_exc())
            assert False
