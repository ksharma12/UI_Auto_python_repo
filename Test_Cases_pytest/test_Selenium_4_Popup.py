import pytest
from Pages.Selenium_4_Popup_Page import Selenium_4_Popup_Page
from Test_Cases_pytest.BaseTest import BaseTest
import logging
from Utils.Logging_Operations import Logger

log = Logger(__name__, logging.INFO)


class Test_Selenium_4_Registration(BaseTest):

    @pytest.mark.regression
    def test_close_selenium_pop_up(self):
        Selenium4PopUpPage = Selenium_4_Popup_Page(self.driver)
        log.logger.info("********** Test close selenium pop up started **********")
        Selenium4PopUpPage.close_selenium_four_popup()
        log.logger.info("********** Test close selenium pop up Ended **********")