import unittest, time
import portal_common, common

from selenium import webdriver
from json.decoder import errmsg

class MwbtestSelfServePurchaseMBAM(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(30)
        self.product = 'MBAM-B'
        self.portal_link = portal_common.portal_link_generator(False, self.product)
        
        self.verify = []
        
        print "^" * 100
        print "Currently testing: %s" % (self._testMethodName)
        print "-" * 70
        
        
    def test_check_remove_link(self):
           
        browser = self.browser
          
        empty_cart_msg = 'Your cart is empty. Please restart your order process.'
           
        browser.get(self.portal_link)
           
        elem_remove = browser.find_element_by_xpath('//*[@class="remove"]/a')
        elem_remove.click()
           
        time.sleep(1)
        elem_empty_cart_msg = browser.find_element_by_xpath('//*[@class="span10"]/p[contains(text(),"Your cart is empty.")]')
#        print elem_empty_cart_msg.text
           
        assert elem_empty_cart_msg.text == empty_cart_msg, \
            "Empty cart message not found"
     
        print "PASSED"
        
        
    def test_check_volume_pricing(self):             
        browser = self.browser
         
        browser.get(self.portal_link)
         
        elem_volume_pricing = browser.find_element_by_id('0')
        common.hover(browser, elem_volume_pricing)
        
        if elem_volume_pricing.text != "Volume Pricing":  #verify that link says "Volume Pricing"
            self.verify.append('Checking "Volume Pricing" link.... \n"Volume Pricing" is not link text.\n') 

        elem_volume_pricing_hover_header = browser.find_element_by_xpath('//*[@id = "scale_0"]/div/h3')
        
        if elem_volume_pricing_hover_header.text != "Volume Pricing":
            self.verify.append('Checking header text for "Volume Pricing" hover box.... \n"Volume Pricing" is not the header text for the hover box.\n')    
        
        price_qty_1_24 = browser.find_element_by_xpath('//*[@id="tier-pricing"]/tbody/tr[2]/td[2]/p').text
        price_qty_25_49 = browser.find_element_by_xpath('//*[@id="tier-pricing"]/tbody/tr[3]/td[2]/p').text
        price_qty_50_99 = browser.find_element_by_xpath('//*[@id="tier-pricing"]/tbody/tr[4]/td[2]/p').text
         
        b_price_qty_1_24 = price_qty_1_24 == "$29.95"
        b_price_qty_25_49 = price_qty_25_49 == "$25.46"
        b_price_qty_50_99 = price_qty_50_99 == "$22.46" 
        
        tier_pricing = b_price_qty_1_24 & b_price_qty_25_49 & b_price_qty_50_99

        if not (tier_pricing):
            self.verify.append("Checking tiered pricing in hover box.... \nOne or more of the tiered price failed. \nThe price for 1-24 is: %s. \nThe price for 25-49 is: %s. \nThe price for 50-99 is: %s.\n" %(price_qty_1_24, price_qty_25_49, price_qty_50_99))
            
        common.verify_end(self)
       
        print "PASSED"
               
    def test_check_qty_error(self):
        browser = self.browser
        error = 'The quantity should be in between the minimum and maximum values allowed to purchase.'
            
        browser.get(self.portal_link) #go to the URL
            
        portal_common.select_qty(browser, '')
        time.sleep(1) #give it a second, has to load error message
        elem_error = browser.find_element_by_xpath('//*[@id="product"]/div[contains(text(),error)]')         
 #       print elem_error.text
            
        assert elem_error.text == error, \
            "error message not found"
            
        print "PASSED"
         
    def test_check_qty_0(self):
        browser = self.browser
 
        browser.get(self.portal_link) #go to the URL
          
        portal_common.select_qty(browser, '0')
        elem_qty = browser.find_element_by_id('cart_subscription_attributes_cart_items_attributes_0_charges_attributes_1_quantity')
        qty = elem_qty.get_attribute('value')
          
        assert qty == '1', \
            "qty is not 1"
      
        print "PASSED"
        
    def test_check_qty_12(self):
        browser = self.browser
          
        browser.get(self.portal_link)
          
        portal_common.select_qty(browser, '12')
        elem_qty = browser.find_element_by_id('cart_subscription_attributes_cart_items_attributes_0_charges_attributes_1_quantity')
        qty = elem_qty.get_attribute('value')
          
        assert qty == '12', \
            "qty is not 12"
 
        print "PASSED"
        
    def test_select_qty_price(self):
        qty = 10
        browser = self.browser
         
        browser.get(self.portal_link)
         
        portal_common.select_qty(browser, str(qty))
         
        unit_price_s = browser.find_element_by_xpath('//*[@class = "per-product-price"]/p/span').text
        unit_price = float(unit_price_s[1:])
        qty_num_s = browser.find_element_by_id('cart_subscription_attributes_cart_items_attributes_0_charges_attributes_1_quantity').get_attribute('aria-valuenow')
        qty_num = float(qty_num_s)
        subtotal_actual_s = browser.find_element_by_xpath('//*[@class = "product-price"]/p').text
        subtotal_actual = float(subtotal_actual_s[1:])
         
        subtotal_expected = unit_price*qty_num
         
        assert subtotal_actual == subtotal_expected, \
            "subtotal actual is not equal to the expected"
    
        print "PASSED"
        
        
    def test_different_delivery_address(self):
        qty = "10"
         
        billing_info = common.setup_user(False, '14')
        shipping_info = common.setup_user(True, '16')
         
        browser = self.browser
         
        browser.get(self.portal_link)
         
        portal_common.select_qty(browser, qty)
        portal_common.billing_info(browser, False, billing_info)
        portal_common.diff_delivery_info(browser, True, shipping_info)
         
        time.sleep(1) #too fast so can't pick up the text 
        billing_addr = browser.find_element_by_xpath('//*[@id = "address"]/div[2]/p').text
        input_addr = '%s %s\n%s,\n%s, %s %s\n%s\n%s' %(billing_info.first_name, billing_info.last_name, billing_info.addr1, billing_info.city, billing_info.state, billing_info.zipcode, billing_info.abbr_country, billing_info.email)     
                     
        assert billing_addr == input_addr, "Billing information not showing expected display with input data"
        
        print "PASSED"
        
    def test_check_terms_and_conditions(self):
        browser = self.browser
         
        browser.get(self.portal_link)
        
        billing_info = common.setup_user(False, '25')
         
        portal_common.select_qty(browser, '2')
        portal_common.billing_info(browser, True, billing_info)
        portal_common.payment_info(browser, billing_info)
         
        time.sleep(3)
         
        #parent_handle = browser.current_window_handle
         
        elem_terms_conditions = browser.find_element_by_xpath('//*[@class="span10"]/p/a[contains(text(),"Terms & Conditions")]')
        elem_terms_conditions.click()
        common.switch_new_window(browser)
         
        assert (browser.title == 'Malwarebytes | Website Terms of Service') & (browser.current_url == 'https://www.malwarebytes.org/tos/'), \
            ('not linking to Terms and Conditions page')
             
        #common.switch_back(browser, parent_handle)
        
        print "PASSED"
         
    def test_check_privacy_policy(self):
        browser = self.browser
         
        browser.get(self.portal_link)
        
        billing_info = common.setup_user(False, '26')
         
        portal_common.select_qty(browser, '2')
        portal_common.billing_info(browser, True, billing_info)
        portal_common.payment_info(browser, billing_info)
         
        time.sleep(3)
         
        elem_privacy_policy = browser.find_element_by_xpath('//*[@class="span10"]/p/a[contains(text(),"Privacy Policy")]')
        elem_privacy_policy.click()
        common.switch_new_window(browser)
         
        assert (browser.title == 'Malwarebytes | Privacy Policy') & (browser.current_url == 'https://www.malwarebytes.org/privacy/'), \
            ('not linking to Privacy Policy page')
    
        print "PASSED"
        
    def tearDown(self):
        #print out all the verify errors:
        if self.verify:
            print "Verify errors:"
        for x in self.verify:
            print x
        #clean up verify for the next test case
        del self.verify[:]
        
        self.browser.quit()
        #pass
        