from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class SFDCLoginTestCase (unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def test_login(self):
        browser = self.browser
        
        browser.get('https://cs12.salesforce.com/')
        self.assertIn('salesforce.com - Customer Secure Login Page', browser.title, "title not the same")
        
        elem_uid = browser.find_element_by_name('username') #find username
        elem_uid.send_keys('cli@malwarebytes.org.fullsand')
        
        elem_uid = browser.find_element_by_name('pw')  # Find password
        elem_uid.send_keys('t1j%8ZtdnQ6G')

        elem_uid.send_keys(Keys.RETURN)