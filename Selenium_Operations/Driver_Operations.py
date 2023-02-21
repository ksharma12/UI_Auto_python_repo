import logging
import traceback
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Driver_Operations:

    def __init__(self, driver):
        self.driver = driver

    # Driver Operations
    # This function return browser name
    def get_browser_name(self):
        try:
            browser_name = self.driver.name
            log.logger.info(f"browser name is {browser_name}")
            print(f"browser name is {browser_name}")
            return browser_name
        except:
            print(traceback.print_exc())
            assert False

    # This function get window title
    def get_window_title(self):
        try:
            window_title = self.driver.title
            log.logger.info(f"window title is {window_title}")
            print(f"window title is {window_title}")
            return window_title
        except:
            print(traceback.print_exc())
            assert False

    def quit_browser(self):
        try:
            self.driver.quit()
            log.logger.info("all windows closed successfully")
            print("all windows closed successfully")
        except:
            print(traceback.print_exc())
            assert False

    def maximize_window(self):
        try:
            self.driver.maximize_window()
            log.logger.info("window maximized successfully")
            print("window maximized successfully")
        except:
            print(traceback.print_exc())
            assert False

    def get_session_id(self):
        try:
            session_id = self.driver.session_id
            log.logger.info(f"{session_id} of current driver session")
            print(f"{session_id} of current driver session")
        except:
            print(traceback.print_exc())
            assert False

    def minimize_window(self):
        try:
            self.driver.minimize_window()
            log.logger.info("window minimized successfully")
            print("window minimized successfully")
        except:
            print(traceback.print_exc())
            assert False

    def set_fullscreen_window(self):
        try:
            self.driver.fullscreen_window()
            log.logger.info("Window full screened successfully")
            print("Window full screened successfully")
        except:
            print(traceback.print_exc())
            assert False

        # locator must be id/name of frame

    def switch_to_frame(self, iframe_reference):
        try:
            self.driver.switch_to.frame(iframe_reference)
            log.logger.info("focus shifted to listed iframe successfully")
            print("focus shifted to listed iframe successfully")
        except:
            print(traceback.print_exc())
            assert False

    def close_current_window(self):
        try:
            self.driver.close()
            log.logger.info("only current window closed successfully")
            print("only current window closed successfully")
        except:
            print(traceback.print_exc())
            assert False

    def get_alert_text(self):
        try:
            alert_text = self.driver.switch_to.alert.text
            log.logger.info(f"alert text is {alert_text}")
            print(f"alert text is {alert_text}")
            return alert_text
        except:
            print(traceback.print_exc())
            assert False

    # Bring back focus to current screen
    def switch_to_default_content(self):
        try:
            self.driver.switch_to.default_content()
            log.logger.info("focus shifted to current screen successfully")
            print("focus shifted to current screen successfully")
        except:
            print(traceback.print_exc())
            assert False

    def get_virtual_authenticator_id(self):
        try:
            vir_auth_id = self.driver.virtual_authenticator_id
            log.logger.info(f"{vir_auth_id} virtual authenticator id")
            print(f"{vir_auth_id} virtual authenticator id")
        except:
            print(traceback.print_exc())
            assert False

    def switch_to_window(self, window_handle):
        try:
            self.driver.switch_to.window(window_handle)
            log.logger.info("focus shifted to listed name window successfully")
            print("focus shifted to listed name window successfully")
        except:
            print(traceback.print_exc())
            assert False

    def switch_to_parent_frame(self):
        try:
            self.driver.switch_to.parent_frame()
            log.logger.info("focus shifted to parent frame successfully")
            print("focus shifted to parent frame successfully")
        except:
            print(traceback.print_exc())
            assert False

    def accept_alert(self):
        try:
            self.driver.switch_to.alert.accept()
            log.logger.info("alert accepted successfully")
            print("alert accepted successfully")
        except:
            print(traceback.print_exc())
            assert False

    def write_to_alert(self, send_keys):
        try:
            self.driver.switch_to.alert.send_keys(send_keys)
            log.logger.info("data written on alert successfully")
            print("data written on alert successfully")
        except:
            print(traceback.print_exc())
            assert False

    def dismiss_alert(self):
        try:
            self.driver.switch_to.alert.dismiss()
            log.logger.info("alert dismissed successfully")
            print("alert dismissed successfully")
        except:
            print(traceback.print_exc())
            assert False

    def switch_to_active_element(self):
        try:
            ele = self.driver.switch_to.active_element
            log.logger.info(f"{ele} focus shifted to active_web_element successfully")
            print(f"{ele} focus shifted to active_web_element successfully")
            return ele
        except:
            print(traceback.print_exc())
            assert False

    def switch_to_new_window(self):
        flag = False
        try:
            self.driver.switch_to.new_window()
            flag = True
            log.logger.info("focus shifted to new window successfully")
            print("focus shifted to new window successfully")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    def get_window_handles(self):
        try:
            all_open_window_handles = self.driver.window_handles
            log.logger.info(f"get all open window handles {all_open_window_handles}")
            print(f"get all open window handles {all_open_window_handles}")
            return all_open_window_handles
        except:
            print(traceback.print_exc())
            assert False

    def get_application_cache_status(self):
        try:
            application_cache_status = self.driver.application_cache.status
            log.logger.info(f"get all open window handles {application_cache_status}")
            print(f"get all open window handles {application_cache_status}")
            return application_cache_status
        except:
            print(traceback.print_exc())
            assert False

    def get_window_current_url(self):
        try:
            current_url = self.driver.current_url
            log.logger.info(f"get current window url: {current_url}")
            print(f"get current window url: {current_url}")
            return current_url
        except:
            print(traceback.print_exc())
            assert False

    def navigate_back(self):
        try:
            self.driver.back()
            log.logger.info("navigated back successfully")
            print("navigated back successfully")
        except:
            print(traceback.print_exc())
            assert False

    def navigate_forward(self):
        try:
            self.driver.forward()
            log.logger.info("navigated forward successfully")
            print("navigated forward successfully")
        except:
            print(traceback.print_exc())
            assert False

    def get_current_window_handle(self):
        try:
            current_window_handle = self.driver.current_window_handle
            log.logger.info(f"get current window handle: {current_window_handle}")
            print(f"get current window handle: {current_window_handle}")
            return current_window_handle
        except:
            print(traceback.print_exc())
            assert False

    def get_url(self, url):
        flag = False
        try:
            self.driver.get(url)
            flag = True
            log.logger.info(f"User Navigated to {url}")
            print(f"User Navigated to {url}")
        except:
            print(traceback.print_exc())
            assert False
        return flag

    def set_driver_implicit_wait(self, implicit_wait):
        try:
            self.driver.implicitly_wait(implicit_wait)
            log.logger.info(f"Implicit wait set to {implicit_wait}")
            print(f"Implicit wait set to {implicit_wait}")
        except:
            print(traceback.print_exc())
            assert False
