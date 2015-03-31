import unittest, time
import portal_common, common, zuora_common

from selenium import webdriver

class MwbtestSelfServePurchaseMBAM(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        
        self.verify = []
        
        print "^" * 100
        print "Currently testing: %s" % (self._testMethodName)
        print "-" * 70
    
    def test_mwbtest_self_serve_purchase_MBAM(self):
      
        browser = self.browser
  
        user = common.User(False, '34')
        portal_link = portal_common.portal_link_generator(False, 'MBAM-B')
        browser.get(portal_link)
        portal_common.portal_purchase(browser, user, '10')

        
#        zuora_common.login(browser)
#        zuora_common.check_subscription(browser, user)
        
    # def test_mwbtest_self_serve_purchase_MBAE(self):
       
        # browser = self.browser
   
        # portal_link = portal_common.portal_link_generator(False, 'MBAE-B')
        # browser.get(portal_link)
        # portal_common.portal_purchase(browser)      
# 
#     def test_mwbtest_self_serve_purchase_MBES(self):
#        
#         browser = self.browser
#    
#         portal_link = portal_common.portal_link_generator(False, 'MBES-B')
#         browser.get(portal_link)
#         portal_common.portal_purchase(browser)     
    
    def tearDown(self):
        #pass
        
        if self.verify:
            print "Verify errors:"
        for x in self.verify:
            print x
        #clean up verify for the next test case
        del self.verify[:]
        
        #self.browser.quit()