import unittest, time
import SFDC_common, portal_common, common

from selenium import webdriver

class MwbtestSalesAssistedPurchaseMBAM(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        
    def test_mwbtest_sales_assisted_purchase_MBAM(self):
        browser = self.browser
        SFDC_common.login(browser)
        
    def tearDown(self):
        pass
        #self.browser.quit()