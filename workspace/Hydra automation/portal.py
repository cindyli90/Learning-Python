from selenium import webdriver

import portal_common


class SelfServe:
    def __init__(self, test, product):
        self.test = test #true/false value to show whether to use mwbtest or prod
        self.product = product #one of the products: MBAM-B, MBAE-B, MBES-B
        
        #self.browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)

    def self_serve_purchase(self):
      
        portal_link = portal_common.portal_link_generator(self.test, self.product)
        self.browser.get(portal_link)
        portal_common.portal_purchase(self.browser)
        
    def self_serve_activate(self):
        
        elem_here_link = self.browser.find_element_by_xpath('//*[@href="/verifyEmail"]')
        elem_here_link.click()
        
        portal_common.portal_activate(self.browser)
  
 
#     def test_mwbtest_self_serve_purchase_MBAE(self):
#      
#         browser = self.browser
#  
#         portal_link = portal_common.portal_link_generator(False, 'MBAE-B')
#         browser.get(portal_link)
#         portal_common.portal_purchase(browser)       
           
#         ids = browser.find_elements_by_xpath('//*[id="submit-hpm-button"]/div/div/*[@class]')
#         for i in ids:
#             print i.get_attribute("class")
     
    def tearDown(self): 
        self.browser.quit()