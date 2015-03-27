from selenium import webdriver

import unittest

import portal_common

class JustToRunTestCase(unittest.TestCase):
    
    def setUp(self):
        #self.browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        
        
#     def test_prod_self_serve_purchase_MBAM(self):
#      
#         browser = self.browser
#  
#         portal_link = portal_common.portal_link_generator(True, 'MBAM-B')
#         browser.get(portal_link)
#         portal_common.portal_purchase(browser)
# 
#     def test_prod_self_serve_purchase_MBAE(self):
#       
#         browser = self.browser
#   
#         portal_link = portal_common.portal_link_generator(True, 'MBAE-B')
#         browser.get(portal_link)
#         portal_common.portal_purchase(browser)        
#
#     def test_prod_self_serve_purchase_MBES(self):
#       
#         browser = self.browser
#   
#         portal_link = portal_common.portal_link_generator(True, 'MBES-B')
#         browser.get(portal_link)
#         portal_common.portal_purchase(browser)     
  
    def test_mwbtest_self_serve_purchase_MBAM(self):
      
        browser = self.browser
  
        portal_link = portal_common.portal_link_generator(False, 'MBAM-B')
        browser.get(portal_link)
        portal_common.portal_purchase(browser)
  
    def test_mwbtest_self_serve_purchase_MBAE(self):
      
        browser = self.browser
  
        portal_link = portal_common.portal_link_generator(False, 'MBAE-B')
        browser.get(portal_link)
        portal_common.portal_purchase(browser)      

    def test_mwbtest_self_serve_purchase_MBES(self):
       
        browser = self.browser
   
        portal_link = portal_common.portal_link_generator(False, 'MBES-B')
        browser.get(portal_link)
        portal_common.portal_purchase(browser)     
  
   
           
#         ids = browser.find_elements_by_xpath('//*[id="submit-hpm-button"]/div/div/*[@class]')
#         for i in ids:
#             print i.get_attribute("class")
     
   # def tearDown(self): 
        #self.browser.quit()