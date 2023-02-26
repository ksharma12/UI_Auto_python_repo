import os
import traceback

import configparser
from selenium.webdriver.common.by import By
from Utils.IniFile_Reader_Writer_Operations import IniFile_Reader_Writer_Operations


class Common_Operations:

    def __init__(self, driver):
        self.driver = driver

    _confi_file_path = "../conf.ini"
    _js_arg_ele_border_color = "red"
    _selectors_dict = {
        "XPATH": By.XPATH,
        "ID": By.ID,
        "TAG_NAME": By.TAG_NAME,
        "NAME": By.NAME,
        "CSS": By.CSS_SELECTOR,
        "CLASS_NAME": By.CLASS_NAME,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT
    }

    def get_locator_signature(self, locator):
        selector = str(locator).split("__")[1]
        return self._selectors_dict[selector]

    def get_locator_values(self, key):
        # get locators from .ini file
        conf = IniFile_Reader_Writer_Operations(self._confi_file_path)
        return conf.get_value_from_key_in_section("LOCATORS", key)

    def get_basic_config_values(self, key):
        conf = IniFile_Reader_Writer_Operations(self._confi_file_path)
        return conf.get_value_from_key_in_section("BASIC_CONFIGS", key)

    # This function highlight respective element
    def highlight_element(self, web_element):
        flag = False
        try:
            self.execute_js_script(f"arguments[0].style.border='2px solid {self._js_arg_ele_border_color}'",
                                   web_element)
            flag = True
            print(f"{web_element} element highlighted with border color {self._js_arg_ele_border_color}")
        except:
            print(traceback.print_exc())
        return flag

    # This function execute required js script on respective element
    def execute_js_script(self, js_script, web_element):
        flag = False
        try:
            self.driver.execute_script(js_script, web_element)
            flag = True
        except:
            print(traceback.print_exc())
        return flag

    @staticmethod
    def read_data(file_name, section_name, key_name):
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        initfile = os.path.join(thisfolder, file_name)
        config = configparser.RawConfigParser()
        res = config.read(initfile)
        data = config.get(section_name, key_name).split(",")
        return data
