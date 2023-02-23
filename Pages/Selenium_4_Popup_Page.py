from Selenium_Operations.Element_Operations import Element_Operations


class Selenium_4_Popup_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def close_selenium_four_popup(self):
        self.wait_until_element_present("Selenium4_popup_close_icon__XPATH")
        self.click("Selenium4_popup_close_icon__XPATH")
