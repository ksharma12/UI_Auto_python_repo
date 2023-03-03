from Selenium_Operations.Element_Operations import Element_Operations


class Home_Page(Element_Operations):

    def __init__(self, driver):
        self.driver = driver
        Element_Operations.__init__(self, self.driver)

    def moving_to_Dummy_Registration_Page(self):
        self.wait_until_element_present_visible("resources__XPATH")
        self.move_to_element("resources__XPATH").perform_after_actionChains()
        self.wait_until_element_present_visible("resources_practice_site_1__XPATH")
        self.click("resources_practice_site_1__XPATH")
