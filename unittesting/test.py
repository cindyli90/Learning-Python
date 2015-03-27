from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest

class SFDCLoginTestCase(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def test_login(self):
		browser = self.browser
		
		browser.get('https://cs12.salesforce.com/')
		self.assertIn('salesforce.com - Customer Secure Login Page', browser.title)
		
		elem_uid = browser.find_element_by_name('username')  # Find user name
		elem_uid.send_keys('cli@malwarebytes.org.fullsand')

		elem_uid = browser.find_element_by_name('pw')  # Find password
		elem_uid.send_keys('t1j%8ZtdnQ6G')

		elem_uid.send_keys(Keys.RETURN)
		
		#self.assertIn('salesforce.com - Enterprise Edition', browser.title)

	def test_newAcct(self):
		browser = self.browser
		
		accounts_tab_uid = browser.find_element_by_name('Account_Tab')
		accounts_tab_uid.click()
		
		
	
	#def tearDown(self):
		#self.browser.quit()


if '__name__' == '__main__':
	unittest.main()